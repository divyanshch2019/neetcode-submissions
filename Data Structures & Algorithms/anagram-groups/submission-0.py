class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #calculate the hash for each str and store it in a hashmap 
        # where key is the str hash (tuple) and the value is a list
        # in the end traverse the list and add all hashmap values to the result list
        result = []
        data_map = {}
        def get_hash(s):
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            return tuple(count)
        for s in strs:
            hash = get_hash(s)
            if hash in data_map:
                data_map[hash].append(s)
            else:
                data_map[hash] = [s]
        for _,val in data_map.items():
            result.append(val)
        return result
        