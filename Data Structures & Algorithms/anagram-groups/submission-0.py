from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # counter of all words --> easy to filter out (improvement idea)
        counter_words = defaultdict(list)
        for i, w in enumerate(strs):
            counter = Counter(w)
            key = tuple(sorted(counter.items()))  # <-- Hashable + deterministic
            counter_words[key].append(w)
        
        return list(counter_words.values())

