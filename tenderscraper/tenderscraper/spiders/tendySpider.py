import scrapy
import ssl
import time
import smtplib
from datetime import date
import random


class tendySpider(scrapy.Spider):
    name='tendySpider'

    article_list = []
    
    def start_requests(self): 
        urls=['http://arepublixchickentendersubsonsale.com/']
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]


    def parse(self, response):
        url = response.url
        # print(response.css('title::text').get())
        if response.css('title::text').get() == 'YES THEY ARE!':
            print('Chicken tender subs are on sale, sending text to colins phone') 
            port = 465
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as loggerserver:
                loggerserver.login('csalogger@gmail.com', 'loggerpy')
                # loggerserver.sendmail('csalogger@gmail.com', '2057890837@txt.att.net', 'Chicken Tender subs are on SALE MOTHERFUCKER!!!!')
                time.sleep(1)
                loggerserver.sendmail('csalogger@gmail.com', '8509100769@txt.att.net', 'Chicken Tender subs are on SALE!!!!')
                time.sleep(1)
                # loggerserver.sendmail('csalogger@gmail.com', '8508164533@txt.att.net', 'Chicken Tender subs are on SALE MOTHERFUCKER!!!!')