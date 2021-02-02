import re
import pdb


class Dojo:
    def __init__(self):
        with open('input5.txt') as f:

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

    def run(self, *params):

        for line in self.input:

            self.row = 0
            self.rows = [0, 127]

            self.columns = [0, 7]
            self.column = 0

            for l in line:
                self.range_split(l)

            if self.ID < self.row * 8 + self.column:
                self.ID = self.row * 8 + self.column
                print("ROW")
                print(line)
                print(self.row)
                print(self.column)

        return self.ID


if __name__ == "__main__":
    dojo = Dojo()
    print(dojo.run())