class Solution:
    def romanToInt(self, s: str) -> int:
        valores = {
            'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }

        total = 0
        prev = 0

        for i in reversed(s):
            atual = valores[i]
            if atual < prev:
                total -= atual
            else:
                total += atual
            
            prev = atual
        return total
    

print(Solution.romanToInt(Solution, 'III')) # 3
print(Solution.romanToInt(Solution, 'IV')) # 4
print(Solution.romanToInt(Solution, 'IX')) # 9