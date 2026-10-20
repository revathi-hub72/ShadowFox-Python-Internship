# Task 4: If Condition

# Program 1: BMI Calculator
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

bmi = weight / (height * height)
print("BMI:", round(bmi, 2))

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")

# Program 2: City and Country
cities = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

city = input("\nEnter a city: ").strip().lower()
country_found = False

for country, city_list in cities.items():
    if city in [c.lower() for c in city_list]:
        print(city.title(), "belongs to", country)
        country_found = True
        break

if not country_found:
    print("City not found in the given list.")

# Program 3: Check Two Cities
city1 = input("\nEnter the first city: ").strip().lower()
city2 = input("Enter the second city: ").strip().lower()

country1 = None
country2 = None

for country, city_list in cities.items():
    if city1 in [c.lower() for c in city_list]:
        country1 = country
    if city2 in [c.lower() for c in city_list]:
        country2 = country

if country1 is None or country2 is None:
    print("One or both cities are not in the given list.")
elif country1 == country2:
    print("Both cities belong to", country1)
else:
    print("The cities belong to different countries.")


