# Personal Bio-Data Card
print("Welcome to the personal bio-data card generator!")

#Step 1 : Read personal Details
full_name = input("Enter your full name: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
is_student = input("Are you a student? (Yes/No) : ").strip().lower()=='yes' # Convert the input to a boolean value (True for 'yes', False for 'no')
birthday = int(input("Enter your birth day (1-31): "))
month = int(input("Enter your birth month (1-12): "))
year = int(input("Enter your birth year: "))
birthday_tuple = (birthday, month, year)
hobbies = []
for i in range(3):
    hobby = input(f"Enter hobby {i+1}: ")
    hobbies.append(hobby)                                               # Use a list to store hobbies as they can be repeated
languages = set()
for i in range(3):
    language = input(f"Enter language {i+1}: ")
    languages.add(language)                                             # Use a set to store languages to ensure uniqueness

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
}                                                                       # Create a dictionary to store all the personal details


#Step 3 : Display the bio-data card
print("\n--- Personal Bio-Data Card ---")
for key, value in profile.items():
    print(f"{key}: {value} ({type(value).__name__})")                   # Display the key and value in a formatted way    

 # Display additional information
print(f"\nFirst letter of the name: {profile['Full Name'][0]}")         # Access the first letter of the full name
print(f"Number of hobbies: {len(profile['Hobbies'])}")                  # Calculate the number of hobbies using the length of the hobbies list
print(f"Number of unique languages: {len(profile['Languages'])}")       # Calculate the number of unique languages using the length of the languages set


