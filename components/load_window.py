import time
import tkinter
from conf.config import Config
from conf.static import StaticValues, Messages
from lib.component_lib import Others


class LoadWindow:
    __loading_label: tkinter.Label = None
    __loading_window: tkinter.Tk = None
    __load_is_done = False

    @staticmethod
    def init():
        LoadWindow.__loading_window = tkinter.Tk()
        LoadWindow.__loading_window.title(StaticValues.LOAD_WINDOW_TITLE)
        LoadWindow.__loading_window.geometry(Config.LOAD_WINDOW_GEOMETRY)
        tkinter.Label(LoadWindow.__loading_window).pack()
        LoadWindow.__loading_label = tkinter.Label(
            LoadWindow.__loading_window,
            font=('Corbal', 14),
            text=Messages.REQ_LOADING
        )
        Others.set_padding(LoadWindow.__loading_label, 0, 2)
        LoadWindow.__loading_label.pack()
        LoadWindow.__loading_window.update()
        time.sleep(1)

    @staticmethod
    def update_loading_msg(msg: str):
        LoadWindow.__loading_label.config(text=msg)
        LoadWindow.__loading_label.update()

    @staticmethod
    def get_loaded():
        return LoadWindow.__load_is_done

    @staticmethod
    def destroy():
        LoadWindow.__load_is_done = True
        LoadWindow.update_loading_msg(Messages.APP_STARTING)
        time.sleep(0.5)
        LoadWindow.__loading_window.destroy()
