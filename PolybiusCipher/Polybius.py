def  getmsg():
    msg = input("entre msg ")
    return msg

#crypt
def chefpolybius(msg):
     alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G' 'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
     num = [11,12,13,14,15,21,22,23,24,25,31,32,33,34,35,41,42,43,44,45,51,52,53,54,55,11,12,13,14,15,21,22,23,24,25,31,32,33,34,35,41,42,43,44,45,51,52,53,54,55]
     for ch in msg:
         index = alpha.index(ch)
         if index:
             crypt = num(index)
         else:
             crypt = ch
     print(ch)
     return ch
#decryp
def dechefpolybius(msg):
     alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G' 'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
     num =[11,12,13,14,15,21,22,23,24,25,31,32,33,34,35,41,42,43,44,45,51,52,53,54,55,11,12,13,14,15,21,22,23,24,25,31,32,33,34,35,41,42,43,44,45,51,52,53,54,55]
     for ch in num :
         index = num.index(ch)
         print(index)
         if index :
             crypt = alpha(index)
         else:
             crypt = ch
     print(ch)
     return ch
def main ():
    msg = getmsg()
    dechefpolybius(msg)


mamain()
