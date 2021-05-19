from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import *
# from Player import Player

app= Ursina()
punch_sound   = Audio('assets/punch',loop = False, autoplay = False)

blocks = [
    load_texture('assets/grass.png'), # 0
    load_texture('assets/grass.png'), # 1
    load_texture('assets/stone.png'), # 2
    load_texture('assets/gold.png'),  # 3
    load_texture('assets/lava.png'),  # 4
]
block_id = 1
# earth
Entity(
    parent = scene,
    model = 'sphere',
    texture = load_texture('assets/sky.jpg'),
    scale = 500,
    double_sided = True
)


def input(key):
    global block_id, hand
    if key.isdigit():
        block_id = int(key)%len(blocks)
        hand.texture = blocks[block_id]


hand = Entity(
    parent=camera.ui,
    model='assets/block',
    texture=blocks[block_id],
    scale=0.2,
    rotation=Vec3(-10, -10, 10),
    position=Vec2(0.6, -0.6)
)

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=blocks[block_id]):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                hand.position = self.position
                Voxel(position=self.position + mouse.normal, texture=blocks[block_id])
                punch_sound.play()
            elif key == 'right mouse down':
                punch_sound.play()
                destroy(self)


# map
for z in range(10):
    for x in range(10):
        voxel = Voxel(position=(x,0,z))


player = FirstPersonController()
app.run()