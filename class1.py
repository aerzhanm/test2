class Hello:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return  self.name


class Hi(Hello):
    def __init__(self, name):
        super().__init__(name)




person = Hi('Erzhan')
print(person)