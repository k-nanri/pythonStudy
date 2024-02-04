import click

@click.command()
@click.option('--username')
@click.option("--job", envvar="JOB")
def hello(username, job):

    click.echo("username = " + str(username))
    click.echo("job      = " + str(job))

if __name__ == "__main__":
    hello(auto_envvar_prefix="HELLO")