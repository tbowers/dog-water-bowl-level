import RPi.GPIO as GPIO
import time

SPEED_OF_SOUND_CM_S=17150

TRIG=21
ECHO=20

# for info GPIO lib https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

GPIO.cleanup(TRIG)
GPIO.cleanup(ECHO)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print 'measuring...'

while True:
    GPIO.output(TRIG, False)
    
    print 'settling...'
    time.sleep(2)
    
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()

    print 'calculating...'
    pulse_duration=pulse_end-pulse_start
    distance_cm=pulse_duration*SPEED_OF_SOUND_CM_S
    distance_in = distance_cm / 2.54
    
    #distance_cm=round(distance_cm,2)
    #distance_in=round(distance_in,2)

    #if distance_cm > 20 and distance_cm < 400:
    print 'distance:',distance_in,'in (',distance_cm,'cm)'
    #else:
    # print 'out of range'

