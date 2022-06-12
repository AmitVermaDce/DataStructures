def my_generator(n):
    for i in range(n):
        yield i

value = my_generator(23)
for x in value:
    print(x)