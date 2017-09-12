class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # iterate through all the strings
        # sort the string and store the sorted string as a variable
        # use that sorted string as a key and add to a dictionary
        # if a value associated with the key does not exist, create a new array with the value
        # else append to the array corresponding to the key
        # return the dictionary's values (array of arrays)
        similiarityDict = {}
        for word in strs:
            orderedWord = ''.join(sorted(strs))
            # orderedWord is the key in the dict
            if orderedWord in similiarityDict:
                similiarityDict[orderedWord].append(word)
            else:
                similiarityDict[orderedWord] = [word]
        return similiarityDict.values()


        
