import RPi.GPIO as GP
import urllib.request
import time 

GPIO.setmode(GPIO.BCM)

Trig=16
echo=18
GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)


def distCalculation():
    GPIO.output(Trig,True)
    time.sleep(5)
    GPIO.output(Trig,False)
    
    while GPIO.input(echo)==0:
        start=time.time()
    while GPIO.input(echo)==1:
        end=time.time()
    
    distance=((end-start)*17150)/2
    distance=round(distance,2)
    return distance
    

while True:
    distane=distCalculation()
    #enter your api key in thingspeak here api_key=......
    url="https://thingspeak.com/update?api_key= &field1={}".format(distance)
    urllib.request.urlopen(url)
    
    time.sleep(1)
