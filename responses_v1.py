#### Project name: Alfred Bot
### File: responses.py
## Function: processing of the bots' chat replies to declutter main python file
# Creation Date // Last Updated: 03/12/2022 // 10/12/2022

from random import randint
import requests

# process news request for good morning
newsapi = 'YOUR NEWS API KEY'

news_url_de = "https://newsapi.org/v2/top-headlines?country=de&pageSize=1&apiKey="+newsapi
news_de = requests.get(news_url_de).json()
article_de = news_de["articles"]
title_de = article_de[0]["title"]
url_de = article_de[0]["url"]

news_url_ca = "https://newsapi.org/v2/top-headlines?country=ca&pageSize=1&apiKey="+newsapi
news_ca = requests.get(news_url_ca).json()
article_ca = news_ca["articles"]
title_ca = article_ca[0]["title"]
url_ca = article_ca[0]["url"]

# process crypto prices for good morning
btc_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
btc_data = requests.get(btc_url).json()
btc = btc_data['price']

eth_url = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
eth_data = requests.get(eth_url).json()
eth= eth_data['price']

# grocery list formatting help
def formatgrocery(grocerylist):
    text = ""
    for item in grocerylist:
        text = text + "> " + item + "\n"
    
    return text

# help text for /help
helptext="""
I'm a very versatile little assistant and can assist you in many different ways:

Basic Functions
/meditation - turn on/off playful daily meditation/mindfulness reminder
/remindme <time> <message> - message yourself in the future, no matter if it's a reminder or just saying hi :)
--> accepted input: minutes and hours, e.g. "/remindme 30m <text>" or "/remindme 1h <text>"

Good Morning
/gm - enable/disable morning briefs
/gm trigger - trigger morning brief manually

Grocery List
/grocery add <item> - add item to shopping list
/grocery remove <item> - remove item from shopping list
/grocery view - view shopping list
"""

# pool of quotes to pick from for good morning message
quote_pool=[
    'Dont take life/yourself so seriously (unattributed)', 
    'Think less, do more (unattributed)', 
    'The only constant is change (Heraclitus)',
    'The master has failed more times than the beginner has even tried (Stephen McCranie)',
    'Compare yourself to who you were yesterday, not to who someone else is today (Jordan B. Peterson, Rule 4',
    'You know, my father used to say, whatever you do, do it 100%. When you work, work. When you laugh, laugh. When you eat, eat like it\'s your last meal. (Tony Lip, Green Book)',
    'Yesterday is history, tomorrow is a mystery, but today is a gift that is why it is called the present. (Master Oogway)',
    'Whatever you do in this life, it\'s not legendary, unless your friends are there to see it. (Barney Stinson)',
    'The trick is to choose trouble for oneself in the direction of what one would like to become at a level of difficulty close to the edge of one\'s competence.',
    'Plant trees under whose shade you do not plan to sit. (Jay Shetty)',
    'We\'re all going to die, all of us. What a circus! That alone should make us love each other, but it doesn\'t. We are terrorized and flattened by life\'s trivialities; we are eaten up by nothing. (Charles Bukowski)',
    'A healthy person wants a thousand things, a sick person only wants one. (Confucius)'
]

# good morning message formatting
gm_text="""
<b>Good morning</b> ya lazy bum. Hope you slept enough and well &#x1F970

Here's some food for thought to start your day off right: 
<i>{quote}</i>  &#x1F9E0

To prevent you from becoming even more stupid here's two news stories from Germany and Canada I picked out just for you. &#x1F4F0
🇩🇪 <a href="{url_de}">{title_de}</a>
🇨🇦 <a href="{url_ca}">{title_ca}</a>

&#x1F4C8 Relevant stonks: BTC is currently at {btcprice:.2f}$ and ETH at {ethprice:.2f}$

Have a nice day! &#x1F496
""".format(quote=quote_pool[randint(0,11)], url_de=url_de, title_de=title_de, url_ca=url_ca, title_ca=title_ca, btcprice=float(btc), ethprice=float(eth))

# meditation reminder text
med_text = """
    Have you meditated today already? Treat yourself!
    """

# help variable to store remindme data
event = ""