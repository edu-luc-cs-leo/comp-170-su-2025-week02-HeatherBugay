# Problem 1: Function to greet a person
def greet(name):
    return f"Hello {name}. How are you?"

# Problem 2: Greet a few friends
my_friends = ["Luke", "Leia", "Han"]
def greet_friends(friends):
    for friend in friends:
        print(greet(friend))

# Problem 3: Solve an equation
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("no real solutions")
    else:
        x_1 = (-b - math.sqrt(discriminant)) / (2 * a)
        x_2 = (-b + math.sqrt(discriminant)) / (2 * a)
        print(f"x_1 = {x_1}, x_2 = {x_2}")