# encoding:utf-8


class Dojo08:
    def __init__(self):
        with open('input8.txt') as f:
            self.input = f.readlines()  # Returns a list object
        self.lines_passed = set()
        self.line_update = 0

    def run_part_1(self) -> int:
        """
        Encontra o valor do acumulador imediatamente antes de executar o loop.
        :return: o valor do acumulador
        """
        total = 0
        current_pointer = 0
        while current_pointer not in self.lines_passed:
            self.lines_passed.add(current_pointer)

            current_line = self.input[current_pointer]
            operation, quantity = current_line.split(' ')
            if operation == 'nop':
                current_pointer += 1
            elif operation == 'jmp':
                current_pointer += int(quantity)
            else:
                current_pointer += 1
                total += int(quantity)

        return total

    def aux_func(self, arr):
        total = 0
        current_pointer = 0
        lines_passed = set()
        while current_pointer not in lines_passed and current_pointer < len(
                arr):
            lines_passed.add(current_pointer)

            current_line = arr[current_pointer]
            operation, quantity = current_line.split(' ')
            if operation == 'nop':
                current_pointer += 1
            elif operation == 'jmp':
                current_pointer += int(quantity)
            else:
                current_pointer += 1
                total += int(quantity)

        return total, current_pointer

    def run_part_2(self):
        """
        Encontra qual a instrução que está errada (jmp ou nop), uma vez alterada, encontra o valor
        que o accumulador deveria ter ao fim da execução.
        :return: o valor final do acumulador, quando não há mais instruções para executar.
        """

        self.run_part_1()

        for line in self.lines_passed:
            copy_input = list(self.input)
            operation, quantity = copy_input[line].split(' ')
            if operation == 'acc':
                continue
            elif operation == 'jmp':
                copy_input[line] = f'nop {quantity}'
            else:
                copy_input[line] = f'jmp {quantity}'
            total, current_pointer = self.aux_func(copy_input)
            if current_pointer == len(self.input):
                return total

