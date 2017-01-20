# GPIO_ON_Raspberry
GPIO24.py	            
 - made RPi's GPIO to a object for light.
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

PhpGpioControler.php
 - It's a UI for set gpio initialization
 - made a config data that Json element from UI
 - renew view to add GPIO button and lock config
 - exec cmd using ajax 
 
GpioCMD.php
 - controler GPIO using php like on and off
 - argv:
 - action & PinNum
 
SQLSstructure.sql
 - It's SQL structure and sample data for index.php and RJ.php
