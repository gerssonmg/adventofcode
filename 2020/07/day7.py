import re
import pdb


class Dojo:
    def __init__(self):
        with open('input7.txt') as f:
            self.graph = {}
            self.node_head = ''
            self.node_can_contain = set()
            self.input = f.readlines()  # Returns a list object

    def clean_line(self, line: str):
        rules, bags_or_not = line.split('contain')
        rules = rules.replace('bags', 'bag')  # Primeira parte da regra
        rules = rules.replace(' ', '')  # Primeira parte da regra
        bags_or_not = bags_or_not.replace('bags', 'bag')
        bags_or_not = bags_or_not.replace(' ', '')
        bags_or_not = bags_or_not.replace('.', '')
        bags_or_not = bags_or_not.replace('\n', '')
        for i in range(0, 10):  # Limpando numeros do array
            bags_or_not = bags_or_not.replace(str(i), '')

        bags_or_not = bags_or_not.split(',')  # Quebrando em varias bags
        return [rules, bags_or_not]

    def build_graph(self, line: str):
        rules, bags_or_not = self.clean_line(line)
        self.graph[rules] = bags_or_not
        return None

    def dfs(self, node: str):
        edges = self.graph[node]
        if edges[0] == 'nootherbag':
            return None
        for edge in edges:
            if edge == 'shinygoldbag':
                self.node_can_contain.add(self.node_head)
                return None
            self.dfs(edge)

    def run(self, *params):

        for line in self.input:
            self.build_graph(line)
        for node in self.graph:
            self.node_head = node
            if node != 'shinygoldbag':
                self.dfs(node)

        return len(self.node_can_contain)


if __name__ == "__main__":
    dojo = Dojo()
    print(dojo.run())

    # 672