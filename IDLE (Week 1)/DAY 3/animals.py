class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print('The ' + self.name + ' says ' + self.sound)

dog = Animal('dog','bark!')
cat = Animal('cat','meow!')
bird = Animal('bird','chirp!')

dog.speak()
cat.speak()
bird.speak()
