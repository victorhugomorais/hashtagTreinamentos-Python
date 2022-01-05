meta = 0.05
taxa = 0

rendimento = 0.19

if rendimento > meta :
    taxa = 0.02
    if rendimento > 0.2 :
        taxa = 0.05
        
    print('taxa foi {}:'.format(taxa))    
else:
    taxa = 0
    print('taxa foi {}:'.format(taxa))
    
        
