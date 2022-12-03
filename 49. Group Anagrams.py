class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dic = {}

        for c in strs:
            key = "".join(sorted(list(c)))
            if key in dic:
                dic[key].append(c)
            else:
                dic[key] = [c]
        
        for key in dic:
            result.append(dic[key])

        return result
