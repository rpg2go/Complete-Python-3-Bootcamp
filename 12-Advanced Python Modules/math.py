import math
import random

def math_functions():
    value = 4.35

    print(value)
    print(math.floor(value))
    print(math.ceil(value))
    print(round(value))
    print(math.pi)
    print(math.nan)
    print(math.e)
    print(math.log(100, 10))

    print(math.sin(10))
    print(math.degrees(math.pi / 2))
    print(math.radians(180))


def random_functions():
    print(random.randint(0, 100))

    #print(random.seed(101))
    print(random.randint(0, 100)) #74
    print(random.randint(0, 100)) #24
    print(random.randint(0, 100)) #69
    print(random.randint(0, 100)) #45

    mylist = list(range(0, 20))
    print(mylist)
    print(random.choice(mylist))

    #sample with replacement
    print(random.choices(population=mylist, k=10))

    # sample without replacement
    print(random.sample(population=mylist, k=10))

    print("as is mylist:")
    print(mylist)
    print("shuffle mylist:")
    random.shuffle(mylist)
    print(mylist)

    print(random.uniform(a=0, b=100))

    print(random.gauss(mu=0, sigma=100))

if __name__ == "__main__":
    #math_functions()
    random_functions()