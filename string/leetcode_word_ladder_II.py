#-*- encoding: utf8 -*-
__author__ = 'flappy'

'''
   Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
'''

class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        transform_dict = self.transform_dict(wordlist)
        for w in wordlist:
            if self.is_transformable(endWord, w) == 1:
                transform_dict.setdefault(w, {})
                transform_dict[w].add(endWord)
        # print(transform_dict)
        if beginWord == endWord: return [[beginWord, endWord],]
        if self.is_transformable(beginWord, endWord): return [[beginWord, endWord],]

        possible_paths = []
        for w in wordlist:
            if self.is_transformable(beginWord, w) == 1:
                self.helper(w, endWord, transform_dict, [beginWord, ], possible_paths)

        print(possible_paths)

        res, min_path = [], -1
        for path in possible_paths:
            if min_path == -1 or min_path > len(path):
                min_path = len(path)
                res = []
                res.append(path)
            elif min_path == len(path):
                res.append(path)
        return res

    def helper(self, w, endWord, transform_dict, curr, possible_paths):
        '''
            如果transform_dict[w] == [], 说明无法继续走下去, 返回空
        :param w:
        :param endWord:
        :param transform_dict:
        :return:
        '''
        min_path_len, min_paths = -1, []
        path = []
        if endWord in transform_dict[w]:
            # print(w, endWord, curr)
            curr.append(w)
            curr.append(endWord)
            possible_paths.append(curr)
        else:
            count = 0
            for w1 in transform_dict[w]:
                if not (w1 in curr): # 不能往回走
                    count += 1
                    self.helper(w1, endWord, transform_dict, curr + [w], possible_paths)

    def transform_dict(self, wordslist):
        res = {}
        for i in range(len(wordslist)):
            for j in range(i):
                w1, w2 = wordslist[i], wordslist[j]
                if self.is_transformable(w1, w2) == 1:
                    res.setdefault(w1, set())
                    res.setdefault(w2, set())
                    res[w1].add(w2)
                    res[w2].add(w1)
        return res

    def is_transformable(self, w1, w2):
        if len(w1) != len(w2): return False
        count = 0
        for i, c1 in enumerate(w1):
            if c1 != w2[i]: count += 1
        return count

def test():
    solution = Solution()
    def Print(beginWord, endWord, wordlist):
        print(beginWord, endWord, wordlist, solution.findLadders(beginWord, endWord, wordlist))

    Print("hit", "cog", ["hot","dot","dog","lot","log"])
    # [
    #     ["hit","hot","dot","dog","cog"],
    #     ["hit","hot","lot","log","cog"]
    # ]
    Print('a', 'c', ['a', 'b', 'c'])
if __name__ == '__main__':
    test()
