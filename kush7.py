#dictionary
DOB={
    "kushal": "19/12/2006",
    "manjunath": "04/04/2006",
    "archit": "15/08/2006",
}
print(DOB)
print(DOB["kushal"])
print(DOB.get("hemavthi","not found"))

#adding new key value pair

DOB["hemavthi"]="12/12/2006"
print(DOB["hemavthi"])

#updating the value of existing key

DOB["kushal"]="20/12/2006"
print(DOB["kushal"])

#removing the key value pair
DOB.pop("archit")
print(DOB)

del DOB["manjunath"]
print(DOB)


print(DOB.keys())
print(DOB.values())
print(DOB.items())

kush={
    "name": "Kushal",
    "age": 17,
    "DOB": "19/12/2006"
}
DOB.update(kush)
print(DOB)



k={
    "name": "Kushal",
    "age": 17,
    }

j={
    "name":"gowtham",
    "age": 17,
}
print(f"total number of age :{k['age']+j['age'] } years old")