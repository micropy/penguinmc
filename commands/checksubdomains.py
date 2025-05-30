import random
import dns.resolver
import socket
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

# create a rich console object for styled terminal output
console = Console()

# function to check subdomains of a given domain
def checksubdomains(domain):
    resolver = dns.resolver.Resolver()

    # load resolver IPs from file, removing empty lines
    with open('checksubdomains/resolvers.txt', encoding='utf-8') as resolvers:
        resolvers_list = [row.strip() for row in resolvers if row.strip()]
    
    # load subdomains from wordlist file
    with open("wordlist.txt", encoding='utf-8') as subdomains:
        subdomains_wordlist = [word.strip() for word in subdomains if word.strip()]

        # print a styled rule and panel to indicate start of brute force
        console.rule(f"[bold cyan]🔍 Subdomain Scan on [green]{domain}[/green]")
        console.print(
            Panel(
                Text("BruteForcing subdomains", justify="center"),
                style="bold yellow",
                box=box.ROUNDED
            )
        )

        # iterate through the subdomain wordlist
        for word in subdomains_wordlist:
            full_domain = f"{word}.{domain}"
            # pick a random resolver from the list
            resolver.nameservers = [random.choice(resolvers_list)]

            try:
                # try resolving the full domain to get its IP
                answer = resolver.resolve(full_domain, "A")
                for data in answer:
                    # if resolution is successful, print the result in a styled panel
                    console.print(
                        Panel.fit(
                            f"[bold green]{full_domain}[/bold green] → [blue]{data}[/blue]",
                            title="✅ Found",
                            style="bold green",
                            box=box.HEAVY
                        )
                    )
            except:
                # ignore failed resolutions
                pass

# function to execute checksubdomains using a thread pool
def execute_with_threading(domain):
    if __name__ == "__main__":
        with ThreadPoolExecutor(max_workers=50) as executor:
            # submit the domain scanning task to the thread pool
            future = executor.submit(checksubdomains, domain)
