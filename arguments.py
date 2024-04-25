def greet(name, message):
    print(f"Hello, {name}! {message}")

greet("Alice", "How are you?")
greet(message="Nice to meet you!", name="Bob")


def greet(name, message="Good morning!"):
    print(f"Hello, {name}! {message}")

greet("Charlie")  # Output: Hello, Charlie! Good morning!


def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")



def greet(**kwargs):
    for name, message in kwargs.items():
        print(f"Hello, {name}! {message}")

greet(Alice="Good morning!", Bob="How are you?")


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")


def greet(name, **kwargs):
    message = kwargs.get("message", "Hello!")
    print(f"{message} {name}")

greet("Alice", message="Good morning!")


def print_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

info = {"name": "Alice", "age": 25, "city": "New York"}
print_info(**info)
