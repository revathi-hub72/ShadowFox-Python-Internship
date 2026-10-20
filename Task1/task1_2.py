# TASK 2: NUMBERS

# PROGRAM 1: Number Formatting

def format_number(number, symbol):
    return format(number, symbol)

result = format_number(145, "o")
print("Program 1 Output:", result)

# PROGRAM 2: Circular Pond

radius = 84
pi = 3.14

area = pi * radius * radius
water = area * 1.4

print("Program 2 - Area of pond:", int(area))
print("Program 2 - Water required:", int(water))

# PROGRAM 3: Calculate Speed

distance = 490
time_minutes = 7

time_seconds = time_minutes * 60
speed = distance / time_seconds

print("Program 3 - Speed:", int(speed), "m/s")


