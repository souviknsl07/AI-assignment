import tkinter as tk
from collections import deque
def water_jug_problem(capacity_jug1, capacity_jug2, target):
    visited = set()
    queue = deque([(0, 0, [])])
    while queue:
        x, y, steps = queue.popleft()
        if x == target or y == target:
            return steps
        if (x, y) in visited:
            continue
        visited.add((x, y))
        queue.append((capacity_jug1, y, steps + [(x, y, f"Fill jug 1")]))
        queue.append((x, capacity_jug2, steps + [(x, y, f"Fill jug 2")]))
        queue.append((0, y, steps + [(x, y, f"Empty jug 1")]))
        queue.append((x, 0, steps + [(x, y, f"Empty jug 2")]))
        pour_amount = min(x, capacity_jug2 - y)
        queue.append((x - pour_amount, y + pour_amount, steps + [(x, y, f"Pour jug 1 to jug 2")]))
        pour_amount = min(y, capacity_jug1 - x)
        queue.append((x + pour_amount, y - pour_amount, steps + [(x, y, f"Pour jug 2 to jug 1")]))
    return []
def solve_water_jug_problem():
    jug1_capacity = int(jug1_entry.get())
    jug2_capacity = int(jug2_entry.get())
    target_amount = int(target_entry.get())
    steps = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)
    if steps:
        display_steps(steps)
    else:
        result_text.config(text=f"It is not possible to measure {target_amount} units of water.")
def display_steps(steps):
    result_text.delete("1.0", tk.END)
    for i, step in enumerate(steps):
        x, y, action = step
        result_text.insert(tk.END, f"Step {i+1}: Jug 1={x} units, Jug 2={y} units\n")
        result_text.insert(tk.END, f"Action: {action}\n\n")
        result_text.update()
# Create the main window
window = tk.Tk()
window.title("Water Jug Problem Solver")
jug1_label = tk.Label(window, text="Jug 1 Capacity:")
jug1_label.pack()
jug1_entry = tk.Entry(window)
jug1_entry.pack()
jug2_label = tk.Label(window, text="Jug 2 Capacity:")
jug2_label.pack()
jug2_entry = tk.Entry(window)
jug2_entry.pack()
target_label = tk.Label(window, text="Target Amount:")
target_label.pack()
target_entry = tk.Entry(window)
target_entry.pack()
solve_button = tk.Button(window, text="Solve", command=solve_water_jug_problem)
solve_button.pack()
result_text = tk.Text(window, height=10, width=40)
result_text.pack()
window.mainloop()
