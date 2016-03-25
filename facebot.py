from config import *
import telepot
import time
from shutil import copyfile

FILE_QUALITY = 2 - 1
DL_PATH = "temp/dl.jpg"
OUTPUT_PATH = "temp/output.jpg"

def process(fileid, chatid):

	bot.downloadFile(fileid, DL_PATH)

	# TODO PROCESS HERE
	copyfile(DL_PATH, OUTPUT_PATH)

	pic = open(OUTPUT_PATH, "rb")
	bot.sendPhoto(chatid, pic)



# Handle all messages
def handle(msg):
	try:
		if "photo" in msg:
			process(msg["photo"][FILE_QUALITY]["file_id"], msg["chat"]["id"])
	except e:
		print "ERROR! " + e

bot = telepot.Bot(key)

bot.notifyOnMessage(handle)
print "Running..."

while 1:
	time.sleep(30)
