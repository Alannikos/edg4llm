from pyfiglet import Figlet
from termcolor import colored

def display_ascii_art():
    f = Figlet(font="straight", width=200)
    ascii_art = f.renderText("WELCOME TO EDG4LLM")

    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]

    for i, line in enumerate(ascii_art.splitlines()):
        print(colored(line, colors[i % len(colors)]))

if __name__ == "__main__":
    display_ascii_art()
