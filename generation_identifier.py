while True:
    user_birth_year = input("Hello there. What year were you born?\n")
    if len(user_birth_year) == 4 and user_birth_year.isdigit():
        break  # Exit the loop when the input is valid
    print("Invalid input. Try again.")

user_birth_year = int(user_birth_year)  # Convert the inputted string to an integer
# A dictionary that assigns a corresponding generation to each birth year range
gens = {
    'Generation Alpha': range(2010, 2026),
    'Generation Z': range(1997, 2013),
    'Millennial': range(1981, 1997),
    'Generation X': range(1965, 1981),
    'Baby Boomer': range(1946, 1965),
    'The Silent Generation': range(1928, 1946)
}
# To loop through the items in each 'gen' and find the right fit
for gen, years in gens.items():
    if user_birth_year in years:
        print(f"You are part of {gen}.")
else:
    print("Your birth year does not fall into a defined generation.")
