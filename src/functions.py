def greet(name: str) -> str:
    return f"Hello, {name}!"

def is_even(n: int) -> bool:
    return n % 2 == 0

print(greet("Ali"))
print("10 even?", is_even(10))
print("7 even?", is_even(7))
