class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        h = len(haystack)
        n = len(needle)
        # iterate from index 0 to index h-n
        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1
