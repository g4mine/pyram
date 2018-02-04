import os
import base64
inp = input (str ())
filenames = os.listdir(inp)
for arq in filenames:
	pathname = os.path.join("data", arq)
	file = open(pathname, 'r')
	text = file.read()
	enc = base64.b64encode(text)
	file = open(pathname, 'w')
	file.write(enc)
	file.close()
