def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)

calculate(add = 3, muliply = 5)