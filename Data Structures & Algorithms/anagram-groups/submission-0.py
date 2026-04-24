class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_maps = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagram_maps:
                anagram_maps[sorted_word] = []
            anagram_maps[sorted_word].append(word)
        return list(anagram_maps.values())