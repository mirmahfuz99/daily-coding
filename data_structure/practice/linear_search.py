pos = -1
def linearSearch(list,n):

    i = 0

    while i < len(list):
        
        if list[i] == n:
            globals()['pos'] = i
            return True

        i = i+1    
    return False                    

if(linearSearch([1,2,3] , 2)):
    print("Found At ", pos)
else:    
    print("Found At ", pos)
