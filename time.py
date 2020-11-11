import time
from time import sleep

now = time.time()
print(now)

sleep(0.2)
later = time.time()
print(later - now)
