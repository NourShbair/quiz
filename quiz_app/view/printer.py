
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import shutil


colorama_init()

def colored_print(text, color, position):
    """
    This function to customize the print function to produce
    interestring user interface by adding text colors
    """
    if position == "center":
        columns = shutil.get_terminal_size().columns
        text = text.center(columns)
    print(f"{color}+{text}+{Style.RESET_ALL}")


def colored_print_fb(text, color, back_color, position):
    """
    This function to customize the print function to produce
    interestring user interface by adding front and back colors
    """
    if position == "center":
        columns = shutil.get_terminal_size().columns
        text = text.center(columns)
    print(f"{color}+{back_color}+{text}+{Style.RESET_ALL}")

