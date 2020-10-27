import xbox
joy = xbox.Joystick()         #Initialize joystick

prevXval = 0
while not joy.Back():
    currXval = joy.rightX
    if currXval >= prevXval:
        prevXval = currXval 
        print (joy.rightX())
