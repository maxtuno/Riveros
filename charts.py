import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.unicode_minus": False,
    "axes.edgecolor": "#c9c9c9",
    "axes.linewidth": 0.8,
    "figure.dpi": 150,
})

OUT = "graficos"
os.makedirs(OUT, exist_ok=True)

INK = "#1d2733"
GREY = "#9aa5b1"
RED = "#c1121f"
GREEN = "#2a9d8f"
BLUE = "#3d5a80"
LIGHT = "#e6e9ee"

SOURCE = "Fuente: The Art Basel & UBS Art Market Report 2026 (Arts Economics)"


def finish(fig, ax_list, path, note=SOURCE):
    for ax in ax_list:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(colors=INK, labelsize=9)
        ax.set_axisbelow(True)
    fig.text(0.01, 0.015, note, fontsize=7.5, color="#6b7280")
    fig.savefig(os.path.join(OUT, path), bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", path)


# ---------------------------------------------------------------- 1. mercado
def chart_global():
    years = ["2020", "2021", "2022", "2023", "2024", "2025"]
    vals = [50.3, 66.1, 68.1, 65.2, 57.4, 59.6]
    colors = [GREY, GREY, GREY, GREY, RED, BLUE]
    fig, ax = plt.subplots(figsize=(9, 5.2))
    bars = ax.bar(years, vals, color=colors, width=0.62, zorder=3)
    ax.axhline(68.1, color=RED, ls="--", lw=1.2, zorder=2)
    ax.text(5.45, 68.5, "Pico 2022: 68,1", color=RED, fontsize=9, ha="right")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.9, f"{v:.1f}", ha="center",
                fontsize=9.5, color=INK, fontweight="bold")
    ax.annotate("2025: 59,6\n(+4%)", xy=(5, 59.6), xytext=(4.15, 63),
                fontsize=9, color=BLUE, ha="center",
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1))
    ax.set_ylim(0, 76)
    ax.set_ylabel("Miles de millones de USD", fontsize=9.5)
    ax.set_title("El mercado global volvió a crecer en 2025 (+4%)…\n"
                 "pero sigue un 12% por debajo del pico de 2022",
                 fontsize=12.5, color=INK, fontweight="bold", loc="left")
    ax.grid(axis="y", color=LIGHT, zorder=0)
    finish(fig, [ax], "01_mercado_global.png")


# ------------------------------------------------------ 2. variación anual
def chart_yoy():
    years = ["2021", "2022", "2023", "2024", "2025"]
    vals = [31, 3, -4, -12, 4]
    colors = [GREEN if v > 0 else RED for v in vals]
    fig, ax = plt.subplots(figsize=(9, 5.2))
    bars = ax.bar(years, vals, color=colors, width=0.6, zorder=3)
    ax.axhline(0, color=INK, lw=1)
    for b, v in zip(bars, vals):
        off = 1.2 if v >= 0 else -2.6
        ax.text(b.get_x() + b.get_width() / 2, v + off, f"{v:+d}%", ha="center",
                fontsize=10, fontweight="bold", color=INK)
    ax.annotate("el +4% de 2025 es un rebote\npequeño tras dos años de caída",
                xy=(4, 4), xytext=(2.55, 17), fontsize=9.5, color=RED, ha="center",
                arrowprops=dict(arrowstyle="->", color=RED, lw=1))
    ax.set_ylim(-16, 36)
    ax.set_ylabel("Variación anual de las ventas (%)", fontsize=9.5)
    ax.set_title("Rebote, no recuperación: el «+4%» llega después de caer 12% (2024) y 4% (2023)",
                 fontsize=12, color=INK, fontweight="bold", loc="left")
    ax.grid(axis="y", color=LIGHT, zorder=0)
    finish(fig, [ax], "02_variacion_anual.png")


# ------------------------------------------------------ 3. galerías / márgenes
def chart_dealers():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.2))
    labels = ["Ventas", "Costos\noperativos"]
    vals = [2, 5]
    bars = ax1.bar(labels, vals, color=[BLUE, RED], width=0.55, zorder=3)
    for b, v in zip(bars, vals):
        ax1.text(b.get_x() + b.get_width() / 2, v + 0.15, f"+{v}%", ha="center",
                 fontsize=12, fontweight="bold", color=INK)
    ax1.set_ylim(0, 6)
    ax1.set_ylabel("Cambio 2024–2025 (%)", fontsize=9.5)
    ax1.set_title("Los costos suben más que las ventas", fontsize=11.5,
                  color=INK, fontweight="bold", loc="left")
    ax1.grid(axis="y", color=LIGHT, zorder=0)

    seg = ["Más rentable\nque 2024", "Igual", "Menos rentable\nque 2024"]
    sv = [33, 29, 38]
    sc = [GREEN, GREY, RED]
    bars2 = ax2.bar(seg, sv, color=sc, width=0.55, zorder=3)
    for b, v in zip(bars2, sv):
        ax2.text(b.get_x() + b.get_width() / 2, v + 0.6, f"{v}%", ha="center",
                 fontsize=12, fontweight="bold", color=INK)
    ax2.set_ylim(0, 45)
    ax2.set_ylabel("Galerías (%)", fontsize=9.5)
    ax2.set_title("Más galerías ganaron menos que más", fontsize=11.5,
                  color=INK, fontweight="bold", loc="left")
    ax2.grid(axis="y", color=LIGHT, zorder=0)

    fig.suptitle("Galerías 2025: venden apenas más, pero gastan más rápido",
                 fontsize=13, color=INK, fontweight="bold", x=0.01, ha="left", y=1.02)
    finish(fig, [ax1, ax2], "03_galerias_margenes.png")


# ------------------------------------------------------ 4. concentración
def chart_concentration():
    labels = ["Top 1 artista\n(media general)", "Top 3 artistas\n(media general)",
              "Top 3 en galerías\npequeñas (<250k$)", "Top 3 en galerías\ngrandes (>10M$)"]
    vals = [33, 58, 65, 48]
    colors = [BLUE, RED, RED, BLUE]
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    bars = ax.barh(labels[::-1], vals[::-1], color=colors[::-1], height=0.6, zorder=3)
    for b, v in zip(bars, vals[::-1]):
        ax.text(v + 1, b.get_y() + b.get_height() / 2, f"{v}%", va="center",
                fontsize=11, fontweight="bold", color=INK)
    ax.set_xlim(0, 75)
    ax.set_xlabel("Porcentaje de las ventas de una galería", fontsize=9.5)
    ax.set_title("Pocos artistas sostienen casi todo el negocio\n"
                 "Con ~32 artistas por galería, el 11% genera el 58% de las ventas",
                 fontsize=12, color=INK, fontweight="bold", loc="left")
    ax.grid(axis="x", color=LIGHT, zorder=0)
    finish(fig, [ax], "04_concentracion_artistas.png")


# ------------------------------------------------------ 5. subastas segmentos
def chart_auction_segments():
    labels = ["Obras > $10 M", "$1 M – $10 M", "$50k – $250k", "Obras < $50k"]
    vals = [30, 21, 0, -2]
    colors = [GREEN, GREEN, GREY, RED]
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    bars = ax.barh(labels[::-1], vals[::-1], color=colors[::-1], height=0.58, zorder=3)
    ax.axvline(0, color=INK, lw=1)
    for b, v in zip(bars, vals[::-1]):
        off = 0.7 if v >= 0 else -2.6
        ax.text(v + off, b.get_y() + b.get_height() / 2, f"{v:+d}%", va="center",
                fontsize=11, fontweight="bold", color=INK)
    ax.set_xlim(-7, 36)
    ax.set_xlabel("Cambio en el valor de las ventas 2024–2025 (%)", fontsize=9.5)
    ax.set_title("En subasta, solo crece la punta\n"
                 "El 95% de las obras vendidas cuesta menos de $50.000 y ese segmento cae",
                 fontsize=12, color=INK, fontweight="bold", loc="left")
    ax.grid(axis="x", color=LIGHT, zorder=0)
    finish(fig, [ax], "05_subastas_segmentos.png")


# ------------------------------------------------------ 6. contemporáneo
def chart_contemporary():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.2))
    bars = ax1.bar(["2021\n(pico)", "2025"], [21, 3], color=[GREY, RED], width=0.5, zorder=3)
    for b, v in zip(bars, [21, 3]):
        ax1.text(b.get_x() + b.get_width() / 2, v + 0.5, str(v), ha="center",
                 fontsize=13, fontweight="bold", color=INK)
    ax1.set_ylim(0, 25)
    ax1.set_ylabel("Nº de obras recientes vendidas > $10 M", fontsize=9.5)
    ax1.set_title("Obras creadas en los últimos 20 años\nque superaron $10 M en subasta",
                  fontsize=11, color=INK, fontweight="bold", loc="left")
    ax1.grid(axis="y", color=LIGHT, zorder=0)

    ax2.plot(["2021", "2022", "2023", "2025"], [34, 30, 23, 19], color=RED,
             marker="o", lw=2.5, zorder=3)
    for x, y in zip(["2021", "2022", "2023", "2025"], [34, 30, 23, 19]):
        ax2.text(x, y + 1.4, f"{y}%", ha="center", fontsize=10.5, fontweight="bold", color=INK)
    ax2.set_ylim(0, 40)
    ax2.set_ylabel("% del valor del sector", fontsize=9.5)
    ax2.set_title("Peso del arte «reciente» en el sector\ncontemporáneo: en caída",
                  fontsize=11, color=INK, fontweight="bold", loc="left")
    ax2.grid(axis="y", color=LIGHT, zorder=0)

    fig.suptitle("El arte contemporáneo lleva 4 años cayendo y el arte nuevo se reduce",
                 fontsize=13, color=INK, fontweight="bold", x=0.01, ha="left", y=1.02)
    finish(fig, [ax1, ax2], "06_contemporaneo.png",
           SOURCE + "  |  Sector Postguerra/Contemporáneo: 4.500 M$ en 2025, mínimo en 10 años.")


# ------------------------------------------------------ 7. género
def chart_gender():
    groups = ["Todas las galerías", "Galerías < $250k", "Galerías > $10 M"]
    rep = [45, 55, 35]
    sal = [37, 43, 27]
    x = range(len(groups))
    w = 0.36
    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    b1 = ax.bar([i - w / 2 for i in x], rep, width=w, color=BLUE,
                label="% de artistas mujeres representadas", zorder=3)
    b2 = ax.bar([i + w / 2 for i in x], sal, width=w, color=RED,
                label="% de ventas generadas por mujeres", zorder=3)
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1,
                    f"{b.get_height():.0f}%", ha="center", fontsize=10,
                    fontweight="bold", color=INK)
    ax.set_xticks(list(x))
    ax.set_xticklabels(groups, fontsize=10)
    ax.set_ylim(0, 65)
    ax.set_ylabel("Porcentaje (%)", fontsize=9.5)
    ax.legend(frameon=False, fontsize=9.5, loc="upper right")
    ax.set_title("Más representación, menos ventas: la brecha no se cierra al subir\n"
                 "En subasta, solo 11% de los 200 artistas más vendidos son mujeres (8% del valor)",
                 fontsize=11.5, color=INK, fontweight="bold", loc="left")
    ax.grid(axis="y", color=LIGHT, zorder=0)
    finish(fig, [ax], "07_genero.png")


chart_global()
chart_yoy()
chart_dealers()
chart_concentration()
chart_auction_segments()
chart_contemporary()
chart_gender()
print("OK")
