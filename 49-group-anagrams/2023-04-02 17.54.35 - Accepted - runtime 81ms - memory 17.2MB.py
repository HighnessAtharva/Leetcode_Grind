class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store={}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in store:
                store[sorted_word]=[]
            
            store[sorted_word].append(word)

        return list(store.values())