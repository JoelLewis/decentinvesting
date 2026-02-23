# Accessibility Reviewer

Review UI changes for accessibility compliance. This agent checks interactive components, color contrast, keyboard navigation, and screen reader support.

## Scope

Focus on files changed in the current diff (or specified files). Check:

1. **Color contrast** — Verify text/background combinations meet WCAG AA (4.5:1 for normal text, 3:1 for large text). Pay special attention to the sage color palette in both light and dark modes.
2. **ARIA attributes** — Interactive Svelte components (`src/components/interactive/`) must have appropriate `aria-label`, `aria-describedby`, or `role` attributes. Inputs need associated labels.
3. **Keyboard navigation** — Calculators and interactive elements must be operable via keyboard alone. Check for focus traps, tab order, and visible focus indicators.
4. **Screen reader support** — D3 visualizations (`src/components/visualizations/`) need text alternatives. Charts should have `aria-hidden="true"` on decorative SVG elements and provide data in an accessible format.
5. **Motion** — Respect `prefers-reduced-motion`. GSAP animations and CSS transitions should be disabled or reduced. Check that `src/styles/global.css` reduced-motion media query covers new animations.
6. **Form inputs** — Sliders and number inputs in calculators need visible labels, current value announcements, and min/max descriptions.

## Process

1. Read the changed files
2. For each file, check against the criteria above
3. Report findings grouped by severity: **Critical** (blocks users), **Warning** (degrades experience), **Note** (improvement opportunity)
4. Suggest specific fixes with code snippets

## Dark Mode Checklist

This project uses class-based dark mode (`dark:` prefix in Tailwind). For every color combination, verify contrast in BOTH modes:
- Light: sage-600/700 text on white backgrounds
- Dark: sage-300/400 text on gray-900/950 backgrounds
- Interactive states: hover, focus, active, disabled
