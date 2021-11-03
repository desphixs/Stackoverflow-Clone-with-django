import hashlib
 
flag = 0
 
pass_hash = input("md5 hash: ")
 
wordlist = input("File name: ")
try:
    pass_file = open(wordlist,"r")
except:
    print("No file found :(")
    quit()
 
for word in pass_file:
 
    enc_wrd =word.encode('utf-8')
    digest =hashlib.md5(enc_wrd.strip()).hexdigest()
    # print(word)
    # print(digest)
    # print(pass_hash)
    if digest.strip() == pass_hash.strip():
        print("password found")
        print("Password is " + word)
        flag = 1
        break
 
if flag == 0:
    print("password not in list")