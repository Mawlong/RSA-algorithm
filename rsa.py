# RSA algorithm
# author: Leon Patrick Mawlong, Tanuj Chakraborty
# NIT Meghalaya: Network Security and Cryptography Assignment 

# RSA uses a one way trapdoor function (there is no way to undo the encryption unless the trapdoor is known. Here the factors of 'n' is the trap door)
# However n is public, why is it difficult to find it? 
# Answer: Prime factorization - fundamental theorem of arithmetic.It says that for any number greate than 1, there is only one unique combination of the product of two prime numbers to obtain the number.
#Public key: e and n
#Private key: d

import gmpy2
import random
from Crypto.Util import number
import time

start = time.time()

# Making use of Extrended GCD Euclidean algorithm to find weather inverse exists
def gcdExtended(r1, r2):
    
    s1 = t2 = 1
    s2 = t1 = 0 
    a = r1
    while(r2>0):
        q = r1//r2
        r = r1 - q*r2
        r1 = r2
        r2 = r
        s = s1 - q * s2
        s1 = s2
        s2 = s
        t = t1 - q * t2
        t1 = t2
        t2 = t

    if(r1 == 1):
        if(t1<0):
            return (t1 % a)
        else:
            return t1
    else:
        #Inverse does not exist
        return -1

#Encryption of the plaintext using public keys e and n
def encrypt(e,n, plaintext):
    cipher = [gmpy2.powmod(ord(char), e, n) for char in plaintext]
    return cipher

#Decryption of the ciphertext using private keys d
def decrypt(d,n, ciphertext):
    decipher = [chr(gmpy2.powmod(char, d, n)) for char in ciphertext]
    return ''.join(map(lambda x: str(x), decipher))


message = str(input ("\nEnter the message you want to encrypt:\n"))

#Generating prime numbers 1024 bit in size
p = number.getPrime(1024)
q = number.getPrime(1024)

n = p * q

phi = (p-1)*(q-1)

e = random.randint(1,phi)
d = gcdExtended(phi,e)

#incase inverse does not exist between phi and e, we generate a new e and perform the test
while(d==-1):
    e = random.randint(1,phi)
    d = gcdExtended(phi,e)

print("\n\nPublic key:\ne = ", e,"\nn =", n )
print("\n\nPrivate key:\nd = ", d)

cipher_text = encrypt(e,n, message)
print("\nEncrypted message: \n" + ''.join(map(lambda x: str(x), cipher_text)))
print("\n\n\nDecrypted message:\n" + (decrypt(d,n, cipher_text)))

#To print time taken
end = time.time()
print("\n\nTime taken: ", (end - start))