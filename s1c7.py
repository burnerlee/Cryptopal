from Crypto.Cipher import AES
key="YELLOW SUBMARINE"
string1=""
file1 = open('c7.txt', 'r') 
Lines = file1.readlines()
for line in Lines:
        line=line.rstrip()
        string1=string1+line
string1=string1.decode("base64")
cipher=AES.new(key)
result=cipher.decrypt(string1)
print result
