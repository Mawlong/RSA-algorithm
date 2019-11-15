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

message = (input ("\nEnter the message you want to encrypt: "))

a = []

for i in range(len(message)):
    a.append(ord(message[i]))

#print(a)

#p = int(input("\nEnter the first large prime: "))

#p = 179081209581970862429224601857663215147261277689339968201876099196179138805428517493003072088303838668008999097748715006099950947050826721959841869068064396159473805318997606568463513029886212749711990235765643685421549116454866520627960772589158098824417862059378236036266593742758708452800946208862216798967

#q = int(input("\nEnter the second large prime: "))

#q = 146650523061314944919205116005245160985944837646537472972628127836877818778339906010977989972360010244250231635742003565047699276836901991052527418585623414264604188199530379632534167679523668098684372873657858229446080129227778193597570777394103360591709605857965734217008564333135626220959698114795871505623

p = 61

q = 53

#e = int(input("\nEnter the value of e: "))

e = 17

n = p * q
phi = (p-1)*(q-1)

#we calculate d as the inverse of e mod phi = 1
#phi must not share a factor with e
d = gcdExtended(phi,e)

if(d == -1):
    print("\nWrong selection of parameneters")

else:
    print("\nEncrpyted Message = ", end = "")
    c = []
    #Encryption
    #c = (a[0]**e) % n
    for i in range(0, len(a)):
        c.append((a[i]**e)%n)
        print(c[i], end = "")
        

    #Decryption
    #decr = (c**d) % n
    decr = []
    for i in range(0, len(c)):
        decr.append(chr((c[i]**d)%n))
    #print("\n Decrypted Message = ", decr)

    string = ""
    for i in range(0, len(decr)):
        string = string + decr[i]
    print("\nDecrypted Message: ", string)