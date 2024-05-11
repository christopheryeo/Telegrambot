from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram import Update

# Define a function to handle the /start command
def start(update: Update, context):
    update.message.reply_text('Hello! I am your bot.')

# Define a function to handle normal text messages
def echo(update: Update, context):
    update.message.reply_text(update.message.text)

def main():
    # Replace 'YOUR_TOKEN' with your actual bot token
    updater = Updater(token='6391436339:AAHhDbn8YnGN7VaUXaVzZMdUy64dYQesuNo', use_context=True)
    dispatcher = updater.dispatcher

    # Add handlers for /start and text messages
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text & ~Filters.command, echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
