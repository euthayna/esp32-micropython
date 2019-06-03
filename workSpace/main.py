import urequests
import network
from machine import ADC, Pin
import time

station = network.WLAN(network.STA_IF)
station.active(True)

station.connect("nomerede", "senha")

adc_ldr = ADC(Pin(32))
adc_temp = ADC(Pin(33))


api_key = '&api_key=afac5866-28a5-3b98-9645-224be0b1ba5b'
component_id = '1'  
base_url = '/api/feed?'


ref = (1.5/4095) / 0.01

while True:
 
  ldr = str(adc_ldr.read())
  
  value = round(adc_temp.read() * ref, 2)
  temp = str(value)

  path = base_url+'&compId=1'+'&temperature=' + temp + '&luminosit=' + ldr  
  url = 'http://www.grovestreams.com'+path+api_key
  
  print('------------------')
  print('Temperatura: ', temp)
  print('Luminosidade: ', ldr)
  print('------------------')
  print(url)
 
  urequests.put(url)
  
  time.sleep(30)



