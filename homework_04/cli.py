import asyncio
import typer

import models

cli = typer.Typer()


@cli.command()
def db_init_models():
    asyncio.run(models.init_models())
    print("Done")


if __name__ == "__main__":
    cli()
