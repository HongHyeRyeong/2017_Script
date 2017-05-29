from pico2d import *

import game_framework
import search
import reserve
import traffic

name = "menu"
image = None
mouseX, mouseY = 0, 0

def enter():
    global image
    open_canvas(600, 800)
    image = load_image('image/menu.png')

def exit():
    global image
    del(image)
    close_canvas()

def update(frame_time):
    pass

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(300, 400)
    update_canvas()

def handle_events(frame_time):
    global mouseX, mouseY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mouseX, mouseY = event.x, event.y
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if 200 < mouseX < 400:
                if 200 < mouseY < 270:
                    game_framework.change_state(search)
                elif 380 < mouseY < 440:
                    game_framework.change_state(reserve)
                elif 580 < mouseY < 630:
                    game_framework.change_state(traffic)

def pause(): pass

def resume(): pass