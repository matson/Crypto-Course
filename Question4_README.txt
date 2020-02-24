Question 4:

4) [15 points] Can you prove that the construction you implemented in question 3 above is semantically secure? In you answer, also discuss any assumptions you have made.

In order to have a semantically secure cipher, the construction must include the IND-CPA format or have randomized encryption.  It must randomize the encryption process and 
return different ciphertexts when the same plaintext is encrypted twice.  It must follow the C = E(K, R, P) format where the R represents random bits.
Regardless of randomness, you should also be able to convert back to a plaintext regardless of the value of your R.
The textbook also states that to achieve this randomness, one could simply use the DRBG which returns random-looking bits with some secret value.
For my code, I chose to use the random() libraries in python 3 to achieve this random output goal.  Testing with print statements, I saw that each 
value for the key + random values printed totally random combinations each time I ran the functions.  I then used the encrypt function to finally xor the result together 
to still achieve the random values.  I then decrypted the process, and printed my plaintext again at its normal state.
One assumption I can make is that my implementation was correct since I receive the original ciphertext.  Another assumption I 
can make is how I can make it even more randomized and therefore making it even more secure.
