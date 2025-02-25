import os
import time
from datetime import datetime
import keyboard
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

previous_ip = ""

def print_current_ip():
    """Prints the current IP with a timestamp in green."""
    ping_command = "curl -s ip.me"
    current_ip = os.popen(ping_command).read().strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(Fore.GREEN + f"[{timestamp}] Current IP: {current_ip}")

# Register the hotkey to immediately print IP when 'p' is pressed
keyboard.add_hotkey("p", print_current_ip)

# Get initial IP and print it
ping_command = "curl -s ip.me"
previous_ip = os.popen(ping_command).read().strip()
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(Fore.CYAN + f"[{timestamp}] Initial IP: {previous_ip}")

while True:
    ping_command = "curl -s ip.me"
    current_ip = os.popen(ping_command).read().strip()
    
    if current_ip and current_ip != previous_ip:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(Fore.RED + f"[{timestamp}] IP changed to: {current_ip}")
        previous_ip = current_ip
    
    time.sleep(1)
