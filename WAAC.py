import termcolor
import colorama
colorama.init()
from termcolor import colored

print("\n")
print(colored(r"""
█░█░█ █░█ ▄▀█ ▀█▀ █▀ ▄▀█ █▀█ █▀█   ▄▀█ █░█ ▄▀█ █ █░░ ▄▀█ █▄▄ █ █░░ █ ▀█▀ █▄█   █▀▀ █▄▀ █▀▀ █▀▀ █▄▀ █▀▀ █▀█
▀▄▀▄▀ █▀█ █▀█ ░█░ ▄█ █▀█ █▀▀ █▀▀   █▀█ ▀▄▀ █▀█ █ █▄▄ █▀█ █▄█ █ █▄▄ █ ░█░ ░█░   █▄▄ █░█ ██▄ █▄▄ █░█ ██▄ █▀▄""", 'light_magenta'))
print("\n")
print(colored("V3.0".center(100,"-"), 'yellow'))
print("\n")
print(colored("© PASINDU THARUSHA - All Rights Reserved. \nThis project is based on open source dependencies built by open source communities.\nThe software is licensed under GPL V3 Licence. \nE-mail : pasindutharushahewage@outlook.com", 'light_magenta'))
print("\n")

from rich.progress import track
from rich.console import Console
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import pandas

colorama_init()
excel_data = pandas.read_excel('Recipients data.xlsx', sheet_name='Recipients')

count = 0

options = Options()
service = Service()
options.add_argument(r"--user-data-dir=C:\\Users\\5523\\AppData\\Local\\Google\\Chrome\\User Data\\")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://web.whatsapp.com")

input(colored("Press ENTER after login into Whatsapp Web and your chats are visiable.", 'yellow'))
for column in track(excel_data['Contact'].tolist(), description="Sending Messages..."):
    try:
        url = 'https://web.whatsapp.com/send?phone=' + str(excel_data['Contact'][count])
        sent = False
        # It tries 3 times to send a message in case if there any error occurred
        driver.get(url)
        try:
            click_btn = WebDriverWait(driver, 35).until(
                EC.presence_of_element_located((By.CLASS_NAME, '_3XKXx')))
        except Exception as e:
            print(f"{Fore.RED}NOPE: {Style.RESET_ALL}" + str(excel_data['Contact'][count]))
            log_file = open('log.txt', 'a')
            log_file.write("NOPE: " + str(excel_data['Contact'][count]) + '\n')
        else:
            sleep(2)
            sent = True
            sleep(5)
            print(f"{Fore.GREEN}HAVE: {Style.RESET_ALL}" + str(excel_data['Contact'][count]))
            log_file = open('log.txt', 'a')
            log_file.write('HAVE: ' + str(excel_data['Contact'][count]) + '\n')
        count = count + 1
    except Exception as e:
        print(f"{Fore.RED}NOPE: {Style.RESET_ALL}" + str(excel_data['Contact'][count]) + str(e))
        log_file = open('log.txt', 'a')
        log_file.write("NOPE: " + str(excel_data['Contact'][count]) + str(e) + '\n')
driver.quit()
print("The script executed successfully.")
