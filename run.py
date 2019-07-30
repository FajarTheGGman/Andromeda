# Copyright© 2019 By Fajar Firdaus 
# Please Don't Recode My Program because i take a long time to complete this project

import tkinter as gui
import urllib3 as url
import os.path
import time

class Request:

    def linux():
        user = str(input("[?] Input Website : "))

        run = url.PoolManager()
        req = run.request("GET", user)

        interface = gui.Tk()
        
        spasi = gui.Label(interface, text=" ")
        title = gui.Label(interface, text="[=====[Result]=====]")
        status = gui.Label(interface, text="[Status] > " + str(req.status))
        data = gui.Label(interface, text=str(req.data))
        headers = gui.Label(interface, text=str(req.headers))
        
        data_title = gui.Label(interface, text="[=====[Content]=====]")
        headers_title = gui.Label(interface, text="[=====[Headers]=====]")

        # View

        title.pack()
        spasi.pack()
        status.pack()
        spasi.pack()
        data_title.pack()
        spasi.pack()
        data.pack()
        spasi.pack()
        headers_title.pack()
        spasi.pack()
        headers.pack()

        interface.mainloop()

    def Android():

        user = str(input("[?] Input Website : "))

        run = url.PoolManager()
        req = run.request("GET", user)

        print("[Status] : ", req.status, "\n")
        print("[Content] : ", req.data, "\n")
        print("[Headers] : ", req.headers, "\n")


class AdminFinder:
    def main():
       if os.path.isfile("wordlist.txt") == True:
           f = open("wordlist.txt", "r")

           connect = url.PoolManager()

           user_input = str(input("[+] Input Website >_ "))

           for list in f.readlines():
               req = connect.request("GET", user_input + "/" + list)
               if req.status == 200:
                   print("[+] Found " + user_input + "/" + list)
                   break
               else:
                   print("[!] Not Found " + user_input + "/" + list )
               
        
       else:
            print("[!] Wordlist Not Found")
            time.sleep(3)
            open("wordlist.txt", "w+")
            print("[>] Downloading Wordlist")

            r = url.PoolManager()
            requestData = r.request("GET", "https://pastebin.com/raw/HtriRnQ1")

            file = open("wordlist.txt", "w")
            file.write(str(requestData.data))
            file.close()
            print("[+] Wordlist Downloaded")
            time.sleep(1)
            print("[!] Please Run Again the program")

class Revdns:
    def main():
        print("[!] Dont Use 'www' and 'http://'\n")
        user = str(input("[?] Input Website : "))

        run = url.PoolManager()
        req = run.request("GET", "https://api.hackertarget.com/reversedns/?q=" + user)

        print("[======[Result]======]\n")
        print(req.data)

class TrackIP:
    def main():
        user = str(input("[?] Input IP : "))

        run = url.PoolManager()
        req = run.request("GET", "https://ip-api.com/json/" + user)

        print("[======[Result]======]\n")
        print(req.data)

class Menu():

    def main():
        
        def help():
            print("[--------------------]")
            print("[-] request --windows [Http Request For Linux]")
            print("[-] request --android [Http Request For Android]")
            print("[-] adminfinder [Admin Finder]")
            print("[-] reversedns [Reverse Link]")
            print("[-] trackip [Tracking IP]")
            print("[-] help [See all commands]")
            print("[--------------------]\n")

        print("   _                     ")
        print("  |(|         _          ")
        print("  |=|        / \         ")
        print(" /   \      /   \        ")
        print(" |.--|     /     \       ")
        print(" ||  |    /_______\      ")
        print(" ||  |   /         \     ")
        print(" |'--|  /           \ Ndromeda  ")
        print(" '-=-'                   \n")

        print("[------------------------]")
        print("Coder : Fajar Firdaus")
        print("FB : Fajar Firdaus")
        print("IG : fajar_firdaus_7")
        print("YT : iTech7732")
        print("[------------------------]\n")
        print("[!] Report Error to my social media :)\n")

        user = str(input("[/A\] >_ "))

        if user == "request --linux":
            run = Request.linux()
        elif user == "request --android":
            run = Request.Android()
        elif user == "adminfinder":
            run = AdminFinder.main()
        elif user == "reversedns":
            run = Revdns.main()
        elif user == "trackip":
            run = TrackIP.main()
        elif user == "help":
            help()
        else:
            print("\n[!] Wrong Command")
            help()

run = Menu.main()

# user_input = str("[]")