import random
import string

from utils import constants


def get_random_list(size, limit=constants.MAX_VALUE):
    answer = []
    while len(answer) < size:
        answer.append(random.randint(0, limit))
    return answer


def random_interval(init, end):
    return random.randint(init, end)


def random_string(min_size, max_size):
    len_str = random_interval(min_size, max_size)
    ans = ""
    for i in range(0, len_str):
        ans += string.ascii_letters[random_interval(0, len(string.ascii_letters) - 1)]

    return ans


def get_random_x(limit=constants.MAX_VALUE):
    return random.randint(1, limit)


def generate_possible_palindrome(size, probability=50):
    random_num = get_random_x(limit=100)

    if random_num < probability:
        palindrome = random_string(size // 2, size // 2)

        return palindrome + palindrome[::-1]
    else:
        return random_string(size, size)
