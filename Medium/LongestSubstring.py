class Solution(object):
    def lengthOfLongestSubstring(self, s):
       
        list_a = []  
        max_len = 0  
        i = 0  
        j = 0  
        length = len(s)
      
        while j < length:
            if s[j] not in list_a:
                list_a.append(s[j])
                max_len = max(max_len, j - i + 1)
                j += 1
            else:
                list_a.remove(s[i])
                i += 1
        
        return max_len