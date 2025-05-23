import RPi.GPIO as GPIO
import time
import dht11
GPIO.setmode (GPIO.BCM)
GPIO.setup (5, GPIO.IN)   #Button
GPIO.setup (19, GPIO.IN)  #Button
GPIO.setup (13, GPIO.IN)  #Button
GPIO.setup (22, GPIO.OUT) #LED
GPIO.setup (17, GPIO.OUT) #LED
GPIO.setup (18, GPIO.OUT) #LED
GPIO.setup (24, GPIO.OUT) #LED
GPIO.setup (23, GPIO.OUT) #Klicker
GPIO.setup (20, GPIO.OUT) #Temp LED


# read data using pin 26
instance = dht11.DHT11(pin = 26)


while True:
    if GPIO.input(19) == 1:
        GPIO.output(22, 1)  #16 Hinten
        GPIO.output(17, 1)  #17 Vorne
    else:
        GPIO.output(22, 0)  
        GPIO.output(17, 0)  

    if GPIO.input(13) == 1: 
        GPIO.output(18, 1)  #18 Rechts Blinker
        GPIO.output(23, 1)  #23 Klicker
        time.sleep(0.5)
        GPIO.output(18, 0)
        GPIO.output(23, 0)
        time.sleep(0.5)

    if GPIO.input(5) == 1:
        GPIO.output(24, 1)  #24 Links Blinker
        GPIO.output(23, 1)  #23 Klicker
        time.sleep(0.5)
        GPIO.output(24, 0)
        GPIO.output(23, 0)
        time.sleep(0.5)

    result = instance.read()
    if result.is_valid():
        temp = result.temperature
        print("Temperature: %-3.1f C" % temp)
        print("Humidity: %-3.1f %%" % result.humidity)

        if temp > 25:
            GPIO.output(20, 1)  # LED an
        else:
            GPIO.output(20, 0)  # LED aus
    else:
        print("Error: %d" % result.error_code)
        GPIO.output(20, 0)  # LED aus, wenn Fehler
        time.sleep(1)