class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output=[]
        visited= set()

        for i_index in range(len(strs)):


            if i_index not in visited:
                
                group=[strs[i_index]]
                visited.add(i_index)
                for j_string in range(i_index+1 ,len(strs)):    
                        if j_string in visited:
                            continue
                        anag_check = []
                        if len(strs[i_index]) == len(strs[j_string]):
                            for j_str in strs[j_string]:
                                anag_check.append(j_str)
                            for check_str in strs[i_index]:
                                if check_str not in anag_check:
                                    break

                                
                                    
                                else:
                                    anag_check.remove(check_str)

                            if len(anag_check) == 0:
                                    group.append(strs[j_string])
                                    visited.add(j_string)
                        
                output.append(group)
                
        return output
           

        

                
            
        