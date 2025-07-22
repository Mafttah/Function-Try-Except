def register_user():
    while True:
            name = input("Enter your name: ").strip()
            if not name:
                print("Name cannot be empty!")
                print("Going back to the start.")
                continue
            if not name.isalpha():
                print("Please enter your name using letters only.")
                print("Going back to the start.")
                continue
            if len(name) >= 7:
                print("Please enter a shorter name.")
                continue
            break
    
    email = input("Enter your email: ").strip()
    if not email:
            return("Email cannot be empty!")   # Fast fail
    if "@" not in email:
        return("Invalid email format!")  # Fast fail

    print(f"User registered: {name} with email {email}")

register_user()


def check_age():
    age = input("Enter your age: ").strip()
    try:
        age= int(age)
    except ValueError:
        print("Age must be an integer!")
        return
    
    if age <= 0 or age >= 80:
        print("Age must be a positive integer and less than 80!")        
        return

    print(f"Age is valid: {age}")

check_age()