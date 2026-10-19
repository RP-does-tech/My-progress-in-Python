#Display user prediction
print("Prediction for student time minutes and distance in km")

#STEP 1 Calculating the average for X time_minutes
Students = [5, 10, 15, 20]

#Calculation for x average
x = sum(Students) / 4
print(f"This is the value for x average = {x} minutes")

#Calculating the average for Y distamces_km
Students_distances = [0.5, 1.0, 1.5, 2.0]

#Calculation for y average
y = sum(Students_distances) / 4
print(f"This is the value for y average = {y} km")

#Calculation for the M slope with the formula M = (x-x) * (y - y) / (x - x) ** 2
m = (max(Students) - min(Students)) * (max(Students_distances) - min(Students_distances)) / (max(Students) - min(Students)) ** 2
print(f"This is the slope M = {m}")

#Calculation for B Intercept
b = y - m * x
print(f"This is the value for intercept B = {b}")

#Ask user prediction for distance walking
x = int(input("Please enter the time distance in minutes : "))
time_distance_prediction = b + m*x
print(f"Your distance travelled is", time_distance_prediction, "km")




