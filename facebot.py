from config import *
import telepot
import time

# Handle all messages
def handle(msg):
    print msg

bot = telepot.Bot(key)

bot.notifyOnMessage(handle)
print "Running..."

while 1:
    time.sleep(30)
