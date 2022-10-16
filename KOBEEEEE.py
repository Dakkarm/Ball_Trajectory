def fun(n):
    if n>0: 
        counter=0
        
        spazio=' '
        stelle='*'
        while counter<n:
            n_spazi = n-counter

            for _ in range(0, n_spazi):
                spazio=str(spazio)+' '
            
            print(spazio, end='')
            print(stelle)
            counter = counter + 1
fun(17)