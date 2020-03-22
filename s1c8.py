from Crypto.Cipher import AES
key="abcdefghijklmnop"
file1 = open('c8.txt', 'r') 
Lines = file1.readlines() 
line_no=0
for line in Lines:
	score=0
	line=line.rstrip()
	line_no=line_no+1
	string1=line.decode("hex")
	cipher=AES.new(key)
	result=cipher.decrypt(string1)
	for position in range (0,10):
		for position2 in range(position+1,10):
			if string1[position*16:position*16+16]==string1[position2*16:position2*16+16]:
				if result[position*16:position*16+16]==result[position2*16:position2*16+16]:
					score=score+1
					
	if score>0:
		print "Score is: " + str(score) + " for line " + str(line_no)

print "205 line is actually the blank line so ignore it"
#so the answer is the 133rd line
