import os
import time

while True:
    ping_command = "curl -s ip.me"
    ping_output = os.popen(ping_command).read().strip()
    print(ping_output)
    time.sleep(1)
