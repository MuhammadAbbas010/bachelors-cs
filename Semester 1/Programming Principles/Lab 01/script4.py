mass = float(input("Enter the mass of your object (kg) : "))
velocity = float(input("Enter the velocity of your object (m/s) : "))

momentum = mass * velocity
KE = 0.5 * mass * (velocity * velocity)

print(f"The momentum of your object is = {momentum}(kg.m/s) and its kinectic energy is = {KE}(J)")
