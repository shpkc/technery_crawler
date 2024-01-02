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
        default_img = "https://images.unsplash.com/photo-1547394765-185e1e68f34e?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fGNvbXB1dGVyfGVufDB8fDB8fHww"
        return default_img