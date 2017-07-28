def getmsg () :
    msg = input("Enter msg : ")
    return msg

def ceasarShift(msg):
    ciphertext =''
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G' 'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    shiftNum = 3
    for ch in msg :
        index = alpha.index(ch)
        newindex = index + shiftNum
        shiftedCharacter = alpha[newindex]
        ciphertext  =  ciphertext + shiftedCharacter
        #print(ciphertext)
    return ciphertext
def main () :
    msg = getmsg()
    ciphertext = ceasarShift(msg)
    print(ciphertext)
main ()
