#Display user prediction
print("Prediction for student time minutes and distance in km")

#Time minutes and distance km for walking 
data = [
    {"student_A_time_minutes": 5, "distance_km": 0.5}, #5 minutes of walking gives around 0.5 km
    {"student_B_time_minutes": 10, "distance_km": 1.0}, #10 minutes of walking gives around 1.0 km
    {"student_C_time_minutes" : 15, "distance_km" : 1.5}, #15 minutes of walking gives around 1.5 km
    {"student_D_time_minutes" : 20, "distance_km" : 2.0} #20 minutes of walking gives around 2.0 km
]

#STEP 1 Calculating the average for X time_minute
student_A_time_minutes = 5
student_B_time_minutes = 10
student_C_time_minutes = 15
student_D_time_minutes = 20

x = [student_A_time_minutes, student_B_time_minutes, student_C_time_minutes ,student_D_time_minutes]

#Calculation for x (X1 + X2 + X3 + X4) / 4 
x = sum(x) / 4
print(f"This is the value for x average student time minutes {x}")

#Calculating the average for Y distamces_km
student_A_distances = 0.5
student_B_distances = 1.0
student_C_distances = 1.5
student_D_distances = 2.0

y = [student_A_distances, student_B_distances, student_C_distances, student_D_distances]


#Calculation for y (Y1 + Y2 + Y3 + Y4) / 4
y = sum(y) / 4
print(f"This is the value for y average student time minutes {y}")

#STEP 2 Calculating the M slope m = (X - X) * (Y - Y)  / (X - X) ** 2
m = x(3) - x(0) * y(3) -y(0)  / x(3) - x(0) ** 2
print(m, "This is the value for m slope")

#Calculation for intercept b 
b = y - (m) * (x)
print(b, "This is the value for b")

#Ask user prediction for distance walking
x = int(input("Please enter the time distance : "))
time_distance_prediction = 0.0 + 0.1*x
print(f"your distance travelled is", time_distance_prediction, "km")