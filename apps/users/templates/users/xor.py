3. XOR decryption:
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
Your task has been made easy, as the encryption key consists of three lower case characters. Write a function that takes as a parameter, an array (or list) containing the encrypted ASCII codes, and using the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.


def xor(cipher, key):
    run= True
    while run == True:
        key = key
        crypt = cipher

        result =[]
        asc_key=[]
        out=''
        n=1
        i=0
        p=0
        I=0
        j=0

        crypt = crypt.replace('n','xA')
        crypt = crypt.replace('r','xD')
        crypt = crypt.replace('t','x9')

        result = crypt.split('\\x')


        while p <= len(key)-1:
            asc_key.append(ord(key[p]))
            p+=1


        while n <= len(result)-1:
            result[n]= chr((asc_key[i])^(int(result[n],16)))
            n+=1
            if i == (len(key)-1):
                i = 0
            else: i+=1
        while I <= len(result)-1:
            out+= (result[I])
            I+=1
        print ("The correspondant of that key or password is: ",out)
        run = input("Do you need to run another? (y or n): ")
        if run =="y" or "Y":
            run = True
        else:
            run = False