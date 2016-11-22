#-*- encoding: utf8 -*-

# 基本方法：
#    双指针法：start/end，找到所有满足条件得字符串
#    对每个满足条件得字符串：先找到包含目标得[start, end)， 再截短
# 主要解决两个问题：
# 1，何时开始比较minLen ?
# 2, 怎么截断前面不需要得字符 ?

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_counter = dict()
        for c in t:
            t_counter.setdefault(c, 0)
            t_counter[c] += 1

        counter = dict()
        start, end, min_start, min_end, min_len, missing = 0, 0, 0, 0, -1, len(t)
        while end < len(s):
            c = s[end]
            if c in t:
                counter.setdefault(c, 0)
                counter[c] += 1
                if counter[c] <= t_counter[c]:
                    missing -= 1
                # print('missing:', missing, counter[c], t_counter[c], c)
                if missing == 0:
                    i = start
                    print('%d %s' % (start, s[start]))
                    while i < end and ((not t_counter.has_key(s[i])) or counter.get(s[i], 0) > t_counter[s[i]]):
                        print('\t%d %s %d %d %d' % (i, s[i], t_counter.has_key(s[i]), counter.get(s[i], 0), t_counter.get(s[i], -1)))
                        if counter.has_key(s[i]):
                            counter[s[i]] -= 1
                        i += 1
                    start = i
                    print('\t%d %s' % (start, s[start]))
                    curr_len = end + 1 - start
                    print('match_counter:', end, c, curr_len, start, end, s[start:end+1])
                    print('str(counter): ' + str(counter))
                    if min_len == -1 or curr_len < min_len:
                        print('hit min...')
                        min_start, min_end, min_len = start, end, curr_len

                    counter[s[start]] = counter.get(s[start], 1) - 1
                    missing += 1
                    start += 1
            end += 1

        if min_len > 0:
            return s[min_start:min_end+1]
        else:
            return ""


def test():
    solution = Solution()
    print(solution.minWindow("a", "a"))
    print(solution.minWindow("ADOBECODEBANC", "ABC"))

if __name__ == '__main__':
    test()