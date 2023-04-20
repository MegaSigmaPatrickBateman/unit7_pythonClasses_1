#my_pet_1 = 'pet'
#my_pet_1_type = 'cat'
#my_pet_1_noise ='meow'
#my_pet_1_full_name ='Meowskers'

#my_pet_2 ='pet'
#my_pet_2_type ='cat'
#my_pet_2_noise ='meow'
#my_pet_2_full_name ='discord kitten'

#my_pets= [my_pet_1, my_pet_2]
#for pet in my_pets:
   # print(my_pet_1_full_name)
   # print(my_pet_2_full_name)
    #
class Pizza:
    def __init__ (self ,toppingA, toppingB, toppingC):
        self.toppingA = toppingA
        self.toppingB = toppingB
        self.toppingC = toppingC

ingredients = Pizza('Cheese', ' pepperoni', ' sausage')
print(ingredients.toppingA)
print(ingredients.toppingB)
print(ingredients.toppingC)