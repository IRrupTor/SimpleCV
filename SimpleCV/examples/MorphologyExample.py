#!/usr/bin/python 
from SimpleCV import *
from numpy import linspace 
from scipy.interpolate import UnivariateSpline
import sys, time, socket

#settings for the project
srcImg  = "../sampleimages/orson_welles.jpg"     #Path for output files
input = Image(srcImg)
input.save("MorphSource.png")

erode = input.erode(100)
erode.save("Erode.png")

dilate = input.dilate(12)
dilate.save("Dilate.png")

open = input.morphOpen()
open.save("Open.png")

close = input.morphClose()
close.save("Close.png")

grad = input.morphGradient()
grad.save("Gradient.png")