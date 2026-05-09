import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

WALLET = "TTWYTUp1VEbTkQJcwnmujwsfKJ6Ud3Y3au"
CONTACT = "@sajawalbudhana3"
YOUTUBE = "30,000+ subscribers"

# ─────────────────────────────────────────────
# /start
# ─────────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 Channel Subscribers", callback_data="ch_subs")],
        [InlineKeyboardButton("👥 Group Members", callback_data="grp_members")],
        [InlineKeyboardButton("💰 Pricing & Payment", callback_data="pricing")],
        [InlineKeyboardButton("📞 Contact / Order", callback_data="contact")],
        [InlineKeyboardButton("ℹ️ About Us", callback_data="about")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        "🌟 *TG Promotion Hub* 🌟\n\n"
        "Apke Telegram channel aur group ko grow karein — "
        "real, active members ke saath!\n\n"
        "Neeche se apni zaroorat chunein 👇"
    )
    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=reply_markup)


# ─────────────────────────────────────────────
# Channel Subscribers
# ─────────────────────────────────────────────
async def ch_subs_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("🔙 Back", callback_data="main_menu")],
        [InlineKeyboardButton("📞 Order Now", callback_data="contact")],
    ]
    text = (
        "📢 *Channel Subscribers Services*\n\n"
        "✅ *Real Subscribers* (Organic)\n"
        "├ 500  subs — $5\n"
        "├ 1000 subs — $9\n"
        "├ 5000 subs — $40\n"
        "└ 10,000 subs — $75\n\n"
        "✅ *Proxy / Mixed Subscribers*\n"
        "├ 1000  subs — $4\n"
        "├ 5000  subs — $18\n"
        "└ 10,000 subs — $32\n\n"
        "✅ *Ad-Based Subscribers* (targeted)\n"
        "├ 1000  subs — $7\n"
        "├ 5000  subs — $30\n"
        "└ 10,000 subs — $55\n\n"
        "⚡ Delivery: 24–72 hours\n"
        "🔒 Safe — no password required\n\n"
        "Order ke liye contact karein 👇"
    )
    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


# ─────────────────────────────────────────────
# Group Members
# ─────────────────────────────────────────────
async def grp_members_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("🔙 Back", callback_data="main_menu")],
        [InlineKeyboardButton("📞 Order Now", callback_data="contact")],
    ]
    text = (
        "👥 *Group Members Services*\n\n"
        "✅ *Real Group Members*\n"
        "├ 500  members — $6\n"
        "├ 1000 members — $11\n"
        "├ 5000 members — $48\n"
        "└ 10,000 members — $88\n\n"
        "✅ *Proxy / Mixed Members*\n"
        "├ 1000  members — $5\n"
        "├ 5000  members — $20\n"
        "└ 10,000 members — $35\n\n"
        "✅ *Ad-Based Members* (targeted niche)\n"
        "├ 1000  members — $8\n"
        "├ 5000  members — $35\n"
        "└ 10,000 members — $60\n\n"
        "⚡ Delivery: 24–72 hours\n"
        "🔒 Safe — no admin rights required\n\n"
        "Order ke liye contact karein 👇"
    )
    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


# ─────────────────────────────────────────────
# Pricing & Payment
# ─────────────────────────────────────────────
async def pricing_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("📢 Channel Subs", callback_data="ch_subs")],
        [InlineKeyboardButton("👥 Group Members", callback_data="grp_members")],
        [InlineKeyboardButton("🔙 Back", callback_data="main_menu")],
    ]
    text = (
        "💰 *Payment Info*\n\n"
        "Hum sirf *TRC20 (USDT)* accept karte hain:\n\n"
        f"`{WALLET}`\n\n"
        "📌 *Payment Process:*\n"
        "1. Service aur quantity chunein\n"
        "2. Payment karein upar diye wallet par\n"
        "3. Screenshot aur apna channel/group link bhejein\n"
        f"4. Contact karein: {CONTACT}\n"
        "5. Delivery shuru ho jaye gi 24–72 hours mein\n\n"
        "⚠️ Payment confirm hone ke baad kaam shuru hoga"
    )
    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


# ─────────────────────────────────────────────
# Contact
# ─────────────────────────────────────────────
async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [[InlineKeyboardButton("🔙 Back", callback_data="main_menu")]]
    text = (
        "📞 *Order / Contact*\n\n"
        f"Humse directly baat karein: {CONTACT}\n\n"
        "Order karte waqt yeh info bhejein:\n"
        "• Service type (subs/members)\n"
        "• Quantity\n"
        "• Channel/Group link\n"
        "• Payment screenshot (TRC20)\n\n"
        "⏱ Reply time: 1–6 hours\n"
        "🕐 Available: 9 AM – 11 PM (PKT)"
    )
    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


# ─────────────────────────────────────────────
# About
# ─────────────────────────────────────────────
async def about_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [[InlineKeyboardButton("🔙 Back", callback_data="main_menu")]]
    text = (
        "ℹ️ *About TG Promotion Hub*\n\n"
        "Hum Telegram growth services provide karte hain — "
        "real subscribers aur members ke saath apna channel/group "
        "grow karein.\n\n"
        f"👤 *Owner:* {CONTACT}\n"
        f"🎥 *YouTube:* {YOUTUBE} subscribers\n"
        "📍 *Location:* Pakistan\n\n"
        "✅ Trusted service\n"
        "✅ Fast delivery\n"
        "✅ 24/7 support available\n\n"
        "Kisi bhi sawaal ke liye contact karein!"
    )
    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


# ─────────────────────────────────────────────
# Main Menu (back button)
# ─────────────────────────────────────────────
async def main_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("📢 Channel Subscribers", callback_data="ch_subs")],
        [InlineKeyboardButton("👥 Group Members", callback_data="grp_members")],
        [InlineKeyboardButton("💰 Pricing & Payment", callback_data="pricing")],
        [InlineKeyboardButton("📞 Contact / Order", callback_data="contact")],
        [InlineKeyboardButton("ℹ️ About Us", callback_data="about")],
    ]
    text = (
        "🌟 *TG Promotion Hub* 🌟\n\n"
        "Apke Telegram channel aur group ko grow karein — "
        "real, active members ke saath!\n\n"
        "Neeche se apni zaroorat chunein 👇"
    )
    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(ch_subs_handler,    pattern="^ch_subs$"))
    app.add_handler(CallbackQueryHandler(grp_members_handler, pattern="^grp_members$"))
    app.add_handler(CallbackQueryHandler(pricing_handler,    pattern="^pricing$"))
    app.add_handler(CallbackQueryHandler(contact_handler,    pattern="^contact$"))
    app.add_handler(CallbackQueryHandler(about_handler,      pattern="^about$"))
    app.add_handler(CallbackQueryHandler(main_menu_handler,  pattern="^main_menu$"))

    logger.info("Bot chalu ho gaya...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
