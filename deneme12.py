def kinetic_energy():
    mass = int(input("pls enter the mass: "))
    velocity = int(input("pls enter the velocity: "))
    kinetic__energy = (1/2) * mass * (velocity**2)
    return kinetic__energy


result = kinetic_energy()
print(f"your kinetic energy is: {result} ")
