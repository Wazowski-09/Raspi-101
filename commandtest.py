import time
import commands

print(commands.getoutput('hostname -I'))

time.sleep(10.0)  # Wait 5 seconds
