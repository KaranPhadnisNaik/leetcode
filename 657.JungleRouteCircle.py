class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        directions = {
            'R':1,
            'L':-1,
            'U':1,
            'D':-1
        }
        start =[0,0]
        for move in moves:
            if move in ['R','L']:
                start[0] += directions[move]
            elif move in ['U', 'D']:
                start[1] += directions[move]
            else:
                return False
        return start == [0,0]
