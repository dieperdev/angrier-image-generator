import os

def clear_data() -> None:
    if os.path.isdir('assets/temp'):
        try:
            os.remove('assets/temp')
        except:
            pass