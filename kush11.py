#loop practice  
l = [1,2,3,4,5,6,7,8,9,10]
t=0
for i in l:
    t += i
print(t)

l = [1,2,3,4,5,6,7,8,9,10]
dl = []
for i in l:
    dl.append(i*2)
print(dl)

k={
    "kushal": 1,
    "gowtham": 2,
    "abhi":3
}
for student,marks in k.items():
    print(f"{student}--{marks}")


h=["hema","manju","kalpa",]
k=[67,68,69,]
student_with_marks={}
for i in range(len(h)):
    student_with_marks[h[i]]=k[i]
print(student_with_marks)

#List compration
l=[j for j in range(1,11)]
dl=[i*2 for i in l if i%2==0]
print(l)
print(dl)



k={
    "kushal":100,
    "hema":78,
    "kalps":67,

}
kl={name:marks for name,marks in k.items() if marks>=70}
print(kl)

k=[(num) for num in input("enter the numbers: ").split(" ")]
l=[int(num) for num in input("enter the numbers: ").split(" ")]
m={}
for i in range(len(k)):
    m[k[i]]=l[i]
print(m)


l=[int(num) for num in input("enter the numbers: ").split(" ")]
l.sort()
l.sort(reverse=True)
print(k)
print(m)