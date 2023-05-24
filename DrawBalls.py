import math #gotta use a lot of equations
startDraw = "yes"
while startDraw == "yes":
#The earth has about a 9.8 sec gravitional pull so we use that to go along with the math used for the ball to roll down the hill
    GRAVITY = 9.8  
    TIME_STEP = 0.1  #seconds

    hill_height = float(input("Enter the height of the hill (in meters): "))
    initial_velocity = float(input("Enter the initial velocity of the ball (how fast the ball is in meters per second): "))

    time_of_flight = math.sqrt((2 * hill_height) / GRAVITY)

    time = 0
    speed = initial_velocity
    distance = 0

    while time < time_of_flight:
   
        time += TIME_STEP
        distance = speed * time

    # Kinetic equation we found off google
        speed = initial_velocity - (GRAVITY * time)

    # Seeing when the ball gets to the bottom of the hill
        if distance > hill_height:
            distance = hill_height
            time = time_of_flight
            speed = 0

    #in order to make it easier we just use the "round" function.
        print("Time:", round(time, 2), "s | Distance:", round(distance, 2), "m | Velocity:", round(speed, 2), "m/s")

#When the ball is done rolling
    print("The ball has finished the bottom of the hill.")
    startDraw = input("Do you want to draw another ball? ")
    