from pico2d import *
import random


# fill here
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')


def handle_events():
    global running
    global x, y
    events = get_events()
    # fill here

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False







running = True
frame = 0

# fill here

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hide_cursor()

while running:

    x1, y1 =x, y


    cursorx, cursory = random.randint(50, 750), random.randint(50, 550)

    for i in range(0, 100 + 1, 4):
        t = i / 100
        x = (1 - t) * x1 + t * cursorx
        y = (1 - t) * y1 + t * cursory

        clear_canvas()

        # fill here
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        cursor.draw(cursorx, cursory)
        if (cursorx - x1) >=0:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        else:
            character.clip_composite_draw(frame * 100, 100 * 1, 100, 100,0 , 'h' ,x, y, 100, 100)

        update_canvas()
        handle_events()
        frame = (frame + 1) % 8
        delay(0.05)

close_canvas()




