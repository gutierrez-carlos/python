vnum=True

while vnum==True:

    num=int(input("Ingrese un numero: "))    
    su=0
    re=0
    
    if num>=1:
        vnum=False
        
        for i in range(1,num+1,2):
            su+=i**i
        for i in range(2,num+1,2):
            re+=i**i
            
        print(f"La suma es: {su-re}")
        
    else:
        print("Ingrese un valor positivo...")