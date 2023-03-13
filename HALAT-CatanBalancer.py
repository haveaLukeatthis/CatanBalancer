# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np
import random
import math

plt.rcParams['figure.dpi']=1000
fig, ax = plt.subplots(1)
ax.set_aspect('equal')
ax.axis([-7, 7, -7, 7])
plt.axis('off')

numOfTileFails = 0
numOfNumberFails = 0

hasFailed = 0
successfulBoard = 1

#config
defaultPortLocations = 1
portCheck = 1


hexRad = 2/np.sqrt(3)

#Hexagon locations using a doubled coordinate system
#x location, y location, ID, type of tile, dice roll number
doubleCoord = [[-2,2,0,'',0],
			   [0,2,1,'',0],
			   [2,2,2,'',0],
			   [-3,1,3,'',0],
			   [-1,1,4,'',0],
			   [1,1,5,'',0],
			   [3,1,6,'',0],
			   [-4,0,7,'',0],
			   [-2,0,8,'',0],
			   [0,0,9,'',0],
			   [2,0,10,'',0],
			   [4,0,11,'',0],
			   [-3,-1,12,'',0],
			   [-1,-1,13,'',0],
			   [1,-1,14,'',0],
			   [3,-1,15,'',0],
			   [-2,-2,16,'',0],
			   [0,-2,17,'',0],
			   [2,-2,18,'',0]]

#port locations
#x location (pier 1), y location (pier 1), x location (pier 2), y location (pier 2) ID, type of port
portCoord = [[-1,3.5*hexRad,0,4*hexRad,0,''],
			   [2,4*hexRad,3,3.5*hexRad,1,''],
			   [4,2*hexRad,4,hexRad,2,''],
			   [4,-hexRad,4,-2*hexRad,3,''],
			   [3,-3.5*hexRad,2,-4*hexRad,4,''],
			   [0,-4*hexRad,-1,-3.5*hexRad,5,''],
			   [-3,-2.5*hexRad,-4,-2*hexRad,6,''],
			   [-5,-0.5*hexRad,-5,+0.5*hexRad,7,''],
			   [-4,2*hexRad,-3,2.5*hexRad,8,'']]

#List of tiles that are too close to the port to match the port's resource type
#Note tile ID 20 is used as filler/placeholder where less than 5 banned tiles are needed
#Port ID, Tile ID 1,  Tile ID 2,  Tile ID 3,  Tile ID 4,  Tile ID 5
portBannedTiles = [[0,0,1,2,4,5],
				   [1,1,2,5,6,20],
				   [2,2,5,6,10,11],
				   [3,10,11,14,15,18],
				   [4,14,15,17,18,20],
				   [5,13,14,16,17,18],
				   [6,7,8,12,13,16],
				   [7,3,7,8,12,20],
				   [8,0,3,4,7,8]]

listOfPortsStart = ['wood',
			   '?',
			   'wheat',
			   'stone',
			   '?',
			   'sheep',
			   '?',
			   '?',
			   'brick']

listOfPorts = listOfPortsStart[:]

listOfRollNumbersStart = [2,
					 3,
					 3,
					 4,
					 4,
					 5,
					 5,
					 6,
					 6,
					 8,
					 8,
					 9,
					 9,
					 10,
					 10,
					 11,
					 11,
					 12]

for p in portCoord:
	
	portColour = 'black'
	
	if defaultPortLocations == 1:
		p[5] = listOfPorts[p[4]]
	else:
		p[5] = random.choice(listOfPorts)
		listOfPorts.remove(p[5])
	

listOfTilesStart = ['sheep',
			   'sheep',
			   'sheep',
			   'sheep',
			   'wheat',
			   'wheat',
			   'wheat',
			   'wheat',
			   'wood',
			   'wood',
			   'wood',
			   'wood',
			   'stone',
			   'stone',
			   'stone',
			   'brick',
			   'brick',
			   'brick',]


while successfulBoard == 1:
	#reset
	successfulBoard = 0
	hasFailed = 0
	listOfTiles = listOfTilesStart[:]
	for c in doubleCoord:
		c[3] = ''
	
	
	for c in doubleCoord:
		# fix radius here
		tileColour = 'black'
		if c[0]==0 and c[1]==0:
			c[3] = 'desert'
		else:
			timeOutCounter = 0
			if portCheck == 1:
				isBannedByPort = 1
				while isBannedByPort==1 and timeOutCounter < 100:
					tileNotAllowed = 0
					#pick a tile resource
					c[3] = random.choice(listOfTiles)
					#loop through the port IDs
					for p in portCoord:
						#check if the port type is equal to the selected tile resource
						if p[5] == c[3]:
							#check if the current hex ID is on the banned list for that port
							for i in range(5):
								if portBannedTiles[p[4]][i+1] == c[2]:
									tileNotAllowed = 1
							if tileNotAllowed == 0:
								isBannedByPort = 0
					timeOutCounter = timeOutCounter + 1
				
			else:
				c[3] = random.choice(listOfTiles)
			if timeOutCounter >= 100:
				#print("Port Failed")
				successfulBoard = 1
			
			if len(listOfTiles)!=1:
				listOfTiles.remove(c[3])
	
	#brick and stone check
	for c in doubleCoord:
		if c[3] =='stone' or c[3] =='brick':
			#run through tiles - if one is a neighbour then check if it is the same resource
			for d in doubleCoord:
				if (d[0]==c[0]+2 and d[1]==c[1]) or (d[0]==c[0]+1 and d[1]==c[1]+1) or (d[0]==c[0]-1 and d[1]==c[1]+1) or (d[0]==c[0]-2 and d[1]==c[1]) or (d[0]==c[0]-1 and d[1]==c[1]-1 or (d[0]==c[0]+1 and d[1]==c[1]-1)):
					#print(str(d[2]) + " is a neighbour of " + str(c[2]))
					if d[3]==c[3]:
						hasFailed = 1
						
	#other resources check
	for c in doubleCoord:
		if c[3] =='wheat' or c[3] =='wood' or c[3] =='sheep':
			#run through tiles - if one is a neighbour then check if it is the same resource
			for d in doubleCoord:
				if (d[0]==c[0]+2 and d[1]==c[1]) or (d[0]==c[0]+1 and d[1]==c[1]+1) or (d[0]==c[0]-1 and d[1]==c[1]+1) or (d[0]==c[0]-2 and d[1]==c[1]) or (d[0]==c[0]-1 and d[1]==c[1]-1 or (d[0]==c[0]+1 and d[1]==c[1]-1)):
					#print(str(d[2]) + " is a neighbour of " + str(c[2]))
					if d[3]==c[3]:
						#if neighbour is the same resource check all of it's neighbours as well
						for e in doubleCoord:
							if (e[0]==d[0]+2 and e[1]==d[1]) or (e[0]==d[0]+1 and e[1]==d[1]+1) or (e[0]==d[0]-1 and e[1]==d[1]+1) or (e[0]==d[0]-2 and e[1]==d[1]) or (e[0]==d[0]-1 and e[1]==d[1]-1 or (e[0]==d[0]+1 and e[1]==d[1]-1)):
								if e[2]!=c[2] and e[3]==d[3]:								
									hasFailed = 1
	
	if hasFailed == 1:
		hasFailed = 0
		successfulBoard = 1
		#print("FAILED")
		numOfTileFails = numOfTileFails + 1
		
		
#Asigning numbers
successfulNumbers = 1
while successfulNumbers == 1:
	#reset
	successfulNumbers = 0
	listOfRollNumbers = listOfRollNumbersStart[:]
	hasFailedNumber = 0
	
	for c in doubleCoord:
		if c[0]==0 and c[1]==0:
			pass
		else:			
			c[4] = random.choice(listOfRollNumbers)
			if len(listOfRollNumbers)!=1:
				listOfRollNumbers.remove(c[4])
	
	
	#check no two of the same number next to eachother
	for c in doubleCoord:
		for d in doubleCoord:
			if (d[0]==c[0]+2 and d[1]==c[1]) or (d[0]==c[0]+1 and d[1]==c[1]+1) or (d[0]==c[0]-1 and d[1]==c[1]+1) or (d[0]==c[0]-2 and d[1]==c[1]) or (d[0]==c[0]-1 and d[1]==c[1]-1 or (d[0]==c[0]+1 and d[1]==c[1]-1)):
				#print(str(d[2]) + " is a neighbour of " + str(c[2]))
				if d[4]==c[4]:
					hasFailedNumber = 1
	
	#no two of the same number on one resource check
	for c in doubleCoord:
		for d in doubleCoord:
			if d[2]!=c[2]:
				if d[3]==c[3] and d[4]==c[4]:
					hasFailedNumber = 1
					
	#no six and eight on the same resource
	for c in doubleCoord:
		if c[4] == 6 or c[4] == 8:
			for d in doubleCoord:
				if d[2]!=c[2]:
					if d[3]==c[3] and (d[4]==6 or d[4]==8):
						hasFailedNumber = 1
	
	#no six and eight next to eachother check
	for c in doubleCoord:
		if c[4]==6 or c[4]==8:
			for d in doubleCoord:
				if (d[0]==c[0]+2 and d[1]==c[1]) or (d[0]==c[0]+1 and d[1]==c[1]+1) or (d[0]==c[0]-1 and d[1]==c[1]+1) or (d[0]==c[0]-2 and d[1]==c[1]) or (d[0]==c[0]-1 and d[1]==c[1]-1 or (d[0]==c[0]+1 and d[1]==c[1]-1)):
					#print(str(d[2]) + " is a neighbour of " + str(c[2]))
					if d[4]==6 or d[4]==8:
						hasFailedNumber = 1
	
	
	if hasFailedNumber == 1:
		hasFailedNumber = 0
		successfulNumbers = 1
		#print("NUMBER FAILED")
		numOfNumberFails = numOfNumberFails + 1
		
print("Number of tile fails = " + str(numOfTileFails) + " and number of number fails = " + str(numOfNumberFails))

#Plotting
outerCoord1 = [[2,4*hexRad], [2,5*hexRad], [-5*(hexRad/np.sqrt(3)),5*hexRad], [-3-(hexRad/2)*np.sqrt(3),4*hexRad], [-3,3.5*hexRad], [-2,4*hexRad], [-1,3.5*hexRad], [0,4*hexRad], [1,3.5*hexRad]]
outerCoord1.append(outerCoord1[0]) #repeat the first point to create a 'closed loop'

arr = np.array(outerCoord1)
arr2 = np.transpose(arr)

rotArr = np.array([[math.cos(math.radians(60)), -math.sin(math.radians(60))], [math.sin(math.radians(60)), math.cos(math.radians(60))]])
outerCoord2 = np.matmul(rotArr,arr2)
outerCoord3 = np.matmul(rotArr,outerCoord2)
outerCoord4 = np.matmul(rotArr,outerCoord3)
outerCoord5 = np.matmul(rotArr,outerCoord4)
outerCoord6 = np.matmul(rotArr,outerCoord5)

oceanAlpha = 0.2

xs, ys = zip(*outerCoord1) #create lists of x and y values
ax.plot(xs,ys,color='blue', alpha = oceanAlpha) 

outerCoord2 = np.transpose(outerCoord2)
outerCoord2 = outerCoord2.tolist()
xs, ys = zip(*outerCoord2) #create lists of x and y values
ax.plot(xs,ys,color='blue', alpha = oceanAlpha) 

outerCoord3 = np.transpose(outerCoord3)
outerCoord3 = outerCoord3.tolist()
xs, ys = zip(*outerCoord3) #create lists of x and y values
ax.plot(xs,ys,color='blue', alpha = oceanAlpha) 

outerCoord4 = np.transpose(outerCoord4)
outerCoord4 = outerCoord4.tolist()
xs, ys = zip(*outerCoord4) #create lists of x and y values
ax.plot(xs,ys,color='blue', alpha = oceanAlpha) 

outerCoord5 = np.transpose(outerCoord5)
outerCoord5 = outerCoord5.tolist()
xs, ys = zip(*outerCoord5) #create lists of x and y values
ax.plot(xs,ys,color='blue', alpha = oceanAlpha) 

outerCoord6 = np.transpose(outerCoord6)
outerCoord6 = outerCoord6.tolist()
xs, ys = zip(*outerCoord6) #create lists of x and y values
ax.plot(xs,ys,color='blue', alpha = oceanAlpha) 

for c in doubleCoord:
	
	if c[3] == 'sheep':
		tileColour = 'green'
	elif c[3] == 'wood':
		tileColour = '#023020'
	elif c[3] == 'wheat':
		tileColour = 'yellow'
	elif c[3] == 'brick':
		tileColour = 'red'
	elif c[3] == 'stone':
		tileColour = 'gray'
	elif c[3] == 'desert':
		tileColour = 'orange'
		
	hexagon = RegularPolygon((c[0], c[1]*1.5*hexRad), numVertices=6, radius=hexRad, alpha=0.6, edgecolor='k', facecolor=tileColour)
	ax.add_patch(hexagon)

for p in portCoord:
	
	if p[5] == 'sheep':
		portColour = 'green'
	elif p[5] == 'wood':
		portColour = '#023020'
	elif p[5] == 'wheat':
		portColour = 'yellow'
	elif p[5] == 'brick':
		portColour = 'red'
	elif p[5] == 'stone':
		portColour = 'gray'
	elif p[5] == '?':
		portColour = 'black'
	
	circlePort = plt.Circle((p[0], p[1]), 0.2, edgecolor=portColour, fill=False)
	ax.add_patch(circlePort)
	circlePort = plt.Circle((p[2], p[3]), 0.2, edgecolor=portColour, fill=False)
	ax.add_patch(circlePort)

#plot circles for numbers
for c in doubleCoord:
	if c[0]==0 and c[1]==0:
		pass
	else:
		numberCircle = plt.Circle((c[0], c[1]*1.5*hexRad), 0.4, edgecolor='black', facecolor='white')	
		ax.add_patch(numberCircle)
		if c[4]==6 or c[4]==8:
			textColour = 'red'
		else:
			textColour = 'black'
		plt.text(c[0],c[1]*1.5*hexRad,c[4],ha='center',va='center',size=6, color=textColour)

#plt.autoscale(enable = True)
plt.show()


