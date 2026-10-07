#!/usr/bin/env python3
from signal import signal, SIGINT, SIGQUIT
from pynput.keyboard import KeyCode, Key, GlobalHotKeys, Listener, HotKey
from pynput.mouse import Button, Controller as MouseController

TOGGLE_KEY = "<alt>+<shift>"
HOLD_KEY = Key.caps_lock


def format_keys(keys: Key | KeyCode | list[KeyCode]) -> str:
    if type(keys) == Key:
        return "<" + keys.name + ">"
    elif type(keys) == KeyCode:
        return keys.char or "<" + str(keys.vk) + ">"
    elif type(keys) == list:
        strings = [format_keys(k) for k in keys]
        return "+".join(strings)
    return ""


class MouseToggler:
    state: bool
    controller: MouseController

    def __init__(self):
        self.controller = MouseController()
        self.state = False

    def toggle(self):
        self.state = not self.state
        if self.state:
            # print("ENABLE")
            self.controller.press(Button.right)
        else:
            # print("DISABLE")
            self.controller.release(Button.right)


mt = MouseToggler()


def shutdown():
    hold_listener.stop()
    hotkey_listener.stop()


hotkey_listener = GlobalHotKeys(
    {
        TOGGLE_KEY: mt.toggle,
    }
)


def on_press(key):
    if key == HOLD_KEY:
        mt.toggle()


def on_release(key):
    if key == HOLD_KEY:
        mt.toggle()


def handle_signal(signum, frame):
    shutdown()


hold_listener = Listener(on_press=on_press, on_release=on_release)

hold_listener.start()
hotkey_listener.start()
print(f"Press {format_keys(HotKey.parse(TOGGLE_KEY))}: toggle rmb")
print(f"Hold {format_keys(HOLD_KEY)}: press or release rmb")

signal(SIGINT, handle_signal)  # ^c
signal(SIGQUIT, handle_signal)  # ^\

hold_listener.join()
hotkey_listener.join()

if mt.state:
    mt.toggle()
print("BYE")
