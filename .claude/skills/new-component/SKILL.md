---
name: new-component
description: Scaffold a new Svelte or Astro component in the correct category directory with appropriate boilerplate
disable-model-invocation: true
---

# New Component Scaffold

Create a new component with the right boilerplate for its category.

## Usage

`/new-component <category> <ComponentName>`

Categories: `interactive`, `visualizations`, `content`, `navigation`, `layout`, `ui`

## Process

1. Determine the category and component name from arguments
2. Choose file type based on category:
   - `interactive/`, `visualizations/`, `navigation/`, `ui/` → Svelte 5 (`.svelte`)
   - `layout/`, `content/` → Astro (`.astro`), unless interactivity is needed (then Svelte)
3. Create the file at `src/components/<category>/<ComponentName>.svelte` (or `.astro`)
4. Apply the category-specific boilerplate below

## Boilerplate by Category

### interactive/ (Svelte 5)
Financial calculators with user inputs. Include:
- TypeScript `<script lang="ts">` block
- Import from `@/lib/calculations.ts` and `@/lib/constants.ts` as needed
- Svelte 5 runes (`$state`, `$derived`) for reactive values
- Accessible form inputs with labels
- Responsive container with dark mode support
- `prefers-reduced-motion` consideration for any animations

### visualizations/ (Svelte 5)
D3-powered charts. Include:
- TypeScript script block
- `import * as d3 from 'd3'` (import only needed modules)
- `$effect` for D3 bindings (binds to DOM after mount)
- Responsive SVG with viewBox
- `aria-hidden="true"` on decorative SVG, text alternative for screen readers
- Dark mode color awareness (check for `.dark` class or use CSS custom properties)
- Cleanup in `$effect` return function

### content/ (Astro)
Reusable content elements (callouts, disclosures, tooltips). Include:
- Typed `Props` with `type Props = { ... }`
- Tailwind classes with dark mode variants
- Semantic HTML
- Slot for child content where appropriate

### navigation/ (Svelte 5)
Navigation components. Include:
- TypeScript script block
- Props for current state (active page, scroll position, etc.)
- ARIA navigation roles (`role="navigation"`, `aria-current="page"`)
- Keyboard navigation support
- Responsive behavior (mobile/desktop variants)

### layout/ (Astro)
Page-level structural components. Include:
- Typed `Props`
- Slot for main content
- Tailwind layout utilities (flex, grid, max-w, mx-auto)

### ui/ (Svelte 5)
Reusable UI primitives (inputs, buttons). Include:
- TypeScript script block
- Props with sensible defaults
- Full accessibility: labels, ARIA attributes, keyboard support
- Forwarded events where needed
- Dark mode variants

## Example

For `/new-component interactive TaxBracketCalculator`:

Creates `src/components/interactive/TaxBracketCalculator.svelte` with:
```svelte
<script lang="ts">
  import { CONTRIBUTION_LIMITS } from '@/lib/constants';

  let income = $state(75_000);

  const effectiveTaxRate = $derived(/* calculation */);
</script>

<div class="rounded-lg border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-900 p-6">
  <h3 class="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-4">
    Tax Bracket Calculator
  </h3>

  <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
    Annual Income
    <input
      type="number"
      bind:value={income}
      class="mt-1 block w-full rounded-md border-gray-300 dark:border-gray-600 dark:bg-gray-800"
    />
  </label>

  <p class="mt-4 text-gray-600 dark:text-gray-400">
    Effective tax rate: <strong>{effectiveTaxRate}%</strong>
  </p>
</div>
```
