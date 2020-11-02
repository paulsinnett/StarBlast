from optparse import OptionParser

parser = OptionParser(usage="usage: %prog input output")
(options, args) = parser.parse_args()

with open (args[0], "rb") as input_file:
	with open (args[1], "wb") as output_file:
		content = input_file.read()
		content = content.replace(b"\r\n", b"\r")
		output = [byte | 0x80 for byte in content]
		output_file.write(bytes(output))
