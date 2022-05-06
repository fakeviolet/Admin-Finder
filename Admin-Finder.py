import os
from sys import platform
from requests import post

try:
    import colorama
    import pyfiglet
except:
    os.system("pip install colorama && pip install pyfiglet")
from colorama import Fore
import pyfiglet

def clear():
    
    if platform == 'win32':
    
        os.system("cls && title Admin-Finder by Fakeviolet")
    
    if platform == 'linux' or platform == 'linux2':
    
        os.system("clear")

clear()

print(Fore.CYAN)

print(f"""

 █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
███████║██║  ██║██╔████╔██║██║██╔██╗ ██║    █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║    ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                         """)

try:
    
    website = input(f"{Fore.RED}[+] {Fore.WHITE}Enter your target: ")
    if not website.startswith("http://") or not website.startswith("https://"):
        website  = "http://" + website

    # url file (You can change it)
    urlfile = open("login.txt")
    print("")

    # find admin page
    for url in urlfile:
        url = url.strip("\n")
        full_address = website + "/" + url
        response = post(full_address)
        if response.status_code == 200:
            print(Fore.GREEN + " [200] {} ==> Found".format(full_address))
        else:
            print(Fore.RED + " [404] {} ==> Not Found".format(full_address))

except:
    
    print(f"{Fore.RED} [!] Error: Check Internet Connection or Domain")


print(Fore.RESET)
