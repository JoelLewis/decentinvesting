"""
Compound interest growth visualization.
Renders a 30-second clip showing $10K growing over 30 years at 8%.

Usage:
    manim render manim/scenes/compounding.py CompoundingScene -qh
"""

from manim import *


class CompoundingScene(Scene):
    def construct(self):
        # Title
        title = Text("The Power of Compounding", font_size=36, color=WHITE)
        subtitle = Text(
            "$10,000 at 8% annual return", font_size=24, color=GREY_B
        )
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Axes
        axes = Axes(
            x_range=[0, 30, 5],
            y_range=[0, 120000, 20000],
            x_length=10,
            y_length=5,
            axis_config={"include_numbers": False, "color": GREY_C},
        )

        x_labels = axes.get_x_axis().add_labels(
            {0: "0", 5: "5", 10: "10", 15: "15", 20: "20", 25: "25", 30: "30yr"},
            font_size=20,
        )
        y_labels = axes.get_y_axis().add_labels(
            {
                0: "$0",
                20000: "$20K",
                40000: "$40K",
                60000: "$60K",
                80000: "$80K",
                100000: "$100K",
            },
            font_size=18,
        )

        self.play(Create(axes), run_time=1)

        # Growth curve
        rate = 0.08

        def growth(t):
            return 10000 * (1 + rate) ** t

        curve = axes.plot(growth, x_range=[0, 30], color="#4a7c59", stroke_width=3)

        # Contribution baseline (flat line at $10K)
        baseline = axes.plot(lambda t: 10000, x_range=[0, 30], color=GREY_B)
        baseline_label = Text("Your $10K", font_size=16, color=GREY_B)
        baseline_label.next_to(axes.c2p(30, 10000), RIGHT, buff=0.2)

        self.play(Create(baseline), Write(baseline_label), run_time=1)

        # Animate growth
        self.play(Create(curve), run_time=4, rate_func=linear)

        # Final value label
        final_val = growth(30)
        final_label = Text(
            f"${final_val:,.0f}", font_size=28, color="#4a7c59", weight=BOLD
        )
        final_label.next_to(axes.c2p(30, final_val), RIGHT, buff=0.3)

        growth_label = Text(
            f"${final_val - 10000:,.0f} in growth", font_size=18, color="#6aad7a"
        )
        growth_label.next_to(final_label, DOWN, buff=0.2)

        self.play(Write(final_label), run_time=0.5)
        self.play(FadeIn(growth_label, shift=UP * 0.2), run_time=0.5)

        # Fill area under curve
        area = axes.get_area(curve, x_range=[0, 30], color="#4a7c59", opacity=0.2)
        self.play(FadeIn(area), run_time=1)

        # Message
        message = Text(
            "Time is the most powerful ingredient.",
            font_size=24,
            color=WHITE,
        )
        message.to_edge(DOWN, buff=0.5)
        self.play(Write(message), run_time=1.5)
        self.wait(2)
