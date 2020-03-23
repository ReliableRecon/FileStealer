from telnetlib import Telnet 
import time 
tn = Telnet('192.168.1.4')
time.sleep(1)
tn.read_until(b"/ #")
tn.write(b"ls\n")
tn.read_until(b"/ #")
tn.write(b"cat boot.sh\n")
x =  tn.read_until("/ #")
print x
F = open("testfile.txt", "w")
F.write(x)
F.close()

