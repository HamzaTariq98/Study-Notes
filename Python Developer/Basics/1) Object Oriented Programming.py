import gc

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod  #Same as defining a function outside the class
    def find_oldest_cat(list_cat):
        oldest_cat_age = 0
        oldest_cat = None

        for cat in list_cat:
            if cat.age > oldest_cat_age:
                oldest_cat = cat
                oldest_cat_age = cat.age
        return oldest_cat

    def test(self,a,b):
        return a+b

class Bengal(Cat):
    my_dict = {
        'name': 'cat name',
        'age': 5
    }
    def __repr__(self):
        return f'{self.name} is {self.age} months old.'
    def __str__(self):
        return f'{self.name} is good cat :D'
    
    def __len__(self):
        return 5
    def __call__(self):
        print(f'I am a Bengal cat named: {self.name}')
    def __getitem__(self,i):
        return self.my_dict[i]



cat1 = Cat('first_cat', 5)
cat2 = Cat('second_cat', 8)
cat3 = Bengal(name='bengola', age = 10)

list_cat = []
for obj in gc.get_objects():
    if isinstance(obj, Cat):
        list_cat.append(obj)
oldest_cat = Cat.find_oldest_cat(list_cat)
print(f'Oldest cat is {oldest_cat.name}, with age of {oldest_cat.age}', end='\n\n')

print(cat3['age'])
