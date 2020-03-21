def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def positive_sum(arr):
    result = 0
    for i in arr:
        if i > 0:
            result += i
    return result


def remove_char(s):
    return s[1:-1]


def getCount(inputStr):
    num_vowels = 0
    vowel_letters = ('a', 'e', 'i', 'o', 'u')
    for letter in inputStr:
        if letter in vowel_letters:
            num_vowels += 1
    return num_vowels


def get_middle(s):
    for letters in s:
        if len(s) >= 3:
            s = s[1:-1]
    return s


def xo(s):
    counter_x = 0
    counter_o = 0
    for letter in s:
        if letter == 'x' or letter == 'X':
            counter_x += 1
        elif letter == 'o' or letter == 'O':
            counter_o += 1
    if counter_o == counter_x:
        return True
    else:
        return False


def persistence(n):
    if (n < 10):
        return 0
    times_done = 0
    while n >= 10:
        solution = 1
        str_number = str(n)
        for x in range(len(str_number)):
            solution *= int(str_number[x])
        times_done += 1
        n = solution
    return times_done


def solution(number):
    solution = 0
    for i in range(1, number):
        if (i % 3 == 0) or (i % 5 == 0):
            solution += i
    return solution


def digital_root(n):
    while n >= 10:
        solution = 0
        str_number = str(n)
        for x in range(len(str_number)):
            solution += int(str_number[x])
        n = solution
    return n




def find_outlier(integers):
    odd_num = 0
    even_num = 0
    count_odd = 0
    count_even = 0
    for num in range(len(integers)):
        if (integers[num] % 2 != 0):
            odd_num = integers[num]
            count_odd += 1
        else:
            even_num = integers[num]
            count_even += 1
    if (count_even > count_odd):
        return odd_num
    else:
        return even_num


def spin_words(sentence):
    words = sentence.split()
    number_of_words = len(words)
    i = 0
    while (number_of_words > 0):
        if (len(words[i]) >= 5):
            words[i] = ''.join(reversed(words[i]))
        i += 1
        number_of_words -= 1
    return " ".join(words)


def find_it(seq):
    for i in range(0, len(seq)):
        count = 0
        for j in range(0, len(seq)):
            if (seq[i] == seq[j]):
                count += 1
        if (count % 2 != 0):
            return seq[i]
    return -1


def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split()]
    return str(max(numbers)) + ' '+str(min(numbers))


    # return str(numbers_compare[0])+ ' ' +  str(numbers_compare[len(numbers_compare-1)])
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))  # , "542 -214"))

# programming language:

# java: 1387
# javascript: 966
# .NET: 703º
# python: 539

# git
# openCV - sistemas de visión artificial
# curso de EPLAN
# openGL
# python
# C++ and SQL
