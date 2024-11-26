#This file to declare all the colors constants to use by colorama
from colorama import init as colorama_init
from colorama import Fore
from colorama import Back
from colorama import Style
import shutil


RED = Fore.RED
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
GREEN = Fore.GREEN
WHITE = Fore.WHITE
BLACK = Fore.BLACK

B_RED = Back.RED
B_YELLOW = Back.YELLOW
B_BLUE = Back.BLUE
B_MAGENTA = Back.MAGENTA
B_CYAN = Back.CYAN
B_GREEN = Back.GREEN
B_WHITE = Back.WHITE
B_BLACK = Back.BLACK



columns = shutil.get_terminal_size().columns
CENTER_SPACE = " " * (columns//2)



WELCOME_MESSAGE = """
                                            ▒█░░▒█ █▀▀ █░░ █▀▀ █▀▀█ █▀▄▀█ █▀▀ 　 ▀▀█▀▀ █▀▀█ 　 ▀▀█▀▀ █░░█ █▀▀ 　 █░░█ █░░ ▀▀█▀▀ ░▀░ █▀▄▀█ █▀▀█ ▀▀█▀▀ █▀▀ 
                                            ▒█▒█▒█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀ 　 ░░█░░ █░░█ 　 ░░█░░ █▀▀█ █▀▀ 　 █░░█ █░░ ░░█░░ ▀█▀ █░▀░█ █▄▄█ ░░█░░ █▀▀ 
                                            ▒█▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀ 　 ░░▀░░ ▀▀▀▀ 　 ░░▀░░ ▀░░▀ ▀▀▀ 　 ░▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀░░░▀ ▀░░▀ ░░▀░░ ▀▀▀ 

                                                                    █▀▀█ █░░█ ░▀░ ▀▀█ 　 █▀▀ █░░█ █▀▀█ █░░ █░░ █▀▀ █▀▀▄ █▀▀▀ █▀▀ 
                                                                    █░░█ █░░█ ▀█▀ ▄▀░ 　 █░░ █▀▀█ █▄▄█ █░░ █░░ █▀▀ █░░█ █░▀█ █▀▀ 
                                                                    ▀▀▀█ ░▀▀▀ ▀▀▀ ▀▀▀ 　 ▀▀▀ ▀░░▀ ▀░░▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀▀ ▀▀▀
"""