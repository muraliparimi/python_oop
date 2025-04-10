import random
import string

def infinite_id_generator():
    while True:
        yield ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def main():
    id_generator = infinite_id_generator()

    for _ in range(5):
        print(next(id_generator))


if __name__ == '__main__':
    main()
