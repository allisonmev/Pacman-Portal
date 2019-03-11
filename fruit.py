from walls import Block
from random import choice
from sprite_sheet import ImageManager


class Fruit(Block):
    def __init__(self, x, y, width, height):
        fruit_images = ['apple.png', 'orange_fruit.png']
        fruit_image, _ = ImageManager(img=choice(fruit_images), resize=(width // 2, height // 2)).get_image()
        super(Fruit, self).__init__(x, y, width, height, fruit_image)
