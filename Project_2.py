#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Amna Khalid
Sept 28 2018
Project_2.py
This is Project 2 for CS 112-01 showing the use of turtle graphics.

"""

import turtle
import random

def square(tortoise, fcolor, size):
    '''
    This function makes squares of different colors.
    Input:
        tortoise = name of turtle
        fcolor = fill inside of shape
        size = size of shape
    Return:
        squares with different colors
    '''
    pcolor = random.choice(['black','maroon','midnightblue'])
    tortoise.pencolor(pcolor)
    tortoise.fillcolor(fcolor)
    tortoise.begin_fill()
    for segment in range(4):
        tortoise.forward(size)
        tortoise.left(90)
    tortoise.end_fill()
    
def squareflowers(tortoise, fcolor, size):
    '''
    This function makes a flower out of the 'square' function above.
    Input:
        tortoise = name of turtle
        fcolor = fill inside of shape
        size = size of shape
    Return:
        squares flowers with different colors 
    '''
    for segment in range(6):
        square(tortoise, fcolor, size)
        tortoise.left(60)
        
def squarex(tortoise, fcolor, size):
    '''
    Combines above two functions
    '''
    square(tortoise, fcolor, size)
    squareflowers(tortoise, fcolor, size)

def growsquareflowers(x, y):
    '''
    Grows square flowers in random areas and random colors.
    '''
    spread = random.randrange(10,50)
    fill = random.choice(['steelblue','crimson','teal','orchid','hotpink','yellow','orange','lightcoral'])
    tortoise = turtle.Turtle()
    tortoise.hideturtle()
    tortoise.speed(0)
    tortoise.up()
    tortoise.goto(x, y)
    tortoise.setheading(0)
    tortoise.pensize(2)
    tortoise.down()
    squarex(tortoise, fill, spread)

#Shape 2 - draws a kitten 
#===============================================================================
'''
The statements below make a cute kitten in the middle of the flowers. 
'''    
spidy = turtle.Turtle()
spidy.speed(0)
spidy.pencolor('black')
#ear 1
spidy.left(60)
spidy.forward(30)
spidy.right(120)
spidy.forward(30)
#ear 2
spidy.home()
spidy.forward(70)
spidy.left(60)
spidy.forward(30)
spidy.right(120)
spidy.forward(30)
#face
spidy.home()
spidy.fillcolor('lightpink')
spidy.begin_fill()
for i in range(4):
    spidy.forward(100)
    spidy.right(90)
spidy.end_fill()
#eyes
spidy.home()
spidy.penup()
spidy.forward(20)
spidy.right(90)
spidy.forward(30)
spidy.pendown()
spidy.forward(20)
spidy.penup()
spidy.home()
spidy.penup()
spidy.forward(80)
spidy.right(90)
spidy.forward(30)
spidy.pendown()
spidy.forward(20)
spidy.penup()
spidy.home()
spidy.penup()
spidy.forward(40)
spidy.right(90)
spidy.forward(65)
spidy.pendown()
spidy.left(90)
spidy.forward(20)    
spidy.hideturtle()
#=============================================================================
   

spidy = turtle.Turtle()
spidy.hideturtle()
screen = spidy.getscreen()
screen.onclick(growsquareflowers)
screen.mainloop()
