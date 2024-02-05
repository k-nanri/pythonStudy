import click

@click.command()
@click.option("--brithplace", prompt="出身は？")
@click.option("--schoolname", prompt="出身校は？")
def show_your_birthplace(brithplace, schoolname):
    click.echo("brithplace = " + str(brithplace))
    click.echo("schoolname = " + str(schoolname))

if __name__ == '__main__':
    show_your_birthplace()