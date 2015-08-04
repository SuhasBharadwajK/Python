k=raw_input()
s=0
    for i in range(k):
        l=i
        while(True):
            if(s==89 or s==1):
                    break
                while(l==0):
                    s=(l%10)**2+s
                    l=l/10
                print l
            
