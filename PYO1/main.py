



def hello_world():
    """
    helloes the world!
    """

    print("hello, world!")



hello_world()



sample1 = [1, 2, 3]
sample2 = [4, 5]



sample1.extend(sample2)

print(len(sample1))


for i in range(10, 15, 1):

    print(i, end=", ")

print("pynative"[1:3])



class Animal:

    def walk(self):

        print("animal walking")



class Dog(Animal):

    def bark(self):
        print("dog barking")


dog = Dog()

dog.walk()
dog.bark()



