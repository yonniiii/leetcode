class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l:int, r:int) ->str:  ## 최대 팰린드롬 return 함수
            while l >= 0 and r < len(s) and s[l]==s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        if len(s) ==1:
            return s

        result = ''
        for i in range(len(s)-1):
            result = max (
                result,
                expand(i,i+1), #팰린드롬이 짝수인 경우
                expand(i,i+2), #팰린드롬이 홀수인 경우
                key =len
            )
        return result