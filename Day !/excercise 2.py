name = "Muhsinah"
age = "24"
hobby = "watching movies"

def update_profile():
    global age, hobby
    age = "25"
    hobby = "reading books"
    print(f"Inside function: age is now {age} and hobby is now, {hobby}")

update_profile()