def add(a, b):
    return a + b

def get_message(name):
    return f"Hello, {name}!"

def test_add():
    assert add(2, 3) == 5

def test_get_message():
    assert get_message("David") == "Hello, David!"