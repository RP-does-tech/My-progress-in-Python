#Student information
student_name = {
    "name" : "Davinci",
    "age" : 17,
    "programme" : "O level",
    "school" :  "Sekolah Menengah Sultan Sharif Ali",
    "address" : "Kampong Tanah Jambu",
}

query = "Davinci"
query1 = "Sekolah Menengah Sultan Sharif Ali"
query2 = "Tanah Jambu"
query3 = 17

match_count = 0

print("\n===Find the query===")
if query.lower() in str(student_name["name"]).lower() :
    print("query is found")
    match_count += 1
else :
    print("query is not found")


print("\n===Find the query1===")
if query1.lower() in str(student_name["school"]).lower() :
    print("query is found")
    match_count += 1
else : 
    print("query is not found")


print("\n===Find the query2===")
if query2.lower() in str(student_name["address"]).lower() :
    print("query is found")
    match_count += 1
else : 
    print("query is not found")


print("\n===Find the query3===")
if query3 == student_name["age"] :
    print("query is found")
    match_count += 1
else : 
    print("query is not found")

print("\n=== Match count ===")
print("The match count is :", match_count)

#Counting the words for the
print("\n=== Words Count ===")
print("The words count is:", len(student_name))