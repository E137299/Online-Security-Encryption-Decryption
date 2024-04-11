# Cesar Cipher
### Note: The unit tests returns a string of capitalized letters. Ex. cesar_encrypt("abc",1)>>>>"BCD"   


- ### caesar(text, shift):
	- Inputs:
	  - Text to be encrypted
	  - Number of places that each letter will be displaced

    - Output:
	    - Encrypted text will be returned. The letters in the text will all be capitalized.


	[Cesar Cipher Video Tutorial](https://youtu.be/fR8rVR72a6o)



# Vigenere
![Vigenere](vig.PNG)

The objective of this lab is to implement the [Vigenère Cipher](https://privacycanada.net/classical-encryption/vigenere-cipher/). The Vigenère Cipher, uses a special keyword to encrypt a message - i.e. to create the cipher text. Each letter in the message and each letter in the keyword is represented by its position in the alphabet (A=0, B=1, … , Z=25). To create the cipher text, the integer value of the nth letter of each are added. Using modulus with 27 allows you to keep the result in the range of alphabetic values including a space.  If the keyword is shorter than the message, we simply repeat the keyword.

[Vigenere Tutorial Video](https://youtu.be/E352JJ8xv48)

| **Message**     | **CRYPTOGRAPHY** | 
| :---            |    ----       | 
| **Keyword**     | **ABCD**ABCDABCD | 
| **Cipher Text** | **CSASTPIUAQJB** | 


[Try the Vigenere Cipher Here](https://studio.code.org/s/vigenere/lessons/1/levels/1)

Your mission is to write a program that will read a message and a keyword and apply the Vigenère Cipher to it (see [video](https://www.youtube.com/watch?v=E352JJ8xv48) explanation of Vigenère Cipher).

Your program should prompt the user for some plain text to be encrypted. Then, it should prompt the user for some text which will serve as a keyword. 

To perform the encryption, you need to loop through the plain text and add the index value for each letter from the keyword to it, mod 27. Unfortunately, neither the letters in the plain text nor in the keyword have values between 0 and 27. You will have to convert those letter values so that they are between 0 and 27, then do the add, then do the mod, then convert them back to the proper ASCII values. 
	
You only need one loop for this program. However, the plain text is generally longer than the keyword. So, though you will only need one loop, you need to keep track of where you are in the keyword independently of the plain text. Whenever you get to the end of the keyword, you should set that index back to 0.

### Functions
- ### vigenere_encrypt(text, key)
	- Input:
	  - text that will be encrypted
      - key
    - Output:
	    - encrypted text in which each letter is capitalized
- ### vigenere_decrypt(text, key)
	- Input:
	  - text to be decrypted
      - key
    - Output:
	    - decrypted text in which each letter is capitalized

Example: 
```python
Enter your plaintext:
ATTACKATDAWN

Enter your keyword:
LEMON

Plain Text: ATTACKATDAWN
Key: LEMON
Encrypted Text: LXFOPVEFRNHR


Enter text to be decrypted:
LXFOPVEFRNHR

Enter your keyword:
LEMON

Encrpyted text: LXFOPVEFRNHR
Key:  LEMON
Decrypted Text:  ATTACKATDAWN
```




  
  
