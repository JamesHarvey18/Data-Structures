alphabet = set('abcdefghijklmnopqrstuvwxyz')


def is_pangram(string):
    return set(string.lower()) >= alphabet


string = 'the quick brown fox jumps over the lazy dog'

print(is_pangram(string))
print('aa' in alphabet)
