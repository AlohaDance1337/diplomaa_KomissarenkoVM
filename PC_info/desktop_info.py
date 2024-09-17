from pathlib import Path

import os
import pyautogui


class DesktopInfo:
    def get_desktop_info(self):
        screen_width, screen_height = pyautogui.size()
        desktop_path = Path.home() / 'Desktop'
        return {"resolution": f"{screen_width}x{screen_height}", "path": f"{desktop_path}"}

    def get_desktop_files(self):
        files = os.listdir(self.get_desktop_info().get("path"))
        return len(files)