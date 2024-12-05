import maya.cmds as cmds
import random

# Function to create a tree
def create_tree(height=5, radius=0.5):
    group = cmds.group(em=True, name="tree_group")
    trunk = cmds.polyCylinder(h=height, r=radius, sx=10, sy=1, sz=1, name="trunk")[0]
    cmds.move(0, height / 2, 0, trunk)
    cmds.parent(trunk, group)
    foliage = cmds.polySphere(r=radius * 3, sx=20, sy=20, name="foliage")[0]
    cmds.move(0, height + (radius * 2), 0, foliage)
    cmds.setAttr(f"{foliage}.overrideEnabled", 1)
    cmds.setAttr(f"{foliage}.overrideColor", 14)  # Green
    cmds.parent(foliage, group)
    return group

# Function to create a rock
def create_rock(size=1.0):
    group = cmds.group(em=True, name="rock_group")
    rock = cmds.polySphere(r=size, sx=10, sy=10, name="rock")[0]
    cmds.scale(random.uniform(0.5, 1.5), random.uniform(0.5, 1.5), random.uniform(0.5, 1.5), rock)
    cmds.setAttr(f"{rock}.overrideEnabled", 1)
    cmds.setAttr(f"{rock}.overrideColor", 2)  # Gray
    cmds.parent(rock, group)
    return group

# Function to create a flower
def create_flower(petals=6):
    group = cmds.group(em=True, name="flower_group")
    for i in range(petals):
        petal = cmds.polyPlane(w=0.2, h=0.5, sx=1, sy=1, name="petal")[0]
        cmds.rotate(0, i * (360 / petals), 90, petal)
        cmds.move(0, 0.25, 0.3, petal)
        cmds.setAttr(f"{petal}.overrideEnabled", 1)
        cmds.setAttr(f"{petal}.overrideColor", 13)  # Red
        cmds.parent(petal, group)
    stem = cmds.polyCylinder(h=0.5, r=0.05, name="stem")[0]
    cmds.move(0, 0.25, 0, stem)
    cmds.setAttr(f"{stem}.overrideEnabled", 1)
    cmds.setAttr(f"{stem}.overrideColor", 6)  # Yellow
    cmds.parent(stem, group)
    return group

# Function to generate the scene
def generate_scene(num_trees=5):
    if cmds.objExists("forest_scene"):
        cmds.delete("forest_scene")
    forest = cmds.group(em=True, name="forest_scene")
    # Create a ground plane
    ground = cmds.polyPlane(w=20, h=20, sx=1, sy=1, name="ground")[0]
    cmds.setAttr(f"{ground}.overrideEnabled", 1)
    cmds.setAttr(f"{ground}.overrideColor", 7)  # Light gray
    cmds.parent(ground, forest)

    # Add trees
    for _ in range(num_trees):
        tree = create_tree(height=random.uniform(4, 8), radius=random.uniform(0.2, 0.5))
        cmds.move(random.uniform(-10, 10), 0, random.uniform(-10, 10), tree)
        cmds.parent(tree, forest)

    # Add rocks
    for _ in range(num_trees // 2):
        rock = create_rock(size=random.uniform(0.3, 1))
        cmds.move(random.uniform(-10, 10), 0, random.uniform(-10, 10), rock)
        cmds.parent(rock, forest)

    # Add flowers
    for _ in range(num_trees // 3):
        flower = create_flower(petals=random.randint(5, 8))
        cmds.move(random.uniform(-10, 10), 0, random.uniform(-10, 10), flower)
        cmds.parent(flower, forest)

# Create slider to control the number of trees
if cmds.window("control_window", exists=True):
    cmds.deleteUI("control_window")
control_window = cmds.window("control_window", title="Scene Controller", widthHeight=(300, 100))
cmds.columnLayout(adjustableColumn=True)
cmds.intSliderGrp("numTreesSlider", label="Number of Trees", field=True, minValue=1, maxValue=20, value=5,
                  dragCommand=lambda value: generate_scene(value))
cmds.showWindow(control_window)
generate_scene(5)

