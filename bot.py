import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ChannelPostHandler

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

async def react_to_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post and update.channel_post.chat.id == CHANNEL_ID:
        try:
            await context.bot.set_message_reaction(
                chat_id=CHANNEL_ID,
                message_id=update.channel_post.message_id,
                reaction="👍"
            )
        except Exception as e:
            print("Reaction error:", e)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(ChannelPostHandler(react_to_post))
app.run_polling()
