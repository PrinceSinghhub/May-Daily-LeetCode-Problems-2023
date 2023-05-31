class Solution:
    def diagonalSum(self, mat):


        L = (len(mat)-1) % 2



        if(L==0):
            f = []
            # todo for front
            for i in range(len(mat)):
                f.append(mat[i][i])

            # todo for back
            mid = int((len(mat)-1)/2)

            row = 0
            for i in range(len(mat)-1,-1,-1):
                if i == mid:
                    row+=1
                    continue
                else:
                    f.append(mat[row][i])
                    row+=1

            return sum(f)

        else:
            f =[]
            for i in range(len(mat)):
                f.append(mat[i][i])

            row = 0
            for i in range(len(mat) - 1, -1, -1):
                f.append(mat[row][i])
                row+=1

            return sum(f)