class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow_hashmap = {}
        con_hashmap = {}

        for i in s:
            if i in "a,e,i,o,u":
                if i in vow_hashmap:
                    vow_hashmap[i] += 1
                else:
                    vow_hashmap[i] = 1
            else:
                if i in con_hashmap:
                    con_hashmap[i] += 1 
                else:
                    con_hashmap[i] = 1 
                

        if vow_hashmap:
            vow = 0
            for i in vow_hashmap.values():
                vow = max(vow,i)
        else:
            vow = 0

        if con_hashmap:
            con = 0
            for i in con_hashmap.values():
                con = max(con,i)
        else:
            con = 0
    

        return vow + con