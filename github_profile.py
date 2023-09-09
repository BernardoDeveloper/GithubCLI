import typer

from convert_ascii import convert_image_to_ascii
from get_avatar import get_avatar
from get_markdown import get_markdown

from typing_extensions import Annotated
from typing import Optional
from rich import print

def main(profile: Annotated[Optional[str], typer.Argument()] = None):
    try:
        URL = "https://api.github.com/users/"

        if profile == "" or profile == None:
            profile = input("Type the profile name: ")
    
        URL += profile
        
        print("Acessing...\nURL: ", URL)
        get_avatar(URL)
        print("\n\t\t~~~\n")
        get_markdown(profile)
    except Exception:
        typer.echo(typer.style("[ERROR]: Code is not running", fg=typer.colors.RED))
        print(Exception)

if __name__ == "__main__":
    typer.run(main)