import maya.cmds as cmds

cmds.file(f=True, new=True)
cube = cmds.polyCube(h=2, w=1, d=3, name='cube#')
cmds.move(2,4,5, cube)

import math
angle_step = (2 * math.pi) / 6
for i in range(6) :
    angle = i *angle_step
    x = 3 * math.cos(angle)
    z = 3 * math.sin(angle)
cube = cmds.polyCube()
cmds.move(x, 0, z, cube, absolute = True)
