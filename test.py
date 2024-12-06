#making a rabbit
body = cmds.polySphere(radius=1)[0]
cmds.move(0, 1, 0, body, absolute=True)
head = cmds.polySphere(radius=0.8)[0]
cmds.move(0, 2.2, 0, head, absolute=True)
eye_left = cmds.polySphere(radius=0.1)[0]
cmds.move(0.3, 2.3, 0.7, eye_left, absolute=True)
eye_right = cmds.polySphere(radius=0.1)[0]
cmds.move(-0.3, 2.3, 0.7, eye_right, absolute=True)
ear_left = cmds.polyCylinder(radius=0.2, height=1, sx=8, sy=1, sz=1)[0]
cmds.rotate(0, 0, -30, ear_left, absolute=True)
cmds.move(0.7, 3, 0, ear_left, absolute=True)
ear_right = cmds.polyCylinder(radius=0.2, height=1, sx=8, sy=1, sz=1)[0]
cmds.rotate(0, 0, 30, ear_right, absolute=True)
cmds.move(-0.7, 3, 0, ear_right, absolute=True)
nose = cmds.polySphere(radius=0.15)[0]
cmds.move(0, 2, 0.8, nose, absolute=True)
# Group all parts of the rabbit
rabbit_grp = cmds.group(body, head, eye_left, eye_right, ear_left, ear_right,
nose, name="rabbit_grp")

#create a shader
material = cmds.shadingNode('lambert', asShader=True)
#set the color of your material to RGB (this is blue)
cmds.setAttr(material + ".color", 0, 0, 1, type="double3")
#assign the material to the desired object
cmds.select(sphere)
cmds.hyperShade(assign=material)