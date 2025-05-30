from rstatus import RStatusClient
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule

# create a rich console instance for styled output
console = Console()

# function to check the status of a minecraft server
def servercheck(ip_port):
    # join input arguments into a single string
    ip_port = ''.join(ip_port)
    try:
        # print a styled rule as a header
        console.print(Rule(title="[bold cyan]🌐 Server Status Checker[/bold cyan]", characters="━"))

        # initialize the rstatus client with the given ip and port
        client = RStatusClient(ip_port)

        # fetch server data (without using a bot)
        server_data = client.get_server_data(bot=False)

        # if server data is received, print info in a styled panel
        if server_data:
            console.print(
                Panel.fit(
                    f"[bold blue]📍 IP:[/bold blue] [bold yellow]{server_data.ip_address}[/bold yellow]\n"
                    f"[bold blue]👥 Players Online:[/bold blue] [bold green]{server_data.players.online}[/bold green]",
                    title="✅ [bold green]Server Online[/bold green]",
                    border_style="green"
                )
            )

    except Exception as e:
        # handle and print any error that occurs
        console.print(
            Panel.fit(
                f"[bold red]An error occurred:[/bold red]\n[italic]{str(e)}[/italic]",
                title="❌ [bold red]Exception[/bold red]",
                border_style="red"
            )
        )
