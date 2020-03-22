priority=5
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

string_input=raw_input("Enter the string\n")
string_input=string_input.decode("hex");
score=0
#character frequency data taken from the internet
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
#taking xor with each every character which gives back the original text and then we check the score of text for each value of b and see
#where is comes the highest
finalscore=[]
for b in range (256):
	
	scores = 0
	for char_1 in string_input:
		value=(chr(ord(char_1)^b).upper())
		score = character_frequencies.get(value, 0)
		scores=scores+score	
	finalscore.append(scores)					#storing all the scores in a list
topscores=Nmaxelements(finalscore,priority)			#selecting the top 5 scores


elements=[]

for b in range (256):
	scores = 0
	for char_1 in string_input:
		value=(chr(ord(char_1)^b).upper())
		score = character_frequencies.get(value, 0)
		scores=scores+score	
	if scores>=topscores[priority-1]:					#if the score is greater than or equal to 5th top score
		elements.append(chr(b))					#then store the corresponding b in elements

for element in elements:				#printing the xor-decode using those 5 values of b
	print "For the character:"
	print element
	c=ord(element)
	final=[]
	for char_2 in string_input:
		value=(chr(ord(char_2)^c))
		final.append(value)
	final="".join(final)	
	print final
