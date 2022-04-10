def my_number():
    
        r = int(input("Enter value  "))
        num=[]
        if(0<r & r<=10): 
         for i in range(0,r):
            x=int(input(""))
            num.append(x)
   
        for i in num:
         if(i%2==0):
                print(i,"is even number")
         else:
                print(i , "is odd number")


my_number()
