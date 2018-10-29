# Written and debugged under Python 3.4.1 on Windows 8
# SJHSTONE, SIST, ShanghaiTech

import random

def gen(size):
  map = []
  def linegen():
    tmp = ''
    for i in range(size):
      tmp += str(random.randint(0,1))
    return tmp
  for j in range(size):
    map.append(linegen())
  def posegen():
    pose = [random.randrange(0,size), random.randrange(0,size), random.randrange(0,3)]
    count = 0
    while map[len(map) - pose[1] - 1][pose[0]] != '0':
      pose = [random.randrange(0,size), random.randrange(0,size), random.randrange(0,3)]
      count += 1
      # Deal with rare cases where 
      if count > size**2:
        print('# Another unlucky day, too many iterations.\n# Please try again!\n# Reduce the size of the map may help.')
        exit(1)
    return pose
  pose = posegen()
  return pose, map
plate = int(input())
if plate > 50:
  print('# The size exceeds the recommended value.\n# Modify the source code if you want a bigger map.')
  exit(1)
print('# RandomMapGen by SJHSTONE\n# Initial Pose')
holder = gen(plate)
print(holder[0][0], holder[0][1], holder[0][2])
print('# Map')
for j in range(len(holder[1])-1):
  print(holder[1][j])
print(holder[1][-1], end = '')