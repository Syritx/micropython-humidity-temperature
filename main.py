import machine
import dht
import time

LED_PIN_NB = 2
led = machine.Pin(LED_PIN_NB, machine.Pin.OUT)
led.on()

def flash_led(is_on):
    if is_on:
	led.on()
	is_on = False

    else:
	led.off()
	is_on = True

    #debugging purposes
    print("receiving data")

    return is_on

def get_temperature(iterations, time_delay, is_farenheit):

    dht22 = dht.DHT22(machine.Pin(4))
    dat_temp = []
    led.off() # turns on the LED
    is_on = True    

    for i in range(iterations):
    	dht22.measure()
    	temp = dht22.temperature()
	is_on = flash_led(is_on)

	if is_farenheit:
	    temp = temp * 9 / 5 + 32
	
	dat_temp.append(temp)
	time.sleep(time_delay)
    
    led.on() # turns off the led
    return dat_temp

def get_humidity(iterations, time_delay):

    dht22 = dht.DHT22(machine.Pin(4))
    dat_humidity = []
    
    led.off()
    is_on = True    

    for i in range(iterations):
	dht22.measure()
	is_on = flash_led(is_on)

	humidity = dht22.humidity()
	dat_humidity.append(humidity)
	time.sleep(time_delay)
    
    led.on()
    return dat_humidity
