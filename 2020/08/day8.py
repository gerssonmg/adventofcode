import re
import pdb


class Dojo:
    def __init__(self):
        with open('input8.txt') as f:
            self.accumulator = 0
            self.program = []
            self.input = f.readlines()  # Returns a list object

    def build_program(self, line: str):
        line = line.replace('\n', '')
        self.program.append([line, False])
        return None

    def execute_program(self):
        # for index in range(0,len(self.program)):
        index = 0
        while True:

            if self.program[index][1]:  # Ja executou uma vez
                break
            else:  # Não executou ainda
                self.program[index][1] = True

            instruction = self.program[index]
            key, value = instruction[0].split(' ')

            op = value[0]  # Pega sinal de + ou -
            value = int(value.replace(op, ''))

            if key == 'nop':
                index = index + 1
                continue

            if key == 'acc':
                if op == '+':
                    index = index + 1
                    self.accumulator = self.accumulator + value
                    continue
                else:
                    index = index + 1
                    self.accumulator = self.accumulator - value
                    continue

            if key == 'jmp':
                if op == '+':
                    index = index + value
                else:
                    index = index - value

    def run(self, *params):

        for line in self.input:
            self.build_program(line)
        self.execute_program()
        return self.accumulator


if __name__ == "__main__":
    dojo = Dojo()
    print(dojo.run())

    # 672