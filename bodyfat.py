import math

# The US Navy formula uses Imperial units, and there are log10's involved.
# So we must convert cm into inches.

def inch(x):
    xinch = 0.3937*x
    return xinch

while True:
    sex = input("Enter your sex, m for male, f for female: ").casefold()

    if sex == "m" or sex == "male":
        wgh = float(input("Your weight in kg: "))
        hgt = inch(float(input("Your height in cm: ")))
        abd = inch(float(input("Your belly circumference in cm: ")))
        nck = inch(float(input("Your neck circumference in cm: ")))
        print("")
        bf = (86.010*math.log10(abd-nck))-(70.041*math.log10(hgt))+36.76
        print("Your body fat percentage is {:.2f}%".format(bf))

# The body fat percentage is unitless and there are no logs involved,
# so any unit of mass can be used.

        wgh_bf = wgh*(bf/100)
        wgh_lean = wgh - wgh_bf
        print("Body fat weight: {:.2f} kg".format(wgh_bf))
        print("Lean body weight: {:.2f} kg".format(wgh_lean))
        print("")

    elif sex == "f" or sex == "female":
        wgh = float(input("Your weight in kg: "))
        hgt = inch(float(input("Your height in cm: ")))
        abd = inch(float(input("Your belly circumference in cm: ")))
        hip = inch(float(input("Your hip circumference in cm: ")))
        nck = inch(float(input("Your neck circumference in cm: ")))
        print("")
        bff = (163.05*math.log10(abd+hip-nck))-(97.684*math.log10(hgt))-78.387
        print("Your body fat percentage is {:.2f}%".format(bff))

        wgh_bff = wgh*(bff/100)
        wgh_lean = wgh - wgh_bff
        print("Body fat weight: {:.2f} kg".format(wgh_bff))
        print("Lean body weight: {:.2f} kg".format(wgh_lean))
        print("")

    done = input("Are you done? Enter 'done' if you are. ").casefold()
    if done == "done":
        break
