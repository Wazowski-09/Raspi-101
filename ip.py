import socket
import commands

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#connect to any target website
s.connect(('google.com', 0))
ipAddress = s.getsockname()[0]
s.close()

print("IP Address from socket:")
print(ipAddress)
print("")

print("ifconfig output:")
print(commands.getoutput("ifconfig"))
print("inet addr from ifconfig output:")
print(commands.getoutput("ifconfig").split("\n")[1].split()[1][5:])