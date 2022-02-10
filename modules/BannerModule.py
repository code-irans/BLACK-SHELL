import subprocess, os, colorama


def banner(): # func print banner

    os.system("cls")

    print(colorama.Fore.RESET)

    

    bann = subprocess.getoutput("neofetch -c red -ac green")

    print(bann)

