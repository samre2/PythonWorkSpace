#Cinema Ticket Pricing System

print("Welcome to the Cinema Ticket Pricing System!")

#Step 1 : Reading Customer Details

age = int(input("Enter the customer's age: "))
day_of_week = input("Enter the day of the week: ").strip().lower()
is_member = input("Is the customer a member? (Yes/No): ").strip().lower() == 'yes'  # Convert to boolean

#Step 2 : Set base price by age

if age < 5:
    base_price = 0
    category = "Child (Free)"
elif age <= 18:
    base_price = 50 #Assuming full price is Rs. 100, so 50% off is 50
    category = "Minor"
elif age >= 60:
    base_price = 70 #Assuming full price is Rs. 100, so 30% off is 70
    category = "Senior"
else:
    base_price = 100 #Full price
    category = "Adult"

#Step 3 : Apply extra discount for members on weekdays

weekdays = {"monday", "tuesday", "wednesday", "thursday", "friday"}

if is_member  and day_of_week in weekdays:       
    discount =  base_price * 0.10 #If the customer is a member and it's a weekday, apply a 10% discount
else:
    discount = 0
final_price: float = base_price - discount #Calculate the final price after applying the discount

#Step 4 : Decide popcorn offer using a nested if

if final_price == 0:
    
        popcorn_offer = "No popcorn offer (Free entry)"
    
else:
  if is_member:
        popcorn_offer = "Free large popcorn for members!"
  else:
        popcorn_offer = "No popcorn offer."


#Step 5: Closing message using ternary expression

closing_message = "Free entry!" if final_price == 0 else "Enjoy the show!"

#Step 6 : Print summary
print("\n--- Ticket Summary ---")
print(f"Category: {category}")
print(f"Base Price: Rs. {base_price:.2f}")
print(f"Discount Applied: Rs. {discount}")
print(f"Popcorn Offer: {popcorn_offer}")
print(f"Final Price: Rs. {final_price:.2f}")
print(f"Closing Message: {closing_message}")

#Run the program for at least two different customers to confirm the branches behave correctly.


