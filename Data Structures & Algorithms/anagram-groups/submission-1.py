class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_unique_signature(s):
            chars = [0]*26
            for c in s:
                chars[ord(c)-ord('a')]+=1
            return tuple(chars)
        anagrams_map= {}
        for st in strs:
            signature = get_unique_signature(st)
            if signature in anagrams_map:
                anagrams_map[signature].append(st)
                continue
            anagrams_map[signature]=[st]
        return [v for v in anagrams_map.values() ]


        