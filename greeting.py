from telegram.ext import Updater, CommandHandler
import telegram
import os


class GreetingBot:

    def greet(self):
        bot = telegram.Bot(os.environ["TELEGRAM_BOT_TOKEN"])
        message = bot.send_message(chat_id='-1001098649642',text="Welcome to <b>FansUnite</b> - The Protocol for Sports Betting Applications. Check out our <a href='https://fansunite.io'>Website</a> for more details. \n\nPlease note the core team all reside in Vancouver PST, we'll get to your questions as soon as we're awake :)",parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)

if __name__ == '__main__':
    c = GreetingBot()

    c.greet()