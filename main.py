import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Simple Chaikin smoothing
# -------------------------
def chaikin_smooth(points, iterations=3):
    pts = np.asarray(points)
    for _ in range(iterations):
        new_pts = []
        n = len(pts)
        for i in range(n):
            p0 = pts[i]
            p1 = pts[(i + 1) % n]
            Q = 0.75 * p0 + 0.25 * p1
            R = 0.25 * p0 + 0.75 * p1
            new_pts.append(Q)
            new_pts.append(R)
        pts = np.array(new_pts)
    return pts

# -------------------------
# Grid Kolam functions
# -------------------------
def make_dot_grid(rows=5, cols=5, spacing=1.0, offset=False):
    pts = []
    for r in range(rows):
        for c in range(cols):
            x = c * spacing + (0.5 * spacing if (offset and (r % 2 == 1)) else 0)
            y = -r * spacing
            pts.append((x, y))
    return np.array(pts)

def create_loops(rows, cols, spacing=1.0, margin=0.18):
    loops = []
    for r in range(rows - 1):
        for c in range(cols - 1):
            p1 = np.array([c * spacing, -r * spacing])
            p2 = np.array([(c + 1) * spacing, -r * spacing])
            p3 = np.array([(c + 1) * spacing, -(r + 1) * spacing])
            p4 = np.array([c * spacing, -(r + 1) * spacing])
            m1 = (p1 + p2) / 2 + np.array([0, margin])
            m2 = (p2 + p3) / 2 + np.array([margin, 0])
            m3 = (p3 + p4) / 2 + np.array([0, -margin])
            m4 = (p4 + p1) / 2 + np.array([-margin, 0])
            loop = np.vstack([m1, m2, m3, m4, m1])
            loops.append(loop)
    return loops

def plot_grid_kolam(rows=6, cols=6, spacing=1.0, offset=True, show_dots=True, smooth_iters=1,
                    linewidth=1.6, figsize=6, color="black"):
    """
    Grid Kolam generator:
    - Creates a dot grid
    - Draws rounded loops around each 2x2 square
    - Avoids spiral-like distortion
    """
    grid = make_dot_grid(rows, cols, spacing, offset)
    loops = create_loops(rows, cols, spacing)

    fig, ax = plt.subplots(figsize=(figsize, figsize))
    ax.set_facecolor("white")

    # draw dots
    if show_dots:
        ax.scatter(grid[:, 0], grid[:, 1], s=25, c="black")

    # draw loops
    for loop in loops:
        # Instead of over-smoothing, keep curves simple
        if smooth_iters > 0:
            smooth = chaikin_smooth(loop, iterations=smooth_iters)
            ax.plot(smooth[:, 0], smooth[:, 1], "-", lw=linewidth, color=color)
        else:
            ax.plot(loop[:, 0], loop[:, 1], "-", lw=linewidth, color=color)

    ax.set_aspect("equal")
    ax.axis("off")
    plt.tight_layout()
    return fig


# -------------------------
# Polar Kolam functions
# -------------------------
def plot_polar_kolam(symmetry=6, size=10, color="#1f77b4", linewidth=0.8, figsize=6):
    fig = plt.figure(figsize=(figsize, figsize))
    ax = plt.subplot(111, polar=True)
    ax.set_facecolor("white")
    plt.axis("off")

    num_circles = max(1, symmetry)
    num_lines = max(6, symmetry * 6)

    for i in range(1, num_circles + 1):
        radius = size * i / num_circles
        theta = np.linspace(0, 2 * np.pi, 400)
        ax.plot(theta, [radius] * len(theta), color="black", lw=0.6)

    for i in range(num_lines):
        angle = 2 * np.pi * i / num_lines
        ax.plot([angle, angle], [0, size], color="black", lw=0.6)

    for i in range(num_circles):
        radius = size * (i + 0.5) / num_circles
        for j in range(num_lines):
            angle = 2 * np.pi * j / num_lines
            delta = np.pi / num_lines
            theta = np.linspace(angle - delta, angle + delta, 40)
            r = radius + 0.08 * size * np.sin(5 * theta)
            ax.plot(theta, r, color=color, lw=linewidth)

    plt.tight_layout()
    return fig

# 1. Flower Petal Kolam 🌸
def plot_flower_kolam(petals=8, radius=5, color="purple", linewidth=1.5, figsize=6):
    fig, ax = plt.subplots(figsize=(figsize, figsize))
    ax.set_facecolor("white")
    ax.set_aspect("equal")
    plt.axis("off")

    theta = np.linspace(0, 2 * np.pi, 200)
    for i in range(petals):
        angle = 2 * np.pi * i / petals
        x = radius * np.cos(theta + angle) * np.sin(theta)
        y = radius * np.sin(theta + angle) * np.sin(theta)
        ax.plot(x, y, color=color, lw=linewidth)

    plt.tight_layout()
    return fig

# 2. Star/Polygon Kolam ⭐
def plot_star_kolam(sides=6, layers=3, size=5, color="green", linewidth=1.5, figsize=6):
    fig, ax = plt.subplots(figsize=(figsize, figsize))
    ax.set_facecolor("white")
    ax.set_aspect("equal")
    plt.axis("off")

    angles = np.linspace(0, 2 * np.pi, sides, endpoint=False)
    for layer in range(1, layers + 1):
        r = size * (layer / layers)
        x = r * np.cos(angles)
        y = r * np.sin(angles)
        ax.plot(np.append(x, x[0]), np.append(y, y[0]), color=color, lw=linewidth)

    plt.tight_layout()
    return fig

# 3. Spiral Kolam 🌀
def plot_spiral_kolam(turns=3, points=500, spacing=0.2, color="red", linewidth=1.5, figsize=6):
    fig, ax = plt.subplots(figsize=(figsize, figsize))
    ax.set_facecolor("white")
    ax.set_aspect("equal")
    plt.axis("off")

    theta = np.linspace(0, 2 * np.pi * turns, points)
    r = spacing * theta
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y, color=color, lw=linewidth)

    plt.tight_layout()
    return fig


# -------------------------
# Standalone run (for testing)
# -------------------------
if __name__ == "__main__":
    fig = plot_grid_kolam(rows=6, cols=6, spacing=1.0)
    plt.show()
