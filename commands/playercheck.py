from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box
import requests
import sys

# create a rich console instance for styled output
console = Console()

# function to check mojang player data by username
def playercheck(username):
    # take the first element in case a list is passed
    username = username[0]

    # print a styled section header
    console.rule(f"[bold cyan]🔍 Mojang API Lookup[/bold cyan]")

    # build the mojang api url
    api = f'https://api.mojang.com/users/profiles/minecraft/{username}'

    # send a get request to the api
    response = requests.get(api)

    # if the request is successful and data is returned
    if response.status_code == 200:
        infojson = response.json()

        # create a styled table for displaying player info
        table = Table(title=f"[bold green]Minecraft Profile[/bold green] 🎮", box=box.ROUNDED, expand=False)
        table.add_column("Field", style="bold magenta", justify="center")
        table.add_column("Value", style="bold yellow", justify="center")

        # add rows for username and uuid
        table.add_row("Username", infojson["name"])
        table.add_row("UUID", infojson["id"])

        # print the table
        console.print(table)

    # if the username doesn't exist (no content returned)
    elif response.status_code == 204:
        console.print(
            Panel.fit(f"[bold red]User '{username}' not found.[/bold red]", border_style="red", title="Error ❌")
        )

    # handle other response codes (errors)
    else:
        console.print(
            Panel.fit(f"[bold red]Request failed (status code {response.status_code})[/bold red]", border_style="red", title="Error ⚠️")
        )
