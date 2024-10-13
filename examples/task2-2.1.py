def example(color):
    if color == "red":
        return "This is red car"
    elif color == "yellow":
        return "This is banana"
    else:
        return None

example_result = example("blue")
if example_result is None:
    print("It's nothing")
else:
    print(f"It's something: {example_result}")
