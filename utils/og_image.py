import requests
from bs4 import BeautifulSoup

def og_image(url):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    og_image_tag = soup.find('meta', attrs={'property': 'og:image'})

    if og_image_tag:
        og_image_url = og_image_tag.get('content')
        return og_image_url
    else:
        return None