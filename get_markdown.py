import requests

def get_markdown(profile):
    # Markdown File
    markdown_url = "https://raw.githubusercontent.com/" + profile + "/" + profile + "/main/README.md"
    'Requests:' in markdown_url
    markdown = requests.get(markdown_url)
    # markdown = await asyncio.gather(*map(get_async, markdown_url))
    markdown.headers['Content-Type']

    if markdown.status_code == 200:
        print(markdown.text)