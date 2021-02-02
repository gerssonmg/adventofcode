import re
import pdb


class Dojo:
    def __init__(self):
        with open('input7.txt') as f:
            self.graph = {}
            self.node_head = ''
            self.cont_edges = 0
            self.input = f.readlines()  # Returns a list object

    def clean_line(self, line: str):
        rules, bags_or_not = line.split('contain')
        rules = rules.replace('bags', 'bag')  # Primeira parte da regra
        rules = rules.replace(' ', '')  # Primeira parte da regra
        bags_or_not = bags_or_not.replace('bags', 'bag')
        bags_or_not = bags_or_not.replace(' ', '')
        bags_or_not = bags_or_not.replace('.', '')
        bags_or_not = bags_or_not.replace('\n', '')
        bags_or_not = bags_or_not.split(',')  # Quebrando em varias bags

        # E pq nao tem quantidade logo e nootherbag
        if bags_or_not[0][0] == 'n':
            return [rules, bags_or_not]

        # Novo vetor que vai ter as bags repetidas tantas vezes suas quantidade
        bags = []

        for bag in bags_or_not:
            count_this_bag = bag[0]

            for i in range(0, 10):  # Limpando numeros da bag
                bag = bag.replace(str(i), '')

            for i in range(0, int(count_this_bag)):
                bags.append(bag)

        return [rules, bags]

    def build_graph(self, line: str):
        rules, bags_or_not = self.clean_line(line)
        self.graph[rules] = bags_or_not
        return None

    def dfs(self, node: str):
        edges = self.graph[node]
        if edges[0] == 'nootherbag':
            return None
        for edge in edges:
            self.cont_edges = self.cont_edges + 1
            self.dfs(edge)

    def run(self, *params):
        for line in self.input:
            self.build_graph(line)

        node_start = 'shinygoldbag'
        self.dfs(node_start)

        for node in self.graph:
            print(node)
            print(self.graph[node])

        # print(self.graph)
        return self.cont_edges


if __name__ == "__main__":
    dojo = Dojo()
    print(dojo.run())

    # 672