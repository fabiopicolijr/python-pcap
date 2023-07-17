class Art():
    masterpiece = 'John'

    def __init__(self):
        self.name = 'One'


art = Art()

print(len(Art().__dict__))
print(Art().__dict__)

print(len(art.__dict__))
print(art.__dict__)