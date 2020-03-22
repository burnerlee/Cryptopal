string_input=raw_input("Enter the string\n")
string_input=string_input.decode("hex");
   'M' :  2.53 ,       'W' :  1.83,
'D' :  3.87   ,     'N' :  7.17  ,      'X' :  0.19,
'E' : 12.10  ,      'O' :  7.47    ,    'Y' :  1.72,
'F' :  2.18 ,       'P' :  2.07   ,     'Z' :  0.11,
'G' :  2.09     ,   'Q' :  0.10                , 
'H' :  4.96      ,  'R' :  6.33                 ,
'I' :  7.33    ,    'S' :  6.73                 ,
'J' :  0.22   ,     'T' :  8.94   
}
for b in range (256):
	print chr(b)
	scores = []
	for char_1 in string_input:
		value=(chr(ord(char_1)^b).upper())
		score = character_frequencies.get(value, 0)
		scores.append(score)	
	print sum(scores)
	print "\n"
#this gives the score for each element, we find the scores are 149 for r,R and 198 for ~,a and 140 for x,X so putting all these in list
#and xoring for each of them we get that actually it X and we get the decoded message

elements=['r','R','x','X','~','a']
for element in elements:
	print "The character is "
	print element
	c=ord(element)
	final=[]
	for char_2 in string_input:
		value=(chr(ord(char_2)^c))
		final.append(value)
	final="".join(final)	
	print final
