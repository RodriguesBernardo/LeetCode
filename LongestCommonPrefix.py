from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
print(Solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Saída: "fl"
print(Solution.longestCommonPrefix(["dog", "racecar", "car"]))     # Saída: ""
print(Solution.longestCommonPrefix(["interspecies", "interstellar", "interstate"]))