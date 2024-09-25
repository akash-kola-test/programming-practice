class Solution:
    def longestPalindrome(self, input_string: str) -> str:
        lps = ""

        for i in range(0, len(input_string)):
            low = i
            high = i

            while low >=0 and high < len(input_string):
                if not input_string[low] == input_string[high]:
                    break
                if len(input_string[low:high+1]) > len(lps):
                    lps = input_string[low:high+1]
                low -= 1
                high += 1
            
            low = i
            high = i + 1

            while low >= 0 and high < len(input_string):
                if not input_string[low] == input_string[high]:
                    break
                if len(input_string[low:high+1]) > len(lps):
                    lps = input_string[low:high+1]
                low -= 1
                high += 1

        return lps

print(Solution().longestPalindrome("dbbc"))
