class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for word in strs:
            word_sorted = "".join(sorted(word))

            if word_sorted not in anagram_dict:
                anagram_dict[word_sorted] = []

            anagram_dict[word_sorted].append(word)
        
        return list(anagram_dict.values())