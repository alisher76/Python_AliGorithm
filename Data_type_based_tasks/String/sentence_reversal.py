"""
Sentence Reversal
Problem
Given a string of words, reverse all the words. For example:
Given:
'This is the best'
Return:
'best the is This'
As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
'  space here'  and 'space here      '
both become:
'here space'
"""

def rev_word(s):
    return ' '.join(s.split()[::-1])

print(rev_word('Hi John,   are you ready to go?'))

# 'go? to ready you are John, Hi'

def rev_word2(s):

    words = []
    length = len(s)
    spaces = [' ']

    i = 0

    # while index is less than length of string
    while i < length:

        if s[i] not in spaces:

            word_start = i

            while i < length and s[i] not in spaces:

                i += 1

            words.append(s[word_start:i])
        i += 1

    return " ".join(reversed(words))

print(rev_word2('Hi John,   are you ready to go?'))