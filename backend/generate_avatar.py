from random import randint

from PIL import Image

AVATAR_WIDTH = AVATAR_HEIGHT = 100
REPEAT_WIDTH = REPEAT_HEIGHT = 200


def generate_avatar():
    plaid = Image.open('slack-plaid.png').convert('RGB')
    width, height = plaid.size

    x = width/2 - REPEAT_WIDTH/2 + randint(0, REPEAT_WIDTH)
    y = height/2 - REPEAT_HEIGHT/2 + randint(0, REPEAT_HEIGHT)

    box = (x, y, x + AVATAR_WIDTH, y + AVATAR_HEIGHT)
    avatar = plaid.rotate(randint(0, 360), Image.BICUBIC).crop(box)
    return avatar
