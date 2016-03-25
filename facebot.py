from config import *
import telepot
import time
import sys
import os
import faceswap.faceswap as faceswap

FILE_QUALITY = 2 - 1
DL_PATH = "temp/dl.jpg"
OUTPUT_PATH = "temp/output.jpg"

def process(fileid, chatid):

	print "Processing image from: ", chatid

	bot.downloadFile(fileid, DL_PATH)

	faceswap.process_images(DL_PATH, FACE_SOURCE, OUTPUT_PATH)

	pic = open(OUTPUT_PATH, "rb")
	bot.sendPhoto(chatid, pic)

# Handle all messages
def handle(msg):
	try:
		if "photo" in msg:
			process(msg["photo"][FILE_QUALITY]["file_id"], msg["chat"]["id"])
	except:
		e = sys.exc_info()[0]
		print "ERROR! ", e

bot = telepot.Bot(key)

bot.notifyOnMessage(handle)

if not os.path.exists("./temp"):
	os.mkdir("./temp")

print "Running..."

while 1:
	time.sleep(30)
