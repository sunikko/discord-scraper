from bs4 import BeautifulSoup
import requests


class Scraper:
    def __init__(self):        
        self.__url = 'https://www.amazon.co.uk/s?'

        self.__params = {"k":"fathers+day+gifts",
                "crid":"1OWFS0AIWHSTL",
                "sprefix":"fathers%2Caps%2C144",
                "ref":"nb_sb_ss_ts-doa-p_1_7",}
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.106 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }

    def scrape(self):
        response = requests.get(self.__url, params=self.__params, headers=self.__headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('div', role='listitem')

        stocks = []
        for item in items:
            stock_title = None
            stock_price = None
            img_url = None
            stock_url = None
            containder_div = item.find('div', class_='s-product-image-container')
            if containder_div:
                img_div = containder_div.find('img')
                if img_div:
                    img_url = img_div.get('src')

                url = containder_div.find('a')
                if url:
                    stock_url = "https://www.amazon.co.uk/" + url.get('href')

            title_div = item.find('div', attrs={'data-cy': 'title-recipe'})
            if title_div:
                span = title_div.find('span')
                if span:
                    stock_title = span.get_text(strip=True)

            title_div = item.find('div', attrs={'data-cy': 'price-recipe'})
            if title_div:
                span = title_div.find('span', class_='a-offscreen')
                if span:
                    stock_price = span.get_text(strip=True)
            
            if stock_title is not None and "SponsoredSponsored" in stock_title:
                continue
            
            if stock_title and stock_price and img_url and stock_url:
                stock = {
                    'title': stock_title,
                    'price': stock_price,
                    'img_url': img_url,
                    'url': stock_url,
                }
                stocks.append(stock)

        return stocks[:5]
            

if __name__ == "__main__":
    scraper = Scraper()
    scraper.scrape()
