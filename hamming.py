def  countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 
string1=raw_input("enter the first string\n")
string2=raw_input("enter the second string\n")
length=len(string1)
sum=0
for a in range(length):
	value=ord(string1[a])^ord(string2[a])
	sum=sum+countSetBits(value)

print sum
