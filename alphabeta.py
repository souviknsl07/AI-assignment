def minimax_alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or node.is_terminal_node():
        return node.evaluate()

    if maximizingPlayer:
        value = float('-inf')
        for child in node.get_children():
            value = max(value, minimax_alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in node.get_children():
            value = min(value, minimax_alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def is_terminal_node(self):
        return len(self.children) == 0

    def evaluate(self):
        return self.value

    def get_children(self):
        return self.children

root = Node(0)

child1 = Node(3)
child2 = Node(5)
child3 = Node(2)
root.children = [child1, child2, child3]

best_move = minimax_alpha_beta(root, 3, float('-inf'), float('inf'), True)

print("The best move is:", best_move)
