


import logging


from settings import BOT_TOKEN

from tarjimon import tarjima_qil


from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
    ReplyKeyboardMarkup
)
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
    MessageHandler,
    Filters,
)




# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND = 'bir', 'ikki'
# Callback data
ONE, TWO, THREE, FOUR = range(4)

main_buttons = ReplyKeyboardMarkup([
	["⚙️ Til sozlamalari 🔧"]
	],
    resize_keyboard=True
)

tillar = {
    'uz': '🇺🇿 Uzbek',
    'ru': '🇷🇺 Russian',
    'en': '🇬🇧 English',
    'auto': '🔍 Avtomatik'
}

til1 = 'auto'
til2 = 'uz'







def start(update: Update, context: CallbackContext):
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    username = update.effective_user.full_name
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [
            InlineKeyboardButton("🇺🇿 Uzbek 🇺🇿", callback_data=str(ONE)),
            InlineKeyboardButton("🇬🇧 English 🇺🇸", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("🇷🇺 Russian 🇷🇺", callback_data=str(THREE)),
            InlineKeyboardButton("🔎 Avtomatik 🔍", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_html(
        f"<b>Assalom-u alaykum, <i> {username}</i> </b>\n\n\
🤖 Men <b>iTarjimon_bot'</b>man 🌐\n\
Istalgan tildagi matnlarni uch tildan biriga tarjima qila olaman")

    update.message.reply_html("<b>Birinchi tilni tanlang:</b> \n\n\
Bunda agar <i>\"Avto\"</i> tanlansa, kiritilgan matn tili \
<i>bot</i> tomonidan <u>avtomatik</> aniqlanadi ", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST


def reset(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("🇺🇿 Uzbek 🇺🇿", callback_data=str(ONE)),
            InlineKeyboardButton("🇬🇧 English 🇺🇸", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("🇷🇺 Russian 🇷🇺", callback_data=str(THREE)),
            InlineKeyboardButton("🔎 Avtomatik 🔍", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_html("<b>Tilni qayta sozlash</b>")
    update.message.reply_html("<b>Birinchi tilni tanlang: </b> \n\
Bunda agar <i>\"Avto\"</i> tanlansa, kiritilgan matn tili \
<i>bot</i> tomonidan <u>avtomatik</> aniqlanadi ", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST


def ortga(update: Update, context: CallbackContext):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🇺🇿 Uzbek 🇺🇿", callback_data=str(ONE)),
            InlineKeyboardButton("🇬🇧 English 🇺🇸", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("🇷🇺 Russian 🇷🇺", callback_data=str(THREE)),
            InlineKeyboardButton("🔎 Avtomatik 🔍", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    query.edit_message_text(text="Birinchi tilni tanlang: \n\n\
Bunda agar \"Avto\" tanlansa, kiritilgan matn tili \
bot tomonidan avtomatik aniqlanadi ", reply_markup=reply_markup)

    return FIRST



def funka1(update: Update, context: CallbackContext):
    """Show new choice of buttons"""
    global til1
    til1 = 'uz'
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🇬🇧 English 🇺🇸", callback_data=str(TWO)),
            InlineKeyboardButton("🇷🇺 Russian 🇷🇺", callback_data=str(THREE)),
        ],
        [
            InlineKeyboardButton("🔙 Ortga", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Ikkinchi tilni tanlang: ⤵️", reply_markup=reply_markup
    )
    return SECOND

def funka2(update: Update, context: CallbackContext):
    """Show new choice of buttons"""
    global til1
    til1 = 'en'
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🇺🇿 Uzbek 🇺🇿", callback_data=str(ONE)),
            InlineKeyboardButton("🇷🇺 Russian 🇷🇺", callback_data=str(THREE)),
        ],
        [
            InlineKeyboardButton("🔙 Ortga", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Ikkinchi tilni tanlang: ⤵️", reply_markup=reply_markup
    )
    return SECOND

def funka3(update: Update, context: CallbackContext):
    """Show new choice of buttons"""
    global til1
    til1 = 'ru'
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🇺🇿 Uzbek 🇺🇿", callback_data=str(ONE)),
            InlineKeyboardButton("🇬🇧 English 🇺🇸", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("🔙 Ortga", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Ikkinchi tilni tanlang: ⤵️", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return SECOND

def funka4(update: Update, context: CallbackContext):
    """Show new choice of buttons"""
    global til1
    til1 = 'auto'
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🇺🇿 Uzbek 🇺🇿", callback_data=str(ONE)),
            InlineKeyboardButton("🇬🇧 English 🇺🇸", callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("🇷🇺 Russian 🇷🇺", callback_data=str(THREE)),
            InlineKeyboardButton("🔙 Ortga", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Ikkinchi tilni tanlang: ⤵️", reply_markup=reply_markup
    )
    return SECOND



def funkb1(update: Update, context: CallbackContext):
    global til2
    til2 = 'uz'
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("⚙️ Til sozlamalari 🔧", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=f"Siz  \"{tillar[til1]} — {tillar[til2]}\"  tillarini tanladingiz",
        reply_markup=reply_markup
    )
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Tarjima qilish uchun biror matn kiriting: ",
                             reply_markup = main_buttons)
    return SECOND

def funkb2(update: Update, context: CallbackContext):
    global til2
    til2 = 'en'
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("⚙️ Til sozlamalari 🔧", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=f"Siz  \"{tillar[til1]} — {tillar[til2]}\"  tillarini tanladingiz",
        reply_markup=reply_markup
    )
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Tarjima qilish uchun biror matn kiriting: ",
                             reply_markup = main_buttons)
    return SECOND

def funkb3(update: Update, context: CallbackContext):
    global til2
    til2 = 'ru'
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("⚙️ Til sozlamalari 🔧", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=f"Siz  \"{tillar[til1]} — {tillar[til2]}\"  tillarini tanladingiz",
        reply_markup=reply_markup
    )
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Tarjima qilish uchun biror matn kiriting: ",
                             reply_markup = main_buttons)
    return SECOND



def tarjimon(update: Update, context: CallbackContext):
    txt = update.message.text
    tarj = tarjima_qil(txt, til1, til2)
    update.message.reply_text(tarj)

def end(update: Update, context: CallbackContext):
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="See you next time!")
    return ConversationHandler.END


def main():
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start),],
        states={
            FIRST: [
                CallbackQueryHandler(funka1, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(funka2, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(funka3, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(funka4, pattern='^' + str(FOUR) + '$'),
                CommandHandler('reset', reset),
                MessageHandler(Filters.regex(r"⚙️ Tilni qayta sozlash 🔧"), reset),
                MessageHandler(Filters.text & ~Filters.command & ~Filters.regex(r'⚙️ Til sozlamalari 🔧'), tarjimon),
            ],
            SECOND: [
                CallbackQueryHandler(funkb1, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(funkb2, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(funkb3, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(ortga, pattern='^' + str(FOUR) + '$'),
                CommandHandler('reset', reset),
                MessageHandler(Filters.regex(r"⚙️ Til sozlamalari 🔧"), reset),
                MessageHandler(Filters.text & ~Filters.command & ~Filters.regex(r'⚙️ Til sozlamalari 🔧'), tarjimon),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Add ConversationHandler to dispatcher that will be used for handling updates
    dispatcher.add_handler(conv_handler)



    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    try:
        main()
    except:
        print("Xatolik yuz berdi")
