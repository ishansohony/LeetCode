class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        if newColor == oldColor:
            return image
        def dfs(image, sr, sc, newColor, oldColor):
            if((sr < 0) or (sr > len(image) - 1) or (sc < 0) or (sc > len(image[0]) - 1)):
                return image
            
            if(image[sr][sc] == oldColor):
                image[sr][sc] = newColor
                print(image)
                image = dfs(image, sr + 1, sc, newColor, oldColor)
                image = dfs(image, sr - 1, sc, newColor, oldColor)
                image = dfs(image, sr, sc + 1, newColor, oldColor)
                image = dfs(image, sr, sc - 1, newColor, oldColor)
                
            return image
        
        return dfs(image, sr, sc, newColor, oldColor)
        
