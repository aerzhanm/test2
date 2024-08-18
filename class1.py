class Hello:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f'name: {self.name}\n'
                f' age: {self.age}')


class Hi(Hello):
    def __init__(self,name, age):
        super().__init__(name,age)


person = Hi('Erzhan',  17)
print(person)