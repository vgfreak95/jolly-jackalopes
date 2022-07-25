import click
import uvicorn


# When the is ran as script accept args
@click.command()
@click.option("--name", prompt="Please enter your name", help="Enters your name")
def say_name(name: str):
    """This will just give the users name back"""
    click.echo(f"Welcome {name}")


@click.group()
def cli():
    """
    This function acts as the cli tool group to add commands.
    """
    ...


@cli.command()
@click.option("--host", help="The host to run the server on")
@click.option("--port", help="This is your port")
@click.option("--uses_https", help="This is your host name")
@click.option("--dev_mode", help="This is your host name")
def serve(host: str, port: int, uses_https: bool, dev_mode: bool):
    """
    This starts the server when the user calls this command
    """
    uvicorn.run("server:app", port=port, log_level="info")
