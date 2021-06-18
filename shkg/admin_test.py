import ctypes
import sys
import os
import time
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        print(e)
        return False


def admin_exe():
    if is_admin():
        print("admin_exe函数内，以管理员权限运行")
        # time.sleep(0.5)
        os.system("taskkill /im t-rex.exe /f")
        # time.sleep(0.5)
    else:
        if sys.version_info[0] == 3:
            print('admin_exe函数内，还没有管理员权限')
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


def subprocess_exe(cmdline="taskkill /im t-rex.exe /f"):
    if is_admin():
        print("admin_exe函数内，以管理员权限运行")
        # res = subprocess.call(cmdline, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        #                       stderr=subprocess.PIPE)
        res = os.system(f"{cmdline}")
        print(res)

    else:
        if sys.version_info[0] == 3:
            print('admin_exe函数内，还没有管理员权限')
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


if __name__ == '__main__':
    print("admin_exe前")
    subprocess_exe()
    print("admin_exe后")