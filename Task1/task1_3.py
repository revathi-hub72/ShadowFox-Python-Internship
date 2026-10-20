# Task 3: Justice League List

heroes = [
    "Superman", "Batman", "Wonder Woman",
    "Flash", "Aquaman", "Green Lantern"
]

# 1. Count members
print("1. Total members:", len(heroes))
print(heroes)

# 2. Add Batgirl and Nightwing
heroes.extend(["Batgirl", "Nightwing"])
print("\n2. After adding members:", heroes)

# 3. Move Wonder Woman to the beginning
heroes.remove("Wonder Woman")
heroes.insert(0, "Wonder Woman")
print("\n3. Wonder Woman at beginning:", heroes)

# 4. Put Green Lantern between Aquaman and Flash
heroes.remove("Green Lantern")
position = heroes.index("Aquaman") + 1
heroes.insert(position, "Green Lantern")
print("\n4. Updated order:", heroes)

# 5. Replace with new members
heroes = [
    "Cyborg", "Shazam", "Hawkgirl",
    "Martian Manhunter", "Green Arrow"
]
print("\n5. New list:", heroes)

# 6. Sort alphabetically
heroes.sort()
print("\n6. Sorted list:", heroes)
print("Leader at index 0:", heroes[0])


