import os
import base64
filenames = os.listdir("data")
i = 0
while i <= 1:
	pathname = os.path.join("data", filenames[i])
	file = open(pathname, 'r')
	text = file.read()
	enc = base64.b64encode(text)
	file = open(pathname, 'w')
	file.write(enc)
	file.close()
	i += 1
