# Dijkstra's for path planning

# a map class with a get function
# that takes a position as input
# and returns the map value (0 or 1) or,
# in case the position is outside the map, another value (for example 2).
class Map:
    def __init__(self,location):
        self.x,self.y,self.l=location[0],location[1],location
    def get(self):
        if self.y in range(len(wall_map)) and self.x in range(len(wall_map[0])):
            return int(wall_map[-self.y-1][self.x])
            # return the map value in number instead of digit string,
            # according to the true value
        else:return 2
    def dis(self):
        return distance_map[(self.x,self.y)]

# select the first node with the minimum dist value from the wavefront
def choose_node():
    global wavefront
    minimum=float('inf')
    for i in wavefront:
        if Map(i).dis()<minimum:
            minimum=Map(i).dis();position=i
    # remove node from the wavefront
    while position in wavefront:
        wavefront.pop(wavefront.index(position))
    return position

def main(p,d):
    global steps,wavefront,distance_map
    # if the neighbor is valid and not a wall:
    if Map(p).get()==0:
        # increase step counter
        steps+=1
        # neighDist = distance saved in node + distanceToNeighbor (1 or sqrt(2))
        neighDist=Map(node).dis()+d
        # if neighDist < distance saved in neighbor:
        if neighDist < Map(p).dis():
            # update distance saved in neighbor with neighDist
            distance_map[tuple(p)]=neighDist
            # append neighbor to the wavefront (active set)
            wavefront.append(p)

# Create the path:
def getpath():
    if Map(goal).get()!=0:path=[]
    elif Map(goal).dis()==float('inf'):path=[]
    else:
        path,lowest=[goal],float('inf')
        # starting from the goalCell select the neighbor with the lowest distance saved
        # continue with the selection to save it's lowest neighbor till you reached the start point
        while path[-1]!=start:
            for i in order:
                neighbor=Map([path[-1][j]+i[j] for j in[0,1]])
                if neighbor.get()==0 and lowest>neighbor.dis():
                    lowest=neighbor.dis();position=neighbor.l
            #  add the selection to the path
            path.append(position)
        path.reverse()
    return path

# read the input
# if it is useless (for example, blanks or explainations), ignore it
# save the useful messages:
# put the map into MapWall
# get the start and end point
import sys
file=sys.stdin.read().split('\n')
wall_map,f=[],1
for line in file:
    if line=='':pass
    elif line[0]in'$ ':pass
    elif line[0]in'X.':
        wall_map.append(line.replace('X','1').replace('.','0'))
        # to make it easier to find it is wall or not in map class
    else:
        # save the information as number instead of string
        if f:start=[int(i) for i in line.split()];f=0
        else:goal=[int(i) for i in line.split()]

# The oder is given as follows:
# Start with the bottom neighbor (y-1)
# and visit CLOCK-WISE (when looking at the text file) all 8 neighbors.
order=([0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1])
# considering some special cases
# Initialize all map cells with infinite distance
if wall_map==[]:distance_map={}
else:distance_map={(i,j):float('inf') for i in range(len(wall_map[0])) for j in range(len(wall_map))}
# Initialize the start cell with 0 distance
if tuple(start) in distance_map:distance_map[tuple(start)]=0
else:f=1
# step counter = 0
steps=0
# Add start cell to wavefront (active set)
wavefront=[start]

while wavefront and f==0:    # While wavefront not empty:
    node=choose_node()
    if node == goal:break
    # for all 8 neighbors of the node:
    for i in order:
        neighbor=[node[0]+i[0],node[1]+i[1]]
        # send the neighbor position and the distance to neighbor to the main part
        main(neighbor,(i[0]**2+i[1]**2)**0.5)

# Print the map values
for j in range(len(wall_map)-1,-1,-1):
    for i in range(len(wall_map[0])):
        print (format(distance_map[(i,j)], '6.2f'), end = "")
    print('\n',end='')
# Print the number of steps
print ("Found goal in %d steps" % steps)
# Print the path
print (getpath())
