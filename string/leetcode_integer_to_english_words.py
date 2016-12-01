#-*- encoding: utf8 -*-
__author__ = 'flappy'

class Solution(object):
    def numberToWords(self, num):
        """
            每3位作为一个处理单元, 单元间用'Thousand', 'Million', 'Billion' 连接
            注意得是:
                    处理单元内十位为0或 9<<20, 20<<100得特殊情况
                    'Thousand', 'Million', 'Billion' 连接处100000得特殊情况
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
        while num > 0:

            # print(i, res, last_bit)
            if i == 3:
                res.append('Thousand')
            elif i == 6:
                if last_bit == 0 and (res[-1] == 'Zero' or res[-1] == 'Thousand'):
                    res[-1] = 'Million'
                else:
                    res.append('Million')
            elif i == 9:
                if last_bit == 0 and (res[-1] == 'Zero' or res[-1] == 'Thousand' or res[-1] == 'Million'):
                    res[-1] = 'Billion'
                else:
                    res.append('Billion')

            bit = num % 10
            # print(i, bit)
            if i % 3 == 0:
                res.append(int2eng_map[0][bit])
            elif i % 3 == 1:
                if bit == 0:
                    pass
                elif bit == 1:  # 10 <= <20
                    res[-1] = int2eng_map[1][bit * 10 + last_bit - 10]
                else: # 20 <
                    if last_bit == 0:
                        res[-1] = int2eng_map[2][bit-2]
                    else:
                        res.append(int2eng_map[2][bit-2])
            elif i % 3 == 2:
                if bit == 0:
                    if last_bit == 0 and res[-1]=='Zero': # ...000得形式
                        # res = res[:-1]
                        del res[-1]
                elif last_bit == 0:
                    if res[-1] == 'Zero': # ...x00得形式
                        res[-1] = 'Hundred'
                    else:
                        res.append("Hundred") # ...x0z得形式
                    res.append(int2eng_map[0][bit])
                else:
                    res.append('Hundred') # ...xyz得形式
                    res.append(int2eng_map[0][bit])

            i += 1
            num /= 10

            last_bit = bit

        return ' '.join(res[::-1])

def test():
    solution = Solution()
    def Print(num):
        print(num, solution.numberToWords(num))
    Print(0)
    Print(123)
    Print(12345)
    Print(1234567)
    Print(10)
    Print(20)
    Print(200)
    Print(203203)
    Print(1000)
    Print(1001)
    Print(1000001)
    Print(1010101)
    Print(1000000)

if __name__ == '__main__':
    test()