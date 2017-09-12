class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # split by spaces (default), reverse list, then join by spaces
        return " ".join(s.split()[::-1])
