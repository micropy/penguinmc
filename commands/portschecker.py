from rstatus import RStatusClient
import sys
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.rule import Rule

# create a rich console instance for styled output
console = Console()

# function to check the status of ports from a list
def portschecker(file):
    # print a styled rule as a section header
    console.print(Rule(title="[bold cyan]🔌 Port Status Checker[/bold cyan]", characters="━"))
    
    # open the file that contains the list of ip:port combinations
    with open(file, encoding="utf-8") as portsfile:
        readedfile = portsfile.readlines()
        
        # iterate over each line in the file
        for row in readedfile:
            row = row.strip()
            try:
                # create a status client using the current ip:port
                client = RStatusClient(row)

                # try to retrieve the server data
                server_data = client.get_server_data(bot=False)

                # create a minimal table to format the server information
                table = Table(box=box.MINIMAL, show_edge=False, expand=True, padding=(0, 1))
                table.add_column("Info", justify="right", style="bold blue")
                table.add_column("Data", justify="left", style="bold yellow")

                # add ip and player info to the table
                table.add_row("🌐 IP", f"{server_data.ip_address}")
                table.add_row("👥 Players", f"[bold green]{server_data.players.online}[/bold green]")

                # print the formatted server data inside a panel
                console.print(Panel.fit(table, title=f"[bold green]✅ {row}[/bold green]", border_style="green"))

            # handle timeout or refused connections separately
            except (TimeoutError, ConnectionRefusedError):
                console.print(
                    Panel.fit(
                        f"[bold red]{row}[/bold red] - [italic]isn't open[/italic]",
                        title="⚠️ [bold red]Connection Error[/bold red]",
                        border_style="red"
                    )
                )

            # handle other exceptions
            except Exception as e:
                console.print(
                    Panel.fit(
                        f"[bold red]Error:[/bold red] {e}",
                        title="❌ [bold red]Exception[/bold red]",
                        border_style="red"
                    )
                )
