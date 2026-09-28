names = ["Naruto is such a lame guy"
         "Sakura is so such dumbass"
         "Sasuke is so sigma and cool"
]

query = "lame"
query1 = "cool"
query2 = "mamasita"

match_count = 0

print("\n==========")

for name in names :
    if query.lower() in name.lower() :
        print("query found")
    
    else :
        print("query are not found")
    
    match_count == 0

print("\n===========")

for name in names : 
    if query1.lower() in name.lower() :
        print("query found")

    else :
        print("query are not found")

    match_count == 0

print("\n===========")

for name in names :
    if query2.lower() in name.lower() :
        print("query found")
    else : 
        print("query are not found")

    match_count == 0