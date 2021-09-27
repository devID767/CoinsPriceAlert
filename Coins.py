import cloudscraper
from bs4 import BeautifulSoup

import asyncio

def connectToSite():
    url = 'https://opensea.io/collection/monsterbuds?collectionSlug=monsterbuds&search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
    scraper = cloudscraper.create_scraper(
        browser={
            'browser': 'firefox',
            'platform': 'windows',
            'mobile': False
        }
    )
    response = scraper.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    return soup

async def GetPrice():
    soup = connectToSite()
    Coins = []

    coinsDefault = soup.find_all('div', class_="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 SpaceBetweenreact__SpaceBetween-sc-jjxyhg-0 dBFmez jYqxGr gJwgfT")
    currentCount = 0
    maxCount = 5
    for coinDefault in coinsDefault:
        coins = coinDefault.find_all('div',class_="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm Price--amount")
        for coin in coins:
            if currentCount == maxCount:
                break
            Coins.append(float(coin.text))
            print(coin.text)
            currentCount+=1
    Coins.sort()
    return Coins[0]

class Sending:
    _aimprice = 0.0
    def __init__(self, bot, user_id, time, aimprice = 0):
        self._bot = bot
        self.user_id = user_id

        self._aimprice = aimprice

        self._time = time

        self.is_started = False
        self._task = None

    async def Start(self):
        if not self.is_started:
            self.is_started = True
            self._task = asyncio.ensure_future(self._Sending())

    async def Stop(self):
        if self.is_started:
            self.is_started = False
            self._task.cancel()

    async def _Sending(self):
        pricefirst = await GetPrice()
        oldprice = pricefirst
        price = pricefirst
        while True:
            if self._aimprice > 0:
                if self._aimprice > price:
                    await self._bot.send_message(self.user_id, f'Новая стоимость монеты ниже {self._aimprice} \nА именно: {price}')
            else:
                if price < oldprice:
                    await self._bot.send_message(self.user_id, f'Новая стоимость монеты: {price}')

            oldprice = price

            await asyncio.sleep(self._time)
            price = await GetPrice()
