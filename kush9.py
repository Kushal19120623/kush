#while loop
kush= True
p=1
while kush:
    print("condition is true")
    p+=1
    if p>10:
        kush=False
    
k=True
i=1
while k:
    print(f"try{i}")
    i+=1
    if i>10:
        k=False

is_failed=True
i=1
while is_failed:
    if i%2!=0:
        i+=1
        continue
    print(f"try again{i}")
    i+=1
    if i>100:
        break    
print("enough")


u=1
while u<=10:
    l=1
    while u<l:
        print("chandan",end=" ")
        l+=1
    print("")
    u+=1




pin="1912"
h=1
l=1000
while h<3:
    j=input(f"enter your pin trail {h}: ")
    h+=1
    if j==pin:
        print("access granted")
        if j==pin:
            k=int(input("enter the amount to withdraw: "))
            if k<l:
                print(f"withdrawal successful, your remaining balance is {l-k}")
    else:
        print("access denied")
        
