import os
import time

date = time.strftime("%Y-%m-%d")
cmd = 'curl https://recent-messages.robotty.de/api/v2/recent-messages/xqc >> '+date+'-stream-msgs.txt'
print(cmd)

while 1:
    os.system(cmd)
    time.sleep(180000)

