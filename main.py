import requests , os , sys , jwt , pickle , json , binascii , time , urllib3 , base64 , datetime , re , socket , threading , ssl , pytz , aiohttp
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import * ; from xHeaders import *
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from Pb2 import DEcwHisPErMsG_pb2 , MajoRLoGinrEs_pb2 , PorTs_pb2 , MajoRLoGinrEq_pb2 , sQ_pb2 , Team_msg_pb2
from cfonts import render, say
from APIS import insta
from flask import Flask, jsonify, request
import asyncio
import signal
import sys
# Add these imports if not already present
import re
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Telegram Bot Imports
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  

# Enhanced Configuration Variables
ADMIN_UID = "8804135237"
server2 = "BD"
key2 = "mg24"
BYPASS_TOKEN = "your_bypass_token_here"

# Telegram Bot Configuration
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8248104861:AAEmzo4Bx2Ss6uiT3zma4CbCUnU717tRIEw")
ADMIN_TELEGRAM_ID = int(os.environ.get("ADMIN_TELEGRAM_ID", 6848455321))
BASE_WEBHOOK_URL = os.environ.get("BASE_WEBHOOK_URL", "https://your-app-name.onrender.com")

# VariabLes dyli 
#------------------------------------------#
online_writer = None
whisper_writer = None
spam_room = False
spammer_uid = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_Leave = False
fast_spam_running = False
fast_spam_task = None
custom_spam_running = False
custom_spam_task = None
spam_request_running = False
spam_request_task = None
evo_fast_spam_running = False
evo_fast_spam_task = None
evo_custom_spam_running = False
evo_custom_spam_task = None
# Add with other global variables
reject_spam_running = False
insquad = None 
joining_team = False 
reject_spam_task = None
lag_running = False
lag_task = None
# Add these with your other global variables at the top
reject_spam_running = False
reject_spam_task = None
evo_cycle_running = False
evo_cycle_task = None
# Add with other global variables at the top
auto_start_running = False
auto_start_teamcode = None
stop_auto = False
auto_start_task = None
start_spam_duration = 18  # seconds to spam start
wait_after_match = 20  # seconds to wait after match
start_spam_delay = 0.2  # delay between start packets
# Add for Telegram
telegram_bot_running = False
#------------------------------------------#

# Shared variables for Telegram bot access
telegram_bot = None
telegram_dp = None

# Emote mapping for evo commands
EMOTE_MAP = {
    1: 909000063,
    2: 909000081,
    3: 909000075,
    4: 909000085,
    5: 909000134,
    6: 909000098,
    7: 909035007,
    8: 909051012,
    9: 909000141,
    10: 909034008,
    11: 909041002,
    12: 909039004,
    13: 909042008,
    14: 909051014,
    15: 909039012,
    16: 909040010,
    17: 909035010,
    18: 909041005,
    19: 909051003,
    20: 909034001
}

evo_emotes = {
    "1": "909000063",   # AK
    "2": "909000068",   # SCAR
    "3": "909000075",   # 1st MP40
    "4": "909040010",   # 2nd MP40
    "5": "909000081",   # 1st M1014
    "6": "909039011",   # 2nd M1014
    "7": "909000085",   # XM8
    "8": "909000090",   # Famas
    "9": "909000098",   # UMP
    "10": "909035007",  # M1887
    "11": "909042008",  # Woodpecker
    "12": "909041005",  # Groza
    "13": "909033001",  # M4A1
    "14": "909038010",  # Thompson
    "15": "909038012",  # G18
    "16": "909045001",  # Parafal
    "17": "909049010",  # P90
    "18": "909051003"   # m60
}

# RARE LOOK CHANGER BUNDLE ID
BUNDLE = {
    "rampage": 914000002,
    "cannibal": 914000003,
    "devil": 914038001,
    "scorpio": 914039001,
    "frostfire": 914042001,
    "paradox": 914044001,
    "naruto": 914047001,
    "aurora": 914047002,
    "midnight": 914048001,
    "itachi": 914050001,
    "dreamspace": 914051001
}
# Emote mapping for all emote commands
ALL_EMOTE = {
    1: 909000001,
    2: 909000002,
    3: 909000003,
    4: 909000004,
    5: 909000005,
    6: 909000006,
    7: 909000007,
    8: 909000008,
    9: 909000009,
    10: 909000010,
    11: 909000011,
    12: 909000012,
    13: 909000013,
    14: 909000014,
    15: 909000015,
    16: 909000016,
    17: 909000017,
    18: 909000018,
    19: 909000019,
    20: 909000020,
    21: 909000021,
    22: 909000022,
    23: 909000023,
    24: 909000024,
    25: 909000025,
    26: 909000026,
    27: 909000027,
    28: 909000028,
    29: 909000029,
    30: 909000031,
    31: 909000032,
    32: 909000033,
    33: 909000034,
    34: 909000035,
    35: 909000036,
    36: 909000037,
    37: 909000038,
    38: 909000039,
    39: 909000040,
    40: 909000041,
    41: 909000042,
    42: 909000043,
    43: 909000044,
    44: 909000045,
    45: 909000046,
    46: 909000047,
    47: 909000048,
    48: 909000049,
    49: 909000051,
    50: 909000052,
    51: 909000053,
    52: 909000054,
    53: 909000055,
    54: 909000056,
    55: 909000057,
    56: 909000058,
    57: 909000059,
    58: 909000060,
    59: 909000061,
    60: 909000062,
    61: 909000063,
    62: 909000064,
    63: 909000065,
    64: 909000066,
    65: 909000067,
    66: 909000068,
    67: 909000069,
    68: 909000070,
    69: 909000071,
    70: 909000072,
    71: 909000073,
    72: 909000074,
    73: 909000075,
    74: 909000076,
    75: 909000077,
    76: 909000078,
    77: 909000079,
    78: 909000080,
    79: 909000081,
    80: 909000082,
    81: 909000083,
    82: 909000084,
    83: 909000085,
    84: 909000086,
    85: 909000087,
    86: 909000088,
    87: 909000089,
    88: 909000090,
    89: 909000091,
    90: 909000092,
    91: 909000093,
    92: 909000094,
    93: 909000095,
    94: 909000096,
    95: 909000097,
    96: 909000098,
    97: 909000099,
    98: 909000100,
    99: 909000101,
    100: 909000102,
    101: 909000103,
    102: 909000104,
    103: 909000105,
    104: 909000106,
    105: 909000107,
    106: 909000108,
    107: 909000109,
    108: 909000110,
    109: 909000111,
    110: 909000112,
    111: 909000113,
    112: 909000114,
    113: 909000115,
    114: 909000116,
    115: 909000117,
    116: 909000118,
    117: 909000119,
    118: 909000120,
    119: 909000121,
    120: 909000122,
    121: 909000123,
    122: 909000124,
    123: 909000125,
    124: 909000126,
    125: 909000127,
    126: 909000128,
    127: 909000129,
    128: 909000130,
    129: 909000131,
    130: 909000132,
    131: 909000133,
    132: 909000134,
    133: 909000135,
    134: 909000136,
    135: 909000137,
    136: 909000138,
    137: 909000139,
    138: 909000140,
    139: 909000141,
    140: 909000142,
    141: 909000143,
    142: 909000144,
    143: 909000145,
    144: 909000150,
    145: 909033001,
    146: 909033002,
    147: 909033003,
    148: 909033004,
    149: 909033005,
    150: 909033006,
    151: 909033007,
    152: 909033008,
    153: 909033009,
    154: 909033010,
    155: 909034001,
    156: 909034002,
    157: 909034003,
    158: 909034004,
    159: 909034005,
    160: 909034006,
    161: 909034007,
    162: 909034008,
    163: 909034009,
    164: 909034010,
    165: 909034011,
    166: 909034012,
    167: 909034013,
    168: 909034014,
    169: 909035001,
    170: 909035002,
    171: 909035003,
    172: 909035004,
    173: 909035005,
    174: 909035006,
    175: 909035007,
    176: 909035008,
    177: 909035009,
    178: 909035010,
    179: 909035011,
    180: 909035012,
    181: 909035013,
    182: 909035014,
    183: 909035015,
    184: 909036001,
    185: 909036002,
    186: 909036003,
    187: 909036004,
    188: 909036005,
    189: 909036006,
    190: 909036008,
    191: 909036009,
    192: 909036010,
    193: 909036011,
    194: 909036012,
    195: 909036014,
    196: 909037001,
    197: 909037002,
    198: 909037003,
    199: 909037004,
    200: 909037005,
    201: 909037006,
    202: 909037007,
    203: 909037008,
    204: 909037009,
    205: 909037010,
    206: 909037011,
    207: 909037012,
    208: 909038001,
    209: 909038002,
    210: 909038003,
    211: 909038004,
    212: 909038005,
    213: 909038006,
    214: 909038008,
    215: 909038009,
    216: 909038010,
    217: 909038011,
    218: 909038012,
    219: 909038013,
    220: 909039001,
    221: 909039002,
    222: 909039003,
    223: 909039004,
    224: 909039005,
    225: 909039006,
    226: 909039007,
    227: 909039008,
    228: 909039009,
    229: 909039010,
    230: 909039011,
    231: 909039012,
    232: 909039013,
    233: 909039014,
    234: 909040001,
    235: 909040002,
    236: 909040003,
    237: 909040004,
    238: 909040005,
    239: 909040006,
    240: 909040008,
    241: 909040009,
    242: 909040010,
    243: 909040011,
    244: 909040012,
    245: 909040013,
    246: 909040014,
    247: 909041001,
    248: 909041002,
    249: 909041003,
    250: 909041004,
    251: 909041005,
    252: 909041006,
    253: 909041007,
    254: 909041008,
    255: 909041009,
    256: 909041010,
    257: 909041011,
    258: 909041012,
    259: 909041013,
    260: 909041014,
    261: 909041015,
    262: 909042001,
    263: 909042002,
    264: 909042003,
    265: 909042004,
    266: 909042005,
    267: 909042006,
    268: 909042007,
    269: 909042008,
    270: 909042009,
    271: 909042011,
    272: 909042012,
    273: 909042013,
    274: 909042016,
    275: 909042017,
    276: 909042018,
    277: 909043001,
    278: 909043002,
    279: 909043003,
    280: 909043004,
    281: 909043005,
    282: 909043006,
    283: 909043007,
    284: 909043008,
    285: 909043009,
    286: 909043010,
    287: 909043013,
    288: 909044001,
    289: 909044002,
    290: 909044003,
    291: 909044004,
    292: 909044005,
    293: 909044006,
    294: 909044007,
    295: 909044008,
    296: 909044009,
    297: 909044010,
    298: 909044011,
    299: 909044012,
    300: 909044015,
    301: 909044016,
    302: 909045001,
    303: 909045002,
    304: 909045003,
    305: 909045004,
    306: 909045005,
    307: 909045006,
    308: 909045007,
    309: 909045008,
    310: 909045009,
    311: 909045010,
    312: 909045011,
    313: 909045012,
    314: 909045015,
    315: 909045016,
    316: 909045017,
    317: 909046001,
    318: 909046002,
    319: 909046003,
    320: 909046004,
    321: 909046005,
    322: 909046006,
    323: 909046007,
    324: 909046008,
    325: 909046009,
    326: 909046010,
    327: 909046011,
    328: 909046012,
    329: 909046013,
    330: 909046014,
    331: 909046015,
    332: 909046016,
    333: 909046017,
    334: 909047001,
    335: 909047002,
    336: 909047003,
    337: 909047004,
    338: 909047005,
    339: 909047006,
    340: 909047007,
    341: 909047008,
    342: 909047009,
    343: 909047010,
    344: 909047011,
    345: 909047012,
    346: 909047013,
    347: 909047015,
    348: 909047016,
    349: 909047017,
    350: 909047018,
    351: 909047019,
    352: 909048001,
    353: 909048002,
    354: 909048003,
    355: 909048004,
    356: 909048005,
    357: 909048006,
    358: 909048007,
    359: 909048008,
    360: 909048009,
    361: 909048010,
    362: 909048011,
    363: 909048012,
    364: 909048013,
    365: 909048014,
    366: 909048015,
    367: 909048016,
    368: 909048017,
    369: 909048018,
    370: 909049001,
    371: 909049002,
    372: 909049003,
    373: 909049004,
    374: 909049005,
    375: 909049006,
    376: 909049007,
    377: 909049008,
    378: 909049009,
    379: 909049010,
    380: 909049011,
    381: 909049012,
    382: 909049013,
    383: 909049014,
    384: 909049015,
    385: 909049016,
    386: 909049017,
    387: 909049018,
    388: 909049019,
    389: 909049020,
    390: 909049021,
    391: 909050002,
    392: 909050003,
    393: 909050004,
    394: 909050005,
    395: 909050006,
    396: 909050008,
    397: 909050009,
    398: 909050010,
    399: 909050011,
    400: 909050012,
    401: 909050013,
    402: 909050014,
    403: 909050015,
    404: 909050016,
    405: 909050017,
    406: 909050018,
    407: 909050019,
    408: 909050020,
    409: 909050021,
    410: 909050026,
    411: 909050027,
    412: 909050028,
    413: 909547001,
    414: 909550001
}

# Badge values for s1 to s5 commands - using your exact values
BADGE_VALUES = {
    "s1": 1048576,    # Your first badge
    "s2": 32768,      # Your second badge  
    "s3": 2048,       # Your third badge
    "s4": 64,         # Your fourth badge
    "s5": 262144     # Your seventh badge
}

# ------------------- Insta API Thread -------------------
def start_insta_api():
    port = insta.find_free_port()
    print(f"🚀 تشغيل Insta API على المنفذ {port}")
    insta.app.run(host="0.0.0.0", port=port, debug=False)
# ------------------- End Insta API Thread -------------------

# ------------------- Telegram Bot Functions -------------------
async def on_startup(dispatcher: Dispatcher, bot: Bot):
    """Set webhook on startup"""
    await bot.set_webhook(f"{BASE_WEBHOOK_URL}/webhook")
    print(f"✅ Webhook set to {BASE_WEBHOOK_URL}/webhook")

async def on_shutdown(dispatcher: Dispatcher, bot: Bot):
    """Delete webhook on shutdown"""
    await bot.delete_webhook()
    print("❌ Webhook deleted")

async def telegram_startup():
    """Initialize and start the Telegram bot with webhook"""
    global telegram_bot, telegram_dp, telegram_bot_running
    
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    # Initialize bot and dispatcher
    telegram_bot = Bot(token=BOT_TOKEN)
    telegram_dp = Dispatcher()
    
    # Register message handlers
    await register_telegram_handlers(telegram_dp)
    
    # Setup webhook
    telegram_dp.startup.register(on_startup)
    telegram_dp.shutdown.register(on_shutdown)
    
    # Create aiohttp application
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=telegram_dp,
        bot=telegram_bot,
    )
    webhook_requests_handler.register(app, path="/webhook")
    setup_application(app, telegram_dp, bot=telegram_bot)
    
    # Start aiohttp server
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"🤖 بوت التلغرام يعمل الآن على المنفذ {port} مع webhook")
    telegram_bot_running = True
    
    # Keep the server running
    try:
        while True:
            await asyncio.sleep(3600)  # Sleep for an hour
    except asyncio.CancelledError:
        await runner.cleanup()

async def register_telegram_handlers(dp: Dispatcher):
    """Register all telegram command handlers"""
    
    # Helper function to check if user is admin
    def is_admin_user(message: Message):
        return message.from_user.id == ADMIN_TELEGRAM_ID
    
    # Help command
    @dp.message(Command("help"))
    async def help_command(message: Message):
        if not is_admin_user(message):
            await message.reply("⛔ أنت غير مصرح لك باستخدام هذا البوت.")
            return
            
        help_text = """
🤖 **بوت ZAKARIA - أوامر التلغرام**

**أوامر المجموعة:**
/3 - إنشاء مجموعة 3 لاعبين
/5 - إنشاء مجموعة 5 لاعبين
/6 - إنشاء مجموعة 6 لاعبين
/inv [UID] - إرسال دعوة للاعب

**أوامر متقدمة:**
/lag [team_code] - هجوم تأخير على فريق
/stop lag - إيقاف هجوم التأخير

**أوامر الرقصات التطورية:**
/evos [UID] - بدء دورة الرقصات التطورية
/sevos - إيقاف الدورة
/evo [UID] [رقم_الرقصة] - رقصة تطورية واحدة
/evo_fast [UID] [رقم_الرقصة] - سبام سريع للرقصة
/evo_c [UID] [رقم_الرقصة] [عدد] - سبام مخصص للرقصة

**أمر الرقص المدمج:**
/dance [team_code] [UID] [رقم_الرقصة] - انضمام، رقصة، مغادرة

**رقم الرقصة: 1-18 للإيموجيات التطورية**
"""
        await message.reply(help_text)

    # 3, 5, 6 commands
    @dp.message(Command("3", "5", "6"))
    async def squad_size_command(message: Message):
        if not is_admin_user(message):
            await message.reply("⛔ أنت غير مصرح لك باستخدام هذا البوت.")
            return
            
        cmd = message.text[1:]  # Remove the '/'
        await message.reply(f"🚀 جاري إنشاء مجموعة {cmd} لاعبين...")
        
        # Execute squad creation
        try:
            global online_writer, whisper_writer, key, iv, region
            
            uid = ADMIN_UID  # Use admin UID as target
            size = int(cmd)
            
            # Fast squad creation
            PAc = await OpEnSq(key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
            
            C = await cHSq(size, uid, key, iv, region)
            await asyncio.sleep(0.3)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
            
            V = await SEnd_InV(size, uid, key, iv, region)
            await asyncio.sleep(0.3)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
            
            E = await ExiT(None, key, iv)
            await asyncio.sleep(3.5)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
            
            await message.reply(f"✅ تم إنشاء مجموعة {size} لاعبين بنجاح!")
            
        except Exception as e:
            await message.reply(f"❌ خطأ: {str(e)}")

    # Invite command
    @dp.message(Command("inv"))
    async def invite_command(message: Message):
        if not is_admin_user(message):
            await message.reply("⛔ أنت غير مصرح لك باستخدام هذا البوت.")
            return
            
        parts = message.text.split()
        if len(parts) < 2:
            await message.reply("❌ الاستخدام: /inv [UID]")
            return
            
        target_uid = parts[1]
        if not target_uid.isdigit():
            await message.reply("❌ الرجاء إدخال معرف صحيح!")
            return
            
        await message.reply(f"🚀 جاري إرسال دعوة إلى {target_uid}...")
        
        try:
            global online_writer, whisper_writer, key, iv, region
            
            V = await SEnd_InV(4, int(target_uid), key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
            
            await message.reply(f"✅ تم إرسال الدعوة إلى {target_uid} بنجاح!")
            
        except Exception as e:
            await message.reply(f"❌ خطأ: {str(e)}")

    # Lag command
    @dp.message(Command("lag"))
    async def lag_command(message: Message):
        if not is_admin_user(message):
            await message.reply("⛔ أنت غير مصرح لك باستخدام هذا البوت.")
            return
            
        parts = message.text.split()
        if len(parts) < 2:
            await message.reply("❌ الاستخدام: /lag [team_code]")
            return
            
        team_code = parts[1]
        await message.reply(f"🚀 بدء هجوم التأخير على الفريق {team_code}...")
        
        try:
            global online_writer, whisper_writer, key, iv, region, lag_running, lag_task
            
            # Stop any existing lag task
            if lag_task and not lag_task.done():
                lag_running = False
                lag_task.cancel()
                await asyncio.sleep(0.1)
            
            # Start new lag task
            lag_running = True
            lag_task = asyncio.create_task(lag_team_loop(team_code, key, iv, region))
            
            await message.reply(f"✅ بدأ هجوم التأخير على الفريق {team_code}\nلإيقافه استخدم /stop lag")
            
        except Exception as e:
            await message.reply(f"❌ خطأ: {str(e)}")

    # Stop lag command
    @dp.message(Command("stop_lag"))
    async def stop_lag_command(message: Message):
        if not is_admin_user(message):
            await message.reply("⛔ أنت غير مصرح لك باستخدام هذا البوت.")
            return
            
        global lag_running, lag_task
        
        if lag_task and not lag_task.done():
            lag_running = False
            lag_task.cancel()
            await message.reply("✅ تم إيقاف هجوم التأخير بنجاح!")
        else:
            await message.reply("❌ لا يوجد هجوم تأخير نشط!")

    # Evos command - start evo cycle
    @dp.message(Command("evos"))
    async def evos_command(message: Message):
        if not is_admin_user(message):
            await message.reply("⛔ أنت غير مصرح لك باستخدام هذا البوت.")
            return
            
        parts = message.text.split()
        target_uid = ADMIN_UID  # Default to admin
        
        if len(parts) >= 2 and parts[1].isdigit():
            target_uid = parts[1]
            
        await message.reply(f"🚀 بدء دورة الرقصات التطورية على {target_uid}...")
        
        try:
            global online_writer, whisper_writer, key, iv, region, evo_cycle_running, evo_cycle_task
            
            # Stop any existing evo cycle
            if evo_cycle_task and not evo_cycle_task.done():
                evo_cycle_running = False
                evo_cycle_task.cancel()
                await asyncio.sleep(0.5)
            
            # Start new evo cycle
            evo_cycle_running = True
            evo_cycle_task = asyncio.create_task(evo_cycle_spam([target_uid], key, iv, region))
            
            await message.reply(f"✅ بدأت دورة الرقصات التطورية على {target_uid}\nلإيقافها استخدم /sevos")
            
        except Exception as e:
            await message.reply(f"❌ خطأ: {str(e)}")

    # Sevos command - stop evo cycle
    @dp.message(Command("sevos"))
    async def sevos_command(message: Message):
        if not is_admin_user(message):
            await message.reply("⛔ أنت غير مصرح لك باستخدام هذا البوت.")
            return
            
        global evo_cycle_running, evo_cycle_task
        
        if evo_cycle_task and not evo_cycle_task.done():
            evo_cycle_running = False
            evo_cycle_task.cancel()
            await message.reply("✅ تم إيقاف دورة الرقصات التطورية!")
        else:
            await message.reply("❌ لا توجد دورة رقصات تطورية نشطة!")

    # Evo command - single evo emote
    @dp.message(Command("evo"))
    async def evo_command(message: Message):
        if not is_admin_user(message):
            await message.reply("⛔ أنت غير مصرح لك باستخدام هذا البوت.")
            return
            
        parts = message.text.split()
        if len(parts) < 3:
            await message.reply("❌ الاستخدام: /evo [UID] [رقم_الرقصة 1-18]")
            return
            
        target_uid = parts[1]
        if not target_uid.isdigit():
            await message.reply("❌ الرجاء إدخال معرف صحيح!")
            return
            
        try:
            emote_number = int(parts[2])
            if emote_number < 1 or emote_number > 18:
                await message.reply("❌ رقم الرقصة يجب أن يكون بين 1 و 18")
                return
                
            await message.reply(f"🚀 إرسال الرقصة {emote_number} إلى {target_uid}...")
            
            global online_writer, whisper_writer, key, iv, region
            
            emote_id = EMOTE_MAP.get(emote_number)
            if emote_id:
                H = await Emote_k(int(target_uid), emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                await message.reply(f"✅ تم إرسال الرقصة {emote_number} إلى {target_uid}!")
            else:
                await message.reply("❌ معرف الرقصة غير صالح!")
                
        except ValueError:
            await message.reply("❌ رقم الرقصة يجب أن يكون رقماً!")
        except Exception as e:
            await message.reply(f"❌ خطأ: {str(e)}")

    # Evo fast command
    @dp.message(Command("evo_fast"))
    async def evo_fast_command(message: Message):
        if not is_admin_user(message):
            await message.reply("⛔ أنت غير مصرح لك باستخدام هذا البوت.")
            return
            
        parts = message.text.split()
        if len(parts) < 3:
            await message.reply("❌ الاستخدام: /evo_fast [UID] [رقم_الرقصة 1-18]")
            return
            
        target_uid = parts[1]
        if not target_uid.isdigit():
            await message.reply("❌ الرجاء إدخال معرف صحيح!")
            return
            
        try:
            emote_number = int(parts[2])
            if emote_number < 1 or emote_number > 18:
                await message.reply("❌ رقم الرقصة يجب أن يكون بين 1 و 18")
                return
                
            await message.reply(f"🚀 بدء سبام سريع للرقصة {emote_number} على {target_uid}...")
            
            global online_writer, whisper_writer, key, iv, region, evo_fast_spam_running, evo_fast_spam_task
            
            # Stop any existing evo_fast spam
            if evo_fast_spam_task and not evo_fast_spam_task.done():
                evo_fast_spam_running = False
                evo_fast_spam_task.cancel()
                await asyncio.sleep(0.5)
            
            # Start new evo_fast spam
            evo_fast_spam_running = True
            evo_fast_spam_task = asyncio.create_task(evo_fast_emote_spam([target_uid], emote_number, key, iv, region))
            
            await message.reply(f"✅ بدأ السبام السريع للرقصة {emote_number} على {target_uid}\nسيتم إرسال 25 رقصة بسرعة!")
            
        except ValueError:
            await message.reply("❌ رقم الرقصة يجب أن يكون رقماً!")
        except Exception as e:
            await message.reply(f"❌ خطأ: {str(e)}")

    # Evo custom command
    @dp.message(Command("evo_c"))
    async def evo_custom_command(message: Message):
        if not is_admin_user(message):
            await message.reply("⛔ أنت غير مصرح لك باستخدام هذا البوت.")
            return
            
        parts = message.text.split()
        if len(parts) < 4:
            await message.reply("❌ الاستخدام: /evo_c [UID] [رقم_الرقصة 1-18] [عدد_المرات]")
            return
            
        target_uid = parts[1]
        if not target_uid.isdigit():
            await message.reply("❌ الرجاء إدخال معرف صحيح!")
            return
            
        try:
            emote_number = int(parts[2])
            times = int(parts[3])
            
            if emote_number < 1 or emote_number > 18:
                await message.reply("❌ رقم الرقصة يجب أن يكون بين 1 و 18")
                return
                
            if times < 1 or times > 100:
                await message.reply("❌ عدد المرات يجب أن يكون بين 1 و 100")
                return
                
            await message.reply(f"🚀 بدأ السبام المخصص للرقصة {emote_number} على {target_uid} ({times} مرة)...")
            
            global online_writer, whisper_writer, key, iv, region, evo_custom_spam_running, evo_custom_spam_task
            
            # Stop any existing evo_custom spam
            if evo_custom_spam_task and not evo_custom_spam_task.done():
                evo_custom_spam_running = False
                evo_custom_spam_task.cancel()
                await asyncio.sleep(0.5)
            
            # Start new evo_custom spam
            evo_custom_spam_running = True
            evo_custom_spam_task = asyncio.create_task(evo_custom_emote_spam([target_uid], emote_number, times, key, iv, region))
            
            await message.reply(f"✅ بدأ السبام المخصص للرقصة {emote_number} على {target_uid} ({times} مرة)!")
            
        except ValueError:
            await message.reply("❌ الأرقام يجب أن تكون أرقاماً صحيحة!")
        except Exception as e:
            await message.reply(f"❌ خطأ: {str(e)}")

    # Dance command - join, emote, leave
    @dp.message(Command("dance"))
    async def dance_command(message: Message):
        if not is_admin_user(message):
            await message.reply("⛔ أنت غير مصرح لك باستخدام هذا البوت.")
            return
            
        parts = message.text.split()
        if len(parts) < 4:
            await message.reply("❌ الاستخدام: /dance [team_code] [UID] [رقم_الرقصة 1-18]")
            return
            
        team_code = parts[1]
        target_uid = parts[2]
        
        if not target_uid.isdigit():
            await message.reply("❌ الرجاء إدخال معرف صحيح!")
            return
            
        try:
            emote_number = int(parts[3])
            if emote_number < 1 or emote_number > 18:
                await message.reply("❌ رقم الرقصة يجب أن يكون بين 1 و 18")
                return
                
            await message.reply(f"🚀 بدأ أمر الرقص:\n🎯 الفريق: {team_code}\n👤 الهدف: {target_uid}\n💃 الرقصة: {emote_number}")
            
            # Execute dance sequence
            global online_writer, whisper_writer, key, iv, region
            
            # Step 1: Join team
            join_packet = await GenJoinSquadsPacket(team_code, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            await asyncio.sleep(1.5)
            
            # Step 2: Send dance emote
            emote_id = EMOTE_MAP.get(emote_number)
            if emote_id:
                H = await Emote_k(int(target_uid), emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                await asyncio.sleep(0.5)
            
            # Step 3: Leave team
            leave_packet = await ExiT(None, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
            
            await message.reply(f"✅ اكتمل أمر الرقص بنجاح!\nتم إرسال الرقصة {emote_number} إلى {target_uid} والمغادرة.")
            
        except ValueError:
            await message.reply("❌ رقم الرقصة يجب أن يكون رقماً!")
        except Exception as e:
            await message.reply(f"❌ خطأ: {str(e)}")

    # Stop fast spam commands
    @dp.message(Command("stop_fast"))
    async def stop_fast_command(message: Message):
        if not is_admin_user(message):
            await message.reply("⛔ أنت غير مصرح لك باستخدام هذا البوت.")
            return
            
        global fast_spam_running, fast_spam_task
        
        if fast_spam_task and not fast_spam_task.done():
            fast_spam_running = False
            fast_spam_task.cancel()
            await message.reply("✅ تم إيقاف السبام السريع!")
        else:
            await message.reply("❌ لا يوجد سبام سريع نشط!")

    @dp.message(Command("stop_evo_fast"))
    async def stop_evo_fast_command(message: Message):
        if not is_admin_user(message):
            await message.reply("⛔ أنت غير مصرح لك باستخدام هذا البوت.")
            return
            
        global evo_fast_spam_running, evo_fast_spam_task
        
        if evo_fast_spam_task and not evo_fast_spam_task.done():
            evo_fast_spam_running = False
            evo_fast_spam_task.cancel()
            await message.reply("✅ تم إيقاف السبام السريع التطوري!")
        else:
            await message.reply("❌ لا يوجد سبام سريع تطوري نشط!")

    @dp.message(Command("stop_evo_c"))
    async def stop_evo_c_command(message: Message):
        if not is_admin_user(message):
            await message.reply("⛔ أنت غير مصرح لك باستخدام هذا البوت.")
            return
            
        global evo_custom_spam_running, evo_custom_spam_task
        
        if evo_custom_spam_task and not evo_custom_spam_task.done():
            evo_custom_spam_running = False
            evo_custom_spam_task.cancel()
            await message.reply("✅ تم إيقاف السبام المخصص التطوري!")
        else:
            await message.reply("❌ لا يوجد سبام مخصص تطوري نشط!")

# ------------------- End Telegram Bot Functions -------------------

# [باقي دوال البوت كما هي - لم يتم تغييرها]

def uid_generator():
    # ৮ ডিজিটের সর্বনিম্ন সংখ্যা ১০০০০০০০ (10,000,000)
    # আপনার দেওয়া সর্বোচ্চ সীমা ৯৯৯৯৯৯৯৯৯৯৯ (99,999,999,999)
    start = 10000000
    end = 99999999999
    
    for i in range(start, end + 1):
        yield i

def cleanup_cache():
    """Clean old cached data to maintain performance"""
    current_time = time.time()
    # Clean last_request_time
    to_remove = [k for k, v in last_request_time.items() 
                 if current_time - v > CLEANUP_INTERVAL]
    for k in to_remove:
        last_request_time.pop(k, None)
    
    # Clean command_cache if too large
    if len(command_cache) > MAX_CACHE_SIZE:
        oldest_keys = sorted(command_cache.keys())[:len(command_cache)//2]
        for key in oldest_keys:
            command_cache.pop(key, None)

def get_rate_limited_response(user_id):
    """Implement rate limiting to reduce server load"""
    user_key = str(user_id)
    current_time = time.time()
    
    if user_key in last_request_time:
        time_since_last = current_time - last_request_time[user_key]
        if time_since_last < RATE_LIMIT_DELAY:
            return False
    
    last_request_time[user_key] = current_time
    return True

# Helper Functions
def is_admin(uid):
    return str(uid) == ADMIN_UID

# Helper functions for ghost join
def dec_to_hex(decimal):
    """Convert decimal to hex string"""
    hex_str = hex(decimal)[2:]
    return hex_str.upper() if len(hex_str) % 2 == 0 else '0' + hex_str.upper()

async def encrypt_packet(packet_hex, key, iv):
    """Encrypt packet using AES CBC"""
    cipher = AES.new(key, AES.MODE_CBC, iv)
    packet_bytes = bytes.fromhex(packet_hex)
    padded_packet = pad(packet_bytes, AES.block_size)
    encrypted = cipher.encrypt(padded_packet)
    return encrypted.hex()

async def nmnmmmmn(packet_hex, key, iv):
    """Wrapper for encrypt_packet"""
    return await encrypt_packet(packet_hex, key, iv)
    



def get_idroom_by_idplayer(packet_hex):
    """Extract room ID from packet - converted from your other TCP"""
    try:
        json_result = get_available_room(packet_hex)
        parsed_data = json.loads(json_result)
        json_data = parsed_data["5"]["data"]
        data = json_data["1"]["data"]
        idroom = data['15']["data"]
        return idroom
    except Exception as e:
        print(f"خطأ في استخراج معرف الغرفة: {e}")
        return None

async def check_player_in_room(target_uid, key, iv):
    """Check if player is in a room by sending status request"""
    try:
        # Send status request packet
        status_packet = await GeT_Status(int(target_uid), key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', status_packet)
        
        # You'll need to capture the response packet and parse it
        # For now, return True and we'll handle room detection in the main loop
        return True
    except Exception as e:
        print(f"خطأ في التحقق من حالة غرفة اللاعب: {e}")
        return False
        
        
        
async def handle_alll_titles_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type=0):
    """Handle /alltitles command to send all titles sequentially"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) == 1:
        target_uid = uid
        target_name = "نفسك"
    elif len(parts) == 2 and parts[1].isdigit():
        target_uid = parts[1]
        target_name = f"المعرف {target_uid}"
    else:
        error_msg = f"""[B][C][FF0000]❌ خطأ في الاستخدام: /alltitles [معرف]
        
📝 أمثلة:
/alltitles - إرسال جميع الألقاب لنفسك
/alltitles 123456789 - إرسال جميع الألقاب لمعرف محدد

🎯 الوظيفة:
1. إرسال جميع الألقاب الأربعة واحداً تلو الآخر
2. تأخير ثانيتين بين كل لقب
3. إرسال في الخلفية (غير معطل)
4. عرض تحديثات التقدم
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Start the title sequence in the background
    asyncio.create_task(
        send_all_titles_sequentiallly(target_uid, chat_id, key, iv, region, chat_type)
    )
    

async def send_all_titles_sequentiallly(uid, chat_id, key, iv, region, chat_type):
    """Send all titles one by one with 2-second delay"""
    
    # Get all titles
    all_titles = [
        904090014, 904090015, 904090024, 904090025, 904090026, 904090027, 904990070, 904990071, 904990072
    ]
    
    total_titles = len(all_titles)
    
    # Send initial message
    start_msg = f"""[B][C][00FF00] Noobde Black666 ya meku agar tu noob bolra toh tu gay hai


"""
    await safe_send_message(chat_type, start_msg, uid, chat_id, key, iv)
    
    try:
        for index, title_id in enumerate(all_titles):
            title_number = index + 1
            

            
            # Send the actual title using your existing method
            # You'll need to use your existing title sending logic here
            # For example:
            title_packet = await noob(uid, chat_id, key, iv, nickname="MG24", title_id=title_id)
            
            if title_packet and whisper_writer:
                whisper_writer.write(title_packet)
                await whisper_writer.drain()
                print(f"✅ تم إرسال اللقب {title_number}/{total_titles}: {title_id}")
            
            # Wait 2 seconds before next title (unless it's the last one)
            if title_number < total_titles:
                await asyncio.sleep(2)
        
        # Completion message
        completion_msg = f"""[B][C][00FF00]Noobde ab tu bta ye titles aur bol kon noob hai
"""
        await safe_send_message(chat_type, completion_msg, uid, chat_id, key, iv)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ خطأ في إرسال الألقاب: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

async def noob(target_uid, chat_id, key, iv, nickname="MG24", title_id=None):
    """EXACT conversion with customizable title ID"""
    try:
        # Use provided title_id or get random one
        if title_id is None:
            # Get a random title from the list
            available_titles = [904090014, 904090015, 904090024, 904090025, 904090026, 904090027, 904990070, 904990071, 904990072]
            title_id = random.choice(available_titles)
        
        # Create fields dictionary with specific title_id
        fields = {
            1: 1,
            2: {
                1: int(target_uid),
                2: int(chat_id),
                5: int(datetime.now().timestamp()),
                8: f'{{"TitleID":{title_id},"type":"Title"}}',
                9: {
                    1: f"[C][B][FF0000]{nickname}",
                    2: int(await xBunnEr()),
                    4: 330,
                    5: 102000015,
                    8: "BOT TEAM",
                    10: 1,
                    11: 1,
                    13: {
                        1: 2
                    },
                    14: {
                        1: 8804135237,
                        2: 8,
                        3: b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
                    }
                },
                10: "en",
                13: {
                    2: 2,
                    3: 1
                },
                14: {}
            }
        }
        
        # ... rest of your existing function
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"
        
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)
        
        print(f"✅ تم إنشاء حزمة بمعرف اللقب: {title_id}")
        return final_packet
        
    except Exception as e:
        print(f"❌ خطأ في التحويل: {e}")
        return None
        

async def send_title_packet_direct(target_uid, chat_id, key, iv, region="ind"):
    """Send title packet directly without chat context - for auto-join"""
    try:
        print(f"🎖️ إرسال اللقب إلى {target_uid} في الدردشة {chat_id}")
        
        # Method 1: Using your existing function
        title_packet = await convert_kyro_to_your_system(target_uid, chat_id, key, iv)
        
        if title_packet and whisper_writer:
            # Send via Whisper connection
            whisper_writer.write(title_packet)
            await whisper_writer.drain()
            print(f"✅ تم إرسال اللقب عبر Whisper إلى {target_uid}")
            return True
            
    except Exception as e:
        print(f"❌ خطأ في إرسال اللقب مباشرة: {e}")
        import traceback
        traceback.print_exc()
    
    return False

def titles():
    """Return all titles instead of just one random"""
    titles_list = [
        905090075, 904990072, 904990069, 905190079
    ]
    return titles_list  # Return the full list instead of random.choice            
    
    
class MultiAccountManager:
    def __init__(self):
        self.accounts_file = "accounts.json"
        self.accounts_data = self.load_accounts()
    
    def load_accounts(self):
        """Load multiple accounts from JSON file"""
        try:
            with open(self.accounts_file, "r", encoding="utf-8") as f:
                accounts = json.load(f)

                return accounts
        except FileNotFoundError:
            print(f"❌ ملف الحسابات {self.accounts_file} غير موجود!")
            return {}
        except Exception as e:
            print(f"❌ خطأ في تحميل الحسابات: {e}")
            return {}
    
    
    
    async def get_account_token(self, uid, password):
        """Get access token for a specific account"""
        try:
            url = "https://10000067.connect.garena.com/oauth/guest/token/grant"
            headers = {
                "Host": "100067.connect.garena.com",
                "User-Agent": await Ua(),
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "close"
            }
            data = {
                "uid": uid,
                "password": password,
                "response_type": "token",
                "client_type": "2",
                "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
                "client_id": "100067"
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, data=data) as response:
                    if response.status == 200:
                        data = await response.json()
                        open_id = data.get("open_id")
                        access_token = data.get("access_token")
                        return open_id, access_token
            return None, None
        except Exception as e:
            print(f"❌ خطأ في الحصول على رمز {uid}: {e}")
            return None, None

async def send_title_packet_direct(target_uid, chat_id, key, iv, region="ind"):
    """Send title packet directly without chat context - for auto-join"""
    try:
        print(f"🎖️ إرسال اللقب إلى {target_uid} في الدردشة {chat_id}")
        
        # Method 1: Using your existing function
        title_packet = await convert_kyro_to_your_system(target_uid, chat_id, key, iv)
        
        if title_packet and whisper_writer:
            # Send via Whisper connection
            whisper_writer.write(title_packet)
            await whisper_writer.drain()
            print(f"✅ تم إرسال اللقب عبر Whisper إلى {target_uid}")
            return True
            
    except Exception as e:
        print(f"❌ خطأ في إرسال اللقب مباشرة: {e}")
        import traceback
        traceback.print_exc()
    
    return False

async def handle_alll_titles_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type=0):
    """Handle /alltitles command to send all titles sequentially"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) == 1:
        target_uid = uid
        target_name = "نفسك"
    elif len(parts) == 2 and parts[1].isdigit():
        target_uid = parts[1]
        target_name = f"المعرف {target_uid}"
    else:
        error_msg = f"""[B][C][FF0000]❌ خطأ في الاستخدام: /alltitles [معرف]
        
📝 أمثلة:
/alltitles - إرسال جميع الألقاب لنفسك
/alltitles 123456789 - إرسال جميع الألقاب لمعرف محدد

🎯 الوظيفة:
1. إرسال جميع الألقاب الأربعة واحداً تلو الآخر
2. تأخير ثانيتين بين كل لقب
3. إرسال في الخلفية (غير معطل)
4. عرض تحديثات التقدم
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Start the title sequence in the background
    asyncio.create_task(
        send_all_titles_sequentiallly(target_uid, chat_id, key, iv, region, chat_type)
    )
    

def get_random_sticker():
    """
    Randomly select one sticker from available packs
    """

    sticker_packs = [
        # NORMAL STICKERS (1200000001-1 to 24)
        ("1200000001", 1, 24),

        # KELLY EMOJIS (1200000002-1 to 15)
        ("1200000002", 1, 15),

        # MAD CHICKEN (1200000004-1 to 13)
        ("1200000004", 1, 13),
    ]

    pack_id, start, end = random.choice(sticker_packs)
    sticker_no = random.randint(start, end)

    return f"[1={pack_id}-{sticker_no}]"
        
async def send_sticker(target_uid, chat_id, key, iv, nickname="BLACK"):
    """Send Random Sticker using /sticker command"""
    try:
        sticker_value = get_random_sticker()

        fields = {
            1: 1,
            2: {
                1: int(target_uid),
                2: int(chat_id),
                5: int(datetime.now().timestamp()),
                8: f'{{"StickerStr" : "{sticker_value}", "type":"Sticker"}}',
                9: {
                    1: f"[C][B][FF0000]{nickname}",
                    2: int(get_random_avatar()),
                    4: 330,
                    5: 102000015,
                    8: "BOT TEAM",
                    10: 1,
                    11: 66,
                    12: 66,
                    13: {1: 2},
                    14: {
                        1: 8804135237,
                        2: 8,
                        3: b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
                    }
                },
                10: "en",
                13: {
                    2: 2,
                    3: 1
                },
                14: {}
            }
        }

        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()

        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"

        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)

        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)

        print(f"✅ تم إرسال الملصق: {sticker_value}")
        return final_packet

    except Exception as e:
        print(f"❌ خطأ في الملصق: {e}")
        return None

# Alternative: DIRECT port of your friend's function but with your UID
async def send_kyro_title_adapted(chat_id, key, iv, target_uid, nickname="BLACK666FF"):
    """Direct adaptation of your friend's working function"""
    try:
        # Import your proto file (make sure it's in the same directory)
        from kyro_title_pb2 import GenTeamTitle
        
        root = GenTeamTitle()
        root.type = 1
        
        nested_object = root.data
        nested_object.uid = int(target_uid)  # CHANGE: Use target UID
        nested_object.chat_id = int(chat_id)
        nested_object.title = f"{{\"TitleID\":{titles()},\"type\":\"Title\"}}"
        nested_object.timestamp = int(datetime.now().timestamp())
        nested_object.language = "en"
        
        nested_details = nested_object.field9
        nested_details.Nickname = f"[C][B][FF0000]{nickname}"  # CHANGE: Your nickname
        nested_details.avatar_id = int(await xBunnEr())  # Use your function
        nested_details.rank = 330
        nested_details.badge = 102000015
        nested_details.Clan_Name = "BOT TEAM"  # CHANGE: Your clan
        nested_details.field10 = 1
        nested_details.global_rank_pos = 1
        nested_details.badge_info.value = 2
        
        nested_details.prime_info.prime_uid = 8804135237
        nested_details.prime_info.prime_level = 8
        # IMPORTANT: This must be bytes, not string!
        nested_details.prime_info.prime_hex = b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
        
        nested_options = nested_object.field13
        nested_options.url_type = 2
        nested_options.curl_platform = 1
        
        nested_object.empty_field.SetInParent()
        
        # Serialize
        packet = root.SerializeToString().hex()
        
        # Use YOUR encryption function
        encrypted_packet = await encrypt_packet(packet, key, iv)
        
        # Calculate length
        packet_length = len(encrypted_packet) // 2
        
        # Convert to hex (4 characters with leading zeros)
        hex_length = f"{packet_length:04x}"
        
        # Build packet EXACTLY like your friend
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        return bytes.fromhex(final_packet_hex)
        
    except Exception as e:
        print(f"❌ خطأ في التكيف المباشر: {e}")
        import traceback
        traceback.print_exc()
        return None

async def send_all_titles_sequentially(uid, chat_id, key, iv, region, chat_type):
    """Send all titles one by one with 2-second delay"""
    
    # Get all titles
    all_titles = [
        905090075, 904990072, 904990069, 905190079
    ]
    
    total_titles = len(all_titles)
    
    # Send initial message
    start_msg = f"""[B][C][00FF00]🎖️ بدء تسلسل الألقاب!

📊 إجمالي الألقاب: {total_titles}
⏱️ التأخير: ثانيتين بين كل لقب
🔁 الوضع: تسلسلي
🎯 الهدف: {uid}

⏳ جاري إرسال الألقاب...
"""
    await safe_send_message(chat_type, start_msg, uid, chat_id, key, iv)
    
    try:
        for index, title_id in enumerate(all_titles):
            title_number = index + 1
            
            # Create progress message
            progress_msg = f"""[B][C][FFFF00]📤 جاري إرسال اللقب {title_number}/{total_titles}

🎖️ معرف اللقب: {title_id}
📊 التقدم: {title_number}/{total_titles}
⏱️ التالي بعد: ثانيتين
"""
            await safe_send_message(chat_type, progress_msg, uid, chat_id, key, iv)
            
            # Send the actual title using your existing method
            # You'll need to use your existing title sending logic here
            # For example:
            title_packet = await convert_kyro_to_your_system(uid, chat_id, key, iv, nickname="BLACK666FF", title_id=title_id)
            
            if title_packet and whisper_writer:
                whisper_writer.write(title_packet)
                await whisper_writer.drain()
                print(f"✅ تم إرسال اللقب {title_number}/{total_titles}: {title_id}")
            
            # Wait 2 seconds before next title (unless it's the last one)
            if title_number < total_titles:
                await asyncio.sleep(2)
        
        # Completion message
        completion_msg = f"""[B][C][00FF00]✅ تم إرسال جميع الألقاب بنجاح!

🎊 الإجمالي: {total_titles} لقب
🎯 الهدف: {uid}
⏱️ المدة: {total_titles * 2} ثانية
✅ الحالة: مكتمل!

🎖️ الألقاب المرسلة:
1. 905090075
2. 904990072
3. 904990069
4. 905190079
"""
        await safe_send_message(chat_type, completion_msg, uid, chat_id, key, iv)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ خطأ في إرسال الألقاب: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

async def handle_all_titles_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type=0):
    """Handle /alltitles command to send all titles sequentially"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) == 1:
        target_uid = uid
        target_name = "نفسك"
    elif len(parts) == 2 and parts[1].isdigit():
        target_uid = parts[1]
        target_name = f"المعرف {target_uid}"
    else:
        error_msg = f"""[B][C][FF0000]❌ خطأ في الاستخدام: /alltitles [معرف]
        
📝 أمثلة:
/alltitles - إرسال جميع الألقاب لنفسك
/alltitles 123456789 - إرسال جميع الألقاب لمعرف محدد

🎯 الوظيفة:
1. إرسال جميع الألقاب الأربعة واحداً تلو الآخر
2. تأخير ثانيتين بين كل لقب
3. إرسال في الخلفية (غير معطل)
4. عرض تحديثات التقدم
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Start the title sequence in the background
    asyncio.create_task(
        send_all_titles_sequentially(target_uid, chat_id, key, iv, region, chat_type)
    )
    
    # Immediate response
    response_msg = f"""[B][C][00FF00]🚀 بدء تسلسل الألقاب في الخلفية!

👤 الهدف: {target_name}
🎖️ إجمالي الألقاب: 4
⏱️ التأخير: ثانيتين لكل لقب
📱 الحالة: يعمل في الخلفية...

💡 ستتلقى تحديثات التقدم عند إرسال الألقاب!
"""
    await safe_send_message(chat_type, response_msg, uid, chat_id, key, iv)


async def convert_kyro_to_your_system(target_uid, chat_id, key, iv, nickname="BLACK666FF", title_id=None):
    """EXACT conversion with customizable title ID"""
    try:
        # Use provided title_id or get random one
        if title_id is None:
            # Get a random title from the list
            available_titles = [905090075, 904990072, 904990069, 905190079]
            title_id = random.choice(available_titles)
        
        # Create fields dictionary with specific title_id
        fields = {
            1: 1,
            2: {
                1: int(target_uid),
                2: int(chat_id),
                5: int(datetime.now().timestamp()),
                8: f'{{"TitleID":{title_id},"type":"Title"}}',  # Use specific title ID
                # ... rest of your fields
                9: {
                    1: f"[C][B][FF0000]{nickname}",
                    2: int(await xBunnEr()),
                    4: 330,
                    5: 102000015,
                    8: "BOT TEAM",
                    10: 1,
                    11: 1,
                    13: {
                        1: 2
                    },
                    14: {
                        1: 8804135237,
                        2: 8,
                        3: b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
                    }
                },
                10: "en",
                13: {
                    2: 2,
                    3: 1
                },
                14: {}
            }
        }
        
        # ... rest of your existing function
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"
        
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)
        
        print(f"✅ تم إنشاء حزمة بمعرف اللقب: {title_id}")
        return final_packet
        
    except Exception as e:
        print(f"❌ خطأ في التحويل: {e}")
        return None
            
    async def send_join_from_account(self, target_uid, account_uid, password, key, iv, region):
        """Send join request from a specific account"""
        try:
            # Get token for this account
            open_id, access_token = await self.get_account_token(account_uid, password)
            if not open_id or not access_token:
                return False
            
            # Create join packet using the account's credentials
            join_packet = await self.create_account_join_packet(target_uid, account_uid, open_id, access_token, key, iv, region)
            if join_packet:
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
                return True
            return False
            
        except Exception as e:
            print(f"❌ خطأ في إرسال طلب الانضمام من {account_uid}: {e}")
            return False
            
async def SEnd_InV_with_Cosmetics(Nu, Uid, K, V, region):
    """Simple version - just add field 5 with basic cosmetics"""
    region = "ind"
    fields = {
        1: 2, 
        2: {
            1: int(Uid), 
            2: region, 
            4: int(Nu),
            # Simply add field 5 with basic cosmetics
            5: {
                1: "BOT",                    # Name
                2: int(await get_random_avatar()),     # Avatar
                5: random.choice([1048576, 32768, 2048]),  # Random badge
            }
        }
    }

    if region.lower() == "ind":
        packet = '0514'
    elif region.lower() == "bd":
        packet = "0519"
    else:
        packet = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet, K, V)   
            
async def join_custom_room(room_id, room_password, key, iv, region):
    """Join custom room with proper Free Fire packet structure"""
    fields = {
        1: 61,  # Room join packet type (verified for Free Fire)
        2: {
            1: int(room_id),
            2: {
                1: int(room_id),  # Room ID
                2: int(time.time()),  # Timestamp
                3: "BOT",  # Player name
                5: 12,  # Unknown
                6: 9999999,  # Unknown
                7: 1,  # Unknown
                8: {
                    2: 1,
                    3: 1,
                },
                9: 3,  # Room type
            },
            3: str(room_password),  # Room password
        }
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
    
async def leave_squad(key, iv, region):
    """Leave squad - converted from your old TCP leave_s()"""
    fields = {
        1: 7,
        2: {
            1: 12480598706  # Your exact value from old TCP
        }
    }
    
    packet = (await CrEaTe_ProTo(fields)).hex()
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk(packet, packet_type, key, iv)    
    
async def RedZed_SendInv(bot_uid, uid, key, iv):
    """Async version of send invite function"""
    try:
        fields = {
            1: 33, 
            2: {
                1: int(uid), 
                2: "IND", 
                3: 1, 
                4: 1, 
                6: "RedZedKing!!", 
                7: 330, 
                8: 1000, 
                9: 100, 
                10: "DZ", 
                12: 1, 
                13: int(uid), 
                16: 1, 
                17: {
                    2: 159, 
                    4: "y[WW", 
                    6: 11, 
                    8: "1.120.1", 
                    9: 3, 
                    10: 1
                }, 
                18: 306, 
                19: 18, 
                24: 902000306, 
                26: {}, 
                27: {
                    1: 11, 
                    2: int(bot_uid), 
                    3: 99999999999
                }, 
                28: {}, 
                31: {
                    1: 1, 
                    2: 32768
                }, 
                32: 32768, 
                34: {
                    1: bot_uid, 
                    2: 8, 
                    3: b"\x10\x15\x08\x0A\x0B\x13\x0C\x0F\x11\x04\x07\x02\x03\x0D\x0E\x12\x01\x05\x06"
                }
            }
        }
        
        # Convert bytes properly
        if isinstance(fields[2][34][3], str):
            fields[2][34][3] = b"\x10\x15\x08\x0A\x0B\x13\x0C\x0F\x11\x04\x07\x02\x03\x0D\x0E\x12\x01\x05\x06"
        
        # Use async versions of your functions
        packet = await CrEaTe_ProTo(fields)
        packet_hex = packet.hex()
        
        # Generate final packet
        final_packet = await GeneRaTePk(packet_hex, '0515', key, iv)
        
        return final_packet
        
    except Exception as e:
        print(f"❌ خطأ في RedZed_SendInv: {e}")
        import traceback
        traceback.print_exc()
        return None
    
async def request_join_with_badge(target_uid, badge_value, key, iv, region):
    """Send join request with specific badge - converted from your old TCP"""
    fields = {
        1: 33,
        2: {
            1: int(target_uid),
            2: region.upper(),
            3: 1,
            4: 1,
            5: bytes([1, 7, 9, 10, 11, 18, 25, 26, 32]),
            6: "iG:[C][B][FF0000] FLASH_FF",
            7: 330,
            8: 1000,
            10: region.upper(),
            11: bytes([49, 97, 99, 52, 98, 56, 48, 101, 99, 102, 48, 52, 55, 56,
                       97, 52, 52, 50, 48, 51, 98, 102, 56, 102, 97, 99, 54, 49, 50, 48, 102, 53]),
            12: 1,
            13: int(target_uid),
            14: {
                1: 2203434355,
                2: 8,
                3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
            },
            16: 1,
            17: 1,
            18: 312,
            19: 46,
            23: bytes([16, 1, 24, 1]),
            24: int(await get_random_avatar()),
            26: "",
            28: "",
            31: {
                1: 1,
                2: badge_value  # Dynamic badge value
            },
            32: badge_value,    # Dynamic badge value
            34: {
                1: int(target_uid),
                2: 8,
                3: bytes([15,6,21,8,10,11,19,12,17,4,14,20,7,2,1,5,16,3,13,18])
            }
        },
        10: "en",
        13: {
            2: 1,
            3: 1
        }
    }
    
    packet = (await CrEaTe_ProTo(fields)).hex()
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk(packet, packet_type, key, iv)    
    
async def start_auto_packet(key, iv, region):
    """Create start match packet"""
    fields = {
        1: 9,
        2: {
            1: 12480598706,
        },
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def leave_squad_packet(key, iv, region):
    """Leave squad packet"""
    fields = {
        1: 7,
        2: {
            1: 12480598706,
        },
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def join_teamcode_packet(team_code, key, iv, region):
    """Join team using code"""
    fields = {
        1: 4,
        2: {
            4: bytes.fromhex("01090a0b121920"),
            5: str(team_code),
            6: 6,
            8: 1,
            9: {
                2: 800,
                6: 11,
                8: "1.111.1",
                9: 5,
                10: 1
            }
        }
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
    
async def auto_start_loop(team_code, uid, chat_id, chat_type, key, iv, region):
    """Auto start loop that joins, starts match, waits, leaves, repeats"""
    global auto_start_running, stop_auto
    
    print(f"[AUTO] بدء حلقة التشغيل التلقائي للفريق {team_code}")
    
    while not stop_auto:
        try:
            # Send status message
            status_msg = f"[B][C][FFA500]🤖 بوت التشغيل التلقائي\n🎯 الفريق: {team_code}\n⚡ جاري الانضمام إلى الفريق..."
            await safe_send_message(chat_type, status_msg, uid, chat_id, key, iv)
            
            # Join team
            join_packet = await join_teamcode_packet(team_code, key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            await asyncio.sleep(2)
            
            # Send start spam status
            start_msg = f"[B][C][00FF00]✅ تم الانضمام إلى الفريق {team_code}\n🎯 بدء المباراة لمدة {start_spam_duration} ثانية..."
            await safe_send_message(chat_type, start_msg, uid, chat_id, key, iv)
            
            # Start spam
            start_packet = await start_auto_packet(key, iv, region)
            end_time = time.time() + start_spam_duration
            spam_count = 0
            
            while time.time() < end_time and not stop_auto:
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', start_packet)
                spam_count += 1
                await asyncio.sleep(start_spam_delay)
            
            if stop_auto:
                break
            
            # Wait after match
            wait_msg = f"[B][C][FFFF00]⏳ بدأت المباراة! البوت في الردهة ينتظر {wait_after_match} ثانية..."
            await safe_send_message(chat_type, wait_msg, uid, chat_id, key, iv)
            
            waited = 0
            while waited < wait_after_match and not stop_auto:
                await asyncio.sleep(1)
                waited += 1
            
            if stop_auto:
                break
            
            # Leave squad
            leave_msg = f"[B][C][FF0000]🔄 مغادرة الفريق {team_code} لإعادة الانضمام والبدء مرة أخرى..."
            await safe_send_message(chat_type, leave_msg, uid, chat_id, key, iv)
            
            leave_packet = await leave_squad_packet(key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
            await asyncio.sleep(2)
            
        except Exception as e:
            print(f"[AUTO] خطأ في auto_start_loop: {e}")
            error_msg = f"[B][C][FF0000]❌ خطأ في التشغيل التلقائي: {str(e)}\n"
            await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
            break
    
    auto_start_running = False
    stop_auto = False
    print(f"[AUTO] تم إيقاف حلقة التشغيل التلقائي للفريق {team_code}")
    
async def reset_bot_state(key, iv, region):
    """Reset bot to solo mode before spam - Critical step from your old TCP"""
    try:
        # Leave any current squad (using your exact leave_s function)
        leave_packet = await leave_squad(key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        await asyncio.sleep(0.5)
        
        print("✅ تم إعادة تعيين حالة البوت - مغادرة الفريق")
        return True
        
    except Exception as e:
        print(f"❌ خطأ في إعادة تعيين البوت: {e}")
        return False    
    
async def create_custom_room(room_name, room_password, max_players, key, iv, region):
    """Create a custom room"""
    fields = {
        1: 3,  # Create room packet type
        2: {
            1: room_name,
            2: room_password,
            3: max_players,  # 2, 4, 8, 16, etc.
            4: 1,  # Room mode
            5: 1,  # Map
            6: "en",  # Language
            7: {   # Player info
                1: "BotHost",
                2: int(await get_random_avatar()),
                3: 330,
                4: 1048576,
                5: "BOTCLAN"
            }
        }
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)              
            
async def real_multi_account_join(target_uid, key, iv, region):
    """Send join requests using real account sessions"""
    try:
        # Load accounts
        accounts_data = load_accounts()
        if not accounts_data:
            return 0, 0
        
        success_count = 0
        total_accounts = len(accounts_data)
        
        for account_uid, password in accounts_data.items():
            try:
                print(f"🔄 جاري توثيق الحساب: {account_uid}")
                
                # Get proper tokens for this account
                open_id, access_token = await GeNeRaTeAccEss(account_uid, password)
                if not open_id or not access_token:
                    print(f"❌ فشل توثيق {account_uid}")
                    continue
                
                # Create a proper join request using the account's identity
                # We'll use the existing SEnd_InV function but with account context
                join_packet = await create_authenticated_join(target_uid, account_uid, key, iv, region)
                
                if join_packet:
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
                    success_count += 1
                    print(f"✅ تم إرسال طلب انضمام من الحساب الموثق: {account_uid}")
                
                # Important: Wait between requests
                await asyncio.sleep(2)
                
            except Exception as e:
                print(f"❌ خطأ مع الحساب {account_uid}: {e}")
                continue
        
        return success_count, total_accounts
        
    except Exception as e:
        print(f"❌ خطأ في الانضمام متعدد الحسابات: {e}")
        return 0, 0



async def handle_badge_command(cmd, inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle individual badge commands"""
    parts = inPuTMsG.strip().split()
    if len(parts) < 2:
        error_msg = f"[B][C][FF0000]❌ الاستخدام: /{cmd} (معرف)\nمثال: /{cmd} 123456789\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    target_uid = parts[1]
    badge_value = BADGE_VALUES.get(cmd, 1048576)
    
    if not target_uid.isdigit():
        error_msg = f"[B][C][FF0000]❌ الرجاء إدخال معرف لاعب صحيح!\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Send initial message
    initial_msg = f"[B][C][1E90FF]🌀 تم استلام الطلب! جاري إرسال الطلبات إلى {target_uid}...\n"
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
    
    try:
        # Reset bot state
        await reset_bot_state(key, iv, region)
        
        # Create and send join packets
        join_packet = await request_join_with_badge(target_uid, badge_value, key, iv, region)
        spam_count = 3
        
        for i in range(spam_count):
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            print(f"✅ تم إرسال طلب /{cmd} #{i+1} بالشارة {badge_value}")
            await asyncio.sleep(0.1)
        
        success_msg = f"[B][C][00FF00]✅ تم إرسال {spam_count} طلبات انضمام بنجاح!\n🎯 الهدف: {target_uid}\n🏷️ الشارة: {badge_value}\n"
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
        # Cleanup
        await asyncio.sleep(1)
        await reset_bot_state(key, iv, region)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ خطأ في /{cmd}: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

async def create_authenticated_join(target_uid, account_uid, key, iv, region):
    """Create join request that appears to come from the specific account"""
    try:
        # Use the standard invite function but ensure it uses account context
        join_packet = await SEnd_InV(5, int(target_uid), key, iv, region)
        return join_packet
    except Exception as e:
        print(f"❌ خطأ في إنشاء حزمة الانضمام: {e}")
        return None        
    
    async def create_account_join_packet(self, target_uid, account_uid, open_id, access_token, key, iv, region):
        """Create join request packet for specific account"""
        try:
            # This is where you use the account's actual UID instead of main bot UID
            fields = {
                1: 33,
                2: {
                    1: int(target_uid),  # Target UID
                    2: region.upper(),
                    3: 1,
                    4: 1,
                    5: bytes([1, 7, 9, 10, 11, 18, 25, 26, 32]),
                    6: f"BOT:[C][B][FF0000] ACCOUNT_{account_uid[-4:]}",  # Show account UID
                    7: 330,
                    8: 1000,
                    10: region.upper(),
                    11: bytes([49, 97, 99, 52, 98, 56, 48, 101, 99, 102, 48, 52, 55, 56,
                               97, 52, 52, 50, 48, 51, 98, 102, 56, 102, 97, 99, 54, 49, 50, 48, 102, 53]),
                    12: 1,
                    13: int(account_uid),  # Use the ACCOUNT'S UID here, not target UID!
                    14: {
                        1: 2203434355,
                        2: 8,
                        3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
                    },
                    16: 1,
                    17: 1,
                    18: 312,
                    19: 46,
                    23: bytes([16, 1, 24, 1]),
                    24: int(await get_random_avatar()),
                    26: "",
                    28: "",
                    31: {
                        1: 1,
                        2: 32768  # V-Badge
                    },
                    32: 32768,
                    34: {
                        1: int(account_uid),  # Use the ACCOUNT'S UID here too!
                        2: 8,
                        3: bytes([15,6,21,8,10,11,19,12,17,4,14,20,7,2,1,5,16,3,13,18])
                    }
                },
                10: "en",
                13: {
                    2: 1,
                    3: 1
                }
            }
            
            packet = (await CrEaTe_ProTo(fields)).hex()
            
            if region.lower() == "ind":
                packet_type = '0514'
            elif region.lower() == "bd":
                packet_type = "0519"
            else:
                packet_type = "0515"
                
            return await GeneRaTePk(packet, packet_type, key, iv)
            
        except Exception as e:
            print(f"❌ خطأ في إنشاء حزمة الانضمام لـ {account_uid}: {e}")
            return None

# Global instance
multi_account_manager = MultiAccountManager()
    
    
    
async def auto_rings_emote_dual(sender_uid, key, iv, region):
    """Send The Rings emote to both sender and bot for dual emote effect"""
    try:
        # The Rings emote ID
        rings_emote_id = 909050009
        
        # Get bot's UID
        bot_uid = 13777711848
        
        # Send emote to SENDER (person who invited)
        emote_to_sender = await Emote_k(int(sender_uid), rings_emote_id, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_sender)
        
        # Small delay between emotes
        await asyncio.sleep(0.5)
        
        # Send emote to BOT (bot performs emote on itself)
        emote_to_bot = await Emote_k(int(bot_uid), rings_emote_id, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_bot)
        
        print(f"🤖 قام البوت بإرسال إيموجي Rings مزدوج مع المرسل {sender_uid} والبوت {bot_uid}!")
        
    except Exception as e:
        print(f"خطأ في إرسال الإيموجي المزدوج: {e}")    
        
        
async def Room_Spam(Uid, Rm, Nm, K, V):
   
    same_value = random.choice([32768])  #you can add any badge value 
    
    fields = {
        1: 78,
        2: {
            1: int(Rm),  
            2: "iG:[C][B][FF0000] FLASH_FF",  
            3: {
                2: 1,
                3: 1
            },
            4: 330,      
            5: 6000,     
            6: 201,      
            10: int(await get_random_avatar()),  
            11: int(Uid), # Target UID
            12: 1,       
            15: {
                1: 1,
                2: same_value  
            },
            16: same_value,    
            18: {
                1: 11481904755,  
                2: 8,
                3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
            },
            
            31: {
                1: 1,
                2: same_value  
            },
            32: same_value,    
            34: {
                1: int(Uid),   
                2: 8,
                3: bytes([15,6,21,8,10,11,19,12,17,4,14,20,7,2,1,5,16,3,13,18])
            }
        }
    }
    
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0e15', K, V)
    
async def evo_cycle_spam(uids, key, iv, region):
    """Cycle through all evolution emotes one by one with 5-second delay"""
    global evo_cycle_running
    
    cycle_count = 0
    while evo_cycle_running:
        cycle_count += 1
        print(f"بدء دورة الإيموجي التطوري #{cycle_count}")
        
        for emote_number, emote_id in evo_emotes.items():
            if not evo_cycle_running:
                break
                
            print(f"إرسال الإيموجي التطوري {emote_number} (المعرف: {emote_id})")
            
            for uid in uids:
                try:
                    uid_int = int(uid)
                    H = await Emote_k(uid_int, int(emote_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                    print(f"تم إرسال الإيموجي {emote_number} إلى المعرف: {uid}")
                except Exception as e:
                    print(f"خطأ في إرسال الإيموجي التطوري {emote_number} إلى {uid}: {e}")
            
            # Wait 5 seconds before moving to next emote (as requested)
            if evo_cycle_running:
                print(f"انتظار 5 ثوانٍ قبل الإيموجي التالي...")
                for i in range(5):
                    if not evo_cycle_running:
                        break
                    await asyncio.sleep(1)
        
        # Small delay before restarting the cycle
        if evo_cycle_running:
            print("اكتملت دورة كاملة من جميع الإيموجيات التطورية. إعادة التشغيل...")
            await asyncio.sleep(2)
    
    print("تم إيقاف دورة الإيموجي التطوري")
    
async def reject_spam_loop(target_uid, key, iv):
    """Send reject spam packets to target in background"""
    global reject_spam_running
    
    count = 0
    max_spam = 150
    
    while reject_spam_running and count < max_spam:
        try:
            # Send both packets
            packet1 = await banecipher1(target_uid, key, iv)
            packet2 = await banecipher(target_uid, key, iv)
            
            # Send to Online connection
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', packet1)
            await asyncio.sleep(0.1)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', packet2)
            
            count += 1
            print(f"تم إرسال رفض مزعج #{count} إلى {target_uid}")
            
            # 0.2 second delay between spam cycles
            await asyncio.sleep(0.2)
            
        except Exception as e:
            print(f"خطأ في الرفض المزعج: {e}")
            break
    
    return count    
    
async def handle_reject_completion(spam_task, target_uid, sender_uid, chat_id, chat_type, key, iv):
    """Handle completion of reject spam and send final message"""
    try:
        spam_count = await spam_task
        
        # Send completion message
        if spam_count >= 150:
            completion_msg = f"[B][C][00FF00]✅ اكتمل الرفض المزعج بنجاح للمعرف {target_uid}\n✅ إجمالي الحزم المرسلة: {spam_count * 2}\n"
        else:
            completion_msg = f"[B][C][FFFF00]⚠️ اكتمل الرفض المزعج جزئياً للمعرف {target_uid}\n⚠️ إجمالي الحزم المرسلة: {spam_count * 2}\n"
        
        await safe_send_message(chat_type, completion_msg, sender_uid, chat_id, key, iv)
        
    except asyncio.CancelledError:
        print("تم إلغاء الرفض المزعج")
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ خطأ في الرفض المزعج: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, sender_uid, chat_id, key, iv)    
    
async def banecipher(client_id, key, iv):
    """Create reject spam packet 1 - Converted to new async format"""
    banner_text = f"""
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][0000FF]======================================================================================================================================================================================================================================================
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███




"""        
    fields = {
        1: 5,
        2: {
            1: int(client_id),
            2: 1,
            3: int(client_id),
            4: banner_text
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)

async def banecipher1(client_id, key, iv):
    """Create reject spam packet 2 - Converted to new async format"""
    gay_text = f"""
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[0000. 0000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][0000FF]======================================================================================================================================================================================================================================================
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███




"""        
    fields = {
        1: int(client_id),
        2: 5,
        4: 50,
        5: {
            1: int(client_id),
            2: gay_text,
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)
    

async def lag_team_loop(team_code, key, iv, region):
    """Rapid join/leave loop to create lag"""
    global lag_running
    count = 0
    
    while lag_running:
        try:
            # Join the team
            join_packet = await GenJoinSquadsPacket(team_code, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            
            # Very short delay before leaving
            await asyncio.sleep(0.01)  # 10 milliseconds
            
            # Leave the team
            leave_packet = await ExiT(None, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
            
            count += 1
            print(f"دورة التأخير #{count} مكتملة للفريق: {team_code}")
            
            # Short delay before next cycle
            await asyncio.sleep(0.01)  # 10 milliseconds between cycles
            
        except Exception as e:
            print(f"خطأ في حلقة التأخير: {e}")
            # Continue the loop even if there's an error
            await asyncio.sleep(0.1)
 
####################################
def bundle_packet(self, bundle_id, target_uid):
        fields = {
            1: 88,
            2: {
                1: {
                    1: bundle_id,
                    2: 1
                },
                2: 2
            }
        }
        packet = create_protobuf_packet(fields).hex()
        encrypted = encrypt_packet(packet, self.key, self.iv)
        header_length = len(encrypted) // 2
        header_length_hex = dec_to_hex(header_length)

        if len(header_length_hex) == 2:
            final_header = "0515000000"
        elif len(header_length_hex) == 3:
            final_header = "051500000"
        elif len(header_length_hex) == 4:
            final_header = "05150000"
        elif len(header_length_hex) == 5:
            final_header = "0515000"
        else:
            final_header = "0515000000"

        final_packet = final_header + header_length_hex + encrypted
        return bytes.fromhex(final_packet)

async def bundle_packet_async(bundle_id, key, iv, region="ind"):
    """Create bundle packet"""
    fields = {
        1: 88,
        2: {
            1: {
                1: bundle_id,
                2: 1
            },
            2: 2
        }
    }
    
    # Use your CrEaTe_ProTo function
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use your encrypt_packet function
    encrypted = await encrypt_packet(packet_hex, key, iv)
    
    # Use your DecodE_HeX function
    header_length = len(encrypted) // 2
    header_length_hex = await DecodE_HeX(header_length)
    
    # Build final packet based on region
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    
    # Determine header based on length
    if len(header_length_hex) == 2:
        final_header = f"{packet_type}000000"
    elif len(header_length_hex) == 3:
        final_header = f"{packet_type}00000"
    elif len(header_length_hex) == 4:
        final_header = f"{packet_type}0000"
    elif len(header_length_hex) == 5:
        final_header = f"{packet_type}000"
    else:
        final_header = f"{packet_type}000000"
    
    final_packet_hex = final_header + header_length_hex + encrypted
    return bytes.fromhex(final_packet_hex)

	
#Clan-info-by-clan-id
def Get_clan_info(clan_id):
    try:
        url = f"https://get-clan-info.vercel.app/get_clan_info?clan_id={clan_id}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            msg = f""" 
[11EAFD][b][c]
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
▶▶▶▶تفاصيل النقابة◀◀◀◀
الإنجازات: {data['achievements']}\n\n
الرصيد : {fix_num(data['balance'])}\n\n
اسم النقابة : {data['clan_name']}\n\n
وقت انتهاء الصلاحية : {fix_num(data['guild_details']['expire_time'])}\n\n
الأعضاء المتصلون : {fix_num(data['guild_details']['members_online'])}\n\n
المنطقة : {data['guild_details']['regional']}\n\n
وقت المكافأة : {fix_num(data['guild_details']['reward_time'])}\n\n
إجمالي الأعضاء : {fix_num(data['guild_details']['total_members'])}\n\n
المعرف : {fix_num(data['id'])}\n\n
آخر نشاط : {fix_num(data['last_active'])}\n\n
المستوى : {fix_num(data['level'])}\n\n
الترتيب : {fix_num(data['rank'])}\n\n
المنطقة : {data['region']}\n\n
النقاط : {fix_num(data['score'])}\n\n
الطابع الزمني1 : {fix_num(data['timestamp1'])}\n\n
الطابع الزمني2 : {fix_num(data['timestamp2'])}\n\n
رسالة الترحيب: {data['welcome_message']}\n\n
نقاط الخبرة: {fix_num(data['xp'])}\n\n
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
            """
            return msg
        else:
            msg = """
[11EAFD][b][c]
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
فشل الحصول على المعلومات، يرجى المحاولة لاحقاً!!

°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
            """
            return msg
    except:
        pass
#GET INFO BY PLAYER ID
def get_player_info(player_id):
    url = f"https://like2.vercel.app/player-info?uid={player_id}&server={server2}&key={key2}"
    response = requests.get(url)
    print(response)    
    if response.status_code == 200:
        try:
            r = response.json()
            return {
                "مستوى Booyah Pass": f"{r.get('booyah_pass_level', 'N/A')}",
                "تاريخ إنشاء الحساب": f"{r.get('createAt', 'N/A')}",
                "مستوى الحساب": f"{r.get('level', 'N/A')}",
                "إعجابات الحساب": f" {r.get('likes', 'N/A')}",
                "الاسم": f"{r.get('nickname', 'N/A')}",
                "المعرف": f" {r.get('accountId', 'N/A')}",
                "منطقة الحساب": f"{r.get('region', 'N/A')}",
                }
        except ValueError as e:
            pass
            return {
                "error": "استجابة JSON غير صالحة"
            }
    else:
        pass
        return {
            "error": f"فشل جلب البيانات: {response.status_code}"
        }
#GET PLAYER BIO 
def get_player_bio(uid):
    try:
        url = f"https://mg24-gamer-super-info-api.vercel.app/get?uid={uid}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            # Bio is inside socialInfo -> signature
            bio = data.get('socialinfo', {}).get('signature', 'لا توجد سيرة ذاتية')
            if bio:
                return bio
            else:
                return "لا توجد سيرة ذاتية متاحة"
        else:
            return f"فشل جلب السيرة الذاتية. رمز الحالة: {res.status_code}"
    except Exception as e:
        return f"حدث خطأ: {e}"
#GET PLAYER INFO 
def get_player_basic(uid):
    try:
        url = f"https://mg24-gamer-super-info-api.vercel.app/get?uid={uid}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            # basic is inside socialInfo -> signature
            basic = data.get('AccountInfo', {}).get('AccountName', 'غير معروف')
            level = data.get('AccountInfo', {}).get('AccountLevel', None)
            like = data.get('AccountInfo', {}).get('AccountLikes', None)
            region = data.get('AccountInfo', {}).get('AccountRegion', None)
            version = data.get('AccountInfo', {}).get('ReleaseVersion', None)
            guild_name = data.get('GuildInfo', {}).get('GuildName', None)
            bp_badge = data.get('AccountInfo', {}).get('AccountBPBadges', None)
            if basic:
                return f"""
[C][B][FFFF00]━━━━━━━━━━━━
[C][B][FFFFFF]الاسم: [66FF00]{basic}
[C][B][FFFFFF]المستوى: [66FF00]{level}
[C][B][FFFFFF]الإعجابات: [66FF00]{like}
[C][B][FFFFFF]المنطقة: [66FF00]{region}
[C][B][FFFFFF]آخر إصدار دخول: [66FF00]{version}
[C][B][FFFFFF]شارة Booyah Pass: [66FF00]{bp_badge}
[C][B][FFFFFF]اسم النقابة: [66FF00]{guild_name}
[C][B][FFFF00]━━━━━━━━━━━━
"""
            else:
                return "لا توجد معلومات أساسية متاحة"
        else:
            return f"فشل جلب المعلومات الأساسية. رمز الحالة: {res.status_code}"
    except Exception as e:
        return f"حدث خطأ: {e}"
#GET ADD FRIEND
def get_player_add(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=GUEST_UID&password=YOUR_GUEST_UID&friend_uid={uid}"
        res = requests.get(url)
        data = res.json()
            # add is inside socialInfo -> signature
        action = data.get('action', 'Unknown')
        status = data.get('status', 'Unknown')
        message = data.get('message', 'No message received')
        if action:
            return message
        else:
            return message
    except Exception as e:
        return f"حدث خطأ: {e}"

# ১ থেকে ১০০ পর্যন্ত প্রতিটি আইডি এবং পাসওয়ার্ড আলাদা ফাংশন হিসেবে নিচে দেওয়া হলো:
def get_player_add_1(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379818952&password=FLASH_FF_KING_ZL4Y&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_2(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379808011&password=FLASH_FF_KING_M6QE&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_3(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379808118&password=FLASH_FF_KING_KFYN&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_4(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379808121&password=FLASH_FF_KING_DBWT&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_5(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379808005&password=FLASH_FF_KING_A6LQ&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_6(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379808465&password=FLASH_FF_KING_4K2T&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_7(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379808488&password=FLASH_FF_KING_3WYS&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_8(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379808492&password=FLASH_FF_KING_8TO0&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_9(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379808487&password=FLASH_FF_KING_IHLA&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_10(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379808744&password=FLASH_FF_KING_4RLN&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_11(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379808757&password=FLASH_FF_KING_AI2C&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_12(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379808745&password=FLASH_FF_KING_JM3R&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_13(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379808736&password=FLASH_FF_KING_55MV&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_14(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379808779&password=FLASH_FF_KING_OL5G&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_15(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379809073&password=FLASH_FF_KING_4XV3&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_16(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379809095&password=FLASH_FF_KING_9F3O&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_17(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379809093&password=FLASH_FF_KING_87FM&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_18(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379809105&password=FLASH_FF_KING_YYEX&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_19(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379809060&password=FLASH_FF_KING_A0QN&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_20(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379809304&password=FLASH_FF_KING_QX77&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_21(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379809342&password=FLASH_FF_KING_NW2V&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_22(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379809363&password=FLASH_FF_KING_FGOW&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_23(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379809353&password=FLASH_FF_KING_7P6P&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_24(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379809476&password=FLASH_FF_KING_8RMP&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_25(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379809547&password=FLASH_FF_KING_VWJH&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_26(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379809582&password=FLASH_FF_KING_FHE1&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_27(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379809598&password=FLASH_FF_KING_GRCL&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_28(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379809754&password=FLASH_FF_KING_0YSB&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_29(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379810560&password=FLASH_FF_KING_HXLD&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_30(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379810647&password=FLASH_FF_KING_OJVS&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_31(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379810661&password=FLASH_FF_KING_BSK8&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_32(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379810909&password=FLASH_FF_KING_YKF9&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_33(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379810900&password=FLASH_FF_KING_PE0H&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_34(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379810922&password=FLASH_FF_KING_I0QH&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_35(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379811000&password=FLASH_FF_KING_N7NM&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_36(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379810998&password=FLASH_FF_KING_TYRL&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_37(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379811235&password=FLASH_FF_KING_WZB7&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_38(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379811249&password=FLASH_FF_KING_GPS0&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_39(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379811282&password=FLASH_FF_KING_IPS6&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_40(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379811297&password=FLASH_FF_KING_QKR9&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_41(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379811310&password=FLASH_FF_KING_1I6E&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_42(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379811554&password=FLASH_FF_KING_0TCA&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_43(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379811557&password=FLASH_FF_KING_D679&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_44(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379811548&password=FLASH_FF_KING_XOJA&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_45(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379812532&password=FLASH_FF_KING_DYLJ&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_46(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379812544&password=FLASH_FF_KING_F9YB&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_47(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379812595&password=FLASH_FF_KING_GM2M&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_48(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379812617&password=FLASH_FF_KING_EZAC&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_49(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379812814&password=FLASH_FF_KING_MI7R&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_50(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379812846&password=FLASH_FF_KING_PSOO&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_51(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379812813&password=FLASH_FF_KING_IZGI&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_52(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379813093&password=FLASH_FF_KING_B6YS&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_53(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379813089&password=FLASH_FF_KING_UUMA&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_54(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379813180&password=FLASH_FF_KING_TGUJ&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_55(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379813168&password=FLASH_FF_KING_JD3L&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_56(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379813269&password=FLASH_FF_KING_8LQW&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_57(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379813368&password=FLASH_FF_KING_9C9J&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_58(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379813378&password=FLASH_FF_KING_3D3L&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_59(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379813428&password=FLASH_FF_KING_73NT&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_60(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379813435&password=FLASH_FF_KING_BRPO&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_61(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379813559&password=FLASH_FF_KING_BFM3&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_62(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379814432&password=FLASH_FF_KING_ON9Q&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_63(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379814474&password=FLASH_FF_KING_4NVV&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_64(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379814479&password=FLASH_FF_KING_OGK0&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_65(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379814533&password=FLASH_FF_KING_UK5X&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_66(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379814523&password=FLASH_FF_KING_SQ6Q&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_67(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379814748&password=FLASH_FF_KING_KGJX&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_68(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379814764&password=FLASH_FF_KING_R7MR&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_69(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379814813&password=FLASH_FF_KING_EQUM&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_70(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379814861&password=FLASH_FF_KING_QPFL&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_71(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379815049&password=FLASH_FF_KING_M4GH&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_72(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379815096&password=FLASH_FF_KING_1JVT&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_73(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379815083&password=FLASH_FF_KING_C94W&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_74(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379815127&password=FLASH_FF_KING_7IEK&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_75(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379815292&password=FLASH_FF_KING_UZ5A&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_76(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379815109&password=FLASH_FF_KING_KTB2&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_77(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379815329&password=FLASH_FF_KING_G4TJ&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_78(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379815335&password=FLASH_FF_KING_7RAV&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_79(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379815591&password=FLASH_FF_KING_ES3B&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_80(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379816326&password=FLASH_FF_KING_H1C1&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_81(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379816379&password=FLASH_FF_KING_PHE5&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_82(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379816369&password=FLASH_FF_KING_KIM7&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_83(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379816395&password=FLASH_FF_KING_IOHF&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_84(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379817290&password=FLASH_FF_KING_K7SF&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_85(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379817308&password=FLASH_FF_KING_TKHF&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_86(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379817306&password=FLASH_FF_KING_HYR5&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_87(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379817897&password=FLASH_FF_KING_EE0P&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_88(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379817940&password=FLASH_FF_KING_SM3A&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_89(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379818394&password=FLASH_FF_KING_3BXP&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_90(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379818381&password=FLASH_FF_KING_Z3E5&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_91(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379818429&password=FLASH_FF_KING_34YL&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_92(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379818752&password=FLASH_FF_KING_9805&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_93(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379818905&password=FLASH_FF_KING_6R63&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_94(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379818947&password=FLASH_FF_KING_2U5S&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_95(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379819004&password=FLASH_FF_KING_IX2J&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_96(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379818952&password=FLASH_FF_KING_ZL4Y&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_97(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379818900&password=FLASH_FF_KING_6R63&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_98(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379818390&password=FLASH_FF_KING_3BXP&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_99(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379817945&password=FLASH_FF_KING_SM3A&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

def get_player_add_100(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/adding_friend?uid=4379817310&password=FLASH_FF_KING_HYR5&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"خطأ: {e}"

async def send_all_friend_requests_async(target_uid):
    # ১০০টি ফাংশনের মাস্টার লিস্ট
    functions = [
        get_player_add_1, get_player_add_2, get_player_add_3, get_player_add_4, get_player_add_5,
        get_player_add_6, get_player_add_7, get_player_add_8, get_player_add_9, get_player_add_10,
        get_player_add_11, get_player_add_12, get_player_add_13, get_player_add_14, get_player_add_15,
        get_player_add_16, get_player_add_17, get_player_add_18, get_player_add_19, get_player_add_20,
        get_player_add_21, get_player_add_22, get_player_add_23, get_player_add_24, get_player_add_25,
        get_player_add_26, get_player_add_27, get_player_add_28, get_player_add_29, get_player_add_30,
        get_player_add_31, get_player_add_32, get_player_add_33, get_player_add_34, get_player_add_35,
        get_player_add_36, get_player_add_37, get_player_add_38, get_player_add_39, get_player_add_40,
        get_player_add_41, get_player_add_42, get_player_add_43, get_player_add_44, get_player_add_45,
        get_player_add_46, get_player_add_47, get_player_add_48, get_player_add_49, get_player_add_50,
        get_player_add_51, get_player_add_52, get_player_add_53, get_player_add_54, get_player_add_55,
        get_player_add_56, get_player_add_57, get_player_add_58, get_player_add_59, get_player_add_60,
        get_player_add_61, get_player_add_62, get_player_add_63, get_player_add_64, get_player_add_65,
        get_player_add_66, get_player_add_67, get_player_add_68, get_player_add_69, get_player_add_70,
        get_player_add_71, get_player_add_72, get_player_add_73, get_player_add_74, get_player_add_75,
        get_player_add_76, get_player_add_77, get_player_add_78, get_player_add_79, get_player_add_80,
        get_player_add_81, get_player_add_82, get_player_add_83, get_player_add_84, get_player_add_85,
        get_player_add_86, get_player_add_87, get_player_add_88, get_player_add_89, get_player_add_90,
        get_player_add_91, get_player_add_92, get_player_add_93, get_player_add_94, get_player_add_95,
        get_player_add_96, get_player_add_97, get_player_add_98, get_player_add_99, get_player_add_100
    ]

    try:
        loop = asyncio.get_event_loop()
        
        # ThreadPoolExecutor ব্যবহার করে ১০০টি রিকোয়েস্টকে নন-ব্লকিং ভাবে সাজানো
        # max_workers=50 দেওয়া হয়েছে যাতে খুব দ্রুত কাজ শেষ হয়
        with ThreadPoolExecutor(max_workers=50) as executor:
            tasks = [
                loop.run_in_executor(executor, func, target_uid) 
                for func in functions
            ]
            
            # সব রিকোয়েস্ট শেষ হওয়া পর্যন্ত অপেক্ষা (কিন্তু বট ফ্রীজ হবে না)
            results = await asyncio.gather(*tasks)
            
        success_count = len([r for r in results if "خطأ" not in r])
        return f"تمت معالجة {success_count}/100 طلب بنجاح."

    except Exception as e:
        return f"خطأ في النظام: {str(e)}"

#GET ADD FRIEND
def get_player_remove(uid):
    try:
        url = f"https://danger-add-friend.vercel.app/remove_friend?uid=GUEST_UID&password=YOUR_GUEST_UID&friend_uid={uid}"
        res = requests.get(url)
        data = res.json()
            # add is inside socialInfo -> signature
        action = data.get('action', 'Unknown')
        status = data.get('status', 'Unknown')
        message = data.get('message', 'No message received')
        if action:
            return message
        else:
            return message
    except Exception as e:
        return f"حدث خطأ: {e}"
#GET PLAYER BAN STATUS
def get_player_ban_status(uid):
    try:
        url = f"http://amin-team-api.vercel.app/check_banned?player_id={uid}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            # status is inside socialInfo -> signature
            status = data.get('status', 'Unknown')
            player_name = data.get('player_name', 'Unknown')
            if status:
                return f"""
 [FFDD00][b][c]
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
[00D1FF]اسم اللاعب: {player_name}
معرف اللاعب : {xMsGFixinG(uid)} 
الحالة: {status}
[FFDD00]°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
[00FF00][b][c]البوت من صنع FLASH FF 
"""
            else:
                return "لا توجد حالة حظر متاحة"
        else:
            return f"فشل جلب حالة الحظر. رمز الحالة: {res.status_code}"
    except Exception as e:
        return f"حدث خطأ: {e}"
#CHAT WITH AI
def talk_with_ai(question):
    url = f"https://princeaiapi.vercel.app/prince/api/v1/ask?key=prince&ask={question}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        msg = data["message"]["content"]
        return msg
    else:
        return "حدث خطأ في الاتصال بالخادم."
#SPAM REQUESTS
def spam_requests(player_id):
    # This URL now correctly points to the Flask app you provided
    url = f"https://like2.vercel.app/send_requests?uid={player_id}&server={server2}&key={key2}"
    try:
        res = requests.get(url, timeout=20) # Added a timeout
        if res.status_code == 200:
            data = res.json()
            # Return a more descriptive message based on the API's JSON response
            return f"حالة API: نجاح [{data.get('success_count', 0)}] فشل [{data.get('failed_count', 0)}]"
        else:
            # Return the error status from the API
            return f"خطأ API: الرمز {res.status_code}"
    except requests.exceptions.RequestException as e:
        # Handle cases where the API isn't running or is unreachable
        print(f"تعذر الاتصال بـ API السبام: {e}")
        return "فشل الاتصال بـ API السبام."

#ADDING-100-LIKES-IN-24H (معدل لاستخدام API الجديد)
def send_likes(uid):
    try:
        # الرابط الجديد مع server_name=me
        likes_api_response = requests.get(
             f"https://duranto-like-pearl.vercel.app/like?uid={uid}&server_name=me",
             timeout=15
             )
      
        if likes_api_response.status_code != 200:
            return f"""
[C][B][FF0000]━━━━━
[FFFFFF]خطأ في API الإعجابات!
رمز الحالة: {likes_api_response.status_code}
يرجى التحقق من صحة المعرف.
━━━━━
"""

        api_json_response = likes_api_response.json()

        player_name = api_json_response.get('PlayerNickname', 'غير معروف')
        likes_before = api_json_response.get('LikesbeforeCommand', 0)
        likes_after = api_json_response.get('LikesafterCommand', 0)
        likes_added = api_json_response.get('LikesGivenByAPI', 0)
        status = api_json_response.get('status', 0)

        if status == 2 and likes_added > 0:  # في الـAPI الجديد status=2 يعني نجاح
            # ✅ Success
            return f"""
[C][B][11EAFD]‎━━━━━━━━━━━━
[FFFFFF]حالة الإعجابات:

[00FF00]تم إرسال الإعجابات بنجاح!

[FFFFFF]اسم اللاعب : [00FF00]{player_name}  
[FFFFFF]الإعجابات المضافة : [00FF00]{likes_added}  
[FFFFFF]الإعجابات قبل : [00FF00]{likes_before}  
[FFFFFF]الإعجابات بعد : [00FF00]{likes_after}  
[C][B][11EAFD]‎━━━━━━━━━━━━
[C][B][FFB300]اشترك: [FFFFFF]FLASH FF [00FF00]!!
"""
        elif status == 1 or likes_before == likes_after:  # status=1 يعني محدود أو مكرر
            # 🚫 Already claimed / Maxed
            return f"""
[C][B][FF0000]━━━━━━━━━━━━

[FFFFFF]لم يتم إرسال الإعجابات!

[FF0000]لقد استلمت إعجابات بهذا المعرف مسبقاً.
حاول مرة أخرى بعد 24 ساعة.

[FFFFFF]اسم اللاعب : [FF0000]{player_name}  
[FFFFFF]الإعجابات قبل : [FF0000]{likes_before}  
[FFFFFF]الإعجابات بعد : [FF0000]{likes_after}  
[C][B][FF0000]━━━━━━━━━━━━
"""
        else:
            # ❓ Unexpected case
            return f"""
[C][B][FF0000]━━━━━━━━━━━━
[FFFFFF]استجابة غير متوقعة!
حدث خطأ ما.

يرجى المحاولة مرة أخرى أو الاتصال بالدعم.
━━━━━━━━━━━━
"""

    except requests.exceptions.RequestException:
        return """
[C][B][FF0000]━━━━━
[FFFFFF]فشل الاتصال بـ API الإعجابات!
هل خادم API (duranto-like-pearl.vercel.app) متاح؟
━━━━━
"""
    except Exception as e:
        return f"""
[C][B][FF0000]━━━━━
[FFFFFF]حدث خطأ غير متوقع:
[FF0000]{str(e)}
━━━━━
"""

#USERNAME TO insta INFO 
def send_insta_info(username):
    try:
        response = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}", timeout=15)
        if response.status_code != 200:
            return f"[B][C][FF0000]❌ خطأ في API Instagram! رمز الحالة: {response.status_code}"

        user = response.json()
        full_name = user.get("full_name", "غير معروف")
        followers = user.get("edge_followed_by", {}).get("count") or user.get("followers_count", 0)
        following = user.get("edge_follow", {}).get("count") or user.get("following_count", 0)
        posts = user.get("media_count") or user.get("edge_owner_to_timeline_media", {}).get("count", 0)
        profile_pic = user.get("profile_pic_url_hd") or user.get("profile_pic_url")
        private_status = user.get("is_private")
        verified_status = user.get("is_verified")

        return f"""
[B][C][FB0364]╭[D21A92]─[BC26AB]╮[FFFF00]╔═══════╗
[C][B][FF7244]│[FE4250]◯[C81F9C]֯│[FFFF00]║[FFFFFF]معلومات Instagram[FFFF00]║
[C][B][FDC92B]╰[FF7640]─[F5066B]╯[FFFF00]╚═══════╝
[C][B][FFFF00]━━━━━━━━━━━━
[C][B][FFFFFF]الاسم: [66FF00]{full_name}
[C][B][FFFFFF]اسم المستخدم: [66FF00]{username}
[C][B][FFFFFF]المتابعون: [66FF00]{followers}
[C][B][FFFFFF]يتابع: [66FF00]{following}
[C][B][FFFFFF]المنشورات: [66FF00]{posts}
[C][B][FFFFFF]خاص: [66FF00]{private_status}
[C][B][FFFFFF]موثق: [66FF00]{verified_status}
[C][B][FFFF00]━━━━━━━━━━━━
"""
    except requests.exceptions.RequestException:
        return "[B][C][FF0000]❌ فشل الاتصال بـ API Instagram!"
    except Exception as e:
        return f"[B][C][FF0000]❌ خطأ غير متوقع: {str(e)}"

####################################
#CHECK ACCOUNT IS BANNED

Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB52"}

# ---- Random Colores ----
def get_random_color():
    colors = [
        "[FF0000]", "[00FF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]",
        "[A52A2A]", "[800080]", "[000000]", "[808080]", "[C0C0C0]", "[FFC0CB]", "[FFD700]", "[ADD8E6]",
        "[90EE90]", "[D2691E]", "[DC143C]", "[00CED1]", "[9400D3]", "[F08080]", "[20B2AA]", "[FF1493]",
        "[7CFC00]", "[B22222]", "[FF4500]", "[DAA520]", "[00BFFF]", "[00FF7F]", "[4682B4]", "[6495ED]",
        "[5F9EA0]", "[DDA0DD]", "[E6E6FA]", "[B0C4DE]", "[556B2F]", "[8FBC8F]", "[2E8B57]", "[3CB371]",
        "[6B8E23]", "[808000]", "[B8860B]", "[CD5C5C]", "[8B0000]", "[FF6347]", "[FF8C00]", "[BDB76B]",
        "[9932CC]", "[8A2BE2]", "[4B0082]", "[6A5ACD]", "[7B68EE]", "[4169E1]", "[1E90FF]", "[191970]",
        "[00008B]", "[000080]", "[008080]", "[008B8B]", "[B0E0E6]", "[AFEEEE]", "[E0FFFF]", "[F5F5DC]",
        "[FAEBD7]"
    ]
    return random.choice(colors)

print(get_random_color())
    
# ---- Random Avatar ----
async def get_random_avatar():
    await asyncio.sleep(0)  # makes it async but instant
    avatar_list = [
        '902050001', '902050002', '902050003', '902039016', '902050004',
        '902047011', '902047010', '902049015', '902050006', '902049020'
    ]
    return random.choice(avatar_list)
    
async def ultra_quick_emote_attack(team_code, emote_id, target_uid, key, iv, region):
    """Join team, authenticate chat, perform emote, and leave automatically"""
    try:
        # Step 1: Join the team
        join_packet = await GenJoinSquadsPacket(team_code, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
        print(f"🤖 تم الانضمام إلى الفريق: {team_code}")
        
        # Wait for team data and chat authentication
        await asyncio.sleep(1.5)  # Increased to ensure proper connection
        
        # Step 2: The bot needs to be detected in the team and authenticate chat
        # This happens automatically in TcPOnLine, but we need to wait for it
        
        # Step 3: Perform emote to target UID
        emote_packet = await Emote_k(int(target_uid), int(emote_id), key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_packet)
        print(f"🎭 تم أداء الإيموجي {emote_id} إلى المعرف {target_uid}")
        
        # Wait for emote to register
        await asyncio.sleep(0.5)
        
        # Step 4: Leave the team
        leave_packet = await ExiT(None, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        print(f"🚪 تم مغادرة الفريق: {team_code}")
        
        return True, f"اكتمل هجوم الإيموجي السريع! تم إرسال الإيموجي إلى المعرف {target_uid}"
        
    except Exception as e:
        return False, f"فشل هجوم الإيموجي السريع: {str(e)}"
        
        
async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload
    
async def GeNeRaTeAccEss(uid , password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": (await Ua()),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"}
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=Hr, data=data) as response:
            if response.status != 200: return "فشل الحصول على رمز الوصول"
            data = await response.json()
            open_id = data.get("open_id")
            access_token = data.get("access_token")
            return (open_id, access_token) if open_id and access_token else (None, None)

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = "1.120.1"
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWA0FUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return  await encrypted_proto(string)

async def MajorLogin(payload):
    url = "https://loginbp.ggblueshark.com/MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization']= f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def DecRypTMajoRLoGin(MajoRLoGinResPonsE):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(MajoRLoGinResPonsE)
    return proto

async def DecRypTLoGinDaTa(LoGinDaTa):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(LoGinDaTa)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto
    
async def decode_team_packet(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = sQ_pb2.recieved_chat()
    proto.ParseFromString(packet)
    return proto
    
async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9: headers = '0000000'
    elif uid_length == 8: headers = '00000000'
    elif uid_length == 10: headers = '000000'
    elif uid_length == 7: headers = '000000000'
    else: print('طول غير متوقع') ; headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"
     
async def cHTypE(H):
    if not H: return 'Squid'
    elif H == 1: return 'CLan'
    elif H == 2: return 'PrivaTe'
    
async def SEndMsG(H , message , Uid , chat_id , key , iv):
    TypE = await cHTypE(H)
    if TypE == 'Squid': msg_packet = await xSEndMsgsQ(message , chat_id , key , iv)
    elif TypE == 'CLan': msg_packet = await xSEndMsg(message , 1 , chat_id , chat_id , key , iv)
    elif TypE == 'PrivaTe': msg_packet = await xSEndMsg(message , 2 , Uid , Uid , key , iv)
    return msg_packet

async def SEndPacKeT(OnLinE , ChaT , TypE , PacKeT):
    if TypE == 'ChaT' and ChaT: whisper_writer.write(PacKeT) ; await whisper_writer.drain()
    elif TypE == 'OnLine': online_writer.write(PacKeT) ; await online_writer.drain()
    else: return 'نوع غير مدعوم! خطأ (:():)' 

async def safe_send_message(chat_type, message, target_uid, chat_id, key, iv, max_retries=3):
    """Safely send message with retry mechanism"""
    for attempt in range(max_retries):
        try:
            P = await SEndMsG(chat_type, message, target_uid, chat_id, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
            print(f"تم إرسال الرسالة بنجاح في المحاولة {attempt + 1}")
            return True
        except Exception as e:
            print(f"فشل إرسال الرسالة (محاولة {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(0.5)  # Wait before retry
    return False

async def fast_emote_spam(uids, emote_id, key, iv, region):
    """Fast emote spam function that sends emotes rapidly"""
    global fast_spam_running
    count = 0
    max_count = 25  # Spam 25 times
    
    while fast_spam_running and count < max_count:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, int(emote_id), key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"خطأ في fast_emote_spam للمعرف {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # 0.1 seconds interval between spam cycles

# NEW FUNCTION: Custom emote spam with specified times
async def custom_emote_spam(uid, emote_id, times, key, iv, region):
    """Custom emote spam function that sends emotes specified number of times"""
    global custom_spam_running
    count = 0
    
    while custom_spam_running and count < times:
        try:
            uid_int = int(uid)
            H = await Emote_k(uid_int, int(emote_id), key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            count += 1
            await asyncio.sleep(0.1)  # 0.1 seconds interval between emotes
        except Exception as e:
            print(f"خطأ في custom_emote_spam للمعرف {uid}: {e}")
            break

# NEW FUNCTION: Faster spam request loop - Sends exactly 30 requests quickly
async def spam_request_loop_with_cosmetics(target_uid, key, iv, region):
    """Spam request function with cosmetics - using your same structure"""
    global spam_request_running
    
    count = 0
    max_requests = 30
    
    # Different badge values to rotate through
    badge_rotation = [1048576, 32768, 2048, 64, 4094, 11233, 262144]
    
    while spam_request_running and count < max_requests:
        try:
            # Rotate through different badges
            current_badge = badge_rotation[count % len(badge_rotation)]
            
            # Create squad (same as before)
            PAc = await OpEnSq(key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
            await asyncio.sleep(0.2)
            
            # Change squad size (same as before)
            C = await cHSq(5, int(target_uid), key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
            await asyncio.sleep(0.2)
            
            # Send invite WITH COSMETICS (enhanced version)
            V = await SEnd_InV_With_Cosmetics(5, int(target_uid), key, iv, region, current_badge)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
            
            # Leave squad (same as before)
            E = await ExiT(None, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
            
            count += 1
            print(f"✅ تم إرسال طلب تجميلي #{count} إلى {target_uid} بالشارة {current_badge}")
            
            # Short delay
            await asyncio.sleep(0.5)
            
        except Exception as e:
            print(f"خطأ في السبام التجميلي: {e}")
            await asyncio.sleep(0.5)
    
    return count
            


# NEW FUNCTION: Evolution emote spam with mapping
async def evo_emote_spam(uids, number, key, iv, region):
    """Send evolution emotes based on number mapping"""
    try:
        emote_id = EMOTE_MAP.get(int(number))
        if not emote_id:
            return False, f"رقم غير صالح! استخدم 1-21 فقط."
        
        success_count = 0
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                success_count += 1
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"خطأ في إرسال الإيموجي التطوري إلى {uid}: {e}")
        
        return True, f"تم إرسال الإيموجي التطوري {number} (المعرف: {emote_id}) إلى {success_count} لاعب(ين)"
    
    except Exception as e:
        return False, f"خطأ في evo_emote_spam: {str(e)}"

# NEW FUNCTION: all emote spam with mapping
async def play_emote_spam(uids, number, key, iv, region):
    """Send all emotes based on number mapping"""
    try:
        emote_id = ALL_EMOTE.get(int(number))
        if not emote_id:
            return False, f"رقم غير صالح! استخدم 1-414 فقط."
        
        success_count = 0
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                success_count += 1
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"خطأ في إرسال الإيموجي العادي إلى {uid}: {e}")
        
        return True, f"تم إرسال الإيموجي العادي {number} (المعرف: {emote_id}) إلى {success_count} لاعب(ين)"
    
    except Exception as e:
        return False, f"خطأ في play_emote_spam: {str(e)}"

# NEW FUNCTION: Fast evolution emote spam
async def evo_fast_emote_spam(uids, number, key, iv, region):
    """Fast evolution emote spam function"""
    global evo_fast_spam_running
    count = 0
    max_count = 25  # Spam 25 times
    
    emote_id = EMOTE_MAP.get(int(number))
    if not emote_id:
        return False, f"رقم غير صالح! استخدم 1-21 فقط."
    
    while evo_fast_spam_running and count < max_count:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"خطأ في evo_fast_emote_spam للمعرف {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # CHANGED: 0.5 seconds to 0.1 seconds
    
    return True, f"اكتمل السبام السريع للإيموجي التطوري {count} مرة"

# NEW FUNCTION: Custom evolution emote spam with specified times
async def evo_custom_emote_spam(uids, number, times, key, iv, region):
    """Custom evolution emote spam with specified repeat times"""
    global evo_custom_spam_running
    count = 0
    
    emote_id = EMOTE_MAP.get(int(number))
    if not emote_id:
        return False, f"رقم غير صالح! استخدم 1-21 فقط."
    
    while evo_custom_spam_running and count < times:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"خطأ في evo_custom_emote_spam للمعرف {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # CHANGED: 0.5 seconds to 0.1 seconds
    
    return True, f"اكتمل السبام المخصص للإيموجي التطوري {count} مرة"
    

async def ArohiAccepted(uid,code,K,V):
    fields = {
        1: 4,
        2: {
            1: uid,
            3: uid,
            8: 1,
            9: {
            2: 161,
            4: "y[WW",
            6: 11,
            8: "1.114.18",
            9: 3,
            10: 1
            },
            10: str(code),
        }
        }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '0515' , K , V)

async def TcPOnLine(ip, port, key, iv, AutHToKen, reconnect_delay=0.5):
    global online_writer, last_status_packet, status_response_cache, insquad, joining_team, whisper_writer, region
    
    if insquad is not None:
        insquad = None
    if joining_team is True:
        joining_team = False
    
    online_writer = None
    whisper_writer = None
    
    while True:
        try:
            print(f"محاولة الاتصال بـ {ip}:{port}...")
            reader, writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            
            # --- AUTHENTICATION ---
            bytes_payload = bytes.fromhex(AutHToKen)
            online_writer.write(bytes_payload)
            await online_writer.drain()
            print("تم إرسال رمز المصادقة. دخول في حلقة القراءة...")
            
            # --- READING LOOP ---
            while True:
                data2 = await reader.read(9999)
                    
                if not data2: 
                    print("تم إغلاق الاتصال من قبل الخادم.")
                    break
                    
                data_hex = data2.hex()
                
                # =================== EMOTE HIJACK ====================
                if data_hex.startswith('0514'):
                    try:
                        # Try to extract emote info from encrypted packet
                        decrypted = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(decrypted)
                        
                        # Check for Type 21 (emote packet)
                        if packet_json.get('1') == 21:
                            if '2' in packet_json and 'data' in packet_json['2']:
                                emote_data = packet_json['2']['data']
                                
                                if ('1' in emote_data and '2' in emote_data and 
                                    '5' in emote_data and 'data' in emote_data['5']):
                                    
                                    nested = emote_data['5']['data']
                                    
                                    if '1' in nested and '3' in nested:
                                        sender_uid = nested.get('1', {}).get('data')
                                        emote_id = nested.get('3', {}).get('data')
                                        
                                        print(f"🎯 تم اكتشاف اختطاف الإيموجي!")
                                        print(f"👤 المرسل: {sender_uid}")
                                        print(f"🎭 الإيموجي الأصلي: {emote_id}")
                                        
                                        # Send special emote back
                                        special_emote = await Emote_k(int(sender_uid), 909038002, key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', special_emote)
                                        print(f"🎁 تم إرسال إيموجي خاص 909038002 إلى {sender_uid}")
                                        
                                        # Mirror user's emote back
                                        await asyncio.sleep(0.3)
                                        try:
                                            mirror_emote_id = int(emote_id)
                                            mirror_packet = await Emote_k(int(sender_uid), mirror_emote_id, key, iv, region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', mirror_packet)
                                            print(f"🔄 عكس إيموجي المستخدم {emote_id} إليه")
                                        except ValueError:
                                            print(f"❌ لا يمكن تحويل معرف الإيموجي: {emote_id}")
                                        
                                        # Bot also does the emote to itself
                                        await asyncio.sleep(0.2)
                                        try:
                                            bot_uid = 13777711848
                                            bot_self_emote = await Emote_k(bot_uid, int(emote_id), key, iv, region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_self_emote)
                                            print(f"🤖 البوت أيضاً يؤدي الإيموجي {emote_id}")
                                        except Exception as e:
                                            print(f"❌ فشل إيموجي البوت الذاتي: {e}")
                                        
                                        continue  # Skip other processing for this packet
                                        
                    except Exception as e:
                        print(f"❌ خطأ في اختطاف الإيموجي: {e}")
                        pass

                # =================== AUTO ACCEPT HANDLING ===================
                
                # Case 1: Squad is cancelled or left
                if data_hex.startswith('0500') and insquad is not None and joining_team == False:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        
                        if packet_json.get('1') in [6, 7]: 
                             insquad = None
                             joining_team = False
                             print("تم إلغاء أو مغادرة الفريق (كود 6/7).")
                             continue
                             
                    except Exception as e:
                        print(f"خطأ في حالة القبول التلقائي 1: {e}")
                        pass
                
                # Case 2: Receiving an invitation while not in a squad (Auto-Join/Accept)
                if data_hex.startswith("0500") and insquad is None and joining_team == False:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        
                        uid = packet_json['5']['data']['2']['data']['1']['data']
                        invite_uid = packet_json['5']['data']['2']['data']['1']['data']
                        squad_owner = packet_json['5']['data']['1']['data']
                        code = packet_json['5']['data']['8']['data']
                        emote_id = 909050009
                        bot_uid = 13777711848
                            
                        SendInv = await RedZed_SendInv(bot_uid, invite_uid, key, iv)
                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', SendInv)
                        inv_packet = await RejectMSGtaxt(squad_owner, uid, key, iv)
                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', inv_packet)
                            
                        print(f"تم استلام دعوة فريق من {squad_owner}، جاري القبول...")                  
                        Join = await ArohiAccepted(squad_owner, code, key, iv)
                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', Join)
                            
                        await asyncio.sleep(2)
                            
                        emote_to_sender = await Emote_k(int(uid), emote_id, key, iv, region)
                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_sender)
                            
                        bot_emote = await Emote_k(int(bot_uid), emote_id, key, iv, region)
                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_emote)

                        insquad = True
                            
                    except Exception as e:
                        print(f"خطأ في القبول التلقائي: {e}")
                        insquad = None
                        joining_team = False
                        continue
                
                # Case 3: Joining Team/Chat handling (long packet)
                if data_hex.startswith('0500') and len(data_hex) > 1000 and joining_team:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        
                        OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet_json)
                        
                        print(f"تم استلام بيانات الفريق للانضمام، محاولة توثيق الدردشة لـ {OwNer_UiD}...")
                        JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                        await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , JoinCHaT)
                        
                        joining_team = False
                            
                    except Exception as e:
                        print(f"خطأ في توثيق دردشة الانضمام للفريق: {e}")
                        pass

                # =================== STATUS HANDLER ===================
                if data_hex.startswith('0f00') and len(data_hex) > 100:
                    print(f"📡 تم استلام حزمة استجابة الحالة")
    
                    try:
                        # Assuming the protocol structure: 0f00 + length bytes + 08 + actual proto data
                        # The split logic might need refinement based on the exact protocol
                        if '08' in data_hex:
                            proto_part = f'08{data_hex.split("08", 1)[1]}'
                        else:
                            print("⚠️ هيكل حزمة الحالة يفتقد علامة '08'.")
                            continue
        
                        # Assuming get_available_room is available
                        parsed_data = get_available_room(proto_part)
                        if parsed_data:
                            parsed_json = json.loads(parsed_data)
            
                            # Check if it's field 15 (player info)
                            if "2" in parsed_json and parsed_json["2"]["data"] == 15:
                                # Get player ID
                                player_id = parsed_json["5"]["data"]["1"]["data"]["1"]["data"]
                
                                # Assuming get_player_status is available
                                player_status = get_player_status(proto_part) 
                                print(f"✅ تم تحليل حالة {player_id}: {player_status}")
                
                                # Create cache entry
                                cache_entry = {
                                    'status': player_status, 
                                    'packet': proto_part,
                                    'timestamp': time.time(),
                                    'full_packet': data_hex,
                                    'parsed_json': parsed_json
                                }
                
                                # --- SPECIAL CONDITION CHECK ---
                                try:
                                    StatusData = parsed_json
                                    if ("5" in StatusData and "data" in StatusData["5"] and 
                                        "1" in StatusData["5"]["data"] and "data" in StatusData["5"]["data"]["1"] and 
                                        "3" in StatusData["5"]["data"]["1"]["data"] and "data" in StatusData["5"]["data"]["1"]["data"]["3"] and 
                                        StatusData["5"]["data"]["1"]["data"]["3"]["data"] == 1 and 
                                        "11" in StatusData["5"]["data"]["1"]["data"] and "data" in StatusData["5"]["data"]["1"]["data"]["11"] and 
                                        StatusData["5"]["data"]["1"]["data"]["11"]["data"] == 1):
                
                                        print(f"🎯 تم استيفاء الشرط الخاص: اللاعب {player_id} في وضع منفرد مع علامة خاصة 11=1")
                                        cache_entry['special_state'] = 'منفرد_مع_علامة_1'
                
                                except Exception as cond_error:
                                    print(f"⚠️ خطأ في التحقق من الشرط الخاص: {cond_error}")
                                # ------------------------------

                                # If in room, extract room ID
                                if "في غرفة" in player_status:
                                    try:
                                        # Assuming get_idroom_by_idplayer is available
                                        room_id = get_idroom_by_idplayer(proto_part)
                                        if room_id:
                                            cache_entry['room_id'] = room_id
                                            print(f"🏠 تم استخراج معرف الغرفة: {room_id}")
                                    except Exception as room_error:
                                        print(f"فشل استخراج معرف الغرفة: {room_error}")
                
                                # If in squad, extract leader
                                elif "في فريق" in player_status:
                                    try:
                                        # Assuming get_leader is available
                                        leader_id = get_leader(proto_part)
                                        if leader_id:
                                            cache_entry['leader_id'] = leader_id
                                            print(f"👑 معرف القائد: {leader_id}")
                                    except Exception as leader_error:
                                        print(f"فشل استخراج القائد: {leader_error}")
                
                                # Save to FILE cache (Assuming save_to_cache is available)
                                save_to_cache(player_id, cache_entry)
                                print(f"✅ تم الحفظ في الذاكرة المؤقتة: {player_id} = {player_status}")
                
                    except Exception as e:
                        print(f"❌ خطأ في تحليل الحالة: {e}")
                        import traceback
                        traceback.print_exc()
                
                # =================== END STATUS HANDLER ===================               
                # Case 4: General Chat Auth (long packet, not actively joining)
                if data_hex.startswith('0500') and len(data_hex) > 1000 and joining_team == False:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        
                        OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet_json)

                        print(f"تم استلام حزمة طويلة، محاولة توثيق الدردشة العامة لـ {OwNer_UiD}...")
                        JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                        await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , JoinCHaT)

                    except Exception as e:
                        print(f"خطأ في توثيق الدردشة العامة: {e}")
                        pass

                # =================== STATUS HANDLER ===================
                if data_hex.startswith('0f00') and len(data_hex) > 100:
                    print(f"📡 تم استلام حزمة استجابة الحالة")
    
                    try:
                        if '08' in data_hex:
                            proto_part = f'08{data_hex.split("08", 1)[1]}'
                        else:
                            print("⚠️ هيكل حزمة الحالة يفتقد علامة '08'.")
                            continue
        
                        parsed_data = get_available_room(proto_part)
                        if parsed_data:
                            parsed_json = json.loads(parsed_data)
            
                            if "2" in parsed_json and parsed_json["2"]["data"] == 15:
                                player_id = parsed_json["5"]["data"]["1"]["data"]["1"]["data"]
                                player_status = get_player_status(proto_part) 
                                print(f"✅ تم تحليل حالة {player_id}: {player_status}")
                
                                cache_entry = {
                                    'status': player_status, 
                                    'packet': proto_part,
                                    'timestamp': time.time(),
                                    'full_packet': data_hex,
                                    'parsed_json': parsed_json
                                }
                
                                # --- SPECIAL CONDITION CHECK ---
                                try:
                                    StatusData = parsed_json
                                    if ("5" in StatusData and "data" in StatusData["5"] and 
                                        "1" in StatusData["5"]["data"] and "data" in StatusData["5"]["data"]["1"] and 
                                        "3" in StatusData["5"]["data"]["1"]["data"] and "data" in StatusData["5"]["data"]["1"]["data"]["3"] and 
                                        StatusData["5"]["data"]["1"]["data"]["3"]["data"] == 1 and 
                                        "11" in StatusData["5"]["data"]["1"]["data"] and "data" in StatusData["5"]["data"]["1"]["data"]["11"] and 
                                        StatusData["5"]["data"]["1"]["data"]["11"]["data"] == 1):
                
                                        print(f"🎯 تم استيفاء الشرط الخاص: اللاعب {player_id} في وضع منفرد مع علامة خاصة 11=1")
                                        cache_entry['special_state'] = 'منفرد_مع_علامة_1'
                
                                except Exception as cond_error:
                                    print(f"⚠️ خطأ في التحقق من الشرط الخاص: {cond_error}")
                                
                                # Extract room ID if in room
                                if "في غرفة" in player_status:
                                    try:
                                        room_id = get_idroom_by_idplayer(proto_part)
                                        if room_id:
                                            cache_entry['room_id'] = room_id
                                            print(f"🏠 تم استخراج معرف الغرفة: {room_id}")
                                    except Exception as room_error:
                                        print(f"فشل استخراج معرف الغرفة: {room_error}")
                
                                # Extract leader if in squad
                                elif "في فريق" in player_status:
                                    try:
                                        leader_id = get_leader(proto_part)
                                        if leader_id:
                                            cache_entry['leader_id'] = leader_id
                                            print(f"👑 معرف القائد: {leader_id}")
                                    except Exception as leader_error:
                                        print(f"فشل استخراج القائد: {leader_error}")
                
                                # Save to cache
                                # Assuming save_to_cache function exists
                                # save_to_cache(player_id, cache_entry)
                                print(f"✅ تم تحديث ذاكرة الحالة المؤقتة: {player_id} = {player_status}")
                
                    except Exception as e:
                        print(f"❌ خطأ في تحليل الحالة: {e}")
                        import traceback
                        traceback.print_exc()
                

            # --- CLEANUP AFTER INNER LOOP (Connection closed) ---
            if online_writer is not None:
                online_writer.close()
                await online_writer.wait_closed()
                online_writer = None
            
            if whisper_writer is not None:
                try:
                    whisper_writer.close()
                    await whisper_writer.wait_closed()
                except:
                    pass
                whisper_writer = None
                
            insquad = None
            joining_team = False
            
            print(f"تم إغلاق الاتصال. إعادة الاتصال بعد {reconnect_delay} ثانية...")

        except ConnectionRefusedError:
            print(f"تم رفض الاتصال بـ {ip}:{port}. إعادة المحاولة...")
            await asyncio.sleep(reconnect_delay)
        except asyncio.TimeoutError:
            print(f"انتهت مهلة الاتصال بـ {ip}:{port}. إعادة المحاولة...")
            await asyncio.sleep(reconnect_delay)
        except Exception as e:
            print(f"خطأ غير متوقع في TcPOnLine: {e}")
            await asyncio.sleep(reconnect_delay)
                            
async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region , reconnect_delay=0.5):
    print(region, 'TCP CHAT')

    global spam_room , whisper_writer , spammer_uid , spam_chat_id , spam_uid , online_writer , chat_id , XX , uid , Spy,data2, Chat_Leave, fast_spam_running, fast_spam_task, custom_spam_running, custom_spam_task, spam_request_running, spam_request_task, evo_fast_spam_running, evo_fast_spam_task, evo_custom_spam_running, evo_custom_spam_task, lag_running, lag_task, evo_cycle_running, evo_cycle_task, reject_spam_running, reject_spam_task
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            whisper_writer.write(bytes_payload)
            await whisper_writer.drain()
            ready_event.set()
            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                print('\n - البوت المستهدف في نقابة! ')
                print(f' - معرف النقابة > {clan_id}')
                print(f' - تم اتصال البوت بنجاح مع دردشة النقابة! ')
                pK = await AuthClan(clan_id , clan_compiled_data , key , iv)
                if whisper_writer: whisper_writer.write(pK) ; await whisper_writer.drain()
            while True:
                data = await reader.read(9999)
                if not data: break
                
                if data.hex().startswith("120000"):

                    msg = await DeCode_PackEt(data.hex()[10:])
                    chatdata = json.loads(msg)
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        XX = response.Data.chat_type
                        inPuTMsG = response.Data.msg.lower()
                        
                        # Debug print to see what we're receiving
                        print(f"تم استلام رسالة: {inPuTMsG} من المعرف: {uid} في نوع دردشة: {XX}")
                        
                    except:
                        response = None


                    if response:
                        # ALL COMMANDS NOW WORK IN ALL CHAT TYPES (SQUAD, GUILD, PRIVATE)
                        
                        # AI Command - /ai
                        if inPuTMsG.strip().startswith('/ai '):
                            print('معالجة أمر AI في أي نوع دردشة')
                            
                            question = inPuTMsG[4:].strip()
                            if question:
                                initial_message = f"[B][C]{get_random_color()}\n🤖 الذكاء الاصطناعي يفكر...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    ai_response = await loop.run_in_executor(executor, talk_with_ai, question)
                                
                                # Format the AI response
                                ai_message = f"""
[B][C][00FF00]🤖 رد الذكاء الاصطناعي:

[00FFFF]{ai_response}

[C][B][FFB300]السؤال: [FFFFFF]{question}
"""
                                await safe_send_message(response.Data.chat_type, ai_message, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الرجاء كتابة سؤال بعد /ai\nمثال: /ai ما هي لعبة فري فاير؟\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Likes Command - /likes
                        if inPuTMsG.strip().startswith('/likes '):
                            print('معالجة أمر الإعجابات في أي نوع دردشة')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /likes (معرف)\nمثال: /likes 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nجاري إرسال 100 إعجاب إلى {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    likes_result = await loop.run_in_executor(executor, send_likes, target_uid)
                                
                                await safe_send_message(response.Data.chat_type, likes_result, uid, chat_id, key, iv)
                                
                                #TEAM SPAM MESSAGE COMMAND
                        if inPuTMsG.strip().startswith('/ms '):
                            print('معالجة أمر /ms')

                            try:
                                parts = inPuTMsG.strip().split(maxsplit=1)

                                if len(parts) < 2:
                                    error_msg = (
                                        "[B][C][FF0000]❌ خطأ! الاستخدام:\n"
                                        "/ms <الرسالة>\n"
                                        "مثال: /ms FLASH FF"
                                    )
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    user_message = parts[1].strip()

                                    for _ in range(30):
                                        color = get_random_color()  # random color from your list
                                        colored_message = f"[B][C]{color} {user_message}"  # correct format
                                        await safe_send_message(response.Data.chat_type, colored_message, uid, chat_id, key, iv)
                                        await asyncio.sleep(0.5)

                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ خطأ! حدث خطأ ما:\n{str(e)}"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                                #GALI SPAM MESSAGE 
                        if inPuTMsG.strip().startswith('/gali '):
                            print('معالجة أمر /gali')

                            try:
                                parts = inPuTMsG.strip().split(maxsplit=1)

                                if len(parts) < 2:
                                    error_msg = (
                                        "[B][C][FF0000]❌ خطأ! الاستخدام:\n"
                                        "/gali <الاسم>\n"
                                        "مثال: /gali hater"
                                    )
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    name = parts[1].strip()

                                    messages = [
                                        "{Name} يا بن الكلب!!",
                                        "{Name} يا ابن المتناكة, أمك شرموطة!!",
                                        "{Name} يا خول, أمك نيك!!",
                                        "{Name} يا كلب, أمك شرموطة ب 5G!!",
                                        "{Name} يا ابن القحبة, أمك شغالة في الشارع!!",
                                        "اللعنة عليك يا {Name} !!",
                                        "{Name} يا ابن اللذينة, هات مؤخرةك!!",
                                        "{Name} يا شرموط!!",
                                        "{Name} يا كلب, أنا أبو!!",
                                        "{Name} أنا نيكت أمك وجبتك!!",
                                        "{Name} يا ولد المتناكة, يا ابن الكلب!!",
                                        "{Name} يا شرموط, أمك شرموطة بسرعة 180 كم!!",
                                        "{Name} يا ابن الكلب, أيها اللاعب الأحمق!!",
                                        "أكبر بوت في بنغلاديش {Name}",
                                        "{Name} يا حرامي الأحذية!!",
                                        "{Name} يا شرموط, اترك فري فاير والعب لودو!!",
                                        "{Name} مهما تعمل, أنا أبوك لا تنسى هذا أبداً!!"
                                    ]

                                    # Send each message one by one with random color
                                    for msg in messages:
                                        colored_message = f"[B][C]{get_random_color()} {msg.replace('{Name}', name.upper())}"
                                        await safe_send_message(response.Data.chat_type, colored_message, uid, chat_id, key, iv)
                                        await asyncio.sleep(0.5)

                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ خطأ! حدث خطأ ما:\n{str(e)}"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                                #INSTA USERNAME TO INFO-/ig
                        if inPuTMsG.strip().startswith('/ig '):
                            print('معالجة أمر insta في أي نوع دردشة')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /ig <اسم المستخدم>\nمثال: /ig virat.kohli\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_username = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nجلب معلومات Instagram لـ {target_username}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
        
        # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    insta_result = await loop.run_in_executor(executor, send_insta_info, target_username)
        
                                await safe_send_message(response.Data.chat_type, insta_result, uid, chat_id, key, iv)

                                #GET PLAYER BIO-/bio
                        if inPuTMsG.strip().startswith('/bio '):
                            print('معالجة أمر السيرة الذاتية في أي نوع دردشة')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /bio <معرف>\nمثال: /bio 4368569733\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nجلب السيرة الذاتية للاعب...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    bio_result = await loop.run_in_executor(executor, get_player_bio, target_uid)

                                await safe_send_message(response.Data.chat_type, f"[B][C]{get_random_color()}\n{bio_result}", uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/rejectmsg '):
                            print('معالجة أمر السيرة الذاتية في أي نوع دردشة')

                            parts = inPuTMsG.strip().split()
                            uid = parts

                            error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /like <معرف>\nمثال: /like 4368569733\n"
                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                            inv_packet = await RejectMSGtaxt(squad_owner, uid, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', inv_packet)
                                #GET PLAYER LIKE
                        if inPuTMsG.strip().startswith('/like '):
                            print('معالجة أمر الإعجابات في أي نوع دردشة')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /like <معرف>\nمثال: /like 4368569733\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nجاري إرسال الإعجابات...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    like_result = await loop.run_in_executor(executor, send_likes, target_uid)

                                await safe_send_message(response.Data.chat_type, like_result, uid, chat_id, key, iv)

                                #GET PLAYER basic-/info
                        if inPuTMsG.strip().startswith('/info '):
                            print('معالجة أمر المعلومات الأساسية في أي نوع دردشة')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /info <معرف>\nمثال: /info 4368569733\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nجلب معلومات اللاعب...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    basic_result = await loop.run_in_executor(executor, get_player_basic, target_uid)
                                await safe_send_message(response.Data.chat_type, f"\n{basic_result}\n", uid, chat_id, key, iv)

                                #GET PLAYER ADD FRIEND
                        if inPuTMsG.strip().startswith('/add '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /add <معرف>"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}🚀 جاري إرسال طلبات الصداقة..."
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                # ১০০টি রিকোয়েস্ট একসাথে পাঠানোর জন্য মাস্টার ফাংশন কল
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    # এখানে send_all_friend_requests কল করা হচ্ছে
                                    final_result = await loop.run_in_executor(executor, get_player_add, target_uid)

                                await safe_send_message(response.Data.chat_type, f"\n[B][C][00FF00]✅ {final_result}\n", uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/spam_req '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /spam_req <معرف>"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}🚀 جاري إرسال 100 طلب صداقة إلى: {target_uid}..."
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                try:
                                    # এটি ব্যাকগ্রাউন্ডে ১০০টি রিকোয়েস্ট প্রসেস করবে এবং বট ফ্রীজ হবে না
                                    final_result = await send_all_friend_requests_async(target_uid)
                                    
                                    success_msg = f"\n[B][C][00FF00]✅ {final_result}\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    
                                except Exception as e:
                                    await safe_send_message(response.Data.chat_type, f"[B][C][FF0000]❌ خطأ: {str(e)}", uid, chat_id, key, iv)


                                #GET PLAYER REMOVE FRIEND
                        if inPuTMsG.strip().startswith('/remove '):
                            print('معالجة أمر الإزالة في أي نوع دردشة')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /remove <معرف>\nمثال: /remove 4368569733\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}جاري إزالة طلب الصداقة..."
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    remove_result = await loop.run_in_executor(executor, get_player_remove, target_uid)
                                await safe_send_message(response.Data.chat_type, f"\n{remove_result}\n", uid, chat_id, key, iv)

                                initial_message = f"[B][C]{get_random_color()}تمت إزالة الصديق!!"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                #GET PLAYER BAN STATUS
                        if inPuTMsG.strip().startswith('/check '):
                            print('معالجة أمر حالة الحظر في أي نوع دردشة')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /check <معرف>\nمثال: /check 4368569733\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nجلب حالة حظر اللاعب...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    ban_status_result = await loop.run_in_executor(executor, get_player_ban_status, target_uid)
                                await safe_send_message(response.Data.chat_type, f"\n{ban_status_result}\n", uid, chat_id, key, iv)

                        # QUICK EMOTE ATTACK COMMAND - /quick [team_code] [emote_id] [target_uid?]
                        if inPuTMsG.strip().startswith('/quick'):
                            print('معالجة أمر هجوم الإيموجي السريع')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /quick (رمز الفريق) [معرف الإيموجي] [معرف الهدف]\n\n[FFFFFF]أمثلة:\n[00FF00]/quick ABC123[FFFFFF] - انضمام، إرسال إيموجي Rings، مغادرة\n[00FF00]/ghostquick ABC123[FFFFFF] - انضمام خفي، إرسال إيموجي، مغادرة\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
        
                                # Set default values
                                emote_id = parts[0]
                                target_uid = str(response.Data.uid)  # Default: Sender's UID
        
                                # Parse optional parameters
                                if len(parts) >= 3:
                                    emote_id = parts[2]
                                if len(parts) >= 4:
                                    target_uid = parts[3]
        
                                # Determine target name for message
                                if target_uid == str(response.Data.uid):
                                    target_name = "نفسك"
                                else:
                                    target_name = f"المعرف {target_uid}"
        
                                initial_message = f"[B][C][FFFF00]⚡ هجوم إيموجي سريع!\n\n[FFFFFF]🎯 الفريق: [00FF00]{team_code}\n[FFFFFF]🎭 الإيموجي: [00FF00]{emote_id}\n[FFFFFF]👤 الهدف: [00FF00]{target_name}\n[FFFFFF]⏱️ الوقت التقديري: [00FF00]ثانيتين\n\n[FFFF00]جاري تنفيذ التسلسل...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
        
                                try:
                                    # Try regular method first
                                    success, result = await ultra_quick_emote_attack(team_code, emote_id, target_uid, key, iv, region)
            
                                    if success:
                                        success_message = f"[B][C][00FF00]✅ نجاح الهجوم السريع!\n\n[FFFFFF]🏷️ الفريق: [00FF00]{team_code}\n[FFFFFF]🎭 الإيموجي: [00FF00]{emote_id}\n[FFFFFF]👤 الهدف: [00FF00]{target_name}\n\n[00FF00]البوت انضم ← أدى الإيموجي ← غادر! ✅\n"
                                    else:
                                        success_message = f"[B][C][FF0000]❌ فشل الهجوم العادي: {result}\n"
                                    
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    print("فشل")
            
                        if inPuTMsG.startswith('noob'):
                            await handle_alll_titles_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)


# ================= BUNDLE COMMAND START =================
   # ================= FINAL BUNDLE COMMAND (FAST) =================
                        if inPuTMsG.strip().startswith('/bundle'):
                            print('معالجة أمر الحزمة')
    
                            parts = inPuTMsG.strip().split()
                            
                            if len(parts) < 2:
                                # Show available bundles
                                bundle_list = """[B][C][00FF00]🎁 الحزم المتاحة 🎁
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[FFFFFF]• midnight (منتصف الليل)
[FFFFFF]• aurora (الشفق)  
[FFFFFF]• naruto (ناروتو)
[FFFFFF]• paradox (المفارقة)
[FFFFFF]• frostfire (النار الجليدية)
[FFFFFF]• rampage (الهياج)
[FFFFFF]• cannibal (الآكل)
[FFFFFF]• devil (الشيطان)
[FFFFFF]• scorpio (العقرب)
[FFFFFF]• dreamspace (فضاء الأحلام)
[FFFFFF]• itachi (إيتاشي)
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[00FF00]الاستخدام: /bundle [الاسم]
[FFFFFF]مثال: /bundle midnight"""
                                await safe_send_message(response.Data.chat_type, bundle_list, uid, chat_id, key, iv)
                            else:
                                bundle_name = parts[1].lower()
        
                                # All bundles use the same ID: 914000002
                                bundle_id = BUNDLE.get(bundle_name)
        
                                initial_msg = f"[B][C][00FF00]🎁 جاري إرسال {bundle_name}\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Create bundle packet
                                    bundle_packet = await bundle_packet_async(bundle_id, key, iv, region)
            
                                    if bundle_packet and online_writer:
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bundle_packet)
                                        success_msg = f"[B][C][00FF00]✅ تم: {bundle_name}"
                                        await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    else:
                                        error_msg = f"[B][C][FF0000]❌ فشل إنشاء حزمة!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ خطأ في إرسال الحزمة: {str(e)[:50]}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # ===============================================================

                        # Invite Command - /inv (creates 5-player group and sends request)
                        if inPuTMsG.strip().startswith('/inv '):
                            print('معالجة أمر الدعوة في أي نوع دردشة')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /inv (معرف)\nمثال: /inv 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nجاري إنشاء مجموعة 5 لاعبين وإرسال طلب إلى {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:

                                    V = await SEnd_InV(4, int(target_uid), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                                    await asyncio.sleep(0.3)

                                    # SUCCESS MESSAGE
                                    success_message = f"[B][C][00FF00]✅ نجاح! تم إرسال دعوة المجموعة بنجاح إلى {target_uid}!\n"
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                    
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ خطأ في إرسال الدعوة: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)


                        if inPuTMsG.startswith(("/6")):
                            # Process /6 command - Create 4 player group
                            initial_message = f"[B][C]{get_random_color()}\n\nجاري إنشاء مجموعة 6 لاعبين...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite for 4 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(6, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(6, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][00FF00]✅ نجاح! تم إرسال دعوة مجموعة 6 لاعبين بنجاح إلى {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.startswith(("/3")):
                            # Process /3 command - Create 3 player group
                            initial_message = f"[B][C]{get_random_color()}\n\nجاري إنشاء مجموعة 3 لاعبين...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite for 6 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(3, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(3, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][00FF00]✅ نجاح! تم إرسال دعوة مجموعة 3 لاعبين بنجاح إلى {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/roommsg'):
                            print('معالجة أمر رسالة الغرفة')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ الاستخدام: /roommsg (معرف الغرفة) (الرسالة)\nمثال: /roommsg 489775386 مرحباً بالغرفة!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                room_id = parts[1]
                                message = " ".join(parts[2:])
        
                                initial_msg = f"[B][C][00FF00]📢 جاري الإرسال إلى الغرفة {room_id}: {message}\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Get bot UID
                                    bot_uid = LoGinDaTaUncRypTinG.AccountUID if hasattr(LoGinDaTaUncRypTinG, 'AccountUID') else 13699776666
            
                                    # Send room chat using leaked packet structure
                                    room_chat_packet = await send_room_chat_enhanced(message, room_id, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', room_chat_packet)
            
                                    success_msg = f"[B][C][00FF00]✅ تم إرسال الرسالة إلى الغرفة {room_id}!\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    print(f"✅ تم إرسال رسالة الغرفة إلى {room_id}: {message}")
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ فشل: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.startswith(("/5")):
                            # Process /5 command in any chat type
                            initial_message = f"[B][C]{get_random_color()}\n\nجاري إرسال دعوة المجموعة...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(5, uid, key, iv, region)
                            await asyncio.sleep(0.3)  # Reduced delay
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(5, uid, key, iv, region)
                            await asyncio.sleep(0.3)  # Reduced delay
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)  # Reduced from 3 seconds
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][00FF00]✅ نجاح! تم إرسال دعوة المجموعة بنجاح إلى {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.strip() == "/admin":
                            # Process /admin command in any chat type
                            admin_message = """
[C][B][FF0000]╔══════════╗
[FFFFFF]✨ تابعني على اليوتيوب   
[FFFFFF]          ⚡ FLASH FF ❤️  
[FFFFFF]                   شكراً لدعمكم 
[FF0000]╠══════════╣
[FFD700]⚡ المالك : [FFFFFF]FLASH FF    
[FFD700]✨ إذا أحد يريد شراء بوت نقابة، راسلني على التليجرام @juli_dvrma ❤️  
[FF0000]╚══════════╝
[FFD700]✨ المطور —͟͞͞ </> APON GMAING ❄️  ⚡
"""
                            await safe_send_message(response.Data.chat_type, admin_message, uid, chat_id, key, iv)

                        # Add this with your other command handlers in the TcPChaT function
                        if inPuTMsG.strip().startswith('/multijoin'):
                            print('معالجة طلب انضمام متعدد الحسابات')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ الاستخدام: /multijoin (معرف الهدف)\nمثال: /multijoin 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                if not target_uid.isdigit():
                                    error_msg = f"[B][C][FF0000]❌ الرجاء إدخال معرف لاعب صحيح!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                initial_msg = f"[B][C][00FF00]🚀 بدء هجوم انضمام متعدد على {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Try the fake multi-account method (more reliable)
                                    success_count, total_attempts = await real_multi_account_join(target_uid, key, iv, region)
            
                                    if success_count > 0:
                                        result_msg = f"""
[B][C][00FF00]✅ اكتمل هجوم الانضمام المتعدد!

🎯 الهدف: {target_uid}
✅ الطلبات الناجحة: {success_count}
📊 إجمالي المحاولات: {total_attempts}
⚡ تم إرسال مجموعات مختلفة!

💡 تحقق من طلبات الانضمام في لعبتك!
"""
                                    else:
                                        result_msg = f"[B][C][FF0000]❌ فشلت جميع طلبات الانضمام! تحقق من اتصال البوت.\n"
            
                                    await safe_send_message(response.Data.chat_type, result_msg, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ خطأ في الانضمام المتعدد: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

           
                        if inPuTMsG.strip().startswith('/fastmultijoin'):
                            print('معالجة سبام انضمام متعدد سريع')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /fastmultijoin (معرف)\nمثال: /fastmultijoin 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                # Load accounts
                                accounts_data = load_accounts()
                                if not accounts_data:
                                    error_msg = f"[B][C][FF0000]❌ خطأ! لم يتم العثور على حسابات!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
                                
                                initial_msg = f"[B][C][00FF00]⚡ سبام انضمام متعدد سريع!\n🎯 الهدف: {target_uid}\n👥 الحسابات: {len(accounts_data)}\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    join_count = 0
                                    # Send join requests rapidly from all accounts
                                    for uid, password in accounts_data.items():
                                        try:
                                            # Use your existing join request function
                                            join_packet = await SEnd_InV(5, int(target_uid), key, iv, region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
                                            join_count += 1
                                            print(f"✅ انضمام سريع من الحساب {uid}")
                    
                                            # Very short delay
                                            await asyncio.sleep(0.1)
                    
                                        except Exception as e:
                                            print(f"❌ فشل الانضمام السريع لـ {uid}: {e}")
                                            continue
            
                                    success_msg = f"[B][C][00FF00]✅ اكتمل الانضمام المتعدد السريع!\n🎯 الهدف: {target_uid}\n✅ الناجح: {join_count}/{len(accounts_data)}\n⚡ السرعة: فائقة السرعة\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ خطأ في الانضمام المتعدد السريع: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
           
           
                        # Update the command handler
                        if inPuTMsG.strip().startswith('/reject'):
                            print('معالجة أمر سبام الرفض في أي نوع دردشة')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /reject (معرف الهدف)\nمثال: /reject 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                # Stop any existing reject spam
                                if reject_spam_task and not reject_spam_task.done():
                                    reject_spam_running = False
                                    reject_spam_task.cancel()
                                    await asyncio.sleep(0.5)
        
                                # Send start message
                                start_msg = f"[B][C][1E90FF]🌀 بدء سبام الرفض على: {target_uid}\n🌀 الحزم: 150 من كل نوع\n🌀 الفاصل: 0.2 ثانية\n"
                                await safe_send_message(response.Data.chat_type, start_msg, uid, chat_id, key, iv)
        
                                # Start reject spam in background
                                reject_spam_running = True
                                reject_spam_task = asyncio.create_task(reject_spam_loop(target_uid, key, iv))
        
                                # Wait for completion in background and send completion message
                                asyncio.create_task(handle_reject_completion(reject_spam_task, target_uid, uid, chat_id, response.Data.chat_type, key, iv))


                        if inPuTMsG.strip() == '/reject_stop':
                            if reject_spam_task and not reject_spam_task.done():
                                reject_spam_running = False
                                reject_spam_task.cancel()
                                stop_msg = f"[B][C][00FF00]✅ تم إيقاف سبام الرفض بنجاح!\n"
                                await safe_send_message(response.Data.chat_type, stop_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ لا يوجد سبام رفض نشط لإيقافه!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                                                    
                                                                        
                        # In your command handler where you call Room_Spam:
                        if inPuTMsG.strip().startswith('/room'):
                            print('معالجة أمر سبام الغرفة المتقدم')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /room (معرف) (معرف الغرفة)\nمثال: /room 123456789 489775386\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                room_id = parts[2]
        
                                if not target_uid.isdigit():
                                    error_msg = f"[B][C][FF0000]❌ خطأ! الرجاء إدخال معرف لاعب صحيح!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                # Send initial message
                                initial_msg = f"[B][C][00FF00]🔍 جاري العمل على سبام الغرفة لـ {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                                
                                try:
                                    # Method 1: Try to get room ID from recent packets
                                
                                    

                                    room_msg = f"[B][C][00FF00]🎯 تم اكتشاف اللاعب في الغرفة {room_id}\n"
                                    await safe_send_message(response.Data.chat_type, room_msg, uid, chat_id, key, iv)
            
                                    # Create spam packet
                                    spam_packet = await Room_Spam(target_uid, room_id, "FLASH FF", key, iv)
            
                                    # Send 99 spam packets rapidly (like your other TCP)
                                    spam_count = 99
                                    
                                    start_msg = f"[B][C][00FF00]🚀 بدء السبام: {spam_count} حزمة إلى الغرفة {room_id}\n"
                                    await safe_send_message(response.Data.chat_type, start_msg, uid, chat_id, key, iv)
            
                                    for i in range(spam_count):
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', spam_packet)
                
                                        # Progress updates
                                        if (i + 1) % 25 == 0:
                                            progress_msg = f"[B][C][00FF00]📦 التقدم: {i+1}/{spam_count} حزمة مرسلة\n"
                                            await safe_send_message(response.Data.chat_type, progress_msg, uid, chat_id, key, iv)
                                            print(f"تقدم سبام الغرفة: {i+1}/{spam_count} إلى المعرف: {target_uid}")
                
                                        # Very short delay (0.05 seconds = 50ms)
                                        await asyncio.sleep(0.05)
            
                                    # Final success message
                                    success_msg = f"[B][C][00FF00]✅ اكتمل سبام الغرفة!\n🎯 الهدف: {target_uid}\n📦 الحزم: {spam_count}\n🏠 الغرفة: {room_id}\n⚡ السرعة: فائقة السرعة\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    print(f"اكتمل سبام الغرفة للمعرف: {target_uid}")
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ خطأ في سبام الغرفة: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    print(f"خطأ في سبام الغرفة: {e}")          
                                    
                                    
                        # Individual command handlers for /s1 to /s5
                        if inPuTMsG.strip().startswith('/s1'):
                            await handle_badge_command('s1', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
    
                        if inPuTMsG.strip().startswith('/s2'):
                            await handle_badge_command('s2', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s3'):
                            await handle_badge_command('s3', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s4'):
                            await handle_badge_command('s4', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s5'):
                            await handle_badge_command('s5', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                            
                            #ALL BADGE SPAM REQUEST 
                        if inPuTMsG.strip().startswith('/spam'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = "[B][C][FF0000]❌ الاستخدام: /spam <معرف>\nمثال: /spam 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                total_requests = 10  # total join requests
                                sequence = ['s1', 's2', 's3', 's4', 's5']  # all badge commands

                                # Send initial consolidated message
                                initial_msg = f"[B][C][1E90FF]🌀 تم استلام الطلب! جاري إرسال السبام إلى {target_uid} بجميع الشارات...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)

                                count = 0
                                while count < total_requests:
                                    for cmd in sequence:
                                        if count >= total_requests:
                                            break
                                        # Build a fake command string like "/s1 123456789"
                                        fake_command = f"/{cmd} {target_uid}"
                                        await handle_badge_command(cmd, fake_command, uid, chat_id, key, iv, region, response.Data.chat_type)
                                        count += 1

                                # Success message after all 30 requests
                                success_msg = f"[B][C][00FF00]✅ تم إرسال {total_requests} طلب انضمام بنجاح!\n🎯 الهدف: {target_uid}\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                                    
                                                                                             #JOIN ROOM       
                        if inPuTMsG.strip().startswith('/joinroom'):
                            print('معالجة أمر الانضمام إلى غرفة مخصصة')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ الاستخدام: /joinroom (معرف الغرفة) (كلمة المرور)\nمثال: /joinroom 123456 0000\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                room_id = parts[1]
                                room_password = parts[2]
        
                                initial_msg = f"[B][C][00FF00]🚀 جاري الانضمام إلى غرفة مخصصة...\n🏠 الغرفة: {room_id}\n🔑 كلمة المرور: {room_password}\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Join the custom room
                                    join_packet = await join_custom_room(room_id, room_password, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            
                                    success_msg = f"[B][C][00FF00]✅ تم الانضمام إلى الغرفة المخصصة {room_id}!\n🤖 البوت الآن في دردشة الغرفة!\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ فشل الانضمام إلى الغرفة: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/createroom'):
                            print('معالجة إنشاء غرفة مخصصة')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ الاستخدام: /createroom (اسم الغرفة) (كلمة المرور) [اللاعبين=4]\nمثال: /createroom BOTROOM 0000 4\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                room_name = parts[1]
                                room_password = parts[2]
                                max_players = parts[3] if len(parts) > 3 else "4"
        
                                initial_msg = f"[B][C][00FF00]🏠 جاري إنشاء غرفة مخصصة...\n📛 الاسم: {room_name}\n🔑 كلمة المرور: {room_password}\n👥 الحد الأقصى للاعبين: {max_players}\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Create custom room
                                    create_packet = await create_custom_room(room_name, room_password, int(max_players), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', create_packet)
            
                                    success_msg = f"[B][C][00FF00]✅ تم إنشاء الغرفة المخصصة!\n🏠 الغرفة: {room_name}\n🔑 كلمة المرور: {room_password}\n👥 الحد الأقصى: {max_players}\n🤖 البوت الآن هو المضيف!\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ فشل إنشاء الغرفة: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)                                                                                                                                                                                                               
                                                
                                              
                                                                                          # FIXED JOIN COMMAND
                        if inPuTMsG.startswith('/join'):
                            # Process /join command in any chat type
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /join (رمز الفريق)\nمثال: /join ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                CodE = parts[1]
                                sender_uid = response.Data.uid  # Get the UID of person who sent the command
        
                                initial_message = f"[B][C]{get_random_color()}\nجاري الانضمام إلى الفريق برمز: {CodE}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
        
                                try:
                                    # Try using the regular join method first
                                    EM = await GenJoinSquadsPacket(CodE, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', EM)
            
                                    # Wait a bit for the join to complete
                                    await asyncio.sleep(2)
            
                                    # DUAL RINGS EMOTE - BOTH SENDER AND BOT
                                    try:
                                        await auto_rings_emote_dual(sender_uid, key, iv, region)
                                    except Exception as emote_error:
                                        print(f"فشل الإيموجي المزدوج لكن الانضمام نجح: {emote_error}")
            
                                    # SUCCESS MESSAGE
                                    success_message = f"[B][C][00FF00]✅ نجاح! تم الانضمام إلى الفريق: {CodE}!\n💍 تم تفعيل الإيموجي المزدوج Rings!\n🤖 البوت + أنت = 💕\n"
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    print(f"فشل الانضمام العادي، محاولة الانضمام الخفي: {e}")
                                    # If regular join fails, try ghost join
                                    try:
                                        # Get bot's UID from global context or login data
                                        bot_uid = LoGinDaTaUncRypTinG.AccountUID if hasattr(LoGinDaTaUncRypTinG, 'AccountUID') else TarGeT
                
                                        ghost_packet = await ghost_join_packet(bot_uid, CodE, key, iv)
                                        if ghost_packet:
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', ghost_packet)
                    
                                            # Wait a bit for ghost join to complete
                                            await asyncio.sleep(2)
                    
                                            # DUAL RINGS EMOTE - BOTH SENDER AND BOT
                                            try:
                                                await auto_rings_emote_dual(sender_uid, key, iv, region)
                                            except Exception as emote_error:
                                                print(f"فشل الإيموجي المزدوج لكن الانضمام الخفي نجح: {emote_error}")
                    
                                            success_message = f"[B][C][00FF00]✅ نجاح! تم الانضمام الخفي إلى الفريق: {CodE}!\n💍 تم تفعيل الإيموجي المزدوج Rings!\n🤖 البوت + أنت = 💕\n"
                                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                        else:
                                            error_msg = f"[B][C][FF0000]❌ خطأ! فشل إنشاء حزمة الانضمام الخفي.\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                    
                                    except Exception as ghost_error:
                                        print(f"فشل الانضمام الخفي أيضاً: {ghost_error}")
                                        error_msg = f"[B][C][FF0000]❌ خطأ! فشل الانضمام إلى الفريق: {str(ghost_error)}\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                
                
                        if inPuTMsG.strip().startswith('/ghost'):
                            # Process /ghost command in any chat type
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /ghost (رمز الفريق)\nمثال: /ghost ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                CodE = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nجاري الانضمام الخفي إلى الفريق برمز: {CodE}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Get bot's UID from global context or login data
                                    bot_uid = LoGinDaTaUncRypTinG.AccountUID if hasattr(LoGinDaTaUncRypTinG, 'AccountUID') else TarGeT
                                    
                                    ghost_packet = await ghost_join_packet(bot_uid, CodE, key, iv)
                                    if ghost_packet:
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', ghost_packet)
                                        success_message = f"[B][C][00FF00]✅ نجاح! تم الانضمام الخفي إلى الفريق برمز: {CodE}!\n"
                                        await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                    else:
                                        error_msg = f"[B][C][FF0000]❌ خطأ! فشل إنشاء حزمة الانضمام الخفي.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ خطأ! فشل الانضمام الخفي: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # NEW LAG COMMAND
                        if inPuTMsG.strip().startswith('/lag '):
                            print('معالجة أمر التأخير في أي نوع دردشة')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /lag (رمز الفريق)\nمثال: /lag ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
                                
                                # Stop any existing lag task
                                if lag_task and not lag_task.done():
                                    lag_running = False
                                    lag_task.cancel()
                                    await asyncio.sleep(0.1)
                                
                                # Start new lag task
                                lag_running = True
                                lag_task = asyncio.create_task(lag_team_loop(team_code, key, iv, region))
                                
                                # SUCCESS MESSAGE
                                success_msg = f"[B][C][00FF00]✅ نجاح! بدأ هجوم التأخير!\nالفريق: {team_code}\nالإجراء: انضمام/مغادرة سريع\nالسرعة: فائقة السرعة (مللي ثانية)\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                        # STOP LAG COMMAND
                        if inPuTMsG.strip() == '/stop lag':
                            if lag_task and not lag_task.done():
                                lag_running = False
                                lag_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ نجاح! تم إيقاف هجوم التأخير بنجاح!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ خطأ! لا يوجد هجوم تأخير نشط لإيقافه!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.startswith('/exit'):
                            # Process /exit command in any chat type
                            initial_message = f"[B][C]{get_random_color()}\nجاري مغادرة الفريق الحالي...\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            leave = await ExiT(uid,key,iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , leave)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][00FF00]✅ نجاح! تم مغادرة الفريق بنجاح!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/start'):
                            # Process /start command in any chat type
                            initial_message = f"[B][C]{get_random_color()}\nجاري بدء المباراة...\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            EM = await FS(key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , EM)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][00FF00]✅ نجاح! تم إرسال أمر بدء المباراة!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.startswith('/title'):
                            await handle_all_titles_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                            

                        # Emote command - works in all chat types
                        if inPuTMsG.strip().startswith('/e'):
                            print(f'معالجة أمر الإيموجي في نوع دردشة: {response.Data.chat_type}')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /e (معرف) (معرف الإيموجي)\nمثال: /e 123456789 909000001\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                continue
                                
                            initial_message = f'[B][C]{get_random_color()}\nجاري إرسال الإيموجي إلى الهدف...\n'
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                            uid2 = uid3 = uid4 = uid5 = None
                            s = False
                            target_uids = []

                            try:
                                target_uid = int(parts[1])
                                target_uids.append(target_uid)
                                uid2 = int(parts[2]) if len(parts) > 2 else None
                                if uid2: target_uids.append(uid2)
                                uid3 = int(parts[3]) if len(parts) > 3 else None
                                if uid3: target_uids.append(uid3)
                                uid4 = int(parts[4]) if len(parts) > 4 else None
                                if uid4: target_uids.append(uid4)
                                uid5 = int(parts[5]) if len(parts) > 5 else None
                                if uid5: target_uids.append(uid5)
                                idT = int(parts[-1])  # Last part is emote ID

                            except ValueError as ve:
                                print("خطأ في القيمة:", ve)
                                s = True
                            except Exception as e:
                                print(f"خطأ في تحليل أمر الإيموجي: {e}")
                                s = True

                            if not s:
                                try:
                                    for target in target_uids:
                                        H = await Emote_k(target, idT, key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        await asyncio.sleep(0.1)
                                    
                                    # SUCCESS MESSAGE
                                    success_msg = f"[B][C][00FF00]✅ نجاح! تم إرسال الإيموجي {idT} إلى {len(target_uids)} لاعب!\nالأهداف: {', '.join(map(str, target_uids))}\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ خطأ في إرسال الإيموجي: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ خطأ! تنسيق معرف غير صالح. الاستخدام: /e (معرف) (معرف الإيموجي)\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                                                # /lvup command - Auto Start Bot
                        if inPuTMsG.strip().startswith('/lw'):
                            print('معالجة أمر التشغيل التلقائي /lvup')
                            global auto_start_running, auto_start_teamcode, stop_auto, auto_start_task
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /lvup (رمز الفريق)\nمثال: /lvup 123456\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
                                
                                # Check if numeric
                                if not team_code.isdigit():
                                    error_msg = f"[B][C][FF0000]❌ خطأ! رمز الفريق يجب أن يكون أرقام فقط!\nمثال: /lvup 123456\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
                                
                                # Check if already running
                                if auto_start_running:
                                    error_msg = f"[B][C][FF0000]❌ خطأ! التشغيل التلقائي قيد التشغيل بالفعل للفريق {auto_start_teamcode}!\nاستخدم /stop للإيقاف أولاً.\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
                                
                                # Start auto start
                                global auto_start_task, stop_auto
                                stop_auto = False
                                auto_start_running = True
                                auto_start_teamcode = team_code
                                
                                # Send initial message
                                initial_msg = f"""
[B][C][00FFFF]🤖 تم تفعيل بوت التشغيل التلقائي!

🎯 رمز الفريق: {team_code}
⚡ الإجراء: انضمام → بدء → انتظار → مغادرة → تكرار
⏰ مدة بدء السبام: {start_spam_duration} ثانية
⏳ وقت الانتظار: {wait_after_match} ثانية
🔄 حلقة: مستمرة 24x7

💡 للإيقاف: /stop
"""
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                                
                                # Start auto loop in background
                                auto_start_task = asyncio.create_task(
                                    auto_start_loop(team_code, uid, chat_id, response.Data.chat_type, key, iv, region)
                                )
                        

                        if inPuTMsG.strip().startswith('/stop'):
                            print('معالجة أمر إيقاف التشغيل التلقائي')
                            
                                # Start auto start
                            stop_auto = True
                            auto_start_running = False
                            auto_start_teamcode = None
                                
                                # Send initial message
                            initial_msg = f"""
[B][C][00FFFF]🤖 تم إيقاف بوت التشغيل التلقائي!

🎯 رمز الفريق: {team_code}
⚡ الإجراء: انضمام → بدء → انتظار → مغادرة → تكرار
⏰ مدة بدء السبام: {start_spam_duration} ثانية
⏳ وقت الانتظار: {wait_after_match} ثانية
🔄 حلقة: مستمرة 24x7

💡 للتشغيل: /lw [رمز الفريق]
"""
                            await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                                

                        # EVO CYCLE START COMMAND - /evos
                        if inPuTMsG.strip().startswith('/evos'):
                            print('معالجة أمر بدء دورة الإيموجي التطوري في أي نوع دردشة')
                            # Declare global variables

                            parts = inPuTMsG.strip().split()
                            uids = []
    
                            # Always use the sender's UID (the person who typed /evos)
                            sender_uid = str(response.Data.uid)
                            uids.append(sender_uid)
                            print(f"استخدام معرف المرسل: {sender_uid}")
    
                            # Optional: Also allow specifying additional UIDs
                            if len(parts) > 1:
                                for part in parts[1:]:  # Skip the first part which is "/evos"
                                    if part.isdigit() and len(part) >= 7 and part != sender_uid:  # UIDs are usually 7+ digits
                                        uids.append(part)
                                        print(f"تمت إضافة معرف إضافي: {part}")

                            # Stop any existing evo cycle
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                await asyncio.sleep(0.5)
    
                            # Start new evo cycle
                            evo_cycle_running = True
                            evo_cycle_task = asyncio.create_task(evo_cycle_spam(uids, key, iv, region))
    
                            # SUCCESS MESSAGE
                            if len(uids) == 1:
                                success_msg = f"[B][C][00FF00]✅ نجاح! بدأت دورة الإيموجي التطوري!\n🎯 الهدف: نفسك\n🎭 الإيموجيات: جميع الإيموجيات التطورية الـ18\n⏰ التأخير: 5 ثوانٍ بين الإيموجيات\n🔄 الدورة: حلقة مستمرة حتى /sevos\n"
                            else:
                                success_msg = f"[B][C][00FF00]✅ نجاح! بدأت دورة الإيموجي التطوري!\n🎯 الأهداف: نفسك + {len(uids)-1} لاعب آخر\n🎭 الإيموجيات: جميع الإيموجيات التطورية الـ18\n⏰ التأخير: 5 ثوانٍ بين الإيموجيات\n🔄 الدورة: حلقة مستمرة حتى /sevos\n"
    
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            print(f"بدأت دورة الإيموجي التطوري للمعرفات: {uids}")
                        
                        # EVO CYCLE STOP COMMAND - /sevos
                        if inPuTMsG.strip() == '/sevos':
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ نجاح! تم إيقاف دورة الإيموجي التطوري بنجاح!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                print("تم إيقاف دورة الإيموجي التطوري بواسطة الأمر")
                            else:
                                error_msg = f"[B][C][FF0000]❌ خطأ! لا توجد دورة إيموجي تطوري نشطة لإيقافها!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Fast emote spam command - works in all chat types
                        if inPuTMsG.strip().startswith('/fast'):
                            print('معالجة سبام الإيموجي السريع في أي نوع دردشة')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /fast معرف1 [معرف2] [معرف3] [معرف4] [1-414]\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and [1-414]
                                uids = []
                                emote_id = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) > 3:  # Assuming UIDs are longer than 3 digits
                                            uids.append(part)
                                        else:
                                            emote_id = ALL_EMOTE.get(int(part))
                                    else:
                                        break
                                
                                if not emote_id and parts[-1].isdigit():
                                    emote_id = parts[-1]
                                
                                if not uids or not emote_id:
                                    error_msg = f"[B][C][FF0000]❌ خطأ! تنسيق غير صالح! الاستخدام: /fast معرف1 [معرف2] [معرف3] [معرف4] [1-414]\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    # Stop any existing fast spam
                                    if fast_spam_task and not fast_spam_task.done():
                                        fast_spam_running = False
                                        fast_spam_task.cancel()
                                    
                                    # Start new fast spam
                                    fast_spam_running = True
                                    fast_spam_task = asyncio.create_task(fast_emote_spam(uids, emote_id, key, iv, region))
                                    
                                    # SUCCESS MESSAGE
                                    success_msg = f"[B][C][00FF00]✅ نجاح! بدأ سبام الإيموجي السريع!\nالأهداف: {len(uids)} لاعب\nالإيموجي: {emote_id}\nعدد السبام: 25 مرة\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                        # Custom emote spam command - works in all chat types
                        if inPuTMsG.strip().startswith('/p'):
                            print('معالجة سبام الإيموجي المخصص في أي نوع دردشة')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 4:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /p (معرف) [1-414] (مرات)\nمثال: /p 123456789 [1-414] 10\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                try:
                                    target_uid = parts[1]
                                    emote_id = ALL_EMOTE.get(int(parts[2]))
                                    times = int(parts[3])
                                    
                                    if times <= 0:
                                        error_msg = f"[B][C][FF0000]❌ خطأ! عدد المرات يجب أن يكون أكبر من 0!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    elif times > 100:
                                        error_msg = f"[B][C][FF0000]❌ خطأ! الحد الأقصى 100 مرة للأمان!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    else:
                                        # Stop any existing custom spam
                                        if custom_spam_task and not custom_spam_task.done():
                                            custom_spam_running = False
                                            custom_spam_task.cancel()
                                            await asyncio.sleep(0.5)
                                        
                                        # Start new custom spam
                                        custom_spam_running = True
                                        custom_spam_task = asyncio.create_task(custom_emote_spam(target_uid, emote_id, times, key, iv, region))
                                        
                                        # SUCCESS MESSAGE
                                        success_msg = f"[B][C][00FF00]✅ نجاح! بدأ سبام الإيموجي المخصص!\nالهدف: {target_uid}\nالإيموجي: {emote_id}\nالمرات: {times}\n"
                                        await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                        
                                except ValueError:
                                    error_msg = f"[B][C][FF0000]❌ خطأ! تنسيق رقم غير صالح! الاستخدام: /p (معرف) [1-414] (مرات)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ خطأ! {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Spam request command - works in all chat types
                        if inPuTMsG.strip().startswith('/spm_inv'):
                            print('معالجة سبام الدعوة مع التجميل')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ الاستخدام: /spm_inv (معرف)\nمثال: /spm_inv 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                # Stop any existing spam request
                                if spam_request_task and not spam_request_task.done():
                                    spam_request_running = False
                                    spam_request_task.cancel()
                                    await asyncio.sleep(0.5)
        
                                # Start new spam request WITH COSMETICS
                                spam_request_running = True
                                spam_request_task = asyncio.create_task(spam_request_loop_with_cosmetics(target_uid, key, iv, region))
        
                                # SUCCESS MESSAGE
                                success_msg = f"[B][C][00FF00]✅ بدأ السبام التجميلي!\n🎯 الهدف: {target_uid}\n📦 الطلبات: 30\n🎭 المميزات: شارات V + تجميل\n⚡ كل دعوة بتجميل مختلف!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                        # Stop spam request command - works in all chat types
                        if inPuTMsG.strip() == '/stop spm_inv':
                            if spam_request_task and not spam_request_task.done():
                                spam_request_running = False
                                spam_request_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ نجاح! تم إيقاف طلب السبام بنجاح!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ خطأ! لا يوجد طلب سبام نشط لإيقافه!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # NEW PLAY COMMANDS
                        if inPuTMsG.strip().startswith('/play '):
                            print('معالجة أمر play في أي نوع دردشة')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /play معرف1 [معرف2] [معرف3] [معرف4] رقم(1-414)\nمثال: /play 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 3:  # Number should be 1-414 (1,2 or 3 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ خطأ! تنسيق غير صالح! الاستخدام: /play معرف1 [معرف2] [معرف3] [معرف4] رقم(1-414)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in ALL_EMOTE:
                                            error_msg = f"[B][C][FF0000]❌ خطأ! الرقم يجب أن يكون بين 1-414 فقط!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            initial_message = f"[B][C]{get_random_color()}\nجاري إرسال الإيموجي {number_int}...\n"
                                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                            
                                            success, result_msg = await play_emote_spam(uids, number_int, key, iv, region)
                                            
                                            if success:
                                                success_msg = f"[B][C][00FF00]✅ نجاح! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            else:
                                                error_msg = f"[B][C][FF0000]❌ خطأ! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ خطأ! تنسيق رقم غير صالح! استخدم (1-414) فقط.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # NEW 100 LV EMOTE COMMANDS
                        if inPuTMsG.strip().startswith('/100 '):
                            print('معالجة أمر 100 في أي نوع دردشة')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /100 معرف1 [معرف2] [معرف3] [معرف4]\nمثال: /100 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 3:  # Number should be 1-414 (1,2 or 3 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ خطأ! تنسيق غير صالح! الاستخدام: /100 معرف1 [معرف2] [معرف3] [معرف4]\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = 268
                                        if number_int not in ALL_EMOTE:
                                            error_msg = f"[B][C][FF0000]❌ خطأ! الرقم يجب أن يكون بين 1-414 فقط!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            initial_message = f"[B][C]{get_random_color()}\nجاري إرسال إيموجي المستوى 100...\n"
                                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                            
                                            success, result_msg = await play_emote_spam(uids, number_int, key, iv, region)
                                            
                                            if success:
                                                success_msg = f"[B][C][00FF00]✅ نجاح! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            else:
                                                error_msg = f"[B][C][FF0000]❌ خطأ! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ خطأ! تنسيق رقم غير صالح! استخدم (1-414) فقط.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # NEW EVO COMMANDS
                        if inPuTMsG.strip().startswith('/evo '):
                            print('معالجة أمر evo في أي نوع دردشة')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /evo معرف1 [معرف2] [معرف3] [معرف4] رقم(1-21)\nمثال: /evo 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number should be 1-21 (1 or 2 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ خطأ! تنسيق غير صالح! الاستخدام: /evo معرف1 [معرف2] [معرف3] [معرف4] رقم(1-21)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ خطأ! الرقم يجب أن يكون بين 1-21 فقط!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            initial_message = f"[B][C]{get_random_color()}\nجاري إرسال الإيموجي التطوري {number_int}...\n"
                                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                            
                                            success, result_msg = await evo_emote_spam(uids, number_int, key, iv, region)
                                            
                                            if success:
                                                success_msg = f"[B][C][00FF00]✅ نجاح! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            else:
                                                error_msg = f"[B][C][FF0000]❌ خطأ! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ خطأ! تنسيق رقم غير صالح! استخدم 1-21 فقط.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/evo_fast '):
                            print('معالجة أمر evo_fast في أي نوع دردشة')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /evo_fast معرف1 [معرف2] [معرف3] [معرف4] رقم(1-21)\nمثال: /evo_fast 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number should be 1-21 (1 or 2 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ خطأ! تنسيق غير صالح! الاستخدام: /evo_fast معرف1 [معرف2] [معرف3] [معرف4] رقم(1-21)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ خطأ! الرقم يجب أن يكون بين 1-21 فقط!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            # Stop any existing evo_fast spam
                                            if evo_fast_spam_task and not evo_fast_spam_task.done():
                                                evo_fast_spam_running = False
                                                evo_fast_spam_task.cancel()
                                                await asyncio.sleep(0.5)
                                            
                                            # Start new evo_fast spam
                                            evo_fast_spam_running = True
                                            evo_fast_spam_task = asyncio.create_task(evo_fast_emote_spam(uids, number_int, key, iv, region))
                                            
                                            # SUCCESS MESSAGE
                                            emote_id = EMOTE_MAP[number_int]
                                            success_msg = f"[B][C][00FF00]✅ نجاح! بدأ السبام السريع للإيموجي التطوري!\nالأهداف: {len(uids)} لاعب\nالإيموجي: {number_int} (المعرف: {emote_id})\nعدد السبام: 25 مرة\nالفاصل: 0.1 ثانية\n"
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ خطأ! تنسيق رقم غير صالح! استخدم 1-21 فقط.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # NEW EVO_CUSTOM COMMAND
                        if inPuTMsG.strip().startswith('/evo_c '):
                            print('معالجة أمر evo_c في أي نوع دردشة')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ خطأ! الاستخدام: /evo_c معرف1 [معرف2] [معرف3] [معرف4] رقم(1-21) مرة(1-100)\nمثال: /evo_c 123456789 1 10\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids, number, and time
                                uids = []
                                number = None
                                time_val = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number or time should be 1-100 (1, 2, or 3 digits)
                                            if number is None:
                                                number = part
                                            elif time_val is None:
                                                time_val = part
                                            else:
                                                uids.append(part)
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                # If we still don't have time_val, try to get it from the last part
                                if not time_val and len(parts) >= 3:
                                    last_part = parts[-1]
                                    if last_part.isdigit() and len(last_part) <= 3:
                                        time_val = last_part
                                        # Remove time_val from uids if it was added by mistake
                                        if time_val in uids:
                                            uids.remove(time_val)
                                
                                if not uids or not number or not time_val:
                                    error_msg = f"[B][C][FF0000]❌ خطأ! تنسيق غير صالح! الاستخدام: /evo_c معرف1 [معرف2] [معرف3] [معرف4] رقم(1-21) مرة(1-100)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        time_int = int(time_val)
                                        
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ خطأ! الرقم يجب أن يكون بين 1-21 فقط!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        elif time_int < 1 or time_int > 100:
                                            error_msg = f"[B][C][FF0000]❌ خطأ! الوقت يجب أن يكون بين 1-100 فقط!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            # Stop any existing evo_custom spam
                                            if evo_custom_spam_task and not evo_custom_spam_task.done():
                                                evo_custom_spam_running = False
                                                evo_custom_spam_task.cancel()
                                                await asyncio.sleep(0.5)
                                            
                                            # Start new evo_custom spam
                                            evo_custom_spam_running = True
                                            evo_custom_spam_task = asyncio.create_task(evo_custom_emote_spam(uids, number_int, time_int, key, iv, region))
                                            
                                            # SUCCESS MESSAGE
                                            emote_id = EMOTE_MAP[number_int]
                                            success_msg = f"[B][C][00FF00]✅ نجاح! بدأ السبام المخصص للإيموجي التطوري!\nالأهداف: {len(uids)} لاعب\nالإيموجي: {number_int} (المعرف: {emote_id})\nالتكرار: {time_int} مرة\nالفاصل: 0.1 ثانية\n"
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ خطأ! تنسيق رقم/وقت غير صالح! استخدم أرقام فقط.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Stop evo_fast spam command
                        if inPuTMsG.strip() == '/stop evo_fast':
                            if evo_fast_spam_task and not evo_fast_spam_task.done():
                                evo_fast_spam_running = False
                                evo_fast_spam_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ نجاح! تم إيقاف السبام السريع التطوري بنجاح!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ خطأ! لا يوجد سبام سريع تطوري نشط لإيقافه!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Stop evo_custom spam command
                        if inPuTMsG.strip() == '/stop evo_c':
                            if evo_custom_spam_task and not evo_custom_spam_task.done():
                                evo_custom_spam_running = False
                                evo_custom_spam_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ نجاح! تم إيقاف السبام المخصص التطوري بنجاح!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ خطأ! لا يوجد سبام مخصص تطوري نشط لإيقافه!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        # status message 
                        if inPuTMsG.strip() == '/status':
                            footer ="""[00FFFA]╔═•══•════════════════•══•═╗
[FF1493]║ ⚡ [B][FFFF00]معلومات البوت[FFFF00][/B] ⚡
[00FFFA]║
[FFFF00]║ 👤 المطور    :: [FF1493]ZAKARIA
[32CD32]║ 💻 الحالة     :: [32CD32]متصل
[1E90FF]║ 🛠 الإصدار    :: [1E90FF]محسّن V2
[00FFFA]╚═•══•════════════════•══•═╝"""

    


                            await safe_send_message(response.Data.chat_type, footer, uid, chat_id, key, iv)

# IMPROVED TREE-STYLE HELP MENU SYSTEM (Commands in their original menus) 🌳
                        if inPuTMsG.strip().lower() in ("help", "/help", "menu", "/menu", "commands"):
                            print(f"أمر المساعدة تم اكتشافه من المعرف: {uid} في نوع دردشة: {response.Data.chat_type}")

                            # Header
                            header = f"[b][c]{get_random_color()}مرحباً بك في بوت ZAKARIA"
                            await safe_send_message(response.Data.chat_type, header, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            # ───── أوامر المجموعة ─────
                            group_commands = """[C][B][FFD700]═══⚡ أوامر المجموعة ⚡═══[00FF00][B]
├─ [00FF00]إرسال إعجابات ✅️✅️
│  └─ [00AAFF]/like [معرف]
├─ [00FF00]إنشاء مجموعة 3 لاعبين
│  └─ [00AAFF]/3
├─ [00FF00]إنشاء مجموعة 5 لاعبين
│  └─ [00AAFF]/5
├─ [00FF00]إنشاء مجموعة 6 لاعبين
│  └─ [00AAFF]/6
├─ [00FF00]دعوة لاعب للفريق
│  └─ [00AAFF]/inv [معرف]
├─ [00FF00]انضمام البوت للفريق
│  └─ [00AAFF]/join [رمز_الفريق]
└─ [00FF00]مغادرة البوت للفريق
   └─ [00AAFF]/exit
[00FF00]━━━━━━━━━━━━[00AAFF]"""
                            await safe_send_message(response.Data.chat_type, group_commands, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            # ───── الأوامر المتقدمة ─────
                            advanced_commands = """[C][B][800080]═══⚡ أوامر متقدمة ⚡═══[00FF00][B]
├─ [00FF00]تشغيل بوت رفع المستوى
│  └─ [00AAFF]/lw [رمز الفريق]
├─ [00FF00]إيقاف بوت رفع المستوى
│  └─ [00AAFF]/stop
├─ [00FF00]تجهيز حزمة نادرة
│  └─ [00AAFF]/bundle [الرمز]
├─ [00FF00]هجوم تأخير على الفريق
│  └─ [00AAFF]/lag [الرمز]
├─ [00FF00]إيقاف هجوم التأخير
│  └─ [00AAFF]/stop lag
└─ [00FF00]سبام الرفض
   └─ [00AAFF]/reject [معرف]
[00FF00]━━━━━━━━━━━━[00AAFF]"""
                            await safe_send_message(response.Data.chat_type, advanced_commands, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            # ───── أوامر الإيموجي ─────
                            emote_commands = """[C][B][32CD32]═══⚡ أوامر الإيموجي ⚡═══[7CFC00][B]
├─ [7CFC00]إرسال إيموجي واحد
│  └─ [32CD32]/play [معرف] [1-414]
├─ [7CFC00]إيموجي سريع (25 مرة)
│  └─ [32CD32]/fast [معرف] [1-414]
├─ [7CFC00]إيموجي مخصص (عدد مرات)
│  └─ [32CD32]/p [معرف] [1-414] [عدد]
├─ [7CFC00]إيموجي المستوى 100
│  └─ [32CD32]/play [معرف] 263
├─ [7CFC00]قائمة الإيموجيات
│  └─ [32CD32]/emote
└─ [7CFC00]إيموجي مخصص (باستخدام المعرف)
   └─ [32CD32]/e [معرف] [رقم]
[7CFC00]━━━━━━━━━━━━[32CD32]"""
                            await safe_send_message(response.Data.chat_type, emote_commands, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            # ───── أوامر الإيموجي التطوري ─────
                            evo_commands = """[C][B][00AAFF]═══⚡ الإيموجيات التطورية ⚡═══[00FF00][B]
├─ [00FF00]إرسال إيموجي تطوري
│  └─ [00AAFF]/evo [معرف] [1-21]
├─ [00FF00]إيموجي تطوري سريع (25 مرة)
│  └─ [00AAFF]/evo_fast [معرف] [1-21]
├─ [00FF00]إيموجي تطوري مخصص (عدد مرات)
│  └─ [00AAFF]/evo_c [معرف] [1-21] [عدد]
├─ [00FF00]دورة تلقائية لجميع الإيموجيات التطورية
│  └─ [00AAFF]/evos [معرف]
└─ [00FF00]إيقاف دورة الإيموجي التطوري
   └─ [00AAFF]/sevos
[00FF00]━━━━━━━━━━━━[00AAFF]"""
                            await safe_send_message(response.Data.chat_type, evo_commands, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            # ───── أوامر الذكاء الاصطناعي والأدوات ─────
                            ai_commands = """[C][B][00AAFF]═══⚡ أدوات وأوامر مسلية ⚡═══[00FF00][B]
├─ [00FF00]الحصول على سيرة اللاعب
│  └─ [00AAFF]/bio [معرف]
├─ [00FF00]جلب معلومات مستخدم Instagram
│  └─ [00AAFF]/ig [اسم_المستخدم]
├─ [00FF00]إرسال رسالة سبام مخصصة
│  └─ [00AAFF]/ms <نص>
├─ [00FF00]سؤال الذكاء الاصطناعي
│  └─ [00AAFF]/ai [سؤال]
├─ [00FF00]معلومات المطور
│  └─ [00AAFF]/admin
└─ [00FF00]فحص حالة البوت
   └─ [00AAFF]/status
[00FF00]━━━━━━━━━━━━[00AAFF]"""
                            await safe_send_message(response.Data.chat_type, ai_commands, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            # ───── أوامر الشارات ─────
                            badge_commands = """[C][B][00AAFF]═══⚡ طلبات انضمام بالشارات ⚡═══[00FF00][B]
├─ [00FF00]طلب انضمام بشارة Craftland
│  └─ [00AAFF]/s1 [معرف]
├─ [00FF00]طلب انضمام بشارة V-جديدة
│  └─ [00AAFF]/s2 [معرف]
├─ [00FF00]طلب انضمام بشارة مشرف
│  └─ [00AAFF]/s3 [معرف]
├─ [00FF00]طلب انضمام بشارة V-صغيرة
│  └─ [00AAFF]/s4 [معرف]
├─ [00FF00]طلب انضمام بشارة محترف
│  └─ [00AAFF]/s5 [معرف]
└─ [00FF00]طلبات انضمام بجميع الشارات
   └─ [00AAFF]/spam [معرف]
[00FF00]━━━━━━━━━━━━[00AAFF]"""
                            await safe_send_message(response.Data.chat_type, badge_commands, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)
                            
                                                        # ───── أوامر المعلومات ─────
                            info_commands = """[C][B][00AAFF]═══⚡ أوامر المعلومات ⚡═══[00FF00][B]
├─ [00FF00]معلومات اللاعب الأساسية
│  └─ [00AAFF]/info [معرف]
├─ [00FF00]فحص حالة حظر الحساب
│  └─ [00AAFF]/check [معرف]
├─ [00FF00]إضافة البوت لقائمة الأصدقاء
│  └─ [00AAFF]/add [معرف]
├─ [00FF00]إزالة من قائمة الأصدقاء
│  └─ [00AAFF]/remove [معرف]
├─ [00FF00]سبام طلبات الصداقة 
│  └─ [00AAFF]/spam_req [معرف]
└─ [00FF00]شتيمة أي صديق
   └─ [00AAFF]/gali [اسم]
[00FF00]━━━━━━━━━━━━[00AAFF]"""
                            await safe_send_message(response.Data.chat_type, info_commands, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            
                            footer ="""[00FFFA]╔═•══•════════════════•══•═╗
[FF1493]║ ⚡ [B][FFFF00]معلومات البوت[FFFF00][/B] ⚡
[00FFFA]║
[FFFF00]║ 👤 المطور    :: [FF1493] ZAKARIA 
[32CD32]║ 💻 الحالة     :: [32CD32]متصل
[1E90FF]║ 🛠 الإصدار    :: [1E90FF]محسّن V2
[00FFFA]╚═•══•════════════════•══•═╝"""

    


                            await safe_send_message(response.Data.chat_type, footer, uid, chat_id, key, iv)
                        response = None
                            
                        try:
                            if whisper_writer:
                                whisper_writer.close()
                                await whisper_writer.wait_closed()
                        except:
                            pass
                        finally:
                            whisper_writer = None
                                
                    	
                    	
        except Exception as e: print(f"خطأ {ip}:{port} - {e}") ; whisper_writer = None
        await asyncio.sleep(reconnect_delay)





async def MaiiiinE():
    Uid , Pw = '4378068850','8C583277F6A0221993BAC8FBBD712BC25B171A445A34FB1DD0966609CB74729D'
    

    open_id , access_token = await GeNeRaTeAccEss(Uid , Pw)
    if not open_id or not access_token: print("خطأ - حساب غير صالح") ; return None
    
    PyL = await EncRypTMajoRLoGin(open_id , access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL)
    if not MajoRLoGinResPonsE: print("الحساب المستهدف => محظور / غير مسجل! ") ; return None
    
    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
    UrL = MajoRLoGinauTh.url
    # In the MaiiiinE function, find and comment out these print statements:
    os.system('clear')
    print("🔄 بدء اتصالات TCP...")
    print("📡 الاتصال بخوادم Free Fire...")
    print("🌐 تم إنشاء اتصال بالخادم")

    region = MajoRLoGinauTh.region

    ToKen = MajoRLoGinauTh.token
    print("🔐 تم المصادقة بنجاح")
    TarGeT = MajoRLoGinauTh.account_uid
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp
    
    LoGinDaTa = await GetLoginData(UrL , PyL , ToKen)
    if not LoGinDaTa: print("خطأ في الحصول على المنافذ من بيانات الدخول!") ; return None
    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)
    OnLinePorTs = LoGinDaTaUncRypTinG.Online_IP_Port
    ChaTPorTs = LoGinDaTaUncRypTinG.AccountIP_Port
    OnLineiP , OnLineporT = OnLinePorTs.split(":")
    ChaTiP , ChaTporT = ChaTPorTs.split(":")
    acc_name = LoGinDaTaUncRypTinG.AccountName
    #print(acc_name)
    
    equie_emote(ToKen,UrL)
    AutHToKen = await xAuThSTarTuP(int(TarGeT) , ToKen , int(timestamp) , key , iv)
    ready_event = asyncio.Event()
    
    # Start Telegram bot as a background task
    telegram_task = asyncio.create_task(telegram_startup())
    
    task1 = asyncio.create_task(TcPChaT(ChaTiP, ChaTporT , AutHToKen , key , iv , LoGinDaTaUncRypTinG , ready_event ,region))
    task2 = asyncio.create_task(TcPOnLine(OnLineiP , OnLineporT , key , iv , AutHToKen))  

    os.system('clear')
    print("جاري تهيئة بوت ZAKARIA...")
    print("┌────────────────────────────────────┐")
    print("│ █████████████░░░░░░░░░░░░░░░░░░ │")
    print("└────────────────────────────────────┘")
    time.sleep(0.5)
    os.system('clear')
    print("الاتصال بخوادم Free Fire...")
    print("┌────────────────────────────────────┐")
    print("│ ██████████████████████░░░░░░░░░░░░ │")
    print("└────────────────────────────────────┘")
    time.sleep(0.5)
    os.system('clear')

    print("🤖 بوت ZAKARIA - متصل")
    print("┌────────────────────────────────────┐")
    print("│ ██████████████████████████████████ │")
    print("└────────────────────────────────────┘")
    print(f"🔹 المعرف: {TarGeT}")
    print(f"🔹 الاسم: {acc_name}")
    print(f"🔹 الحالة: 🟢 جاهز")
    print("")
    print("💡 اكتب /help للأوامر")
    print(f"🤖 بوت التلغرام: @{BOT_TOKEN.split(':')[0]} (تأكد من ضبط التوكن)")
    
    # Wait for all tasks to complete (they run indefinitely)
    await asyncio.gather(task1, task2, telegram_task)
    time.sleep(0.5)
    os.system('clear')
    await ready_event.wait()
    await asyncio.sleep(1)

    os.system('clear')
    print(render('FLASH FFs', colors=['white', 'green'], align='center'))
    print('')
    print("🤖 بوت ZAKARIA - متصل")
    print(f"🔹 المعرف: {TarGeT}")
    print(f"🔹 الاسم: {acc_name}")
    print(f"🔹 الحالة: 🟢 جاهز")
    


def handle_keyboard_interrupt(signum, frame):
    """Clean handling for Ctrl+C"""
    print("\n\n🛑 طلب إيقاف البوت...")
    print("👋 شكراً لاستخدام ZIKO")
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, handle_keyboard_interrupt)
    
async def StarTinG():
    while True:
        try:
            await asyncio.wait_for(MaiiiinE() , timeout = 7 * 60 * 60)
        except KeyboardInterrupt:
            print("\n\n🛑 تم إيقاف البوت بواسطة المستخدم")
            print("👋 شكراً لاستخدام ZIKO!")
            break
        except asyncio.TimeoutError: print("انتهت صلاحية الرمز! إعادة التشغيل")
        except Exception as e: print(f"خطأ في TCP - {e} => إعادة التشغيل ...")

if __name__ == '__main__':
    threading.Thread(target=start_insta_api, daemon=True).start()
    asyncio.run(StarTinG())
