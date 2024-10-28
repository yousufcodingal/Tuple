def palen(ntuple):
    length=len(ntuple)-1
    i = 0
    while(i<length):
        if(ntuple[i]!=ntuple[length]):
            return False 
        length-=1
        i+=1
    return True
ntuple=(1,2,3,3,2,1)
if(palen(ntuple)):
    print("it is a flip flop")
else:
    print("it is not a flip flop")