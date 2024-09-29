import math

repeat = 'y'

# keep doing it while the user wants to

while repeat == 'y':
    
    mass = 0
    angle = -1
    mu_s = -1
    slip = False

    # define function for calculating the angle of slippage based on mu_s

    def slip_angle(mu_s):
        rads = math.atan(mu_s)
        degs = math.degrees(rads)
        return degs

    # get input for the mass, angle, and mu_s:

    while mass <= 0:
        mass = float(input('Enter a mass (kilograms) greater than 0: '))
        if mass <= 0:
            print(f'Mass must be greater than 0. Please enter a new mass.')
        else: continue

    while angle < 0 or angle >= 90:
        angle = float(input('Enter an angle between 0 (inclusive) and 90 (exclusive) degrees: '))
        if angle < 0 or angle > 90:
            print(f'Improper angle entered. Please try again.')
        else: continue

    while mu_s < 0:
        mu_s = float(input('Enter a non-negative number for the coefficent of static friction: '))
        if mu_s < 0:
            print(f'Coefficient must be greater than 0. Please try again.')
        else: continue

    # if the given angle is greater than or equal to than the slippage angle, the block will slip, so turn "slip" to true

    slip_angle = slip_angle(mu_s)
    if angle >= slip_angle:
        slip = True

    # Display the inputs and whether the block will slip

    print()
    print(f'Mass: {mass} kg\nAngle: {angle} degrees\nCoeff_s: {mu_s}')
    if slip:
        print(f'At an angle of {angle} degrees, your block will slip.')
    else:
        print(f'At an angle of {angle} degrees, your block will not slip.')

    print()
    print(f'The shallowest angle at which your block will slip is {slip_angle:.1f} degrees.')

    repeat = input('Would you like to calculate another slippage? (y / n): ')
    print()