def add(*num):
    return sum(num)


print(add(1,11,111))

def attend(**details):
    print(type(details))
    for i,j in details.items():
        print(f"{i}: {j}")

attend(name="kushal",today_attends=1,)
print("----------------------------------")
attend(name="gowthu",today_attends=1,)
print("----------------------------------")


add= lambda a,b: a+b
print(add(12,13))

k=[
   { "name":"kushal","age":18,},
   {"name":"gowthu","age":21,},
   {"name":"abhi","age":20}
]

k.sort(key=lambda s:s["age"],reverse=True)
print(k)


def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(4))