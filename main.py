import os
import platform
import time

os.environ['KIVY_NO_FILELOG'] = 'yes'
platform.system = lambda: 'android'

if __name__ == '__main__':
    import sys
    setattr(sys, 'executable', 'PythonService')

    while True:
        try:
            pass
        except Exception as e:
            import traceback
            traceback.print_exc()
            time.sleep(10)
