a=input("enter first number:")
a=int(a)
opr=input("enter the operator +,-,*,/:")
b=input("enter second number:")
b=int(b)
ans=0
if opr == '+':
        ans=a+b
elif opr== '-':
        ans=a-b
elif opr=='*':        
         ans=a*b
elif opr=='/':        
         ans=a/b
elif opr=='%':        
         ans=a%b
else:
    print("Invlaid operator:");
print(ans);             