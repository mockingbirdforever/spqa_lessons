
def fizz_buzz(n):
    for i in range(0, n):
        if i % 3 == 0 and i % 5 == 0:
            print('FizBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


fizz_buzz(18)
