import os
import wget
import urllib.request
from faker import Faker
import pyaztro
from faker.providers import internet
from bot import dispatcher
from bot.Plugins.disable import DisableAbleCommandHandler
from telegram import Update, ParseMode
from telegram.ext import CallbackContext, run_async


def fakeid(update: Update, context: CallbackContext):
    message = update.effective_message
    dltmsg = message.reply_text("𝕲𝖊𝖓𝖊𝖗𝖆𝖙𝖎𝖓𝖌 𝖋𝖆𝖐𝖊 𝖎𝖉𝖊𝖓𝖙𝖎𝖙𝖞 𝖋𝖔𝖗 𝖞𝖔𝖚...")
    fake = Faker()
    print("𝕯𝖊𝖙𝖆𝖎𝖑𝖘 𝕲𝖊𝖓𝖊𝖗𝖆𝖙𝖎𝖓𝖌\n")
    name = str(fake.name())
    fake.add_provider(internet)
    address = str(fake.address())
    ip = fake.ipv4_private()
    cc = fake.credit_card_full()
    email = fake.ascii_free_email()
    job = fake.job()
    android = fake.android_platform_token()
    pc = fake.chrome()
    message.reply_text(
        f"<b> 𝕱𝖆𝖐𝖊 𝖎𝖓𝖋𝖔𝖗𝖒𝖆𝖙𝖎𝖔𝖓 𝖌𝖊𝖓𝖊𝖗𝖆𝖙𝖊𝖉 </b>\n<b>𝔑𝔞𝔪𝔢 :-</b><code>{name}</code>\n\n<b>𝔄𝔡𝔡𝔯𝔢𝔰𝔰:-</b><code>{address}</code>\n\n<b>ℑ𝔭-𝔄𝔡𝔡𝔯𝔢𝔰𝔰 :-</b><code>{ip}</code>\n\n<b>ℭ𝔯𝔢𝔡𝔦𝔱 𝔠𝔞𝔯𝔡:-</b><code>{cc}</code>\n\n<b>𝔈𝔪𝔞𝔦𝔩-𝔦𝔡:-</b><code>{email}</code>\n\n<b>𝔍𝔬𝔟:-</b><code>{job}</code>\n\n<b>𝔄𝔫𝔡𝔯𝔬𝔦𝔡 𝔲𝔰𝔢𝔯 𝔞𝔤𝔢𝔫𝔱:-</b><code>{android}</code>\n\n<b>𝔓𝔠 𝔲𝔰𝔢𝔯 𝔞𝔤𝔢𝔫𝔱:-</b><code>{pc}</code>",
        parse_mode=ParseMode.HTML,
    )

    dltmsg.delete()




def astro(update: Update, context: CallbackContext):
    message = update.effective_message
    args = message.text.split(" ", 1)
    
    if len(args) == 1:
        message.reply_text('Please choose your horoscope sign. List of all signs - aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius and pisces.')
        return
    else:
        pass
    msg = message.reply_text("Fetching data...")
    try:
        x = args[1]
        horoscope = pyaztro.Aztro(sign=x)
        mood = horoscope.mood
        lt = horoscope.lucky_time
        desc = horoscope.description
        col = horoscope.color
        com = horoscope.compatibility
        ln = horoscope.lucky_number

        result = (
            f"**Horoscope for `{x}`**:\n"
            f"**Mood :** `{mood}`\n"
            f"**Lucky Time :** `{lt}`\n"
            f"**Lucky Color :** `{col}`\n"
            f"**Lucky Number :** `{ln}`\n"
            f"**Compatibility :** `{com}`\n"
            f"**Description :** `{desc}`\n"
        )

        msg.edit_text(result, parse_mode=ParseMode.MARKDOWN)

    except Exception as e:
        msg.edit_text(f"Sorry i haven't found anything!\nmaybe you have given a wrong sign name please check help of horoscope.\nError - {e}")



__help__ = """
 ‣ `/hs <sign>`:
 Usage: it will show horoscope of daily of your sign.
 List of all signs - aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius and pisces.
 ‣ `/fakeid`:
 Usage: it will fake identity for you.
"""

__mod_name__ = "Identity"

FAKER_HANDLER = DisableAbleCommandHandler("fakeid", fakeid, run_async=True)
ASTRO_HANDLER = DisableAbleCommandHandler("hs", astro, run_async=True)
dispatcher.add_handler(FAKER_HANDLER)
dispatcher.add_handler(ASTRO_HANDLER)
