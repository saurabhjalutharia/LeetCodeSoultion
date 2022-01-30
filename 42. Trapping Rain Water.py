class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        finalresult = 0
        left = [0] * n  # l[i] := max(height[0..i])
        right = [0] * n  # r[i] := max(height[i..n))

        for i in range(n):
            left[i] = height[i] if i == 0 else max(height[i], left[i - 1])

        for i in range(n - 1, -1, -1):
            right[i] = height[i] if i == n - 1 else max(height[i], right[i + 1])

        for i in range(n):
            finalresult += min(left[i], right[i]) - height[i]

        return finalresult
