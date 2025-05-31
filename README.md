<!-- ──────────── Demo GIF ──────────── -->
<!-- Replace `Maze-Solver.gif` with your actual file name -->
![Maze-Solver Demo](Maze-Solver.gif)

# Maze-Solver

A fully-animated maze generator and solver built with **Python + Tkinter**.

**Flow**

1. **Grid** – create a 2-D list of `Cell` objects.
2. **Carve** – depth-first search (recursive backtracker) knocks down walls.
3. **Reset** – clear `visited` flags.
4. **Solve** – DFS again: red = forward path, gray = back-track.

Pass a `seed` for repeatable mazes; omit it for fresh randomness.

---

## Features
* Deterministic **seed** option for debugging/benchmarks.
* **Headless unit tests** (UI skipped when `win=None`).
* Clean split: logic (`maze.py`, `cell.py`) vs UI (`window.py`).
* Easy to plug in BFS, A\*, etc.

---

## Setup

```bash
git clone https://github.com/<your-user>/Maze-Solver.git
cd Maze-Solver
python -m venv .venv && source .venv/bin/activate   # optional venv
pip install -r requirements.txt                     # none needed for basic run

Note: Tkinter ships with standard Python on Windows/macOS.
On Linux install it via your package manager (sudo apt install python3-tk).

⸻

Run

python main.py

Tweak size / seed in main.py:

m = Maze(
    x1=40, y1=40,
    num_rows=20, num_cols=30,
    cell_size_x=25, cell_size_y=25,
    win=win,
    seed=0          # comment out for true randomness
)


⸻

Tests

python tests.py

Boot.dev autograder:

bootdev run 4eac6dbf-8944-4d7a-bf4c-c35692b72ad7


⸻

Extension Ideas

Idea	Quick Hint
BFS / A*	Queue or heapq based variant of solve()
Custom colours	Edit literals in cell.py (bg, wall, path)
Variable speed	Replace time.sleep with a Tk slider value
User game	Move a player dot with arrow keys; race the algorithm
3-D maze	Extend cells to (x,y,z) and visualise layers or export to WebGL

