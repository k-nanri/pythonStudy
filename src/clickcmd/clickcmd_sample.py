import click

@click.command()
@click.argument("name")
def hello(name: str):
    click.echo("name: " + name )

if __name__ == "__main__":
    hello()