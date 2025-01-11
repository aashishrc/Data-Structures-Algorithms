class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k >= len([x for x, f in Counter(s).items() if f % 2 == 1])
        