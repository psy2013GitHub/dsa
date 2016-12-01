#-*- encoding: utf8 -*-
__author__ = 'flappy'
'''
    Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
'''

class Solution(object):
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_chars = [], [], 0
        for w in words:
            if num_of_chars + len(w) + len(cur) > maxWidth: # 单词总长度, 现在w长度, 至少得空格长度
                for i in range(maxWidth - num_of_chars):
                    cur[i%(len(cur)-1 or 1)] += ' ' # 轮转加' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur.append(w)
            num_of_chars += len(w)
        res.append(' '.join(cur).ljust(maxWidth))
        return res

def test():
    solution = Solution()
    print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))


if __name__ == '__main__':
    test()