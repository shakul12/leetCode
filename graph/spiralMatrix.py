class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        #column
        #row
        #num
        
        #if column >n -> row+=1
        #if column <0 -> row-=1
        #if row >n -> column-=1
        #else column+=1
        #exit when num >n**2
        
        out= [[0 for i in range(n)] for j in range(n)]
        low=0
        high=n-1
        attempt= int((n+1)/2)
        num=1
        for i in range(attempt):
            for j in range(low, high+1):
                out[i][j]=num
                num+=1
            for j in range(low+1, high+1):
                out[j][high]=num
                num+=1
            for j in range(high-1, low-1, -1):
                out[high][j]=num
                num+=1
            for j in range(high-1, low, -1):
                out[j][low]=num
                num+=1
            low+=1
            high-=1
        return out