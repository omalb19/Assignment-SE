def getslope(source, point):
    '''
    To find slope of line using 2 points
    Arg : source - sun co-ordinates
          point - other point co-ordinates
    output: slope of line
    '''
    
    x1,y1 = source[0], source[1]
    x2,y2 = point[0], point[1]
    if x2 == x1:
        return 0
    else:
        return ((y2-y1)/(x2-x1))



def calY(source, prev , x2): 
    '''
    To calculate new start co-ordiate of Y
    Arg : source - sun co-ordinates
          point - the co-ordinates of previous building
          x2 - X_co-ordinates of current building
    output: new Y_co-ordinates
    '''
    
    x1,y1 = prev[0], prev[1]
    s = getslope(source, prev) 
    return ((s*(x2-x1))+y1) 



def calX(source, prev , y2): 
    '''
    To calculate new start co-ordiate of X
    Arg : source - sun co-ordinates
          point - the co-ordinates of previous building
          y2 - Y_co-ordinates of current building
    output: new X_co-ordinates
    '''
    
    x1,y1 = prev[0], prev[1]
    s = getslope(source, prev) 
    return ( ( (y2-y1)/s ) + x1 ) 



def SurfaceArea(building , newY=None ,newX=None, omit = None):
    '''
    To calculate SurfaceArea of particular building exposed to sunlight
    Arg : building - building co-ordinates
          newY (optional) - the new Y_co-ordinates
          newX (optional) - the new X_co-ordinates
    output: SurfaceArea exposed to sunlight
    '''
    
    if(newX):
        roof = abs(newX - building[2][0])
    else:
        roof = abs(building[0][0] - building[2][0])
    
    
    if(newY):
        side = abs(newY - building[1][1])
    else:
        side = abs(building[0][1] - building[1][1])

        
    if omit == 1:
        return side
    elif omit == 2:
        return roof
    
    return roof+side
    
    
def surfaceAreaExposed(buildings,source):
    '''
    To calculate SurfaceArea of all building exposed to sunlight
    Arg : building - building co-ordinates
          source - sun co-ordinates
    output: Total SurfaceArea exposed to sunlight
    '''
    total_sarea=0
    prev = None
    for building in buildings:

        slope = getslope(source , building[0])

        if(slope <= 0):
            if(prev):
                y = calY(source , prev , building[0][0])
                #print("y= ",y)
                if(y >= building[0][1]):
                    x = calX(source , prev , building[0][1])
                    #print("x= ",x)
                    if(x >= building[3][0]):
                        surfacearea = 0
                        prev = prev
                    else:
                        surfacearea = SurfaceArea(building , omit=2, newX = x)
                        prev = building[3]
                else:   
                    surfacearea = SurfaceArea(building , newY = y)
                    prev = building[3]

                #print(surfacearea)
                total_sarea += surfacearea


            else:
                surfacearea = SurfaceArea(building)
                total_sarea = surfacearea
                #print("1=",surfacearea)
                prev = building[3]


        if(slope > 0):
            if(building[0][0] > source[0]):
                #surfacearea = SurfaceArea(building, omit=1)
                print("Sun can't be below building's level")

            if(building[0][0] < source[0]):
                surfacearea = SurfaceArea(building, omit=2)
                total_sarea += surfacearea


            prev = building[3]   

    return total_sarea
    
    
    
    
#Input Given
buildings =  [[[4,0],[4,-5],[7,-5],[7,0]], [[0.4,-2],[0.4,-5],[2.5,-5],[2.5,-2]]] 
source =  [-3.5,1] 

#Reversing and passing to function
print( surfaceAreaExposed(buildings[::-1],source) )

