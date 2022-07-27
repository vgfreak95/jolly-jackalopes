import click
import uvicorn
import aiohttp
import asyncio


# When the is ran as script accept args
@click.command()
@click.option("--name", prompt="Please enter your name", help="Enters your name")
def say_name(name: str):
    """This will just give the users name back"""
    click.echo(f"Welcome {name}")


@click.group()
def cli():
    """This function acts as the cli tool group to add commands."""
    ...


@cli.command()
@click.option("--host", help="The host to run the server on")
@click.option("--port", help="This is your port")
@click.option("--uses_https", help="This is your host name")
@click.option("--dev_mode", help="This is your host name")
def serve(host: str, port: int, uses_https: bool, dev_mode: bool):
    """This starts the server when the user calls this command"""
    uvicorn.run("server:app", host=host, port=port, log_level="info")


@cli.command()
@click.option("--host", help="The host to run the server on")
@click.option("--port", help="This is your port")
@click.option("--bug", help="This allows you to toggle bugs")
def connect(host: str, port: int, bug: bool):
    """This allows the user to connect to the hostname"""
    session = aiohttp.ClientSession()

    async def wrapper():
        async with session.ws_connect(f"http://{host}:{port}/ws") as ws:
            async for msg in ws:  # Get message from server
                if msg.type == aiohttp.WSMsgType.TEXT:
                    if msg.data == "close cmd":
                        await ws.close()
                        break
                    else:
                        # print("Hello World")
                        await ws.send_str("Hello world")
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    break

    loop = asyncio.get_event_loop()
    coroutine = wrapper()
    loop.run_until_complete(coroutine)
