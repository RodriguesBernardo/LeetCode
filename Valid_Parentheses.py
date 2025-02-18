class Solution:
    def isValid(self, s: str) -> bool:
        pilha = []
        pares = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in pares.values(): 
                pilha.append(char)
            elif char in pares: 
                if not pilha or pilha.pop() != pares[char]:  
                    return False 
            else:
                return False  
        return not pilha
    

sol = Solution()
print(sol.isValid("()"))