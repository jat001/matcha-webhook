import win32gui
import win32con
from sanic.log import logger

from config import config


def search_window(title):
    title = title.lower()
    hwnd_list = []

    def callback(hwnd, _):
        t = win32gui.GetWindowText(hwnd).lower()
        if title == t:
            hwnd_list.append(hwnd)
    win32gui.EnumWindows(callback, None)

    return hwnd_list


def enum_child_window(hwnd):
    child_hwnd_list = []

    def callback(child_hwnd, _):
        print(win32gui.GetWindowText(child_hwnd), win32gui.GetParent(child_hwnd))
        child_hwnd_list.append(child_hwnd)
    win32gui.EnumChildWindows(hwnd, callback, None)

    return child_hwnd_list


def post_message(hwnd, code):
    win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, code, 0)
    win32gui.PostMessage(hwnd, win32con.WM_KEYUP, code, 0)


class Window:
    config = config

    def __init__(self):
        self.hwnd_list = search_window(config['window']['title'])
        logger.info('found %d window' % len(self.hwnd_list))

    # https://stackoverflow.com/questions/53778227

    # Every Win window can have 0 or more child windows,
    # and each of those child windows can also have 0 or more children of their own, and so on...
    # So each window may have a whole tree of children.

    # When sending the message to a window and expecting a certain behavior to occur,
    # the message must be sent to the exact window
    # (or to one of its ancestors which are designed in such a way to forward it),
    # otherwise the message will simply be ignored (as the wrong window doesn't handle that kind of message).

    # There is no way to automatically detect which window is handling the message.
    # We have to test it manually. But for most games, they have only one window.
    def post_message(self, code):
        if not self.hwnd_list:
            return
        for i in self.hwnd_list:
            post_message(i, code)
            logger.info('sent code 0x%02x to window %d' % (code, i))


if __name__ == "__main__":
    window = Window()
    print(window.hwnd_list)
    window.post_message(0x59)
