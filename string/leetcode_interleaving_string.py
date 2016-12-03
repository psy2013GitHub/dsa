#-*- encoding: utf8 -*-

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        self.s1, self.s2, self.s3 = s1, s2, s3
        self.mem = {}
        self.iter = 0
        return self.helper(0, 0, 0)

    def helper(self, i, j, k):
        # print(self.iter,i,j,k,len(self.s1),len(self.s2),len(self.s3),self.s3[k],self.s1[i],self.s2[j])
        self.iter += 1
        # if self.iter > 50:
        #     raise ValueError
        if k >= len(self.s3):
            if i >= len(self.s1) and j >= len(self.s2):
                self.mem[(i,j,k)] = True
                return True
            self.mem[(i,j,k)] = False
            return False

        res = self.mem.get((i, j, k))
        if res:
            return res

        if i >= len(self.s1):
            if self.s3[k] != self.s2[j]:
                self.mem[(i, j, k)] = False
                return False
            res = self.mem.get((i, j + 1, k + 1), -1)
            if res == -1:
                res = self.helper(i, j+1, k+1)
                self.mem[(i, j, k)] = res
            return res

        if j >= len(self.s2):
            if self.s3[k] != self.s1[i]:
                self.mem[(i, j, k)] = False
                return False
            res = self.mem.get((i + 1, j, k + 1), -1)
            if res == -1:
                res = self.helper(i + 1, j, k+1)
                self.mem[(i, j, k)] = res
            return res

        x1, x2 = False, False
        if (i < len(self.s1) and self.s3[k] == self.s1[i]):
            x1 = self.mem.get((i + 1, j, k + 1), -1)
            if x1 == -1:
                x1 = self.helper(i+1, j, k+1)
            # x1 = self.mem.get((i+1,j,k+1), self.helper(i+1, j, k+1))
        if not x1 and (j < len(self.s2) and self.s3[k] == self.s2[j]):
            x2 = self.mem.get((i, j+1, k + 1), -1)
            if x2 == -1:
                x2 = self.helper(i, j+1, k+1)

        self.mem[(i,j,k)] = x1 or x2
        # print('.....end....')
        return x1 or x2


def test():
    solution = Solution()
    def Print(s1, s2, s3):
        print(s1, s2, s3, solution.isInterleave(s1, s2, s3))

    # Print("aabcc", "dbbca", "aadbbcbcac")
    # Print("aabcc", "dbbca", "aadbbbaccc")
    Print("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
"babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
"babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab")

if __name__ == '__main__':
    test()