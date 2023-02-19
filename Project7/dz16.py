def say_hi(name: str, age: int):
    return "Привет, меня зовут {} и мне {} лет.".format(name, age)
name = "Иван"
age = 30
greeting = say_hi(name, age)
print(greeting)
