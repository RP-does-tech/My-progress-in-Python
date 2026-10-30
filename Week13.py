#Before update
girlfriend = {"name":"Aminah Arif",
              "age":23,
              "money_spent":600,
              "restaurant":"Aminah Arif"
}
print(girlfriend["name"])

print(f"Before update : {girlfriend}")

#after update
girlfriend.update({"course":"Computer Science"})

print(f"After update: {girlfriend}")

for key in girlfriend:
    print(girlfriend[key])

    