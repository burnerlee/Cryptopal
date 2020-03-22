string_input=raw_input("enter the line\n")
string_input=string_input.decode("hex");
char_2 =raw_input("enter the char\n");
b=ord(char_2)
final=[]
for char_1 in string_input:
	final.append(chr(ord(char_1)^b))
print "".join(final)
