from thonnycontrib.micropython import MicroPythonProxy, MicroPythonConfigPage
from thonny.globals import get_workbench, get_runner
import os
from thonny import THONNY_USER_BASE
import subprocess
from thonny.ui_utils import SubprocessDialog
import webbrowser

class PyBoardProxy(MicroPythonProxy):
    @property
    def known_usb_vids_pids(self):
        return super().known_usb_vids_pids | {
            # https://forum.micropython.org/viewtopic.php?t=1023&start=10#p5896
            (0xF055, 0x9800), # Pyboard in CDC mode
            (0xF055, 0x9801), # Pyboard in CDC+HID mode
            (0xF055, 0x9802), # Pyboard in CDC+MSC mode
        }

    def select_and_upload_micropython(self):
        webbrowser.open("https://github.com/micropython/micropython/wiki/Pyboard-Firmware-Update")

class PyBoardConfigPage(MicroPythonConfigPage):
    pass


def load_early_plugin():
    get_workbench().add_backend("PyBoard", PyBoardProxy, "MicroPython on PyBoard", PyBoardConfigPage)
