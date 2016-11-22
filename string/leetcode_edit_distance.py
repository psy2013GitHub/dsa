
import sys

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1)==0 or len(word2)==0:
            return len(word1) + len(word2)

        state_mat = [[0,] * (len(word1)+1) for _ in range(len(word2)+1)]
        state_mat[0][0] = 0

        # !!! take care of beginning empty char, if use dp solution for string
        for i in range(1, len(word1)+1):
            state_mat[0][i] = i
        for j in range(1, len(word2)+1):
            state_mat[j][0] = j

        for j in range(len(word2)):
            for i in range(len(word1)):
                state_mat[j+1][i+1] = min(
                    state_mat[j][i+1] + 1, # case `insert`
                    state_mat[j+1][i] + 1, # case `delete`
                    state_mat[j][i] + (1 - int(word1[i]==word2[j])), # case `replace`
                )
                # print(i, j, word1[:i+1], word2[:j+1], state_mat[j][i], state_mat[j][i+1] + 1, state_mat[j+1][i] + 1, state_mat[j][i], int(word1[i]==word2[j]))

        return state_mat[-1][-1]


def test():
    solution = Solution()
    print(solution.minDistance("abc", "def"))
    print(solution.minDistance("abc", "ab"))
    print(solution.minDistance("abc", "abd"))
    print(solution.minDistance("", "ab"))


if __name__ == '__main__':
    test()