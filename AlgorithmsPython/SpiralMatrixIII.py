# LeetCode Spiral Matrix III


class Solution:
    def SpiralMatrixIII(self, R, C, r0, c0):
        """

        :param R:int
        :param C: int
        :param r0: int
        :param c0: int
        :return: List[List[int]]
        """
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        total = R * C
        steps = 1
        increment = 1
        result = [[r0, c0]]

        while len(result) < total:
            for i in range(increment):
                r0, c0 = r0 + dirs[dir_idx][0], c0 + dirs[dir_idx][1]
                if r0 >= 0 and r0 < R and c0 >= 0 and c0 < C:
                    result.append([r0, c0])

                dir_idx = (dir_idx + 1) % 4
                if steps % 2 == 0:
                    increment += 1
                steps += 1

        return result


print(Solution().SpiralMatrixIII(5, 6, 1, 4))
