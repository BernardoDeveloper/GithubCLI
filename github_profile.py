import requests
import typer
from convert_ascii import convert_image_to_ascii

from typing_extensions import Annotated
from typing import Optional
from rich import print

def main(profile: Annotated[Optional[str], typer.Argument()] = None):
    try:
        URL = "https://api.github.com/users/"

        # If don't has a parameter, answer to user
        if profile == "" or profile == None:
            profile = input("Type the profile name: ")
    
        URL += profile
        
        print("Acessing...\nURL: ", URL)
        
        response = requests.get(URL)
        if response.status_code == 200:
            # Download github avatar
            img_url = response.json().get("avatar_url")

            path_img = "image.jpg"
            fp = open(path_img, "wb")
            fp.write(requests.get(img_url).content)
            fp.close()

            print(convert_image_to_ascii(path_img))
            print("\n==================================\n")
        else:
            print("Failed to request")
        
        # Markdown File
        markdown_url = "https://raw.githubusercontent.com/" + profile + "/" + profile + "/main/README.md"
        'Requests:' in markdown_url
        markdown = requests.get(markdown_url)
        markdown.headers['Content-Type']

        if markdown.status_code == 200:
            print(markdown.text)
        else:
            print("This profile don't has README.md file")
    except Exception:
        typer.echo(typer.style("[ERROR]: Code is not running", fg=typer.colors.RED))
        print(Exception)

if __name__ == "__main__":
    typer.run(main)