'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count = 0):
    th = 'th'
    location = word.find(th)
    if location == -1:
        return count
    else:
        count += 1
    return count_th(word[location + 1:], count)
