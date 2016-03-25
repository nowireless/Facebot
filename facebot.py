from config import *
import telepot
import time

FILE_QUALITY = 2 - 1

def addDownload(fileid, chatid):
	print fileid, chatid
	return # TODO

# Handle all messages
def handle(msg):
	if "photo" in msg:
			addDownload(msg["photo"][FILE_QUALITY]["file_id"], msg["chat"]["id"])

bot = telepot.Bot(key)

bot.notifyOnMessage(handle)
print "Running..."

while 1:
    time.sleep(30)
