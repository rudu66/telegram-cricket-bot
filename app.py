import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Telegram token from Render Environment Variable
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
        "🏏 Send match data in this format:\n\nScore Overs Wickets RunRate\n\nExample:\n78 9.0 2 8.6"
    )


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        s, o, w, r = update.message.text.split()

        score =
