class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1,n+1):
            holder = ""
            if i % 3 == 0:
                holder += "Fizz"
            if i % 5 == 0:
                holder += "Buzz"
            if holder == "":
                holder = str(i)
            res.append(holder)
        return res
