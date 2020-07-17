import pygame
from Key import Key

keys_pressed = dict()
key_list = []


def key_input_listener(event):
    check_keys_pressed(event)
    check_keys_down_up(event)


def check_keys_pressed(event):
    if event.type == pygame.KEYDOWN and event.key not in keys_pressed:
        keys_pressed[event.key] = True
    elif event.type == pygame.KEYDOWN and not keys_pressed[event.key] :
        keys_pressed[event.key] = True
    elif event.type == pygame.KEYUP and keys_pressed[event.key]:
        keys_pressed[event.key] = False


def check_keys_down_up(event):
    if event.type == pygame.KEYDOWN and key_in_list(event.key) is None:
        key_list.append(Key(event.key, Key.KeyState.DOWN))
    elif event.type == pygame.KEYDOWN:
        key_in_list(event.key).set_down()
    elif event.type == pygame.KEYUP:
        key_in_list(event.key).set_up()


def reset_key_list():
    for key in key_list:
        key.set_neutral()


def is_key_down(input_key):
    if input_key in keys_pressed:
        return keys_pressed[input_key]
    else:
        return False


def is_key_pressed(input_key):
    key = key_in_list(input_key)
    if key and key.is_down():
        return True
    return False


def is_key_released(input_key):
    key = key_in_list(input_key)
    if key and key.is_up():
        return True
    return False


def key_in_list(input_key):
    for key in key_list:
        if key.key_val == input_key:
            return key
    return None




