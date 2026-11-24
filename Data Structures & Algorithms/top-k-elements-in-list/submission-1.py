class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        res = sorted(list(freq.keys()), key=lambda x: freq[x], reverse=True)[:k]
        return res
