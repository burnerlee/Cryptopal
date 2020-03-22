priority=2
def Nmaxelements(list1, N): 
    final_list = [] 
  
    for i in range(0, N):  
        max1 = 0
          
        for j in range(len(list1)):      
            if list1[j] > max1: 
              max1 = list1[j]; 
                  
        list1.remove(max1)
        final_list.append(max1) 
          
    return final_list 
character_frequencies={
'A' :  8.55  ,     ' K' :  0.81    ,    'U' :  2.68,
'B' :  1.60  ,      'L' :  4.21    ,   ' V' :  1.06,
'C' :  3.16    ,    'M' :  2.53 ,       'W' :  1.83,
'D' :  3.87   ,     'N' :  7.17  ,      'X' :  0.19,
'E' : 12.10  ,      'O' :  7.47    ,    'Y' :  1.72,
'F' :  2.18 ,       'P' :  2.07   ,     'Z' :  0.11,
'G' :  2.09     ,   'Q' :  0.10                , 
'H' :  4.96      ,  'R' :  6.33                 ,
'I' :  7.33    ,    'S' :  6.73                 ,
'J' :  0.22   ,     'T' :  8.94   
}  

def  countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 
string3=""
file1 = open('myfile.txt', 'r') 
Lines = file1.readlines() 
for line in Lines:
	line=line.rstrip()
	string3=string3+line
string3=string3.decode("base64")
keysize_hamm={}
for a in range(2,50):
	no_of_block=0
	position=0
	sum_final=0
	while position<(len(string3)-2*a):
		no_of_block=no_of_block+1
		string1 = string3[position:position+a]
		string2 = string3[position+a:position+a*2]
		length=len(string1)
		sum=0
		for f in range(length):
        		value=ord(string1[f])^ord(string2[f])
	        	sum=sum+countSetBits(value)
		position=(position+a*2)
		sum_final=sum_final+sum
	keysize_hamm['key'+str(a)]=sum_final
print keysize_hamm
#using this we get that the minimum hamming distance in for 29. It was far from the others and 2nd 3rd 4th were rather close. so i decide to 
#test this for first

#we got the keysize as 29
print "\nAccording to 29 as the keysize, the possibilties of each byte, to change the number of bytes change the priority variable\n"
for element in range (29):
	block=[]
	loop=element
	while loop<len(string3):
		block.append(string3[loop])
		loop=loop+29
	final="".join(block)
	finalscore=[]
	finalchar=[]

	for b in range (256):
        	        scores = 0
	                for char_1 in final:
        	                value=(chr(ord(char_1)^b).upper())
                	        score = character_frequencies.get(value, 0)
                        	scores=scores+score
	                finalscore.append(scores)
	toplist=Nmaxelements(finalscore,priority)
        
	for b in range (256):
                        scores = 0
                        for char_1 in final:
                                value=(chr(ord(char_1)^b).upper())
                                score = character_frequencies.get(value, 0)
                                scores=scores+score
                        if scores >= toplist[priority-1]:
				finalchar.append(chr(b))
        print finalchar
#by changing the constant 2, i get the value of top possibilities in order, setting it 2 gives me top 3, setting it 0, gives me top possibility
#each value solving i get the key as: Terminator X: Bring the noise.. further check by taking the xor with this key and make necessary 
#adjustments.

