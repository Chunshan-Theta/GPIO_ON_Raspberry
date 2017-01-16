# -*- coding: utf-8 -*-
#import gpio24
import json

def SetCreat(JsonData):
	PinSet = []
	for d in JsonData:
		#pin = GpioForLights("PinNum",1)
		#PinSet.append(d['pin'])
		PinSet.append(gpio24.GpioForLights(d['pin'],1))
	#for i in PinSet:
	#	print "PinSet"+i
	
	return PinSet

JsonData = json.loads('[{"pin":"7","GPIO":"4","Cost":"20","Device":"風扇"},{"pin":"11","GPIO":"17","Cost":"20","Device":"監視器"},{"pin":"12","GPIO":"18","Cost":"20","Device":"電燈"}]')
GpioSet = SetCreat(JsonData)
for i in GpioSet:
	i.on()

#for d in JsonData:
#	print d['pin']
#	print d['Device']


