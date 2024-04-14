from random import choice, randint, random, sample
from numpy import array, set_printoptions, triu, inf
from pandas import DataFrame, set_option
from datetime import datetime
from os import path, chdir

chdir(path.dirname(path.abspath(__file__)))
# Can use NetworkX for visualization

"""
Projet Graphes WIP
"""
set_option('float_format', '{:.0f}'.format)
set_option('display.max_columns', 100)


def random_event(probability: int):
    "The probability is an int indicating a percentage [probability%]"
    return (random() < (probability / 100))


def format_infinity(x):
    """Used for readability when printing dataframes"""
    if x == inf:
        return '∞'
    elif x == -inf:
        return '-∞'
    return x


class Graph:
    """
    This class represent a non-oriented graph, made of Nodes.
    The matrix is upper half only, excluding the diagonal.
    \nRules are the distribution of nodes per tier
    \nOptional arguments (kwargs):
    \n\tno_generation: bool -> Use to generate a blank Graph, defaults to False
    """

    def __init__(self, name: str = None, size=100, rules=(10, 20, 70), **kwargs):
        self.name = name if name else f"Graph_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}"

        if kwargs.get("no_generation", False):
            self.nodes = [Node() for _ in range(size)]
            self.matrix = self.generate_links(size, rules, no_generation=True)
        else:
            self.nodes = self.__generate_nodes(rules)
            self.matrix = self.__generate_links(size, rules)
            """for node_index in range(len(self.nodes)):
                self.nodes[node_index].neighbors = self.get_neighbors(node_index)"""

            self.translation_table = {self.nodes[index].name: index for index in range(len(self.nodes))}

    def __generate_nodes(self, rules: tuple):
        """Creates the list of Nodes and their distribution"""
        temp = []
        # Backbone
        for iteration in range(1, rules[0] + 1):
            temp += [Node(1, f"B{iteration}")]
        # Transit
        for iteration in range(1, rules[1] + 1):
            temp += [Node(2, f"T{iteration}")]
        # Regular
        for iteration in range(1, rules[2] + 1):
            temp += [Node(3, f"R{iteration}")]
        return (temp)

    def __generate_links(self, size, rules, **kwargs):
        """The matrix follow these rules: A link exists if it's >1, a line show a Node's neighbors, a column show what a Node is connected to, the value represents the speed of the link"""
        temp = array([[0 if row != column else float("inf") for row in range(size)] for column in range(size)])
        if kwargs.get("no_generation", False):
            return (temp)

        # Tier I
        for node_A in range(0, rules[0]):
            for node_B in range(0, rules[0]):
                if (self.get_link(temp, node_A, node_B) == 0) and (random_event(10)):
                    link_value = randint(5, 10)
                    self.set_link(temp, node_A, node_B, link_value)

        # Tier II
        for node_A in range(rules[0] + 1, rules[1]):    # WIP
            candidates = [node_index for node_index in range(rules[0] + 1, rules[1])]
            candidates.remove(node_A)
            selection = sample(candidates, randint(2, 3))
            print(f"{self.nodes[node_A].name}:{selection}")
            for node_B in selection:
                if (self.get_link(temp, node_A, node_B) == 0):
                    link_value = randint(10, 20)
                    self.set_link(temp, node_A, node_B, link_value)

        return (temp)

    def display_links(self, shape=(10, 20), slice: tuple = (0, 999)):
        """
        Will display all the Nodes and their connections.
        However, since a terminal cannot display 100 Nodes
        , this function divide all the nodes by a specified shape.
        \nArguments:
        \n\tshape: tuple (rows, columns)
        \n\tslice: tuple (rows, columns) -> based on the shape, the slice will be multiplied
        """

        set_option('display.width', 9 * shape[1])  # Adjusts the number of columns/raws to display

        slice_size = array(slice) * shape[0]
        slice_diff = (slice_size[1] - slice_size[0])

        matrix = self.matrix[slice_size[0]:slice_size[1]]
        labels = [node.name for node in self.nodes]

        chunks = [matrix[row:row + slice_diff] for row in range(0, len(matrix), slice_diff)]
        dataframes = [DataFrame(chunk) for chunk in chunks]
        for dataframe in dataframes:
            dataframe.index = labels[slice_size[0]:slice_size[1]]
            dataframe.columns = labels
            print(dataframe.map(format_infinity))

    def export(self):
        """Will export the current Graph's matrix in an excel spreadsheet. The file is in the folder "spreadsheets"
        """
        temp_dataframe = DataFrame(self.matrix).map(format_infinity)
        temp_dataframe.index = [node.name for node in self.nodes]
        temp_dataframe.columns = [node.name for node in self.nodes]
        temp_dataframe.to_excel(f"spreadsheets/{self.name}_spreadsheet.xlsx", index=True)

    def get_neighbors(self, node_index):
        """Returns the neighbors of a Node, identified by it's index."""
        temp = []
        for column in range(len(self.matrix)):
            if (0 < self.matrix[node_index, column] < float("inf")):
                temp += [self.nodes[column].name]
        for row in range(len(self.matrix)):
            if (0 < self.matrix[row, node_index] < float("inf")):
                temp += [self.nodes[row].name]

        return (temp)

    def __str__(self) -> str:
        return ('\n'.join(str(node.infos()) for node in self.nodes))

    def get_node(self, index: int):
        return (self.nodes[index - 1])

    def get_node_index(self, node: str | list):
        if isinstance(node, list):
            return [self.translation_table.get(node_iter, 0) for node_iter in node]
        elif isinstance(node, str):
            return (self.translation_table.get(node, 0))
        else:
            print(f"The node's type provided is invalid ({type(node)})")
            return (None)

    def get_link(self, matrix, node1: any, node2: any):
        if isinstance(node1, str) and isinstance(node2, str):  # If given by name
            a, b = self.translation_table.get(node1, 0), self.translation_table.get(node2, 0)
            return (matrix[(a, b) if a < b else (b, a)])
        elif isinstance(node1, int) and isinstance(node2, int):  # If given by index
            return (matrix[(node1, node2) if node1 < node2 else (node2, node1)])
        else:
            print(f"The node's type provided is invalid ({type(node1)}, {type(node2)})")
            return (None)

    def set_link(self, matrix, node1: any, node2: any, value: float):
        if isinstance(node1, str) and isinstance(node2, str):  # If given by name
            a, b = self.translation_table.get(node1, 0), self.translation_table.get(node2, 0)
            if a != b:
                matrix[(a, b) if a < b else (b, a)] = value
                print(f"\033[92mCreated link ({node1}, {node2})={value}\033[0m")
        elif isinstance(node1, int) and isinstance(node2, int):  # If given by index
            if node1 != node2:
                matrix[(node1, node2) if node1 < node2 else (node2, node1)] = value
                print(f"\033[92mCreated link ({self.nodes[node1].name}, {self.nodes[node2].name})={value}\033[0m")
        else:
            print(f"The node's type provided is invalid ({type(node1)}, {type(node2)})")
            return (None)


class Node:
    """Used to represent a Node which is used for Graphs."""

    global_nodes = {}

    def __init__(self, tier: int = 0, name: str = None):
        self.id = id(self)
        self.tier = tier
        self.name = self.set_name(name, self.id)
        self.neighbors = []
        self.global_nodes[self.id] = self.name
        self.routing_table = {}

    def __repr__(self) -> str:
        return (f'{self.infos()}')

    def __str__(self) -> str:
        return (f"{self.name}")

    def set_name(self, name, id):
        if (self.global_nodes).get(name, None):
            return (name + str(id))
        else:
            return (name)

    def infos(self=None):
        """Used to get all attributes of an object"""
        return (vars(self))


G = Graph(no_generation=False)
G.display_links((10, 20), (1, 3))
if input("Would you like to export? Y/N:") == "Y":
    G.export()
