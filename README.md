# GPIO_ON_Raspberry
GPIO24.py	            
 - made RPi to a object for light.
 - could use it to enable and close electic by GPIO.
 - fonction : on , off , flash and clean
GpioForLight.py	
 - control GPIO using command.
 - argv:PIN NUMBER , action cmd(on,off,flash).
GpioSet.py	
 - control a set of GPIO.
 - using Json config to create that. 
RJ.php	
 - output Json config from MySql
index.php
 - insert Json data that recorded gpio setting to Mysql
 - It's a UI 
