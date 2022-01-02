class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        extra = False

        if digits[-1] == 9:
            for i in range(len(digits), 0, -1):
                if digits[i-1] == 9:
                    digits[i-1] = 0
                    extra = True
                else:
                    if extra:
                        digits[i-1] += 1
                        if digits[i-1] == 10:
                            digits[i-1] = 0
                        else:
                            extra = False
                            return digits
                    else:
                        digits[i-1] += 1
                        return digits

                if i == 1:
                    if extra:
                        return [1] + digits
                    else:
                        return digits
                
        else:
            digits[-1] += 1
            return digits
        