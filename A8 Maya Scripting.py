#A8_Scripting_in_Maya: Yejin Jeon & Chanhee Yoo
import maya.cmds as cmds
import random


# Function to create a tree
def create_tree(height=5, radius=0.5):
    group = cmds.group(em=True, name="tree_group")
    trunk = cmds.polyCylinder(h=height, r=radius, sx=10, name="trunk")[0]
    cmds.move(0, height / 2, 0, trunk)
    cmds.parent(trunk, group)
    foliage = cmds.polySphere(r=radius * 3, sx=20, name="foliage")[0]
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


# Function to generate the entire scene
def generate_forest_city_scene(num_trees=5, num_buildings=5, tree_height=6, rock_size=1.0, flower_petals=6):
    if cmds.objExists("forest_city_scene"):
        cmds.delete("forest_city_scene")
    scene = cmds.group(em=True, name="forest_city_scene")

    # Create a ground plane
    ground = cmds.polyPlane(w=40, h=40, sx=1, sy=1, name="ground")[0]
    cmds.setAttr(f"{ground}.overrideEnabled", 1)
    cmds.setAttr(f"{ground}.overrideColor", 7)  # Light gray
    cmds.parent(ground, scene)

    # Add trees
    for _ in range(num_trees):
        tree = create_tree(height=random.uniform(tree_height - 2, tree_height + 2), radius=random.uniform(0.3, 0.5))
        cmds.move(random.uniform(-15, -5), 0, random.uniform(-15, 15), tree)  # Forest on one side
        cmds.parent(tree, scene)

    # Add rocks
    for _ in range(num_trees // 2):
        rock = create_rock(size=random.uniform(rock_size - 0.5, rock_size + 0.5))
        cmds.move(random.uniform(-15, -5), 0, random.uniform(-15, 15), rock)
        cmds.parent(rock, scene)

    # Add flowers
    for _ in range(num_trees // 3):
        flower = create_flower(petals=flower_petals)
        cmds.move(random.uniform(-15, -5), 0, random.uniform(-15, 15), flower)
        cmds.parent(flower, scene)

    # Add buildings
    for _ in range(num_buildings):
        building = cmds.polyCube(h=random.uniform(8, 20), w=3, d=3, name="building")[0]
        cmds.move(random.uniform(5, 15), 0, random.uniform(-15, 15), building)  # City on the other side
        cmds.setAttr(f"{building}.overrideEnabled", 1)
        cmds.setAttr(f"{building}.overrideColor", random.choice([6, 15]))  # Random building color
        cmds.parent(building, scene)


# Create sliders
if cmds.window("forest_city_control", exists=True):
    cmds.deleteUI("forest_city_control")
control_window = cmds.window("forest_city_control", title="Forest and City Controller", widthHeight=(300, 200))
cmds.columnLayout(adjustableColumn=True)

# Slider for number of trees
cmds.intSliderGrp(
    "numTreesSlider", label="Number of Trees", field=True,
    minValue=1, maxValue=20, value=5,
    dragCommand=lambda value: generate_forest_city_scene(
        value,
        cmds.intSliderGrp("numBuildingsSlider", query=True, value=True),
        cmds.floatSliderGrp("treeHeightSlider", query=True, value=True),
        cmds.floatSliderGrp("rockSizeSlider", query=True, value=True),
        cmds.intSliderGrp("flowerPetalsSlider", query=True, value=True)
    )
)

# Slider for number of buildings
cmds.intSliderGrp(
    "numBuildingsSlider", label="Number of Buildings", field=True,
    minValue=1, maxValue=20, value=5,
    dragCommand=lambda value: generate_forest_city_scene(
        cmds.intSliderGrp("numTreesSlider", query=True, value=True),
        value,
        cmds.floatSliderGrp("treeHeightSlider", query=True, value=True),
        cmds.floatSliderGrp("rockSizeSlider", query=True, value=True),
        cmds.intSliderGrp("flowerPetalsSlider", query=True, value=True)
    )
)

# Slider for tree height
cmds.floatSliderGrp(
    "treeHeightSlider", label="Tree Height", field=True,
    minValue=4.0, maxValue=10.0, value=6.0,
    dragCommand=lambda value: generate_forest_city_scene(
        cmds.intSliderGrp("numTreesSlider", query=True, value=True),
        cmds.intSliderGrp("numBuildingsSlider", query=True, value=True),
        value,
        cmds.floatSliderGrp("rockSizeSlider", query=True, value=True),
        cmds.intSliderGrp("flowerPetalsSlider", query=True, value=True)
    )
)

# Slider for rock size
cmds.floatSliderGrp(
    "rockSizeSlider", label="Rock Size", field=True,
    minValue=0.5, maxValue=3.0, value=1.0,
    dragCommand=lambda value: generate_forest_city_scene(
        cmds.intSliderGrp("numTreesSlider", query=True, value=True),
        cmds.intSliderGrp("numBuildingsSlider", query=True, value=True),
        cmds.floatSliderGrp("treeHeightSlider", query=True, value=True),
        value,
        cmds.intSliderGrp("flowerPetalsSlider", query=True, value=True)
    )
)

# Slider for flower petals
cmds.intSliderGrp(
    "flowerPetalsSlider", label="Flower Petals", field=True,
    minValue=3, maxValue=12, value=6,
    dragCommand=lambda value: generate_forest_city_scene(
        cmds.intSliderGrp("numTreesSlider", query=True, value=True),
        cmds.intSliderGrp("numBuildingsSlider", query=True, value=True),
        cmds.floatSliderGrp("treeHeightSlider", query=True, value=True),
        cmds.floatSliderGrp("rockSizeSlider", query=True, value=True),
        value
    )
)

cmds.showWindow(control_window)

# Generate initial scene
generate_forest_city_scene(5, 5, 6.0, 1.0, 6)