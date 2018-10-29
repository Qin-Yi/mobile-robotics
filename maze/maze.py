# implementing a left-hand wall-following algorithm
# that can work on arbitrary complicated input maps with arbitrary start poses.

# a map class with a get function
# that takes a position as input
# and returns the map value (0 or 1) or,
# in case the position is outside the map, another value (for example 2).
#    usually it is because the robot is about to Reach an exit
class Map:
    def __init__(self,x,y):
        self.x,self.y=x,y
    def get(self):
        if self.y in range(len(wallmap)) and self.x in range(len(wallmap[0])):
            return int(wallmap[-self.y-1][self.x])
            # return the map value in number instead of digit string,
            # according to the true value
        else:
            return 2

# moves the provided pose one step forward
# change the position directly
def forward():
    global position
    if position[1]==0:position[0][0]+=1
    elif position[1]==1:position[0][1]+=1
    elif position[1]==2:position[0][0]-=1
    elif position[1]==3:position[0][1]-=1

# turns the provided pose left
# change the position directly
def turnLeft():
    global position
    position[1]=(position[1]+1)%4

# turns the provided pose right
# change the position directly
def turnRight():
    global position
    position[1]=(position[1]-1)%4

# returns true if the cell in front of given pose is occupied
# here we use the map class
def isWallInFront(p):
    if p[1]==0:return Map(p[0][0]+1,p[0][1]).get()
    elif p[1]==1:return Map(p[0][0],p[0][1]+1).get()
    elif p[1]==2:return Map(p[0][0]-1,p[0][1]).get()
    elif p[1]==3:return Map(p[0][0],p[0][1]-1).get()

# returns true if the cell the left of given pose is occupied
# here we use the map class
def isWallLeft(p):
    if p[1]==0:return Map(p[0][0],p[0][1]+1).get()
    elif p[1]==1:return Map(p[0][0]-1,p[0][1]).get()
    elif p[1]==2:return Map(p[0][0],p[0][1]-1).get()
    elif p[1]==3:return Map(p[0][0]+1,p[0][1]).get()

# read the input
# if it is useless (for example, blanks or explainations), ignore it
# save the useful messages:
# put the map into mapwall
# put the start information into startpoint
import sys
file=sys.stdin.read().split('\n')
wallmap=[]
for line in file:
    if line=='':pass
    elif line[0]=='$':pass
    elif line[0]in'X.':
        wallmap.append(line.replace('X','1').replace('.','0'))
        # to make it easier to find it is wall or not in map class
    else:
        startpoint=[int(i) for i in line.split()] # save the information as number instead of string
        position=[startpoint[0:2],startpoint[2]] # get the start pose and then print it out
        print(position)

# in the next two modes,
# First executes the Find Wall algorithm and then the Follow Wall algorithm.
# print out every step, including step forwad, turn left and right
#
# if it reavhes an exit without finding a wall (which has end the Find Wall loop),
# it will jump out of the Follow Wall mode immediately entering

# Find Wall
# Go forward until you either:
#  Reach an exit
#  Have a wall to the left side
#  Have a wall in front of you
#    In this case turn right once
while True:
    if Map(position[0][0],position[0][1]).get()==2:break
    elif isWallLeft(position)==1:break
    elif isWallInFront(position)==1:turnRight();print(position);break
    else:forward();print(position)

# Follow Wall
# Do until you reach an exit:
#  If no wall on your left:
#    Turn left
#    Step forward
#  Else if wall in front of you:
#    Turn right
#  Else:
#    Go forward
while True:
    if Map(position[0][0],position[0][1]).get()==2:break
    elif isWallLeft(position)!=1:turnLeft();print(position);forward()
    elif isWallInFront(position)==1:turnRight()
    else:forward()
    print(position)

# if the begin position is outside the map,
# which means start and end pose are the same,
# print the same pose immediately again
if position==[startpoint[0:2],startpoint[2]]:print(position)
