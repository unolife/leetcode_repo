class Solution:
    def reverse(self, x: int) -> int:
        minus = False
        if x == 0:
            return 0
        if x < 0:
            x = abs(x)
            minus = True
        
        x = list(str(x))
        answer = ''
        for i in reversed(x):
            answer += i
        answer = int(answer)
        if (answer > 2**31-1) or (answer < -2**31):
            return 0

        if minus:
            return "-" + str(answer)
        return answer