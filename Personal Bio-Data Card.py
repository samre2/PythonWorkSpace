# Assignment name: Day 3 – Mini Project: Personal Bio-Data Card

# Description: Build a program that collects a person's details and stores each piece in the appropriate Python data type, then prints a formatted bio-data card.

# Activity instructions: Write a Python program that builds a personal bio-data card. It must deliberately use a different data type for each kind of information:

#Read the full name and city as strings.
#Read age as an int and height as a float.
#Create a boolean (bool) from a yes/no question, for example "Are you a student?".
#Read the birth day, month, and year and store them together in a tuple (immutable).
#Read three hobbies and store them in a list.
#Read three languages and store them in a set, so any duplicate is dropped automatically.
#Combine all of the above into a single dictionary representing the full profile.
#Use string indexing to display the first letter of the name, and len() to report how many hobbies and unique languages there are.
#Print a formatted card, and include type() next to a few fields to confirm the data type used.
#Test it once with a duplicate language entered on purpose, and confirm the set keeps only one copy. Submit the file and your sample output.



#Personal Bio-Data Card
print("Welcome to the personal bio-data card generator!")

#Step 1 : Read personal Details
full_name = input("Enter your full name: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
is_student = input("Are you a student? (Yes/No) : ").strip().lower()=='yes'
birthday = int(input("Enter your birth day (1-31): "))
month = int(input("Enter your birth month (1-12): "))
year = int(input("Enter your birth year: "))
birthday_tuple = (birthday, month, year)
hobbies = []
for i in range(3):
    hobby = input(f"Enter hobby {i+1}: ")
    hobbies.append(hobby)
languages = set()
for i in range(3):
    language = input(f"Enter language {i+1}: ")
    languages.add(language)

    #Step 2 : Combine into a dictinoary

    profile = {
        "Full Name": full_name,
        "City": city,
        "Age": age,
        "Height": height,
        "Is Student": is_student,
        "Birthday": birthday_tuple,
        "Hobbies": hobbies,
        "Languages": languages

    }


    #Step 3 : Display the bio-data card
    print("\n--- Personal Bio-Data Card ---")
    for key, value in profile.items():
        print(f"{key}: {value}")

    # Display additional information
    print(f"\nFirst letter of the name: {profile['Full Name'][0]}")
    print(f"Number of hobbies: {len(profile['Hobbies'])}")
    print(f"Number of unique languages: {len(profile['Languages'])}")


