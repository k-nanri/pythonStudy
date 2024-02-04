import click

@click.command()
@click.option('--password',
              prompt="パスワードを入力してください",
              hide_input=True,
              confirmation_prompt=True)
def hello(password):

    click.echo("入力したパスワード : " + str(password))

if __name__ == "__main__":
    hello()
