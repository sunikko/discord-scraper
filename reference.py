# This is a simple web scraper that uses BeautifulSoup to scrape job postings from a website.
# It sends a GET request to the specified URL with the given parameters and prints the status code of the response.
# [?|&](\w+)=([^\w+]) # 아무런 데이터가 없는거 제거
# (\w+)=(\w+)&? -> replae: "$1":"$2",\n  파라미터 제이슨타입으로 변경 그냥 replace로 바꾸면 된다!!
# (?<=\?)\w+=[^&]+&? -> replace: "$1":"$2",\n  파라미터 제이슨타입으로 변경 그냥 replace로 바꾸면 된다!!

# url = 'https://uk.indeed.com/cmp/Framestore?'

# params = {"from":"mobviewjob",
# "tk":"1iphq0q0s2g5o000",
# "fromjk":"65b1343039bbd37c",
# "attributionid":"mobvjcmp",}

# url = "https://finance.yahoo.com/quote/NQ%3DF/?"

# params = { "guccounter":"1",
# "guce_referrer":"aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8",
# "guce_referrer_sig":"AQAAALzc00FVi1JNNm0sJUawMiRcl61sTtGptOyRowhXJNX9_JDp1WjoDVNJYj5oRkb23DpgjfOEkRAyfo3VOkntXujsPZob-NcYt28U1LO1EGHhjKq0AhMAvJ5OCs676XfzkrXY44A4Ao0zpicjqKFZ3E-TAcw9sGj-qYIAy8v56BTb",}

class Scrapper:
    def __init__(self):        
        self.__url = 'https://www.amazon.co.uk/s?'

        self.__params = {"k":"fathers+day+gifts",
                "crid":"1OWFS0AIWHSTL",
                "sprefix":"fathers%2Caps%2C144",
                "ref":"nb_sb_ss_ts-doa-p_1_7",}
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.106 Safari/537.36',
            'Referer': 'https://uk.indeed.com/',
            'Accept-Language': 'en-US,en;q=0.9'
        }

        # response = requests.get(url, "params":"params",)
        # print(response.status_code)

        # 이렇게 하고  python3 scraper.py 하면 403 에러 발생. 봇에 의한 접근 방지 -> 해결을 위해
        # navigator.userAgent를 크롬 인스펙터에서 해보자.
        # headers = headers 추가
    def scrape(self):
        response = requests.get(self.__url, params=self.__params, headers=self.__headers)
        # print(response.text)
        # print(f"Status Code: {response.status_code}") 
        # print(self.__url, self.__params)

        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.prettify())
        items = soup.find_all('div', role='listitem')
        # items = soup.find('div', attrs={'role': 'listitem'})

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



'''

dis cord
https://discord.com/developers/build

https://discordpy.readthedocs.io/en/stable/

https://discordpy.readthedocs.io/en/stable/intro.html

python3 -m pip install -U discord.py

https://discordpy.readthedocs.io/en/stable/api.html?highlight=embed#discord.Embed

'''

