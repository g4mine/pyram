import os, base64
inp = raw_input("Path to encode: ")
filenames = os.listdir(inp)
for arq in filenames:
	pathname = os.path.join(inp, arq)
	file = open(pathname, 'r')
	text = file.read()
	enc = base64.b64encode(text)
	file = open(pathname, 'w')
	file.write(enc)
	file.close()

