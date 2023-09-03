# -*- coding: utf-8 -*-

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler

logging.basicConfig(level=logging.INFO)

number_emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]

TOKEN = "6494348560:AAEupohvhLNBNsGfsUsRKmm0lhLXmrpPV0E"

SELECT_ACTION, SELECT_WEEK, SELECT_DAY = range(3)

def start(update, context):
    try:
        logging.info("Handling /start command...")
        keyboard = [
            [InlineKeyboardButton("Week 1", callback_data="Week 1")],
            [InlineKeyboardButton("Week 2", callback_data="Week 2")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("Please select a week:", reply_markup=reply_markup)

        return SELECT_WEEK
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def select_action(update, context):
    query = update.callback_query
    query.answer()

    if query.data == "back":
        keyboard = [
            [InlineKeyboardButton("Week 1", callback_data="Week 1")],
            [InlineKeyboardButton("Week 2", callback_data="Week 2")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.edit_text("Please select a week:", reply_markup=reply_markup)
        return SELECT_WEEK

def select_week(update, context):
    query = update.callback_query
    query.answer()

    if query.data == "back":
        return select_action(update, context)

    context.user_data["selected_week"] = query.data

    keyboard = [
        [InlineKeyboardButton("Monday", callback_data="monday")],
        [InlineKeyboardButton("Tuesday", callback_data="tuesday")],
        [InlineKeyboardButton("Wednesday", callback_data="wednesday")],
        [InlineKeyboardButton("Thursday", callback_data="thursday")],
        [InlineKeyboardButton("Friday", callback_data="friday")],
        [InlineKeyboardButton("Saturday", callback_data="saturday")],
        [InlineKeyboardButton("Back ⬅️", callback_data="back")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(f"{context.user_data['selected_week']} - Please select a day:", reply_markup=reply_markup)

    return SELECT_DAY

def select_day(update, context):
    query = update.callback_query
    query.answer()

    selected_day = query.data

    if selected_day == "back":
        return select_week(update, context)

    selected_week = context.user_data["selected_week"]
    query.edit_message_text(f"{selected_week} - {selected_day} selected.")

    if selected_week == "Week 1" and selected_day == "monday":
        message = "<b>{} Фізика (8:30 - 10:05)</b>\nЛекція Литвинова Т.В".format(number_emojis[0])
        query.message.reply_text(message, parse_mode="HTML")

    if selected_week == "Week 1" and selected_day == "tuesday":
        message = (
            f"<b>{number_emojis[0]} Фізика (8:30 - 10:05)</b>\nКонсультація Литвинова Т.В\n\n"
            f"<b>{number_emojis[1]} Інформаційні технології (10:25 - 12:00)</b>\nЛавренюк А.М.\n\n"
            f"<b>{number_emojis[2]} Українська мова (12:20 - 13:55)</b>\nЛекція Кушлаба М.П.\n\n"
            f"<b>{number_emojis[3]} Інформаційні технології, Програмування (14:15 - 15:50)</b>\n Лабораторна Стасюк О.С. Тарасенко С.А.\n\n"
            f"<b>{number_emojis[4]} Інформаційні технології, Програмування (16:10 - 17:45)</b>\n Лабораторна Стасюк О.С. Тарасенко С.А."
        )
        query.message.reply_text(message, parse_mode="HTML")

    if selected_week == "Week 1" and selected_day == "wednesday":
        message = (
            f"<b>{number_emojis[0]} Алгеом (8:30 - 10:05)</b>\nЛекція Хмельницький М.О\n\n"
            f"<b>{number_emojis[1]} Спати, їсти, курити (10:25 - 12:00)</b>\n\n"
            f"<b>{number_emojis[2]} Іноземна мова (12:20 - 13:55)</b>\nПрактика Чугай О.Ю.\n\n"
            f"<b>{number_emojis[3]} Математичний аналіз (14:15 - 15:50)</b>\n Практика Терещенко І.М."
        )
        query.message.reply_text(message, parse_mode="HTML")

    if selected_week == "Week 1" and selected_day == "thursday":
        message = (
            f"<b>{number_emojis[0]} Математичний аналіз (8:30 - 10:05)</b>\nЛекція Кучинська Н.В.\n\n"
            f"<b>{number_emojis[1]} Українська мова (10:25 - 12:00)</b>\nЛекція Кушлаба М.П.\n\n"
            f"<b>{number_emojis[2]} Алгеом (12:20 - 13:55)</b>\nПрактика Циганкова О.В.\n\n"
            f"<b>{number_emojis[3]} Математичний аналіз (14:15 - 15:50)</b>\n Практика Терещенко І.М."
        )
        query.message.reply_text(message, parse_mode="HTML")

    if selected_week == "Week 1" and selected_day == "friday":
        message = (
            f"<b>{number_emojis[0]} Програмування (8:30 - 10:05)</b>\nЛекція Краков'ян М.В.\n\n"
            f"<b>{number_emojis[1]} Вступ до КБ (10:25 - 12:00)</b>\nЛекція Кушлаба М.П.\n\n"
            f"<b>{number_emojis[2]} Фізика (12:20 - 13:55)</b>\nПрактика Мирошникова І.Ю.\n\n"
            f"<b>{number_emojis[3]} Фізика (14:15 - 15:50)</b>\n Лабораторна Тараненко Ю.О. Катасонов А.А."
        )
        query.message.reply_text(message, parse_mode="HTML")

    if selected_week == "Week 1" and selected_day == "saturday":
        message = (
            f"<b>{number_emojis[0]} Математичний аналіз (8:30 - 10:05)</b>\nЛекція Кучинська Н.В.\n\n"
        )
        query.message.reply_text(message, parse_mode="HTML")

    keyboard = [
        [InlineKeyboardButton("Week 1", callback_data="Week 1")],
        [InlineKeyboardButton("Week 2", callback_data="Week 2")],
        [InlineKeyboardButton("Back ⬅️", callback_data="back")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.message.reply_text("Please select a week:", reply_markup=reply_markup)

    return SELECT_WEEK

def cancel(update, context):
    update.message.reply_text("Operation cancelled.")
    return ConversationHandler.END

def main():
    try:
        logging.info("Starting the Telegram bot...")

        updater = Updater(TOKEN, use_context=True)
        dispatcher = updater.dispatcher

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", start)],
            states={
                SELECT_ACTION: [CallbackQueryHandler(select_action)],
                SELECT_WEEK: [CallbackQueryHandler(select_week)],
                SELECT_DAY: [CallbackQueryHandler(select_day)],
            },
            fallbacks=[CommandHandler("cancel", cancel)]
        )

        dispatcher.add_handler(conv_handler)
        updater.start_polling()
        updater.idle()
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()