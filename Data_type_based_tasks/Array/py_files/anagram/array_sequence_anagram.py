"""
Anagram Check

Problem
Given two strings, check to see if they are anagrams.
An anagram is when the two strings can be written using
the exact same letters (so you can just rearrange the
letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".
"""

def anagram(s1,s2):
    str1 = sorted(s1.replace(' ', '').lower())
    str2 = sorted(s2.replace(' ', '').lower())
    return str1 == str2


def anagram2(s1,s2):
    str1 = sorted(s1.replace(' ', '').lower())
    str2 = sorted(s2.replace(' ', '').lower())

    # Edge Case Check
    if len(str1) != len(str2):
        return False

    counter = {}
    for letter in str1:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    for letter in str2:
        if letter in counter:
            counter[letter] -= 1
        else:
            counter = 1
    for k in counter:
        if counter[k] != 0:
            return False
    return True
    pass
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class AnagramTest(object):

    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('public relations','crap built on lies'),True)
        assert_equal(sol('123','1 2'),False)
        print ("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(anagram2)


