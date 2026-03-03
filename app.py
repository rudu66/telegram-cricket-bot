import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

def predict(score, overs, wickets, runrate):
    momentum = runrate + random.uniform(-0.5, 0.5)
    next_over = round(momentum + random.uniform(-2, 2))
    five_overs = round(momentum * 5 + random.uniform(-5, 5))
    final_score = round(score + (momentum * (20 - overs)))
    wicket_prob = round((wickets / 10) * 40 + random.uniform(5, 15), 2)
    confidence = random.choice(["Low", "Medium", "High"])
    return next_over, five_overs, final_score, wicket_prob, confidence

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏏 Send: Score Overs Wickets RunRate\nExample:\n78 9.0 2 8.6"
    )

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        s, o, w, r = update.message.text.split()
        score = int(s)
        overs = float(o)
        wickets = int(w)
        runrate = float(r)

        next_over, five_overs, final_score, wicket_prob, confidence = predict(
            score, overs, wickets, runrate
        )

        reply = f"""
🏏 AI Prediction

Next Over: {next_over}
Next 5 Overs: {five_overs}
Final Score: {final_score}
Wicket Chance: {wicket_prob}%
Confidence: {confidence}
        """

        await update.message.reply_text(reply)

    except:
        await update.message.reply_text("Wrong format.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

if __name__ == "__main__":
    app.run_polling()
