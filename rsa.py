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
        print("Inverse does not exist")
        return -1



#Public key are variables 'e' and 'n'
#Private key is variable d

#RSA uses a one way trapdoor function (there is no way to undo the encryption unless the trapdoor is known. Here the factors of 'n' is the trap door)

# However is n is public, why is it difficult to find it? 
# Answer is Prime factorization - fundamental theorem of arithmetic.
# It says that for any number greate than 1, there is only one unique combination of the product of two prime numbers to obtain the number.  

#example: p = 61, q = 53, e = 17, m = 42

message = int(input ("\nEnter the message you want to encrypt: "))

p = int(input("\nEnter the first large prime: "))
q = int(input("\nEnter the second large prime: "))
e = int(input("\nEnter the value of e: "))

n = p * q
phi = (p-1)*(q-1)

#we calculate d as the inverse of e mod phi = 1
#phi must not share a factor with e
d = gcdExtended(phi,e)

if(d == -1):
    print("\nWrong selection of parameneters")

else:
    #Encryption
    c = (message**e) % n
    print("\n Encrpyted Message = ", c)

    #Decryption
    decr = (c**d) % n
    print("\n Decrypted Message = ", decr)

