#TurtleGraphics.py
#Name:Nidhi Agarwal
#Date:02/12/2026
#Assignment: Turtle Lab work 

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.left(90)
        
def drawSquare2(myTurtle, size):
    for i in range(4):
        myTurtle.right(90)
        myTurtle.forward(size)
              
        
def drawPolygon(yoda, sides):
    for s in range(sides):
        yoda.forward(50)
        yoda.right(360/sides) 
        
def fillCorner(bob, color):
    #drawSquare(bob,200)
    bob.begin_fill()
    drawSquare(bob,200)
    #drawSquare(bob,50)
    bob.end_fill()

def fillCorner2(bob, color):
    #drawSquare(bob,200)
    bob.begin_fill()
    drawSquare2(bob,200)
    #drawSquare(bob,50)
    bob.end_fill()   
    
def squareinSqr (sq, times):
    for t in range(times):
       drawSquare2(sq, 40+(t*35))
       sq.penup()
       sq.goto(20+(15*t), 20+(15*t))
       sq.pendown()
    
    
def main():
    myTurtle = turtle.Turtle()
    
    drawSquare (myTurtle, 100)
        
    #draws a pentagon
    drawPolygon (myTurtle, 5)
        
    #draws an octogon
    drawPolygon (myTurtle, 8)
    

    #draws a square with top right corner filled in.
    fillCorner(myTurtle,2)
    
    #draws a square bottom left corner filled in.
    fillCorner2(myTurtle, 3) 

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    squareinSqr (myTurtle, 5)
    
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares
    squareinSqr (myTurtle,3)
    
main()
