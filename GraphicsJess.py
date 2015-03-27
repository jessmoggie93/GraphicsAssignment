#import modules needed
from graphics import *
from random import randint
from random import shuffle
import random

#sets colour 0-255 to randomise the colour
blue = randint(0,255)
green = randint(0,255)
red = randint(0,255)

data = []

# Read in and print out the data in the data file
window = GraphWin("Visualisation", 300, 300)
datafile = open("data.txt",'r')

#takes the data line by line in the file and stores it in an array
for line in datafile: 
    data.append(line)

#shuffles the data
shuffle(data)

#prints the data in text, sets size, font style and randomises the colour
for i in data:
    text = Text(Point(145,300),i)
    text.setSize(33)
    text.setStyle("bold italic")
    text.setTextColor(color_rgb(blue, green, red))
    print(i)
    
    
for line in datafile:
    data.append(line)
    
shuffle(data)

#draws a line, size changes on whether the data is higher or lower
for i in data:
    line = Line(Point(i,i), Point(float(100)+float(i),float(200)+float(i)))
    line.setWidth(4)
    line.draw(window)
    print(i)
    
for line in datafile:
    data.append(line)
    
shuffle(data)

#floats set the position of the line on the canvas
for i in data:
    line = Line(Point(i,i), Point(float(300)+float(i),float(100)+float(i)))
    line.setWidth(4)
    line.draw(window)
    print(i)
    
#draws cirlces, sets the colour/randomises the colour on the second set of circles and how many times a circle is drawn
for x in range(0,20):
    ball = Circle(Point(10+x*20,100), 10)
    ball.setFill(color_rgb(255,255,0))
    ball.draw(window)
        
for x in range(0,40):
    ball = Circle(Point(10+x*10,200), 10)
    ball.setFill(color_rgb(green, blue, red))
    ball.draw(window)

#draws rectangles, sets the colour, size and sets the points of the shape on the canvas
for x in range(0,40):
    box = Rectangle(Point(25+x*10,50),Point(12,30))
    box.setFill(color_rgb(255,0,0))
    box.draw(window)

blue = randint(0,255)
green = randint(0,255)
red = randint(0,255)


text.draw(window)

# Waits until the mouse is clicked before closing the window
window.getMouse()