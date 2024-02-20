import os
import platform
import subprocess
import tkinter
import pygame
from conf.config import Config
from conf.static import FilePaths, OSValues
from PIL import Image, ImageTk
from text_to_speech import save


class Others:

    @staticmethod
    def get_icon_image(f_path: str, re_size: tuple[int, int], resample=None) -> ImageTk.PhotoImage:
        img = Image.open(f_path)
        if resample is not None:
            img.resize(re_size, resample)
        return ImageTk.PhotoImage(img)

    @staticmethod
    def set_padding(widget: tkinter.Text, padx: int, pady: int):
        widget.configure(padx=padx, pady=pady)

    @staticmethod
    def talk_with_say(answer_r: str) -> None:
        if answer_r is not None and answer_r.strip() != '':
            subprocess.run(Config.MAC_VOICE_CMD + [answer_r])

    @staticmethod
    def talk_with_python(answer_r: str) -> None:
        if os.path.exists(FilePaths.ANSWER_TMP_FILE_PATH):
            os.remove(FilePaths.ANSWER_TMP_FILE_PATH)
        save(answer_r, 'tr', file=FilePaths.ANSWER_TMP_FILE_PATH, slow=False)
        pygame.mixer.init()
        pygame.mixer.music.load(FilePaths.ANSWER_TMP_FILE_PATH)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.quit()

    @staticmethod
    def talk_now(answer_r: str) -> None:
        if platform.system() == OSValues.MACOSX:
            Others.talk_with_say(answer_r)
        else:
            Others.talk_with_python(answer_r)
        print('"{}" message is now voiced.'.format(answer_r))
