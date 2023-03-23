num1=num2=100
max=0
product_inv=''
for j in range(900**2):
    product=str(num1*num2)
    for i in range(len(product)):
        product_inv=product[i]+product_inv
    if product==product_inv:
        product=int(product)
        if max<product:
           max=product
           
    if num2<999:
     num2+=1
    elif num2==999:
        num1+=1
        num2=101
    elif num1>=999:
        break
    
    product_inv=''
    product=''
    
print(max) 
  
