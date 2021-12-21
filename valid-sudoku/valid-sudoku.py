class Solution:

    def check(self, data, each_dict):
        if each_dict.get(data):
            return 1
        else:
            each_dict[data] = '0'
            return 0
        
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        d_row = {
            '0': {},
            '1': {},
            '2': {},
            '3': {},
            '4': {},
            '5': {},
            '6': {},
            '7': {},
            '8': {},

        }
        box = {
            '0_0': {},
            '0_1': {},
            '0_2': {},
            '1_0': {},
            '1_1': {},
            '1_2': {},
            '2_0': {},
            '2_1': {},
            '2_2': {},
        }
        
        for r_idx, row in enumerate(board):
            d_col = {}
            for c_idx, data in enumerate(row):
                if data != ".":
                    if r_idx < 3:
                        r = 0
                    elif r_idx > 5:
                        r = 2
                    else:
                        r = 1

                    if c_idx < 3:
                        c = 0
                    elif c_idx > 5:
                        c = 2
                    else:
                        c = 1
                    res1 = self.check(data, d_col)
                    res2 = self.check(data, d_row[str(c_idx)])                    
                    res3 = self.check(data, box[f"{r}_{c}"])
                    if (res1 + res2 + res3) == 0:
                        continue
                    else:
                        return False
        return True