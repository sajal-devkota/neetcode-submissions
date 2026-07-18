class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        used = [False] * len(strs)

        for i_index in range(len(strs)):

            if used[i_index]:
                continue

            output.append([strs[i_index]])
            out_index = len(output) - 1
            used[i_index] = True

            f = i_index + 1

            if f != len(strs):
                for j_string in range(f, len(strs)):

                    if len(strs[i_index]) == len(strs[j_string]) and not used[j_string]:

                        anag_check = []

                        for j_str in strs[j_string]:
                            anag_check.append(j_str)

                        for check_str in strs[i_index]:
                            if check_str not in anag_check:
                                break
                            anag_check.remove(check_str)
                        else:
                            if len(anag_check) == 0:
                                output[out_index].append(strs[j_string])
                                used[j_string] = True

        return output