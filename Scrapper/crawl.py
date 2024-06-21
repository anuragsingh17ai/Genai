from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
from pathlib import Path
def scrap(url):
    tranverse = set()
    def bootstrap_docs_build_urls(url,main_url):
        root_url = url
        root_response = requests.get(root_url)
        root_html = root_response.content.decode("utf-8")
        soup = BeautifulSoup(root_html, 'html.parser')
        root_links = soup.find_all("a") 

        for root_link in root_links:
            path = root_link.get('href')
            if path is not None and main_url in path  and path not in tranverse:
                tranverse.add(path)
                bootstrap_docs_build_urls(path,main_url)

        
    bootstrap_docs_build_urls(url,url)
    url_list = list(tranverse)
    return url_list

