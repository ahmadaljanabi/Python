def is_prime(number):
    count = 0;

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False

def run():
    number = int(input("Enter a number: "))
    if is_prime(number):
        print('is prime')
    else:
        print('is not prime')

if __name__ == '__main__':
    run()