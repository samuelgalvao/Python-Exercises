class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Find the shortest string in the list
        shortest_str = min(strs, key=len)
        
        for i, char in enumerate(shortest_str):
            # Check if the corresponding character in all strings is the same
            if any(string[i] != char for string in strs):
                return shortest_str[:i]
        
        # If all characters match, return the shortest string
        
        return shortest_str
                
        
                
solo = Solution()
solo.longestCommonPrefix(["flower","flow","flight"])