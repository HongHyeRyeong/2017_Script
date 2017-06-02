from pico2d import *

import search
import reserve
import traffic

def handle_events():
    global running
    global mouseX, mouseY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouseX, mouseY = event.x, event.y
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if 200 < mouseX < 400:
                if 200 < mouseY < 270:
                    search.main()
                elif 380 < mouseY < 440:
                    reserve.main()
                elif 580 < mouseY < 630:
                    traffic.main()

open_canvas(600, 800)
image = load_image('image/menu.png')
mouseX, mouseY = 0, 0
running = True

while (running):
    clear_canvas()
    image.draw(300, 400)
    update_canvas()
    handle_events()

del(image)
close_canvas()