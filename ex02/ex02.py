def alphabet():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    
    alpha_reverse =[]
   

    for i in range(len(alpha)):
        
   
        alpha_reverse.append(ord((alpha[i])))

    for i in range(len(alpha_reverse)):

        print(chr(alpha_reverse[i]))





alphabet()
        
    
    
