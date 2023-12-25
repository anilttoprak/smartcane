# -*- coding: utf-8

import RPi.GPIO as GPIO
import time

# Pin numaralarını tanımla
trig_pin = 23
echo_pin = 24
buzzer_pin = 17
vibration_motor_pin = 18 
# GPIO ayarlarını yap
GPIO.setmode(GPIO.BCM)
GPIO.setup(trig_pin, GPIO.OUT) 
GPIO.setup(echo_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(vibration_motor_pin, GPIO.OUT)

def get_distance():
    pulse_start = 0 
    pulse_end = 0
    # Ultrasonik sensörle mesafe ölçümü
    GPIO.output (trig_pin, True) 
    time.sleep(0.00001)
    GPIO.output (trig_pin, False)
    while GPIO.input (echo_pin) == 0:
        pulse_start = time.time()
    while GPIO.input (echo_pin) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance=pulse_duration * 17150
    distance=round (distance, 2)
    return distance
def set_buzzer_speed (distance):
    #Mesafeye göre buzzer hızını ayarla
    speed_factor = int(70/distance)
    speed = max(1, speed_factor)
    return speed
try:
    while True:
        # Mesafeyi al
        distance = get_distance()
        # Mesafeyi ekrana yazdır
        print (f"Mesafe: {distance} cm")
        # Mesafe 70 cm üzerindeyse
        if distance> 100:
            GPIO.output (buzzer_pin, GPIO.HIGH)
            GPIO.output (vibration_motor_pin, GPIO. LOW)
        else:
            GPIO.output (buzzer_pin, GPIO.LOW)
            # Mesafe 50 cm altına düşerse
            if distance< 50:
                GPIO.output (vibration_motor_pin, GPIO.HIGH)
            else:
                GPIO.output(vibration_motor_pin, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()