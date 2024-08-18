class Hello:
    def __init__(self, str):
        self.str = str

class Hi(Hello):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f'name: {self.name}\n'
                f' age: {self.age}')

person = Hi('Erzhan',  17)
print(person)