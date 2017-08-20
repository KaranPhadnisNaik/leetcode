class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # O(n)
        store = {}
        for char in s:
            store[char] = store.get(char,0) + 1
        for char in t:
            # if char is not found in store or is zero return character
            if char not in store or store[char]==0:
                return char
            else:
                store[char] -= 1
        '''
        # nlogn solution
        # sort the strings
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        # find the first letter in t that doesnt match from s
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        # we know the last letter has to be the one that is off
        return t[-1]
       '''
        
