

def get_input():
    command = input(":").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb{}").format(verb_word)
        return

    if len(command)>=2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb())


def say(noun):
    return 'You said "{}"'.format(noun)



class GameObject:
    class_name = ""
    desc=""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name]=self

    def get_desc(self):
        return self.class_name+"\n"+self.desc
# Создаем класс Гоблин с характеристиками
class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        #Изпользуется частная переменная
        self._desc = "A foul creature"
        self.health = 3
        #super возможно другой
        super().__init__(name)

#создаем свойство
@property
def desc(self):
    if self.health >=3:
        return self._desc
    elif self.health == 2:
        health_line = "It has a wound on its knee."
    elif self.health == 1:
        health_line = "Its left arm has been cut off!"
    elif self.health ==0:
        health_line = "It is dead."
        return self._desc+"\n"+health_line

@desc.setter
def desc(self,value):
    self._desc = value

def hit(noun):
    if noun in GameObject.objects:
        if noun == "goblin":
            Goblin.objects[health] -=1
            msg = "You killed the goblin!"
        else:
            msg = "You hit the {}"
    else:
        print("re")


goblin = Goblin("Gobbly")


def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here.".format(noun)

verb_dict = {"say": say,
                 "examine": examine,
             "hit": hit,
                 }

while True:
    get_input()






