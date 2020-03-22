string1=raw_input("Enter the message\n")
string2 =raw_input("enter the key\n");
length=len(string1)
length2=len(string2)
final=[]
char_1=0
loop2=0
while loop2<length2:
	if char_1<length:
		
		value=chr(ord(string1[char_1])^ord(string2[loop2]))
		loop2=loop2+1
		value=value.encode("hex")
		final.append(value)
		char_1=char_1+1
		if loop2==length2:
			loop2=0
	else:
		break
print "".join(final)
