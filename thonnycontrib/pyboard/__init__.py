from thonnycontrib.micropython import MicroPythonProxy, MicroPythonConfigPage,\
    add_micropython_backend
from thonny import get_workbench, get_runner
import os
from thonny import THONNY_USER_BASE
import subprocess
from thonny.ui_utils import SubprocessDialog
import webbrowser

class PyboardProxy(MicroPythonProxy):
    @property
    def known_usb_vids_pids(self):
        return super().known_usb_vids_pids | {
            # https://forum.micropython.org/viewtopic.php?t=1023&start=10#p5896
            (0xF055, 0x9800), # Pyboard in CDC mode
            (0xF055, 0x9801), # Pyboard in CDC+HID mode
            (0xF055, 0x9802), # Pyboard in CDC+MSC mode
        }

    def _supports_directories(self):
        return True
    
    def _get_fs_mount_name(self):
        return "PYBFLASH"
        
class PyboardConfigPage(MicroPythonConfigPage):
    pass

def select_and_upload_micropython():
    webbrowser.open("https://github.com/micropython/micropython/wiki/Pyboard-Firmware-Update")



def load_plugin():
    add_micropython_backend("PyBoard", PyboardProxy, "MicroPython on pyboard", PyboardConfigPage)
    get_workbench().add_command("uploadmicropythonpyboard", "tools", "Instructions for uploading MicroPython to pyboard ...",
                                select_and_upload_micropython,
                                group=120)
