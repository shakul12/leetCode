class Solution:
    def checkValidString(self, s: str) -> bool:
        if s=="":
            return True
        opens=[]
        star=[]
        for i in range(len(s)):
            if s[i]=="(":
                opens.append(i)
            elif s[i]==")":
                if len(opens)>0:
                    opens.pop()
                elif len(star)>0:
                    star.pop()
                else:
                    return False
            elif s[i]=="*":
                star.append(i)
        if len(opens)==0:
            return True
        else:
            if len(opens)>len(star):
                return False
            else:
                while len(opens)>0:
                    n=opens.pop()
                    s= star.pop()
                    if s<n:
                        return False
                return True