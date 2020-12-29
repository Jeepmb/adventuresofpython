#!/usr/bin/env python3
from random import randint
class Pub:
	def __init__(self,name,openTime,closeTime):
		self.name = name
		self.openTime = openTime
		self.closeTime = closeTime

def main():
	bars = []
	for i in range(100):
		pubName="Pub No."+str(randint(0,100))
		pubOpenTime=randint(0,12)
		pubCloseTime=randint(13,23) # Using military time because why not
		thisPub=Pub(pubName,pubOpenTime,pubCloseTime)
		bars.append(thisPub)

	for bar in bars:
		print("Bar: " + str(bar.name) + " opens at " + str(bar.openTime) + " and closes at " + str(bar.closeTime))
main()
