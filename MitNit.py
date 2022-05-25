print("hello welcome to MitNit")
print()
def secured():
    ask= str(input("do you want to encrypt or decrypt? "))
    print()
    if ask== "encrypt":
        key= int(input("enter encryption key here: "))
        print()
        alphain=  ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    #alphaout= ["g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f"," "]
        alphaout= []
        for i in range(0,len(alphain)):    
            alphaout=alphain[key:]+alphain[0:key]
        if " " in alphaout:
            alphaout.remove(" ")
            alphaout.append(" ")

        '''
    ashmit 
    gynsoz
    '''
        
        inpt= str(input("enter msg to encrypt: "))
        outp= ""
        print()
        for i in range(0,len(inpt)):
            for j in range(0,len(alphain)):
                if alphain[j]== inpt[i]:
                    outp= outp+alphaout[j]
        print(outp)
        print()
    elif ask== "decrypt": 
    #alphain=   ["g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f"," ","!","@","#","$","^","&","*","(",")","-","=","+"]
        alphain=[]
        alphaout=  ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
        print()
        key= int(input("enter key here"))
        print()
        for i in range(0,len(alphaout)):
            alphain= alphaout[key:]+alphaout[0:key]
        if " " in alphain:
            alphain.remove(" ")
            alphain.append(" ")
        print()
        inpt= str(input("enter msg to decrypt: "))
        print()
        outpt=""
        for i in range(0,len(inpt)):
            for j in range(0,len(alphain)):
                if alphain[j]== inpt[i]:
                    outpt= outpt+alphaout[j]
        print(outpt)
        print()
secured()    

while 2>1:
    ask= str(input("do you want to secure another message? "))
    print()
    if ask== "yes":
        secured()
    elif ask== "no":
        print("thank you ")
        print()
        print("credits:- ashMIT tripahti, varNIT kalra")
        print()
        print("git- OP-AT")
        break