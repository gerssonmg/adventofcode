import re
import pdb


class Dojo:
    def __init__(self):
        with open('input3.txt') as f:
            self.position = [0, 0]
            self.count_tree = 0
            self.input = f.readlines()  # Returns a list object

    def step_next(self) -> str:
        # pdb.set_trace()
        self.position[0] = self.position[0] + 1
        self.position[1] = self.position[1] + 3
        print(self.position)
        return self.input[self.position[0]][self.position[1]]

    """
    todo: caminha direita 3
    todo: valida se pode caminhar se não ajusta proxima
    todo: linha
    """

    def run(self, *params):
        max_x = len(self.input[0])
        print(max_x)
        cont = 0
        for line in self.input:
            if self.position[0] < 322:
                street = self.step_next()
                if street == '#':
                    self.count_tree = self.count_tree + 1
            else:
                return self.count_tree


if __name__ == "__main__":
    dojo = Dojo()
    print(dojo.run())