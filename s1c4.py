priority=3
def Nmaxelements(list1, N): 
    final_list = [] 
  
    for i in range(0, N):  
        max1 = 0
          
        for j in range(len(list1)):      
            if list1[j] > max1: 
                max1 = list1[j]; 
                  
        list1.remove(max1); 
        final_list.append(max1) 
          
    return(final_list) 
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
line_no=0
file1 = open('c4.txt', 'r') 
lines = file1.readlines()
final_scores=[] 
for line in lines:						# storing the score for each line for each character in a list->final_scores
	line_no=line_no+1
	line=line.rstrip()
	string_input=line.decode("hex")
	for b in range (256):
		scores = 0
		for char_1 in string_input:
			value=(chr(ord(char_1)^b).upper())
			score = character_frequencies.get(value, 0)
			scores=scores+score
		final_scores.append(scores)
topscore=Nmaxelements(final_scores,priority)	#selecting some highest scores from final_scores		
line_no=0
for line in lines:
    	line_no=line_no+1
	line=line.rstrip()
	string_input=line.decode("hex")
	for b in range (256):
		scores = 0
		for char_1 in string_input:
			value=(chr(ord(char_1)^b).upper())
			score = character_frequencies.get(value, 0)
			scores=scores+score
		if scores>=topscore[priority-1]:			#printing the details for which the score was highest
			print "line no: " + str(line_no) + " with char: '" + chr(b) + "' score: " + str(scores)