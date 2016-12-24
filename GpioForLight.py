#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys




class GpioForLights:
	self.AlertOn = 0
	self.ledPin = 12
	def __init__(self,PinNum,Alert=0):
		#initialization :set output pin
		self.ledPin = PinNum
		GPIO.setup(ledPin, GPIO.OUT)

		#initialization : Pin off
		off()

		#alert text	
		self.AlertOn = Alert
		if self.AlertOn:
			print "Setup Pin "+ledPin+" is OutPut..."


	def on(self):		
  		GPIO.output(self.ledPin, True)

		#alert text
		if self.AlertOn:
			print "Set Output On"
	def off(self):		
  		GPIO.output(self.ledPin, False)

		#alert text
		if self.AlertOn:
			print "Set Output Off"
	
	def flash(self,time=3,SleepTime=1):
		print self.ledPin+" Pin Starting flash... "
		for i in range(time):

		  print "Set Output True"
		  GPIO.output(self.ledPin, True)
		  time.sleep(SleepTime)

		  print "Set Output False"
		  GPIO.output(self.ledPin, False)
		  time.sleep(SleepTime)

		#alert text
		if self.AlertOn:
			print "Set Output Off"

pin = GpioForLights(sys.argv[1],1)
if sys.argv[2] == 0:
	pin.off()
elif sys.argv[2] == 1:
	pin.on()
elif sys.argv[2] == 2:
	pin.flash()
else:
	print "not Found Command"


