class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t and not s:
            return ""

        need = Counter(t)
        window = defaultdict(int)

        required = len(need)
        formed = 0

        l = 0
        best_len = float('inf')
        best_l = 0

        for r, char in enumerate(s):
            window[char] += 1

            if char in need and need[char] == window[char]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l

                left_char = s[l]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                l += 1

        return "" if best_len == float("inf") else s[best_l : best_l + best_len]