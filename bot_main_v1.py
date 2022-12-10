#### Project name: Alfred Bot
### File: telegram.py main source code file
## Function: main program 
# Creation Date // Last Updated: 01/12/2022 // 10/12/2022

# imports
import telegram.ext
import responses
import datetime
import sqlite3
import config
from random import randint

# Basic Initialization of Alfred Bot
TOKEN = config.API_KEY
updater = telegram.ext.Updater(TOKEN, use_context=True)
dp = updater.dispatcher


## Good Morning Message

def gm_message(context):
    chat_id = context.job.context
    context.bot.send_message(text=responses.gm_text, chat_id= chat_id, parse_mode='HTML', disable_web_page_preview=True)

def gm_toggle(update, context):

    chat_id = update.effective_message.chat_id
    job_gm = context.job_queue.get_jobs_by_name("jobqueue_gm")[0]

    if context.args:
        if context.args[0] == "trigger":
            update.message.reply_text("Prompt sent. This is the current configuration of your morning brief:")
            context.job_queue.run_once(gm_message, 1, context=chat_id)
        else:
            update.message.reply_text("I don't understand that, sorry. :(")
        
    else:
        if job_gm.enabled:
            job_gm.enabled = False
            update.message.reply_text("Good morning message disabled.")
        else:
            job_gm.enabled = True
            update.message.reply_text("Good morning message enabled.")


## Grocery List

def grocery(update, context):

    if context.args:
        if context.args[0] == "add":
            cursor.execute(
                "INSERT INTO list VALUES(NULL, ?)",
                 (context.args[1],)
            )
            update.message.reply_text("Succesfully added {item} to your grocery list!".format(item=context.args[1]))

        elif context.args[0] == "remove":
            cursor.execute(
                "DELETE FROM list WHERE item_name = ?", 
                (context.args[1],)
            )
            update.message.reply_text("Succesfully removed {item} from your grocery list!".format(item=context.args[1]))

        elif context.args[0] == "view":
            current_list = cursor.execute(
                "SELECT item_name FROM list"
            ).fetchall()

            result = [tup[0] for tup in current_list]

            update.message.reply_text("Your current grocery list:")
            update.message.reply_text(responses.formatgrocery(result))

    else:
        update.message.reply_text("I don't understand that, sorry. :(")


## Different functions:

# start function for very beginning
def start_command(update, context):
    chat_id = update.effective_message.chat_id

    update.message.reply_text("Welcome! I can help you manage your life. Use the help command to figure out everything I can do. :)")

    job_med = context.job_queue.run_daily(med_text, time=datetime.time(randint(config.GM_INT_START, config.GM_INT_END), randint(0,59)), context=chat_id, name = "jobqueue_med")
    job_gm = context.job_queue.run_daily(gm_message, time=datetime.time(randint(config.GM_INT_START, config.GM_INT_END), randint(0,59)), context = chat_id, name="jobqueue_gm")

# help function
def help_command(update, context):
    update.message.reply_text(responses.helptext)

# toggle meditation reminder
def med_toggle(update, context):
    job_med = context.job_queue.get_jobs_by_name("jobqueue_med")[0]

    if job_med.enabled == True:
        update.message.reply_text("Meditation reminder disabled.")
        job_med.enabled = False
    elif job_med.enabled == False:
        update.message.reply_text("Meditation reminder enabled.")
        job_med.enabled = True

# meditation message
def med_text(context):
    chat_id = context.job.context
    context.bot.send_message(chat_id=chat_id,text=responses.med_text,parse_mode='HTML')

# remindme in x amount of time
def remindme(update, context):
    chat_id=update.effective_message.chat_id

    time = context.args[0]
    event = ""
    i = 1

    while i<len(context.args):
        event = event + context.args[i] + " "
        i = i+1

    responses.event = event

    if time[-1] == "m":
        temp_time = time[:-1]
        time = int(temp_time)*60
        update.message.reply_text("Reminder set in {minute} minutes!".format(minute = temp_time))
    elif time[-1] == "h":
        temptime = time[:-1]
        time = int(temp_time)*3600
        update.message.reply_text("Reminder set in {hour} hours!".format(hour = temp_time))
    else:
        update.message.reply_text("I don't understand that, sorry. :(")

    context.job_queue.run_once(remindme_text, time, context=chat_id)

def remindme_text(context):
    chat_id = context.job.context
    context.bot.send_message(text=responses.event, chat_id=chat_id)


if __name__ == '__main__':

    # database connection
    connection = sqlite3.connect("grocerylist.db", check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS list (item_id INTEGER PRIMARY KEY AUTOINCREMENT, item_name TEXT)")

    # command handlers
    dp.add_handler(telegram.ext.CommandHandler('start', start_command))
    dp.add_handler(telegram.ext.CommandHandler('help', help_command))
    dp.add_handler(telegram.ext.CommandHandler('gm', gm_toggle, pass_args=True))
    dp.add_handler(telegram.ext.CommandHandler('grocery', grocery, pass_args=True))
    dp.add_handler(telegram.ext.CommandHandler('meditation', med_toggle))
    dp.add_handler(telegram.ext.CommandHandler('remindme', remindme, pass_args=True))

    # run the bot
    updater.start_polling(1.0)
    updater.idle()   