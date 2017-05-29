from pico2d import *

import game_framework
import menu

name = "search"
image = None
mouseX, mouseY = 0, 0

def enter():
    global image
    open_canvas(600, 800)
    image = load_image('image/background.png')

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
            game_framework.change_state(menu)
        elif event.type == SDL_MOUSEMOTION:
            mouseX, mouseY = event.x, event.y
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            pass

def pause(): pass

def resume(): pass