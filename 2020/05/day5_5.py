import re
import pdb


class Dojo:
    def __init__(self):
        with open('input5.txt') as f:
            arr_zero = [0, 0, 0, 0, 0, 0, 0, 0]
            self.M = []
            for i in list(range(0, 128)):
                self.M.append(arr_zero)

            self.MATRIX_FLY = [[j for j in range(0, 8)] for i in range(0, 128)]
            pdb.set_trace()
            self.ID = -1
            self.row = 0
            self.column = 0

            self.rows = [0, 127]
            self.columns = [0, 7]

            self.input = f.readlines()  # Returns a list object

    def range_split(self, command) -> None:
        if command == 'F':
            self.rows[1] = int((self.rows[0] + self.rows[1]) / 2)
            self.row = self.rows[1]
            return None
        elif command == 'B':
            self.rows[0] = int((self.rows[0] + self.rows[1]) / 2)
            self.row = self.rows[0] + 1
            return None

        if command == 'L':
            self.columns[1] = int((self.columns[0] + self.columns[1]) / 2)
            self.column = self.columns[0] + 1
            return None

        elif command == 'R':
            self.columns[0] = int((self.columns[0] + self.columns[1]) / 2)
            self.column = self.columns[1]
            return None

    def r(self):
        for i in list(range(0, 128)):
            # print(i)
            print([
                self.MATRIX_FLY[i][0], self.MATRIX_FLY[i][1],
                self.MATRIX_FLY[i][2], self.MATRIX_FLY[i][3],
                self.MATRIX_FLY[i][4], self.MATRIX_FLY[i][5],
                self.MATRIX_FLY[i][6], self.MATRIX_FLY[i][7]
            ])
        print("ALO")
        print("ALO")
        print("ALO")
        for i in list(range(0, 128)):
            print([
                self.M[i][0], self.M[i][1], self.M[i][2], self.M[i][3],
                self.M[i][4], self.M[i][5], self.M[i][6], self.M[i][7]
            ])

    def run(self, *params):

        for line in self.input:

            self.row = 0
            self.rows = [0, 127]

            self.columns = [0, 7]
            self.column = 0

            # if line != 'BBFBBFBLRL':
            for l in line:
                self.range_split(l)
            # print([[self.row], [self.column]])
            # if self.row == 83 and self.column == 1:
            # pdb.set_trace()

            # print([self.row, self.column])
            self.MATRIX_FLY[self.row][self.column] = [[self.row],
                                                      [self.column]]

            #
        pdb.set_trace()
        return self.ID


if __name__ == "__main__":
    dojo = Dojo()
    print(dojo.run())