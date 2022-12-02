class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []

        Anagrams_dic = {}

        for element in strs:
            temp = "".join(sorted(list(element)))
            if temp in Anagrams_dic.keys():
                Anagrams_dic[temp].append(element)
            else:
                Anagrams_dic[temp] = [element]

        for key in Anagrams_dic.keys():
            answer.append(Anagrams_dic[key])

        return answer