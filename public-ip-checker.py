import os
import time

while True:
    # Construct the ping command with the silent flag
    ping_command = "curl -s ip.me"
    
    # Execute the ping command and read the output
    ping_output = os.popen(ping_command).read().strip()
    
    # Print the output (the IP address)
    print(ping_output)
    
    # Wait for a specified amount of time
    time.sleep(1)