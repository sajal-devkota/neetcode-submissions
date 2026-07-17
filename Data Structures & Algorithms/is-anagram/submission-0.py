class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s)!= len(t):
            return False
        anag_check = list(t)
        for i_track in s:
            if i_track in anag_check:
                    anag_check.remove(i_track)
            else:
                    return False
        return True
       