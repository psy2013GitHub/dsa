#-*- encoding: utf8 -*-
__author__ = 'flappy'

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        int2eng_map = [
            ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'],
            ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'],
            ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'],
            ['Hundred', 'Thousand', 'Million']
        ]

        if num == 0: return 'Zero'

        res = []
        i = 0
        last_bit = -1
        while num % 10:

            if i == 3:
                res.append('Thousand')
                # res.append(int2eng_map[0][bit])
            elif i == 6:
                res.append('Million')

            bit = num % 10
            # print(i, bit)
            if i % 3 == 0:
                res.append(int2eng_map[0][bit])
            elif i % 3 == 1:
                if bit == 1:
                    # print(res)
                    if i > 2:
                        res[-1] = int2eng_map[1][bit * 10 + last_bit - 10]
                    else:
                        res[-1] = int2eng_map[1][bit * 10 + last_bit - 10]
                else:
                    res.append(int2eng_map[2][bit-2])
            elif i % 3 == 2:
                res.append('Hundred')
                res.append(int2eng_map[0][bit])

            i += 1
            num /= 10

            last_bit = bit

        return ' '.join(res[::-1])

def test():
    solution = Solution()
    print(solution.numberToWords(0))
    print(solution.numberToWords(123))
    print(solution.numberToWords(12345))
    print(solution.numberToWords(1234567))

if __name__ == '__main__':
    test()