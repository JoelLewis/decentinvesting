# Decent Investing - AI Context

## 1. Project Overview

An educational single-page guide providing simple, practical steps to help most people build a strong financial foundation through investing. The site deliberately avoids complex strategies in favor of accessible, actionable advice.

- **Target Audience**: General public wanting to start investing safely
- **Tone**: Approachable, accessible, non-condescending. "Decent" as in "good enough for most people."
- **Legal**: Includes prominent disclaimers — this is not professional financial advice. Recommends consulting a lawyer, accountant, or registered financial advisor for specific situations.

## 2. Content Structure

Single-page guide (`docs/index.md`) with header-based navigation:

1. Building a cash cushion (emergency funds, savings)
2. Prioritizing investment accounts (401k, HSA, IRA, taxable brokerage — in order of tax efficiency)
3. Simple investment choices (diversified index funds, target date funds)

Content links to external resources (Wikipedia, Vanguard, etc.) for deeper learning.

## 3. Technical Stack

- **Framework**: VitePress (Vue 3-based static site generator)
- **Theme**: Default VitePress + minimal custom CSS
- **Deploy Target**: Cloudflare Pages
- **Note**: VitePress uses Vue under the hood. This is an intentional choice for a documentation site — it does not contradict the global "no Vue" preference for application development.

## 4. Project Structure

```
docs/
├── index.md                    # Main content (single-page guide)
└── .vitepress/
    ├── config.mts              # Site config (title, sidebar, footer)
    ├── theme/
    │   ├── index.ts            # Theme entry point
    │   └── custom.css          # Brand colors (warm sage/forest green palette)
    ├── cache/                  # Build artifacts (gitignored)
    └── dist/                   # Production build output (gitignored)
```

## 5. Conventions

- **Sidebar**: Statically defined in `config.mts`, linking to H2 anchor sections on the homepage
- **Colors**: Warm sage/forest green palette — intentionally "approachable, not finance bro"
- **Content edits**: All content changes go in `docs/index.md`
- **Theme changes**: CSS overrides in `docs/.vitepress/theme/custom.css`
- **Site config**: `docs/.vitepress/config.mts` for title, description, sidebar links, footer
- Clean URLs enabled (no `.html` extensions)
- Local search provider (no external dependencies)

## 6. Development Commands

```bash
npm run docs:dev       # Local development server
npm run docs:build     # Production build → docs/.vitepress/dist
npm run docs:preview   # Preview built site locally
```

## 7. Deployment

Cloudflare Pages with git-based CI/CD. `wrangler.jsonc` points assets to `docs/.vitepress/dist`.
