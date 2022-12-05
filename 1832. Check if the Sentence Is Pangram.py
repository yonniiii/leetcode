# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
# time complexity : O(1)
# space complexity : O(n)

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
        sentence = set(sentence)

        for c in alphabet:
            if c not in sentence:
                return False
        return True
            