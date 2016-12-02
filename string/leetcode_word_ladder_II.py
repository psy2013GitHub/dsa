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
         # Write your code here
        start, end, dict = beginWord, endWord, wordlist
        dict.add(start)
        dict.add(end)

        def buildPath(path,word):
            if len(preMap[word]) == 0:
                result.append([word] + path)
                return
            path.insert(0,word)
            for w in preMap[word]:
                buildPath(path,w)
            path.pop(0)

        length = len(start)
        preMap = {}
        for word in dict:
            preMap[word] = []
        result = []
        cur_level = set()
        cur_level.add(start)

        # bfs 建立前向映射
        while True:
            pre_level = cur_level
            cur_level = set()
            for word in pre_level:
                dict.remove(word) # 出现过得词就删掉,防止重复出现,tle_findLadders就没有解决好。。。
            for word in pre_level:
                for i in range(length):
                    left = word[:i]
                    right = word[i+1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c != word[i]:
                            nextWord = left + c + right
                            if nextWord in dict:
                                preMap[nextWord].append(word)
                                cur_level.add(nextWord)
            if len(cur_level) == 0:
                return []
            if end in cur_level:
                break
        print(preMap)
        buildPath([],end)
        return result

    def tle_findLadders(self, beginWord, endWord, wordlist):
        """
            tle 了。。。
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        wordlist = list(wordlist)
        transform_dict = self.transform_dict(wordlist)
        for w in wordlist:
            if self.is_transformable(endWord, w) == 1:
                transform_dict.setdefault(w, {})
                transform_dict[w].add(endWord)
        # print(transform_dict)
        if beginWord == endWord: return [[beginWord, endWord],]
        if self.is_transformable(beginWord, endWord)==1: return [[beginWord, endWord],]

        possible_paths = []
        for w in wordlist:
            if self.is_transformable(beginWord, w) == 1:
                self.helper(w, endWord, transform_dict, [beginWord, ], possible_paths)

        print('possible_paths', possible_paths)

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
        print(beginWord, endWord, wordlist, solution.tle_findLadders(beginWord, endWord, wordlist))

    Print("hit", "cog", {"hot","dot","dog","lot","log"})
    # [
    #     ["hit","hot","dot","dog","cog"],
    #     ["hit","hot","lot","log","cog"]
    # ]
    Print('a', 'c', {'a', 'b', 'c'})
if __name__ == '__main__':
    test()
