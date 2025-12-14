import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ChannelPostHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
PORT = int(os.environ.get("PORT", 10000))

async def react_to_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    post = update.channel_post
    if post and post.chat.id == CHANNEL_ID:
        await context.bot.set_message_reaction(
            chat_id=CHANNEL_ID,
            message_id=post.message_id,
            reaction="👍"
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(ChannelPostHandler(react_to_post))

app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=os.environ.get("RENDER_EXTERNAL_URL"),
)
