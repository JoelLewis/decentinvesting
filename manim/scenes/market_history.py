"""
The "price of admission" — market drawdowns and recoveries.
Shows major crashes over 50 years, emphasizing that every one recovered.

Usage:
    manim render manim/scenes/market_history.py MarketHistoryScene -qh
"""

from manim import *
import numpy as np


class MarketHistoryScene(Scene):
    def construct(self):
        title = Text("The Price of Admission", font_size=36, color=WHITE)
        subtitle = Text(
            "S&P 500: crashes, recoveries, and new highs",
            font_size=20,
            color=GREY_B,
        )
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Simplified S&P 500 trajectory (log scale feel, annual data)
        # Approximate: 1970=90, peaks and crashes, ending ~4800 in 2024
        years = list(range(1970, 2025))
        # Simplified growth with crashes baked in
        base = np.array([90 * (1.10) ** (y - 1970) for y in years], dtype=float)

        # Apply drawdowns
        crashes = {
            (1973, 1975): 0.52,  # Oil crisis
            (1987, 1988): 0.66,  # Black Monday
            (2000, 2003): 0.51,  # Dot-com
            (2007, 2009): 0.43,  # GFC
            (2020, 2020): 0.66,  # COVID
        }

        values = base.copy()
        for (start, end), trough_mult in crashes.items():
            start_idx = start - 1970
            end_idx = end - 1970
            mid = (start_idx + end_idx) // 2
            for i in range(start_idx, min(end_idx + 1, len(values))):
                progress = abs(i - mid) / max(end_idx - start_idx, 1)
                values[i] *= trough_mult + (1 - trough_mult) * progress

        axes = Axes(
            x_range=[1970, 2025, 10],
            y_range=[0, max(values) * 1.1, 1000],
            x_length=11,
            y_length=5,
            axis_config={"include_numbers": False, "color": GREY_C},
        )

        x_labels = axes.get_x_axis().add_labels(
            {1970: "'70", 1980: "'80", 1990: "'90", 2000: "'00", 2010: "'10", 2020: "'20"},
            font_size=18,
        )

        self.play(Create(axes), run_time=0.5)

        # Draw the growth line year by year
        points = [axes.c2p(years[i], values[i]) for i in range(len(years))]
        path = VMobject(color="#4a7c59", stroke_width=2.5)
        path.set_points_smoothly(points)

        self.play(Create(path), run_time=6, rate_func=linear)

        # Highlight crash zones
        crash_labels = [
            (1974, "Oil\nCrisis\n-48%"),
            (1987, "Black\nMonday\n-34%"),
            (2001, "Dot-com\n-49%"),
            (2008, "Financial\nCrisis\n-57%"),
            (2020, "COVID\n-34%"),
        ]

        for year, label_text in crash_labels:
            idx = year - 1970
            if idx < len(values):
                dot = Dot(axes.c2p(year, values[idx]), radius=0.08, color=RED_C)
                label = Text(label_text, font_size=12, color=RED_C)
                label.next_to(dot, DOWN, buff=0.15)
                self.play(FadeIn(dot), FadeIn(label), run_time=0.3)

        self.wait(1)

        # Final message
        message_1 = Text(
            "Every crash felt like the end of the world.",
            font_size=22,
            color=GREY_B,
        )
        message_1.to_edge(DOWN, buff=0.8)
        self.play(Write(message_1), run_time=1)
        self.wait(1.5)

        message_2 = Text(
            "Every one was followed by new highs.",
            font_size=24,
            color="#4a7c59",
            weight=BOLD,
        )
        message_2.to_edge(DOWN, buff=0.4)
        self.play(FadeOut(message_1), Write(message_2), run_time=1)
        self.wait(2)
