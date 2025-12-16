import os
from telegram.ext import Updater, ChannelPostHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))

def react_to_post(update, context):
    post = update.channel_post
    if post and post.chat.id == CHANNEL_ID:
        context.bot.send_message(
            chat_id=CHANNEL_ID,
            text="👍",
            reply_to_message_id=post.message_id
        )

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(ChannelPostHandler(react_to_post))

updater.start_polling()
updater.idle()
