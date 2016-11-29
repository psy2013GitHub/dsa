#-*- encoding: utf8 -*-
from collections import Counter


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """


        result = []
        word_len = len(words[0])

        for stripe in range(word_len):  # each stripe starts at a different position in s, modulo word_len

            i = stripe  # the next index in s that we want to match a word
            to_match = len(words)  # number of words still to be matched
            freq = Counter(words)  # frequency of each words to be matched

            while i + to_match * word_len <= len(
                    s):  # remainder of s is long enough to hold remaining unmatched words

                word = s[i:i + word_len]  # next part of s attempting to be matched
                print(i, word)
                if word in freq:  # match, decrement freq count
                    freq[word] -= 1
                    if freq[word] == 0:
                        del freq[word]
                    to_match -= 1
                    i += word_len
                    if to_match == 0:  # all matched
                        result.append(i - word_len * len(words))

                elif to_match != len(words):  # some words have been matched
                    nb_matches = len(words) - to_match
                    first_word = s[i - nb_matches * word_len:i - (nb_matches - 1) * word_len]
                    freq.setdefault(first_word, 0)  # put first word matched back in dictionary
                    freq[first_word] += 1
                    to_match += 1

                else:  # no words matched
                    i += word_len

        return result

    def brute_force(self, s, words):
        """
            time complexity: O(mn)
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []

        words_count = {}
        for word in words:
            words_count.setdefault(word, 0)
            words_count[word] += 1
        words_len = len(words_count)

        wlen = len(words[0])
        for i in range(wlen):
            tmp_words_count, found, min_pos = {}, 0, -1
            # print('outer loop', i)
            j = i
            while j < len(s):
                w = s[j:j+wlen]
                # print('inner loop', w)
                if not words_count.has_key(w):
                    j += wlen
                    continue
                if not tmp_words_count.has_key(w):
                    tmp_words_count[w] = 1
                else:
                    tmp_words_count[w] += 1
                # print('init', i, j, w, min_pos, tmp_words_count)
                if tmp_words_count[w] > words_count[w]:
                    # print('break:', i, j, s[:j], w, min_pos, tmp_words_count[w], words_count[w])

                    start = i
                    while tmp_words_count[w] > words_count[w]:
                        first_w = s[start:start + wlen]
                        # print('drop:', i, j, s[:j], first_w, min_pos, tmp_words_count[w], words_count[w])
                        start += wlen
                        if first_w in tmp_words_count:
                            tmp_words_count[first_w] -= 1

                            if tmp_words_count[first_w] + 1 == words_count[w]:
                                found -= 1

                    j += wlen
                    # print('drop found:', j, found)
                    continue

                elif tmp_words_count[w] == words_count[w]:
                    min_pos = min_pos if min_pos!=-1 and min_pos <= i else i
                    # print('found:', i, j, w, min_pos, tmp_words_count[w], words_count[w])
                    found += 1
                    if found == len(words):
                        res.append(j - len(words) * wlen + wlen)
                        print('found:', i, j, w, min_pos, tmp_words_count[w], words_count[w])
                        tmp_words_count, found, min_pos = {}, 0, -1

                j += wlen

        return res

def test():
    solution = Solution()
    print(solution.brute_force('barfoothefoobarman', ["foo", "bar"]))
    # print(solution.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
    # print(solution.brute_force("wordgoodgoodgoodbestword", ["word","good","best","good"]))


if __name__ == '__main__':
    test()