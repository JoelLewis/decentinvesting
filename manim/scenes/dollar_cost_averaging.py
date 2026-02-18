"""
Dollar-cost averaging through volatility.
Shows how regular investing buys more shares when prices are low.

Usage:
    manim render manim/scenes/dollar_cost_averaging.py DCAScene -qh
"""

from manim import *
import numpy as np


class DCAScene(Scene):
    def construct(self):
        title = Text("Dollar-Cost Averaging", font_size=36, color=WHITE)
        subtitle = Text("$500/month, no matter what", font_size=22, color=GREY_B)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Price path with a crash and recovery
        months = 24
        t = np.arange(months)
        # Price: starts at $100, drops to $60, recovers to $120
        price = np.array(
            [
                100, 95, 85, 72, 65, 60, 58, 62, 70, 78, 85, 90,
                95, 100, 105, 108, 110, 112, 115, 118, 120, 122, 125, 128,
            ],
            dtype=float,
        )

        axes = Axes(
            x_range=[0, 24, 6],
            y_range=[0, 150, 30],
            x_length=10,
            y_length=4,
            axis_config={"include_numbers": False, "color": GREY_C},
        )
        axes.shift(UP * 0.5)

        x_labels = axes.get_x_axis().add_labels(
            {0: "0", 6: "6mo", 12: "12mo", 18: "18mo", 24: "24mo"},
            font_size=18,
        )
        y_labels = axes.get_y_axis().add_labels(
            {30: "$30", 60: "$60", 90: "$90", 120: "$120", 150: "$150"},
            font_size=16,
        )

        self.play(Create(axes), run_time=0.5)

        # Animate price line drawing and purchases
        monthly_investment = 500
        total_shares = 0
        total_invested = 0

        shares_text = always_redraw(
            lambda: Text(
                f"Shares: {total_shares:.1f}",
                font_size=20,
                color=GREY_B,
            ).to_corner(DR, buff=0.8)
        )
        invested_text = always_redraw(
            lambda: Text(
                f"Invested: ${total_invested:,.0f}",
                font_size=20,
                color=GREY_B,
            ).next_to(shares_text, UP, buff=0.2)
        )

        self.add(shares_text, invested_text)

        # Draw price line step by step with purchase dots
        for i in range(months):
            shares_bought = monthly_investment / price[i]
            total_shares += shares_bought
            total_invested += monthly_investment

            point = Dot(axes.c2p(i, price[i]), radius=0.06, color="#4a7c59")

            if i > 0:
                line_seg = Line(
                    axes.c2p(i - 1, price[i - 1]),
                    axes.c2p(i, price[i]),
                    color=BLUE_C,
                    stroke_width=2,
                )
                self.play(Create(line_seg), FadeIn(point), run_time=0.15)
            else:
                self.play(FadeIn(point), run_time=0.15)

            # Larger dot during crash (buying more shares)
            if price[i] < 70:
                big_dot = Dot(
                    axes.c2p(i, price[i]),
                    radius=0.12,
                    color="#4a7c59",
                    fill_opacity=0.5,
                )
                self.play(FadeIn(big_dot), run_time=0.1)

        self.wait(0.5)

        # Summary
        final_value = total_shares * price[-1]
        avg_price = total_invested / total_shares

        summary = VGroup(
            Text(f"Total invested: ${total_invested:,.0f}", font_size=22, color=GREY_B),
            Text(f"Average price per share: ${avg_price:.2f}", font_size=22, color=GREY_B),
            Text(
                f"Final value: ${final_value:,.0f}",
                font_size=26,
                color="#4a7c59",
                weight=BOLD,
            ),
        ).arrange(DOWN, buff=0.3)
        summary.to_edge(DOWN, buff=0.4)

        self.play(Write(summary[0]), run_time=0.5)
        self.play(Write(summary[1]), run_time=0.5)
        self.play(Write(summary[2]), run_time=0.5)
        self.wait(1)

        # Message
        message = Text(
            "The crash was the best thing that happened — you bought cheap.",
            font_size=20,
            color="#6aad7a",
        )
        message.to_edge(DOWN, buff=0.2)
        self.play(FadeOut(summary), Write(message), run_time=1)
        self.wait(2)
