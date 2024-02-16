from infinaCuantia.sercop import Sercop
import time

with Sercop() as bot:
    bot.get_url_sercop()
    bot.sercop_report()     
    #bot.next_page()
