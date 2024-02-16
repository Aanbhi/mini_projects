from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import ReplyKeyboardMarkup

# Define states for the conversation
START, CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(4)

# Initialize conversation data
data = {}

# Function to start the conversation
def start(update, context):
    update.message.reply_text(
        "Hi! I'm your chatbot. What can I do for you?"
    )
    return CHOOSING

# Function to handle user's choice
def choice(update, context):
    user = update.message.from_user
    text = update.message.text
    data['choice'] = text
    reply_keyboard = [['Option 1', 'Option 2']]
    update.message.reply_text(
        f'You chose: {text}. Now, please choose an option:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return TYPING_REPLY

# Function to handle user's reply
def received_information(update, context):
    user = update.message.from_user
    text = update.message.text
    data['reply'] = text
    update.message.reply_text(
        "Thank you for sharing your information!"
    )
    return ConversationHandler.END

# Function to handle user's input error
def user_cancel(update, context):
    update.message.reply_text(
        "I'm sorry, there was an error. Please start over."
    )
    return ConversationHandler.END

def main():
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)

    dp = updater.dispatcher

    # Create a ConversationHandler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [MessageHandler(Filters.text & ~Filters.command, choice)],
            TYPING_REPLY: [MessageHandler(Filters.text & ~Filters.command, received_information)],
        },
        fallbacks=[MessageHandler(Filters.command | Filters.text & ~Filters.regex('^Done$'), user_cancel)],
    )

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if _name_ == '__main__':
    main() 
