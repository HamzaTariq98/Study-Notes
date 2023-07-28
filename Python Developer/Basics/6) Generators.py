# Std generator function
def generator_function(num):
    for i in range(num):
        yield i

# Creating iter object
def iter_object(iterable):
    iterable = iter(iterable)
    while True:
        try:
            print(next(iterable))
        except StopIteration:
            pass


#Create our own generator class object
class MyGen:
  current = 0
  def __init__(self, first, last):
    self.first = first
    self.last = last
    MyGen.current = self.first #this line allows us to use the current number as the starting point for the iteration

  def __iter__(self):
    return self

  def __next__(self):
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration

gen = MyGen(1,4)
for i in gen:
    print(i)