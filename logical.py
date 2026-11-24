# # 1) Perfect Number


# n=int(input("Enter a number: "))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("Perfect Number")
# else:
#     print("Not Perfect")





# # 2) Shopping Bill System

# items_list={}
# total=0
# total_bill_amount=0

# n=int(input("Enter the number of products: "))
# for i in range(1,n+1):
#     name=input(f"Enter the name of the product {i}: ")
#     quantity=int(input("Enter the quantity of product: "))
#     price=float(input("Enter the price of the product: "))

#     items_list[name]={
#         "quantity":quantity,
#         "price":price
#     }

#     total=quantity*price
#     print(f"Total of product {i}:",total)
#     total_bill_amount+=total

# print("Total bill amount:",total_bill_amount)
# final_amount=0
# discount=0
# if total_bill_amount>=5000:
#     discount=total_bill_amount*0.10
#     final_amount=total_bill_amount-discount
#     print("Discount: 10%")
#     print("Final amount to pay: ",final_amount)
# else:
#     print("No discount applied.")
# print(items_list)



# # 3) Pattern Printing

n=3
for i in range(n):
    for j in range(2*n-1):
        if j==i or j==2*n-2-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in range(1,n):
    for j in range(2*n-1):
        if j==n-1-i or j==n-1+i:
            print("*",end="")
        else:
            print(" ",end="")
    print()