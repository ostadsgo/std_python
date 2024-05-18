x = 1
f = 1.1

s = "Helllo"
l = [1, 2, 3, 4, 5, "hello"]

new_s = s[0] + " " + s[1]

r = l[0] + l[1]

d = {"name": "John", "age": 25}

contacts = [
    {"name": "John Doe", "phone": "12123123"},
    {"name": "Kate Doe", "phone": "345345435"},
    {"name": "Michel Doe", "phone": "34543543"},
]


item_to_del = "Kate Doe"
i = 0
# for row in contacts:
#     if row["name"] == item_to_del:
#         contacts.pop(i)
#         break
#     i += 1


# myfile = open("mydata.csv", "w")
# for item in contacts:
#     myfile.write(item["name"] + "," + item["phone"] + "\n")
# myfile.close()


def head(myfile, n):
    data = []
    for i in range(n):
        row = myfile.readline()
        data.append(row)

    return data


myfile = open("mydata.txt", "r")
x = head(myfile, 3)
print(x)

myfile.close()

s = "hello"


print("hello world")

