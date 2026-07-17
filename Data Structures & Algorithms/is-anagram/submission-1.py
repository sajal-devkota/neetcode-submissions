class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        
        emp_dict = {}
        anag_dict={}
        
        for i_string in s:
            if i_string not in emp_dict:
                
                emp_dict[i_string] = 1
            else:
                
                emp_dict[i_string] = emp_dict.get(i_string)+1
        
        for j_anag_check in t:
            if j_anag_check not in anag_dict:
                
                anag_dict[j_anag_check]= 1
            else:
                anag_dict[j_anag_check] = anag_dict.get(j_anag_check)+1
        
        if emp_dict == anag_dict:
            return True
        return False