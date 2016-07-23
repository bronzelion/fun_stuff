#!/usr/bin/python

import random
import math
from PIL import Image
from PIL import ImageChops

'''
Using Midpoint displacement in 1D as described in pseudocode here
http://www.gameprogrammer.com/fractal.html
'''

# Midpoint generation
def recurse(a,myseed,stop):
	if stop>0:
		idx = 0
		for i in range(len(a)-1):						
			#a.insert(i+1, (a[i]+a[i+1])/2 + (random.random()*myseed*2)-myseed)
			a.insert(idx+1, (a[idx]+a[idx+1])/2 + (random.random()*myseed*2)-myseed)
			idx = idx+2
		myseed= myseed*0.6
		stop = stop-1
		#print "LEn",len(a)
		#print "a",a
		#print 'myseed',myseed		
		recurse(a,myseed,stop)
	return a

# Main
w = 512
h = 1920
myseed = w/4
a=[h/4+random.random()*myseed*2 -myseed,h/4+random.random()*myseed*2 -myseed]
stop= 10
result = recurse(a,myseed,stop)

# Generate a square image
#image = Image.new('RGB',(h,w*2+1))
image = Image.new('RGBA',(1920,1080))
for i in range(len(result)):
	#val = int(abs((result[i]+8)) %256)
	val = int(math.ceil(result[i]))
	#print i,val
	image.putpixel((i,val),(255,255,255))
	for j in range(val):
		image.putpixel((i,j),(255,255,255,128))
# The fun of the fractal is zooming in / repeating it is also a fractal,
# Just reusing the created sqauare to fill a rectangle,
# Could be more smarter by picking continuity or mirroring from an offset.

idx = len(result)-1
for i in range(idx,h):
	val = int(math.ceil(result[idx]))
	idx=idx-1
	#print i,val
	image.putpixel((i,val),(255,255,255))
	for j in range(val):
		image.putpixel((i,j),(255,255,255))

# The compositing for a simple bg
bg = Image.new('RGBA',(1920,1080))
bg.paste((255,120,0,255))

terrain = ImageChops.subtract(image,bg)
terrain.save('/tmp/terrain.jpg')
print 'Terrain saved as.. /tmp/terrain.jpg with resolution',image.size




