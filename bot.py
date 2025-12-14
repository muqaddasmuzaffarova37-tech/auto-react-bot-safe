import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ChannelPostHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

if not BOT_TOKEN or not CHANNEL_ID:
    raise RuntimeError("BOT_TOKEN yoki CHANNEL_ID topilmadi")

CHANNEL_ID = int(CHANNEL_ID)

async def react_to_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    post = update.channel_post
    if post and post.chat.id == CHANNEL_ID:
        try:
            await context.bot.set_message_reaction(
                chat_id=CHANNEL_ID,
                message_id=post.message_id,
                reaction="👍"
            )
        except Exception as e:
            print("Reaction error:", e)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(ChannelPostHandler(react_to_post))
    print("Bot started")
    app.run_polling()

if __name__ == "__main__":
    main()
