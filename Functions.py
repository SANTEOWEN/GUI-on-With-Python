
#Paramaters serves a variable we use under the function

def sing(name,  age):
    print(f"Happy birthday to {name}")
    print(f" Youre 20 {age} years old")
    
    

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due to: {due_date}")
    

# Return = statement used to end a funnction and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def devide(x, y):
    z = x / y
    return z

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
    
fulname = create_name("Owen", "Sante")

print(fulname)