#Time minutes and distance km for walking 
data = [
    {"student_A_time_minutes": 5, "distance_km": 0.5}, #5 minutes of walking gives around 0.5 km
    {"student_B_time_minutes": 10, "distance_km": 1.0}, #10 minutes of walking gives around 1.0 km
    {"student_C_time_minutes" : 15, "distance_km" : 1.5}, #15 minutes of walking gives around 1.5 km
    {"student_D_time_minutes" : 20, "distance_km" : 2.0} #20 minutes of walking gives around 2.0 km
]

#STEP 1 Calculating the average for X time_minutes
X1 = 5
X2 = 10
X3 = 15
X4 = 20

#Calculation for x (X1 + X2 + X3 + X4) / 4 
x = (5 + 10 + 15 + 20) / 4
print(x, "This is the value for X average")

#Calculating the average for Y distamces_km
Y1 = 0.5
Y2 = 1.0
Y3 = 1.5
Y4 = 2.0

#Calculation for y (Y1 + Y2 + Y3 + Y4) / 4
y = (0.5 + 1.0 + 1.5 + 2.0) / 4
print(y, "This is the value for y average")

#STEP 2 Calculating the M slope with the formula m = (X - X) * (Y - Y)  / (X - X) ** 2
m = (20 - 5) * (2.0 - 0.5) / (20 - 5) ** 2
print(m, "This is the value for m slope")

#STEP 3 Calculating the B
b = y - (m) * (x)

#Calculation for intercept b 
b = 1.25 - (0.1) * (12.5)
print(b, "This is the value for b")

#Ask user prediction for distance walking
x = int(input("Please enter the time distance : "))
time_distance_prediction = b + m*x
print(f"your distance travelled is", time_distance_prediction, "km")




