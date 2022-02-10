from modules import BannerModule, Make_MalwareModule, MenuModule, Access_victimModule, UpdatesModule
from colorama import Fore
import time

BannerModule.banner()
MenuModule.ReturnMenu()
print()
try:

    options = input(Fore.RED + " ┌─[{}]\n {} ".format(Fore.BLUE + "CHOOSE@OPTION", Fore.GREEN + "└──╼ #"))

except KeyboardInterrupt:
    MenuModule.quit_script()

if options == "1":
    MenuModule.Malware()
    print("")
    MenuModule.back_to_menu()

elif options == "2":
    MenuModule.access_shell()

elif options == "3":
    MenuModule.clear_malwares()
    print("")
    MenuModule.back_to_menu()

elif options == "4":
    MenuModule.developer_info()
    MenuModule.back_to_menu()

elif options == "5":
    MenuModule.updater()
    MenuModule.back_to_menu()

elif options == "6":
    MenuModule.quit_script()

elif options == "":
    MenuModule.quit_script()

else:
    BannerModule.banner()
    print(Fore.GREEN + " [-] " + Fore.RED + "Not A valid Option!")
    print()
    MenuModule.back_to_menu()