import math

def InsidePolygon(polygon,point):
    '''
    To Check if a given point Lies within the Polyon or not.
    Args : polygon - contains Coordinates of polygon in list
           point - Coordinates of ponits to be checked
           
    Output - Returns True (if a given Coordinates Lies within the Polyon)
             Or False (if not)
    '''
    
    n = len(polygon)
    angleSum = 0
    for i in range (0,n):
        c1 = polygon[i]
        c2 = polygon[(i+1)%n]
        
        if ( (point[0] == c1[0] and point[1] == c1[1]) or (point[0] == c1[0] and point[1] == c1[1])):
            return("TRUE")
        else:
            angleSum += abs(getAngle(c1, point , c2))
            #print(abs(getAngle(c1, point , c2)))
    
        
    #checks if angleSum is equal to 360 degrees then point inside otherwise outside
    if( abs(round(angleSum) != 360) ):
        return ("FALSE")
    else:
        return("TRUE")
        
        
def getAngle(a, b, c):
    '''
    To calculates the angle between the line AB and line AC
    Arg : a,b,c - Coordinates 
    Output : Angle in degree
    '''
    
    angle1 = math.atan2(c[1]-b[1], c[0]-b[0])
    angle2 = math.atan2(a[1]-b[1], a[0]-b[0])
    angle_formed = math.degrees(angle1 - angle2)
    
    while (angle_formed > 180):
        angle_formed -= 360
    while (angle_formed < -180):
        angle_formed += 360
    
    return angle_formed


#Input 
polygon = [[-3,2], [-2,-0.8], [0,1.2], [2.2,0], [2,4.5]]
point_to_check =[0,0]

#Calling check InsidePolygon function
print(InsidePolygon(polygon, point_to_check))
