class Solution:
    # "/apple//box////c/d//././/.."
    def simplifyPath(self, path: str) -> str:
        path += '/'
        stk = []
        cur_name = ""
        for ch in path:
            if ch == '/':
                if cur_name == "..":
                    if stk:
                        stk.pop()
                elif cur_name != '.' and cur_name != "":
                    stk.append(cur_name)
                cur_name = ""
            else:
                cur_name += ch

        res = ""
        for name in stk:
            res += "/" + name
        if res == "":
            res = "/"
        return res



path = "/apple//box////c/d//././/.."
print('/'.join(path.split('/')))
