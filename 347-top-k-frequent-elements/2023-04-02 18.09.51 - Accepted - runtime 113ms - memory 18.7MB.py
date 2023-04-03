class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=defaultdict(int)

        # key=current number, value=frequency of the number
        for num in nums:
            counter[num]+=1

        # sort by values
        maxElements=[key for key, value in sorted(counter.items(), key=lambda x: x[1], reverse=True)]
        return maxElements[:k]