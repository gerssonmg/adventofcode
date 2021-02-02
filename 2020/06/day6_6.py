import re
import pdb


class Dojo:
    def __init__(self):
        with open('input6.txt') as f:
            self.input = f.readlines()  # Returns a list object

    def run(self, *params):
        cont = 0
        new_set = set()
        first_element = True
        for line in self.input:
            if line != '\n':
                _line = line.split('\n')[0]
                if first_element:
                    new_set = new_set.union(_line)
                    first_element = False
                else:
                    new_set = new_set.intersection(_line)
            else:
                first_element = True
                cont = cont + len(new_set)
                new_set = set()

        return cont


if __name__ == "__main__":
    dojo = Dojo()
    print(dojo.run())