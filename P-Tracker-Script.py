import os
import time
from datetime import datetime
import keyboard

log_file = "ip_log.txt"
previous_ip = ""

def print_current_ip():
    ping_command = "curl -s ip.me"
    current_ip = os.popen(ping_command).read().strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Current IP: {current_ip}")

# Register the hotkey to immediately print IP when 'p' is pressed
keyboard.add_hotkey("p", print_current_ip)

# Get initial IP
ping_command = "curl -s ip.me"
previous_ip = os.popen(ping_command).read().strip()
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"[{timestamp}] Current IP: {previous_ip}")

while True:
    ping_command = "curl -s ip.me"
    current_ip = os.popen(ping_command).read().strip()
    
    if current_ip and current_ip != previous_ip:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] IP changed to: {current_ip}\n"
        print(log_entry, end="")
        
        with open(log_file, "a") as file:
            file.write(log_entry)
        
        previous_ip = current_ip
    
    time.sleep(1)
