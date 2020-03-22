string1 = raw_input("Enter the first string\n")
string1=string1.decode("hex");
string2 = raw_input("Enter the second string\n")
string2=string2.decode("hex");
answer= "".join(chr(ord(char_a)^ord(char_b)) for char_a,char_b in zip (string1,string2))
answer=answer.encode("hex")
print answer
