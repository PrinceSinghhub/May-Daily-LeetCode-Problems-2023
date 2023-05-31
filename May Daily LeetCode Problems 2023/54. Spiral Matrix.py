class Solution:
    def spiralOrder(self, matrix):


        n = len(matrix)
        m = len(matrix[0])

        ans = []

        top = 0
        right = m-1
        left = 0
        buttom = n-1

        while top <= buttom and left <= right:

            # todo for right
            for i in range(left,right+1):
                ans.append(matrix[top][i])

            top+=1

            # todo for buttom
            for i in range(top, buttom+1):
                ans.append(matrix[i][right])

            right-=1

            # todo for left
            # edge case for check if multiple rows present or not

            if top <= buttom:

                for i in range(right, left-1,-1):
                    ans.append(matrix[buttom][i])

                buttom-=1

            # todo for top
            # edge case for check if top present or not

            if left <= right:
                for i in range(buttom, top-1,-1):
                    ans.append(matrix[i][left])

                left+=1

        return ans


# ans = Solution()
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(ans.spiralOrder(matrix))
