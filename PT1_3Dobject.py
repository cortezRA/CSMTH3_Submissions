from vpython import *
from time import *

canvas()
totalHeight = 18; totalLength = 18
mainDistance = 6; mainSize = 6; mainDepth = 3

#Shapes for Cross(Orange)
cross1 = box(pos = vector(0, totalHeight/2, 0), color = color.orange, size = vector(mainSize,.1,mainDepth))
cross2 = box(pos = vector(mainDistance/2, mainDistance, 0), color = color.orange, size = vector(.1,mainSize,mainDepth))
cross3 = box(pos = vector(mainDistance, mainDistance/2, 0), color = color.orange, size = vector(mainSize,.1,mainDepth))
cross4 = box(pos = vector(totalLength/2, 0, 0), color = color.orange, size = vector(.1,mainSize,mainDepth))
cross5 = box(pos = vector(mainDistance, -mainDistance/2, 0), color = color.orange, size = vector(mainSize,.1,mainDepth))
cross6 = box(pos = vector(mainDistance/2, -mainDistance, 0), color = color.orange, size = vector(.1,mainSize,mainDepth))
cross7 = box(pos = vector(0, -totalHeight/2, 0), color = color.orange, size = vector(mainSize,.1,mainDepth))
cross8 = box(pos = vector(-mainDistance/2, -mainDistance, 0), color = color.orange, size = vector(.1,mainSize,mainDepth))
cross9 = box(pos = vector(-mainDistance, -mainDistance/2, 0), color = color.orange, size = vector(mainSize,.1,mainDepth))
cross10 = box(pos = vector(-totalLength/2, 0, 0), color = color.orange, size = vector(.1,mainSize,mainDepth))
cross11 = box(pos = vector(-mainDistance, mainDistance/2, 0), color = color.orange, size = vector(mainSize,.1,mainDepth))
cross12 = box(pos = vector(-mainDistance/2, mainDistance, 0), color = color.orange, size = vector(.1,mainSize,mainDepth))

#Equivalent ball shape for Cross(Orange)
ball = sphere(pos = vector(-mainDistance/3,totalHeight/2-1,0), color = color.cyan, radius = 1)
ballx = mainDistance/3*-1
bally = totalHeight/2-1

#Shapes for Cross(Yellow)
shape1 = box(pos = vector(0, totalHeight/2, 0), color = color.yellow, size = vector(mainDepth,.1,mainSize))
shape2 = box(pos = vector(0, mainDistance, mainDistance/2), color = color.yellow, size = vector(mainDepth,mainSize,.1))
shape3 = box(pos = vector(0, mainDistance/2, mainDistance), color = color.yellow, size = vector(mainDepth,.1,mainSize))
shape4 = box(pos = vector(0, 0, totalLength/2), color = color.yellow, size = vector(mainDepth,mainSize,.1))
shape5 = box(pos = vector(0, -mainDistance/2, mainDistance), color = color.yellow, size = vector(mainDepth,.1,mainSize))
shape6 = box(pos = vector(0, -mainDistance, mainDistance/2), color = color.yellow, size = vector(mainDepth,mainSize,.1))
shape7 = box(pos = vector(0, -totalHeight/2, 0), color = color.yellow, size = vector(mainDepth,.1,mainSize))
shape8 = box(pos = vector(0, -mainDistance, -mainDistance/2), color = color.yellow, size = vector(mainDepth,mainSize,.1))
shape9 = box(pos = vector(0, -mainDistance/2, -mainDistance), color = color.yellow, size = vector(mainDepth,.1,mainSize))
shape10 = box(pos = vector(0, 0, -totalLength/2), color = color.yellow, size = vector(mainDepth,mainSize,.1))
shape11 = box(pos = vector(0, mainDistance/2, -mainDistance), color = color.yellow, size = vector(mainDepth,.1,mainSize))
shape12 = box(pos = vector(0, mainDistance, -mainDistance/2), color = color.yellow, size = vector(mainDepth,mainSize,.1))

#Equivalent ball shape for Cross(Yellow)
ball2 = sphere(pos = vector(0,-(totalHeight/2-1),mainDistance/3), color = color.magenta, radius = 1)
ballz2 = mainDistance/3
bally2 = (totalHeight/2-1)*-1

#Animation for Ball(Cyan)
deltaX = .1 #parameter for change in x
xPOS = ballx
deltaY = .1 #parameter for change in y
yPOS = bally

#Animation for Ball(Magenta)
deltaZ = .1 #parameter for change in z (x equivalent)
zPOS = ballz2
deltaY2 = .1 #parameter for change in y 
y2POS = bally2


while True:
    #Balls transition from Position A to B
    while (xPOS < 1.5 and zPOS > -1.5):
        rate(50)
        xPOS+=deltaX
        zPOS-=deltaZ
        ball.pos = vector(xPOS,yPOS,0)
        ball2.pos = vector(0,y2POS,zPOS)

    #Balls transition from Position B to C
    while (yPOS > 1.5 and y2POS < -1.5):
        rate(50)
        yPOS-=deltaY
        y2POS+=deltaY2
        ball.pos = vector(xPOS,yPOS,0)
        ball2.pos = vector(0,y2POS,zPOS)

    #Balls transition from Position C to D
    while (xPOS < 7.5 and zPOS > -7.5):
        rate(50)
        xPOS+=deltaX
        zPOS-=deltaZ
        ball.pos = vector(xPOS,yPOS,0)
        ball2.pos = vector(0,y2POS,zPOS)

    #Balls transition from Position D to E
    while (yPOS > -1.5 and y2POS < 1.5):
        rate(50)
        yPOS-=deltaY
        y2POS+=deltaY2
        ball.pos = vector(xPOS,yPOS,0)
        ball2.pos = vector(0,y2POS,zPOS)
    
    #Balls transition from Position E to F
    while (xPOS > 1.5 and zPOS < -1.5):
        rate(50)
        xPOS-=deltaX
        zPOS+=deltaZ
        ball.pos = vector(xPOS,yPOS,0)
        ball2.pos = vector(0,y2POS,zPOS)
    
    #Balls transition from Position F to G
    while (yPOS > -7.5 and y2POS < 7.5):
        rate(50)
        yPOS-=deltaY
        y2POS+=deltaY2
        ball.pos = vector(xPOS,yPOS,0)
        ball2.pos = vector(0,y2POS,zPOS)
    
    #Balls transition from Position G to H
    while (xPOS > -1.5 and zPOS < 1.5):
        rate(50)
        xPOS-=deltaX
        zPOS+=deltaZ
        ball.pos = vector(xPOS,yPOS,0)
        ball2.pos = vector(0,y2POS,zPOS)

    #Balls transition from Position H to I
    while (yPOS < -1.5 and y2POS > 1.5):
        rate(50)
        yPOS+=deltaY
        y2POS-=deltaY2
        ball.pos = vector(xPOS,yPOS,0)
        ball2.pos = vector(0,y2POS,zPOS)

    #Balls transition from Position I to J
    while (xPOS > -7.5 and zPOS < 7.5):
        rate(50)
        xPOS-=deltaX
        zPOS+=deltaZ
        ball.pos = vector(xPOS,yPOS,0)
        ball2.pos = vector(0,y2POS,zPOS)

    #Balls transition from Position J to K
    while (yPOS < 1.5 and y2POS > -1.5):
        rate(50)
        yPOS+=deltaY
        y2POS-=deltaY2
        ball.pos = vector(xPOS,yPOS,0)
        ball2.pos = vector(0,y2POS,zPOS)

    #Balls transition from Position K to L
    while (xPOS < -1.5 and zPOS > 1.5):
        rate(50)
        xPOS+=deltaX
        zPOS-=deltaZ
        ball.pos = vector(xPOS,yPOS,0)
        ball2.pos = vector(0,y2POS,zPOS)

    #Balls transition from Position L to A
    while (yPOS < 7.5 and y2POS > -7.5):
        rate(50)
        yPOS+=deltaY
        y2POS-=deltaY2
        ball.pos = vector(xPOS,yPOS,0)
        ball2.pos = vector(0,y2POS,zPOS)