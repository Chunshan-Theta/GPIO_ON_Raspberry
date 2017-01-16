# -*- coding: utf-8 -*-
import GPIO24 as gpio
import json

def SetCreat(JsonData):
	PinSet = []
	for d in JsonData:
		#pin = GpioForLights("PinNum",1)
		#PinSet.append(d['pin'])
		PinSet.append(gpio.GpioForLights(d['pin'],1))
	#for i in PinSet:
	#	print "PinSet"+i
	
	return PinSet

JsonData = json.loads('[{"id":"0","pin":"7","GPIO":"4","Cost":"20","Device":"風扇"},{"id":"1","pin":"11","GPIO":"17","Cost":"20","Device":"監視器"},{"id":"2","pin":"12","GPIO":"18","Cost":"20","Device":"電燈"}]')
GpioSet = SetCreat(JsonData)
for i in GpioSet:
	i.on()
for i in GpioSet:
	i.clean()


#for d in JsonData:
#	print d['pin']
#	print d['Device']
