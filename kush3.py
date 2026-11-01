#concatination
first_name="kushal"
second_name="bharadwaj"
full_name=first_name + " " + second_name
print("full_name: " + full_name)

#repeatation
message="warning "*10
print(message)
#string methods
print(message.upper())
print(message.lower())
print(message.strip())
print(message.replace("waring","warning"))
print(len(message))
#multiyline string
k="""kushal said "hello gowtham"
gowtham said "hello kushal\n" """
print(k)

#accessing string characters
name="kushal"
print(name[0])
print(name[1:6])
print(name[-1])
print(name[-6:-1])
print(name[::2])