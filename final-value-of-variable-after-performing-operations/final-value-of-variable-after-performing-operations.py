class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for op in operations:
            ans = ans + 1 if "+" in op else ans - 1
        return ans
        