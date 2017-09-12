class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # select only alpha numeric characters from s
        s = filter(lambda x: x.isalnum(), s.lower())
        # split in half, check if first half is equal to reverse of the second half
        return s[:len(s)/2] == s[::-1][:len(s)/2]
