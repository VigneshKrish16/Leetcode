class Solution:
    def calPoints(self, op: List[str]) -> int:
        res = []
        for char in op:
            if char == "+":
                res.append(res[-1]+res[-2])
            elif char == "C":
                res.pop()
            elif char == "D":
                res.append(res[-1]*2)
            else:
                res.append(int(char))
    
        return sum(res)
        
