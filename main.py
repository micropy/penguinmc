import subprocess
import os
import sys
from rich.console import Console
from commands.help import *
from commands.playercheck import *
from commands.servercheck import *
from commands.portschecker import *
from commands.checksubdomains import *

# create console to use rich

console = Console()

# execute botsjoining.js

def do_botsjoining(arg):
    arg_splitted = ''.join(arg).split(':')
    subprocess.run(['node', 'commands//botsjoining.js'] + arg_splitted)

# execute checkpassword.js

def do_checkpassword(arg):
    ''.join(arg).split(':')
    subprocess.run(['node', 'commands//checkpassword.js'] + arg)

# dict with commands

actions = {
    'servercheck': servercheck,
    'botsjoining': do_botsjoining,
    'playercheck': playercheck,
    'checkpassword': do_checkpassword,
    'portschecker': portschecker,
    'checksubdomains': execute_with_threading,
    'help': help
}

def menu():
    console.print("[bold blue]PenguinMC[/bold blue]")
    arg = input("> ").split()
    # check if command exists and then execute the command 
    if arg[0] in actions and len(arg) < 2:
        actions[arg[0]]()
    elif arg[0] in actions:
        actions[arg[0]](arg[1:])
    else:
        # if command not exists
        console.print(f"[bold red][+][/bold red] Unknown command: \"{arg[0]}\" write [bold green]help[/bold green] for a list of commands")
print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠺⠓⠢⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠉⠚⠓⠚⡭⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⢜⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡡⠒⠒⠒⠀⠁⠀⠱⡤⢤⣤⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡠⢺⠀⠀⠀⠀⠀⠀⠀⠀⢳⣁⡀⠈⠹⡳⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡠⡴⢾⠂⢸⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠈⠙⠢⡇⡇⠀⠀⠀⠀
⠀⠀⢀⢔⠝⠊⣀⠼⠔⠺⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠈⠀⠀⠀⠀⠀
⠀⡰⡱⢁⡴⠋⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀
⢰⠁⡥⠋⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠛⠁⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⢀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢸⠀⠀⢀⠂⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⢸⢀⣀⣸⠉⠉⠰⣂⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣘⡖⣹⡁⠀⠀⠓⠺⠉⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠷⠄⠸⠑⠂⠀⠀⠀⠀⠻⠛⠓⠻⠇⠒⠒
""")
while True:
    menu()