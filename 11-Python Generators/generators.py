def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result


def create_cubes_v2(n):
    for x in range(n):
        yield x**3


def get_fibonacci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


def get_fibonacci_v0(n):
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a, b = b, a+b
    return output


def simple_gen():
    for x in range(3):
        yield x

# print("create cubes v1")
# for x in create_cubes(10):
#     print(x)


# print("create cubes v2")
# for x in create_cubes_v2(10):
#     print(x)


print(list(create_cubes_v2(10)))

print("Fibonacci implementation using generators")
for number in get_fibonacci(10):
    print(number)

print("Classic Fibonacci implementation")
for number in get_fibonacci_v0(10):
    print(number)

for number in simple_gen():
    print(number)

g = simple_gen()


# iterate through yield value
print(next(g))
print(next(g))
print(next(g))
#print(next(g))

s = 'hello'
for letter in s:
    print(letter)

s_iter = iter(s)
print(next(s_iter))