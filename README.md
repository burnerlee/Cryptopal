# Cryptopal

# SET 1

#Challenge 1
Alright this is a simple program. Simple python code.Run the file simply, it prompts for a hex encoded text and gives the
output as the base64 encoded data

#Challenge 2
Again a simple program, run it using python 2.7 -> enter the first string -> enter the second string -> gives you the output

#Challenge 3
Run the program, and enter the XORed->hex encoded key...The program will calculate the scores for all possible value xor-byte
and then select the top 5 scores... you can change this constant 5 by changing the 'priority' variable. Then for each of these
top byte values, it will decode the text and show the output. The best output gives the result. Here the answer is given
by X: and the message decodes as: Cooking MC's like a pound of bacon.. cool.

#Challenge 4
Run the program, i have already fed the file c4.txt as the input to the file. It decodes it, performs some operations and 
gives you the top possibilities of the line and the character with their scores.. again you can change the number of top
results you want by changing the priority variable. Now you can check for the respective lines with the characters simply
by using the single byte xor. The answer would be line 171 with char '5'
The decoded text: Now that the party is jumping

#Challenge 5
Run the program -> enter the message you want to encrypt -> enter the key -> You get the encrypted message

#Challenge 6
Okay, so this was the best one of the set... i made a python program which takes the input from the file 'c6.txt' and then
finds the hamming distance for all keysize values from 2-40. It prints the hamming distance for each keysize and 29 came out
to be the minimum by far, so i considered my keysize to be 29 for sure.
Now by doing the same steps as in breaking single byte xor, i try to calculate the highest scores according to english 
alphabet frequencies and i print out the possible characters for each byte.. again the number of possibilites for each
byte can be changes by changing the priority variable. Currently i have set it to 1. Change it to 3 and 2 to find bytes at
some positions as there the byte with highest score is not correct.
You will get the key as Terminator X: Bring the noise
If you still have confusion about the cases of some characters, this would be cleared when we decode the code
I have uploaded s1c6mx.py for decoding the text after finding the key. The input is internally fed to the python file.Run
it, it prompts to enter the key. Enter the key with whatever case you like. The positions at which you get vague chars
needs to be changes. Finally you end up with -> 'Terminator X: Bring the noise'
Enter this key and you get the decoded message:
I'm back and I'm ringin' the bell 
A rockin' on the mike while the fly girls yell 
In ecstasy in the back of me 
Well that's my DJ Deshay cuttin' all them Z's 
Hittin' hard and the girlies goin' crazy 
Vanilla's on the mike, man I'm not lazy. ........


#Challenge 7
I have written the python program using pycrypto. It simply takes the message as the input from the file c7.txt. I have 
provided the key to program. It simply prints the output when you run the program.. the output is really cool...
I'm back and I'm ringin' the bell 
A rockin' on the mike while the fly girls yell 
In ecstasy in the back of me 
Well that's my DJ Deshay cuttin' all them Z's 
Hittin' hard and the girlies goin' crazy 
Vanilla's on the mike, man I'm not lazy. .... and so on

#Challenge 8
Well this was an interesting one, the basic idea is to check for each line of input, whether any 16 bytes of data match with 
each other and if they do, whether they also match in the decoded form if decoded by any key.. so i gave it a random key..
later i also read that comparing whether they are equal in the encoded form is quite enough as it is rare case that
16 bytes come out to equal togetherly in a encoded text.
So as you run the program it gives you the score of all the lines having score > 0. The score here is defined as the number
of equal 16 bytes chunks.This comes out to be 6 only in line 133. So line 133 is the required answer
