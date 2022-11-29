class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")":"(","}":"{","]":"["}
        stack = []
        for i in s:
            if i in dic.values():     # 열림기호면 stack에 append
                stack.append(i)
            elif i in dic:           
                if not stack or dic[i] != stack.pop()  :    # 닫힘기호이면서 stack이 비어있거나 stack의 마지막 요소와 짝이 맞지 않으면 False return 
                    return False
        if stack :                    # stack에 요소가 있다면 false retrun 
            return False
        return True                   
            