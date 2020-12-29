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
		bars.append(Pub("Pub No."+str(randint(0,100)),randint(0,12),randint(13,23)))

	for bar in bars:
		print("Bar:",bar.name," opens at ",bar.openTime," and closes at ",bar.closeTime)
main()
