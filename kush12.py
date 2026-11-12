a = 20
b=30 
a,b=b,a
print(f"a = {a} ,b ={b}")

dishes={
    "bengaluru":"bisi bele bath",
    "mysore":"pak",
    "mangaluru":"neer dose",
    "mandya":"ragi mudde",
    "devanagere":"masal dose"
}
dishes["bengaluru"]=["kushal"]
del dishes["mandya"]

student_detials={
    "g":{
        "name":"gowtham",
        "age":19,
        "height":5.6,


    },
    "k":{
        "name":"kushal",
        "age": 20,
        "height":5.5,
        
    }
}


time=int(input("enter the time: "))
if time==8:
    print("its time to breakfast")
elif time==13:
    print("its time to lunch")
elif time==20:
    print("its time to dinner")
else:
    print("invalid input") 


seats=8
while seats>0:
    print("book one seat")
    seats-=1
    
    print("remaining seats",seats)

print("all seats are booked")

import time
i =10
while i>0:
    print(i)
    time.sleep(1)
    i-=1
print("happy new year")

v="aeiou"
k=input("enter the string: ")
count=0
for letter in k:
    if letter in v:
        count+=1
print(count)
d={
     "g":{
            "name":"gowtham",
            "age":19,
            "height":5.6,
    
    
        },
        "k":{
            "name":"kushal",
            "age": 20,
            "height":5.5,
            
        },
        "l":{
            "name":"sabran",
            "age":20,
            "height":5.5

        }

}
for i in d:
    print(i)