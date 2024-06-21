import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


class Data:
    def __init__(self) -> None:
        """Initialization"""

    async def fetch_urls_from(self, url: str, domain: str) -> set:
        self._urls = set()
        await self._fetch_recursive(url, domain)
        return self._urls

    async def _fetch_recursive(self, url: str, domain: str):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=3) as response:
                    if response.status == 200:
                        html = await response.text()
                        soup = BeautifulSoup(html, 'html.parser')
                        tasks = []
                        for link in soup.find_all('a', href=True):
                            href = link['href']
                            absolute_url = urljoin(url, href)
                            if self._is_valid_webpage(absolute_url, domain):
                                if absolute_url not in self._urls:
                                    self._urls.add(absolute_url)
                                    tasks.append(self._fetch_recursive(absolute_url, domain))
                        await asyncio.gather(*tasks)
        except Exception as e:
            pass

    def _is_valid_webpage(self, url: str, domain: str) -> bool:
        parsed_url = urlparse(url)
        if parsed_url.scheme not in ['http', 'https']:
            return False
        if parsed_url.netloc != domain:
            return False
        if parsed_url.path.endswith(('.pdf', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp')):
            return False
        return True


async def main():
    url = 'https://www.kccitm.edu.in/'
    domain = urlparse(url).netloc
    fetch = Data()
    urls = await fetch.fetch_urls_from(url, domain)
    print(urls)

if __name__ == "__main__":
    asyncio.run(main())
