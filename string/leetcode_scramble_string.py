#-*- encoding: utf8 -*-
__author__ = 'flappy'

class Solution(object):
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2): # prunning
            return False
        for i in xrange(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
                (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        return False

def test():
    print(Solution().isScramble('great', 'rgeat'))

if __name__ == '__main__':
    test()