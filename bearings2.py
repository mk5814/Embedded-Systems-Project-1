import math

def bearing(X, Y):
    if X == 0:
        if Y > 0:
            degrees = 90
            #print('East')
        else:
            degrees = 270
            #print('West')
    elif Y == 0:
        if X > 0:
            degrees = 0
            #print('North')
        else:
            degrees = 180
            #print('South')
    else: #X != 0 and Y != 0: #calculate and find the angle from 0 to 360
        degrees = math.atan2(Y, X)
        if (degrees < 0):
            degrees += 2 * math.pi
        degrees = math.degrees(degrees)
    return degrees
