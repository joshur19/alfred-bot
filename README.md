# Alfred Bot
### Your very own (very basic) personal assistant!

Welcome to the **Alfred Bot** repository! Here you'll find a friendly and helpful Telegram Bot that can help you with various daily tasks. The current version of Alfred Bot includes:
- Daily Good Morning Brief/Message
- Grocery List
- RemindMe at specific time
- Daily Reminder for Meditation Habit

#### Deploying Alfred Bot
During the period of class presentation for OSS the Bot should be up and running on my laptop, so feel free to search up Alfreds ID "@AlfredTheWizard_Bot" on Telegram and start chatting!

<p align="center"><img src= "https://i.imgur.com/FipSOL0.png" width="300"></p>

If you want to run Alfred Bot at a later date there's a few steps to get him started.
1) Obtain your Telegram API token by contacting @BotFather on Telegram. [Official Documentation here](https://core.telegram.org/bots/tutorial#obtain-your-bot-token) (alternatively just watch a quick YouTube video, it's super easy!)
2) Obtain a NewsAPI key from [newsapi.org](https://newsapi.org/) (simply register an account)
3) Plug in both the Telegram Bot token and your NewsAPI key into the appropriate places in config.py and responses.py, respectively
4) Install the python package "requests" by your preferred method
5) Done! Start up the code and start chatting with your Bot ID on Telegram! 

<p align="center"><img src= "https://i.imgur.com/tRTH13p.png" width="500"></p>

#### Alfred Basics
Use ``/help`` to list all available commands.
``/gm`` toggles your good morning brief from enabled/disabled and vice versa. ``/gm trigger`` prompts the good morning brief a single time.
``/grocery`` only works with arguments, "``add``", "``remove``", "``view``". These are for manipulating and viewing your grocery list.
``/meditation`` toggles your daily meditation reminder.
``/remindme`` is used for reminding yourself of something in x amount of minutes/hours. The syntax is ``/remindme <time> <message>`` in which time is specified by key characters ``m`` for minutes and ``h`` for hours. E.g. ``/remindme 30m bring out trash`` which will remind you to bring out the trash in 30 minutes.

#### Good Morning Brief
Alfred Bot will automatically send you a message every morning. The good morning message currently includes a quote to ponder about, a news story from Canada and one from Germany, and the current BTC and ETH price in USD.
The time interval for this message can be specificed in config.py. If you want news from different countries or other cryptocurrencies listed in the morning brief you can simply tinker around a bit in the responses.py file, it should be pretty self-explanatory.

<p align="center"><img src= "https://i.imgur.com/uwWaRkT.png" width="500"></p>


#### Grocery List
Alfred can also keep track of your groceries! He uses the python sqlite module to create a local database, and can add and remove items to the stored grocery list. Use ``/grocery view`` to view your current groceries!

<p align="center"><img src= "https://i.imgur.com/jxQz1OA.png" width="500"></p>


#### Meidtation Reminder and RemindMe
The meditation reminder is a simple daily reminder that can be toggled with ``/meditation``.
Use ``/remindme`` to remind yourself of various different things!

<p align="center"><img src= "https://i.imgur.com/hM2G62h.png" width="500"></p>

Have fun with Alfred Bot!
