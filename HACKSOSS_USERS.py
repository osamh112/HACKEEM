# Copyright: Warrior
# Follow us on telegram ( @VnVn6 )
import requests, uuid, sys, os
from random import *
import colorama
from colorama import *
import time, string
from user_agent import generate_user_agent
import random, pyfiglet, os
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')
else:
    try:
        import time
    except:
        os.system('pip install time')
    else:
        os.system('clear')
        try:
            import pyfiglet
        except:
            os.system('pip install pyfiglet')
        else:
            os.system('clear')
            import pyfiglet, os
            from time import sleep
            import webbrowser
            Z = '\x1b[2;31m'
            G = '\x1b[1;32m'
            A = '\x1b[2;39m'
            C = '\x1b[2;35m'
            B = '\x1b[2;36m'
            C = '\x1b[2;35m'
            sleep(0.1)
            os.system('clear')
            import random, uuid, requests, string
            from user_agent import generate_user_agent
            from datetime import datetime
            from random import *
            from time import sleep
            import requests, os, random, json, threading, secrets, uuid
            from colorama import Fore, Style
            from time import sleep
            from datetime import datetime
            from secrets import token_hex
            from uuid import uuid4
            from user_agent import generate_user_agent
            from uuid import uuid4
        Z = '\x1b[1;31m'
        X = '\x1b[1;33m'
        Z1 = '\x1b[2;31m'
        F = '\x1b[2;32m'
        A = '\x1b[2;34m'
        C = '\x1b[2;35m'
        B = '\x1b[2;36m'
        Y = '\x1b[1;34m'

        P55 = pyfiglet.figlet_format("HACKSOSS \n OSAMH ' ")

        def O(z):
            for e in z:
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.0075)


        O(F + P55)
        print(" \n========================================================\n                              1- Pro' USER (4 letter)\n                              2- Pro' USER (5 letter)\n========================================≈===============\n                              \n\n                                    ")
        kai = input('        to choose ==> ')
      
        print('\n')
        print(C + '========================================')
        print('\n')
        kai = int(kai)
        ID = input(C + ' -Enter your   ID : ')
      
        print('\n')
        token = input(X + '  -Enter the Token : ')
        print('\n')
        print(C + '========================================')
        print('\n\n')
        e = '_'
        ktyp = '1234567890qwertyuiopasdfghjklzxcvbnm'
        ku = '{"account_created": false, "errors": {"email": [{"message": "Too many accounts are using a@gmail.com.", "code": "email_sharing_limit"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}'
        if kai == 1:
            Number = 0
            while True:
                uses = str(''.join((random.choice(ktyp) for i in range(4))))
                ks = str(''.join((random.choice(e + uses) for i in range(4))))
                url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
                headers_kai = {'accept':'*/*', 
                 'accept-encoding':'gzip, deflate, br', 
                 'accept-language':'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7', 
                 'content-length':'61', 
                 'content-type':'application/x-www-form-urlencoded', 
                 'cookie':'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI', 
                 'origin':'https://www.instagram.com', 
                 'referer':'https://www.instagram.com/accounts/emailsignup/', 
                 'sec-ch-ua':'"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"', 
                 'sec-ch-ua-mobile':'?0', 
                 'sec-fetch-dest':'empty', 
                 'sec-fetch-mode':'cors', 
                 'sec-fetch-site':'same-origin', 
                 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', 
                 'x-csrftoken':'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI', 
                 'x-ig-app-id':'936619743392459', 
                 'x-ig-www-claim':'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M', 
                 'x-instagram-ajax':'72bda6b1d047', 
                 'x-requested-with':'XMLHttpRequest'}
                datas_kai = {'email':'a@gmail.com', 
                 'username':f"{ks}", 
                 'first_name':'AA', 
                 'opt_into_one_tap':'false'}
                kd = requests.post(url, headers=headers_kai, data=datas_kai).text
                if ku in kd:
                    Number += 1
                    print(C + '[' + F + (f"{Number}") + C + ']' + F + ' Hit ' + F + f" [{ks}]")
                    with open('user.txt', 'a') as (x):
                        x.write(ks + '\n')
                        tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= Hi Pro Fishing From Alosh\n- - - - - - - - - - - - - - - - - - - - - - - - - -\n[=] user =>   ( {ks} )  ✓\n- - - - - - - - - - - - - - - - - - - - - - - - - -\n By :- @BBBBBLL -: @HORO4 "
                else:
                    Number += 1
                    print(C + '[' + F + (f"{Number}") + X + '] No ⭕️ ' + Z + f"- (( {ks} ))")

        if kai == 2:
            Number = 0
            while True:
                uses = str(''.join((random.choice(ktyp) for i in range(5))))
                ks = str(''.join((random.choice(e + uses) for i in range(5))))
                url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
                headers_kai = {'accept':'*/*', 
                 'accept-encoding':'gzip, deflate, br', 
                 'accept-language':'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7', 
                 'content-length':'61', 
                 'content-type':'application/x-www-form-urlencoded', 
                 'cookie':'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI', 
                 'origin':'https://www.instagram.com', 
                 'referer':'https://www.instagram.com/accounts/emailsignup/', 
                 'sec-ch-ua':'"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"', 
                 'sec-ch-ua-mobile':'?0', 
                 'sec-fetch-dest':'empty', 
                 'sec-fetch-mode':'cors', 
                 'sec-fetch-site':'same-origin', 
                 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', 
                 'x-csrftoken':'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI', 
                 'x-ig-app-id':'936619743392459', 
                 'x-ig-www-claim':'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M', 
                 'x-instagram-ajax':'72bda6b1d047', 
                 'x-requested-with':'XMLHttpRequest'}
                datas_kai = {'email':'a@gmail.com', 
                 'username':f"{ks}", 
                 'first_name':'AA', 
                 'opt_into_one_tap':'false'}
                kd = requests.post(url, headers=headers_kai, data=datas_kai).text
                if ku in kd:
                    Number += 1
                    print(C + '[' + F + (f"{Number}") + C + ']' + F + ' Hit ' + F + f" [{ks}]")
                    with open('user.txt', 'a') as (x):
                        x.write(ks + '\n')
                        tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=  \nHi Pro Fishing From Alosh\n- - - - - - - - - - - - - - - - - - - - - - - - - -\n[=] user =>   ( {ks} )  ✓\n- - - - - - - - - - - - - - - - - - - - - - - - - -\n By :- @BBBBBLL -: @HORO4 "
                        req = requests.post(tlg)
                else:
                    Number += 1
                    print(C + '[' + F + (f"{Number}") + X + '] No ⭕️ ' + Z + f"- (( {ks} ))")
