# from base_person import *
import base_person
import warrior as war

man = base_person.Person("Олег", 30, 180)
man.description_person()

warrior = war.Warrior("Конан", 25, 200)
print(f'Нашего воина зовут: {warrior.description_person()}')
