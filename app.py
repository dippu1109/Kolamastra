import streamlit as st
from PIL import Image
import io
import matplotlib.pyplot as plt

# Import Kolam generator functions
from main import (
    plot_grid_kolam, plot_polar_kolam,
    plot_flower_kolam, plot_star_kolam, plot_spiral_kolam
)

# -----------------------
# Helper: convert fig → PNG
# -----------------------
def fig_to_png_bytes(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", dpi=300, facecolor="white")
    buf.seek(0)
    return buf

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="Kolamastra",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Ambient Header
st.markdown(
    """
    <style>
    .main {background-color: #f9fafc;}
    h1 {text-align: center; color: #7b2cbf; font-family: 'Trebuchet MS';}
    h2 {color: #5a189a;}
    .stButton>button {background-color:#7b2cbf;color:white;border-radius:10px;}
    .stButton>button:hover {background-color:#9d4edd;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Kolamastra 🌸")
st.markdown("#### *Preserving tradition through algorithms*")

# Sidebar for global settings
st.sidebar.header("⚙️ Global Settings")
line_width = st.sidebar.slider("Line Width", 0.5, 3.0, 1.5)
fig_size = st.sidebar.slider("Figure Size", 4, 10, 6)

# Dropdown for Kolam type
mode = st.selectbox(
    "✨ Choose Kolam Type",
    ["Grid Kolam", "Polar Kolam", "Flower Kolam", "Star Kolam", "Spiral Kolam"]
)

# -----------------------
# Grid Kolam
# -----------------------
if mode == "Grid Kolam":
    st.subheader("Grid Kolam (Dot Grid Principle)")
    rows = st.slider("Rows", 3, 12, 6)
    cols = st.slider("Columns", 3, 12, 6)
    spacing = st.slider("Spacing", 0.6, 2.0, 1.0)
    offset = st.checkbox("Offset rows", True)
    color = st.color_picker("Choose line color", "#000000")

    if st.button("Generate Grid Kolam"):
        fig = plot_grid_kolam(rows, cols, spacing, offset, True, 3, line_width, fig_size)
        for ax in fig.axes:
            for line in ax.get_lines():
                line.set_color(color)
        buf = fig_to_png_bytes(fig)
        st.image(Image.open(buf), caption="Grid Kolam", use_column_width=True)
        st.download_button("⬇️ Download PNG", data=buf, file_name="grid_kolam.png", mime="image/png")

# -----------------------
# Polar Kolam
# -----------------------
elif mode == "Polar Kolam":
    st.subheader("Polar Kolam (Radial Symmetry)")
    symmetry = st.slider("Symmetry", 3, 12, 6)
    size = st.slider("Size", 4, 20, 10)
    color = st.color_picker("Choose accent color", "#1f77b4")

    if st.button("Generate Polar Kolam"):
        fig = plot_polar_kolam(symmetry, size, color, line_width, fig_size)
        buf = fig_to_png_bytes(fig)
        st.image(Image.open(buf), caption="Polar Kolam", use_column_width=True)
        st.download_button("⬇️ Download PNG", data=buf, file_name="polar_kolam.png", mime="image/png")

# -----------------------
# Flower Kolam
# -----------------------
elif mode == "Flower Kolam":
    st.subheader("Flower Kolam (Petal Symmetry)")
    petals = st.slider("Petals", 4, 16, 8)
    radius = st.slider("Radius", 2, 10, 5)
    color = st.color_picker("Choose petal color", "#d6336c")

    if st.button("Generate Flower Kolam"):
        fig = plot_flower_kolam(petals, radius, color, line_width, fig_size)
        buf = fig_to_png_bytes(fig)
        st.image(Image.open(buf), caption="Flower Kolam", use_column_width=True)
        st.download_button("⬇️ Download PNG", data=buf, file_name="flower_kolam.png", mime="image/png")

# -----------------------
# Star Kolam
# -----------------------
elif mode == "Star Kolam":
    st.subheader("Star Kolam (Polygon Symmetry)")
    sides = st.slider("Star points", 3, 12, 6)
    layers = st.slider("Layers", 1, 5, 3)
    color = st.color_picker("Choose star color", "#2a9d8f")

    if st.button("Generate Star Kolam"):
        fig = plot_star_kolam(sides, layers, 5, color, line_width, fig_size)
        buf = fig_to_png_bytes(fig)
        st.image(Image.open(buf), caption="Star Kolam", use_column_width=True)
        st.download_button("⬇️ Download PNG", data=buf, file_name="star_kolam.png", mime="image/png")

# -----------------------
# Spiral Kolam
# -----------------------
elif mode == "Spiral Kolam":
    st.subheader("Spiral Kolam (Continuous Curves)")
    turns = st.slider("Turns", 2, 10, 4)
    spacing = st.slider("Spacing", 0.1, 0.5, 0.2)
    color = st.color_picker("Choose spiral color", "#e63946")

    if st.button("Generate Spiral Kolam"):
        fig = plot_spiral_kolam(turns, 500, spacing, color, line_width, fig_size)
        buf = fig_to_png_bytes(fig)
        st.image(Image.open(buf), caption="Spiral Kolam", use_column_width=True)
        st.download_button("⬇️ Download PNG", data=buf, file_name="spiral_kolam.png", mime="image/png")
        
import random

# -----------------------
# Surprise Me Mode 🎲
# -----------------------
st.markdown("---")
st.subheader("🎲 Surprise Me!")

if st.button("Generate Random Kolam"):
    mode = random.choice(["Grid Kolam", "Polar Kolam", "Flower Kolam", "Star Kolam", "Spiral Kolam"])
    st.info(f"✨ Surprise Kolam Type: {mode}")

    if mode == "Grid Kolam":
        rows = random.randint(4, 10)
        cols = random.randint(4, 10)
        spacing = round(random.uniform(0.8, 1.5), 2)
        offset = random.choice([True, False])
        color = random.choice(["#000000", "#ff4500", "#1f77b4", "#2a9d8f"])
        fig = plot_grid_kolam(rows, cols, spacing, offset)
        for ax in fig.axes:
            for line in ax.get_lines():
                line.set_color(color)

    elif mode == "Polar Kolam":
        symmetry = random.randint(4, 10)
        size = random.randint(6, 15)
        color = random.choice(["#d62828", "#457b9d", "#ffb703"])
        fig = plot_polar_kolam(symmetry, size, color)

    elif mode == "Flower Kolam":
        petals = random.randint(5, 12)
        radius = random.randint(3, 8)
        color = random.choice(["#9d4edd", "#e63946", "#2a9d8f"])
        fig = plot_flower_kolam(petals, radius, color)

    elif mode == "Star Kolam":
        sides = random.randint(5, 10)
        layers = random.randint(2, 4)
        color = random.choice(["#264653", "#f4a261", "#e76f51"])
        fig = plot_star_kolam(sides, layers, 5, color)

    else:  # Spiral Kolam
        turns = random.randint(3, 8)
        spacing = round(random.uniform(0.15, 0.3), 2)
        color = random.choice(["#118ab2", "#06d6a0", "#ef476f"])
        fig = plot_spiral_kolam(turns, 500, spacing, color)

    buf = fig_to_png_bytes(fig)
    st.image(Image.open(buf), caption=f"🎲 Surprise Kolam: {mode}", use_container_width=True)
    st.download_button("⬇️ Download PNG", data=buf, file_name=f"surprise_{mode.lower().replace(' ','_')}.png", mime="image/png")
    buf = fig_to_png_bytes(fig)
    