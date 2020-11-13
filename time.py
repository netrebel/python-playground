import time
from time import sleep

now = time.time()
print(now)

sleep(0.2)
later = time.time()
print(later - now)

print(time.strftime("%a, %d %b %Y %H:%M:%S UTC", time.gmtime()))
print(time.strftime("%a, %d %b %Y %H:%M:%S local time"))
print(int(time.strftime("%z"))/100) # UTC hours diff