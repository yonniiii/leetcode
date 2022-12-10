class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         dic = {}
#         for i in range(len(arr)):
#             if arr[i] in dic:          #키(숫자)가 중복되면 다음 loop
#                 continue
#             elif arr.count(arr[i]) in dic.values():   #값(숫자의count)가 중복되면 false 반환
#                 return False
#             else:
#                 dic[arr[i]] = arr.count(arr[i])
#         return True


    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in range(len(arr)):
            arr_count = arr.count(arr[i])
            if arr[i] in dic:                 #키(숫자)가 중복되면 다음 loop
                continue
            elif arr_count in dic.values():   #값(숫자의count)가 중복되면 false 반환
                return False
            else:
                dic[arr[i]] = arr_count
        return True
