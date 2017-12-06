#write a program to find prime numbers from 2 to 100
Lower=2
upper=100
print('The prime numbers between 2 and 100')
for num in range(lower,upper ):
   # prime numbers are greater than 1
   if num > 1:

       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
        
        
    

        
        
    

    
    

    
