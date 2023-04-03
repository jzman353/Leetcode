import random


def list_with_16_digits_with_random_numbers_between_1_and_99():
    for i in range(20):
        return random.sample(range(1, 100), 16)

#print(list_with_16_digits_with_random_numbers_between_1_and_99())

#generate square matrixes of size n with either 0's or 1's
def generate_matrix(n):
    return [[random.randint(0, 1) for i in range(n)] for j in range(n)]

"""for i in range(3,5):
    for j in range(3):
        print(generate_matrix(i))"""

def list_with_n_digits_with_random_numbers_between_1_and_9(n):
    return random.sample(range(1, 10), n)

#make length of list between 1 and 7 and print 16 results
for i in [random.randint(1, 7) for j in range(16)]:
    print(list_with_n_digits_with_random_numbers_between_1_and_9(i))