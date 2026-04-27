class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # should we write the algorithm first to generate all the permuatation strings first ?
        # the th. 

        # build a frequency map for string s2

        if len(s1) > len(s2):
            return False

        s1_map = {}
        for i in range(len(s1)):
            s1_map[s1[i]] = s1_map.get(s1[i],0)+1

        # w

        # we are looking for only a fixed length of window size of s1 or s1_map

        # should we create another hashmap for windows ?
        window_map = {}

        for i in range(len(s2)):
            window_map[s2[i]] = window_map.get(s2[i],0)+1

            if(i >= len(s1)):
                char_to_remove = s2[i-len(s1)]
                window_map[char_to_remove]-=1
                if window_map[char_to_remove] == 0:
                    del window_map[char_to_remove]
            
            if(len(window_map) == len(s1_map)):
                if(window_map == s1_map):
                    return True
                continue
        return False