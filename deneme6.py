def falling_distance():
    for i in range(10):
        time = float(input("pls enter the time: "))
        distance = 1 / 2 * 9.8 * (time ** 2)
        print(f"The flying distance is: {distance:.2f}")


falling_distance()

