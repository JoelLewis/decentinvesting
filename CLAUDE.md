Deployment Guide

Follow these steps to structure your project and deploy to Cloudflare Pages.

1. Folder Structure

Create a new folder on your computer and set it up exactly like this:

my-investing-site/
├── package.json              <-- (The file I generated above)
└── docs/
    ├── .vitepress/
    │   └── config.mts        <-- (The file I generated above)
    └── index.md              <-- (RENAME "Decent Investing.md" to this and place here)


Note: VitePress uses index.md as the homepage. You must rename your file.

2. Local Testing (Optional but Recommended)

If you have Node.js installed:

Open your terminal in the my-investing-site folder.

Run npm install to get the dependencies.

Run npm run docs:dev.

Open the localhost link provided to see your site.

3. Push to GitHub/GitLab

Initialize git: git init

Create a .gitignore file with the following content:

node_modules
docs/.vitepress/dist
docs/.vitepress/cache


Commit your files and push them to a new repository on GitHub or GitLab.

4. Deploy to Cloudflare Pages

Log in to the Cloudflare Dashboard.

Go to Workers & Pages -> Create Application -> Connect to Git.

Select the repository you just created.

Build Settings:

Framework Preset: Select VitePress.

Build command: npm run docs:build (Cloudflare should auto-detect this).

Build output directory: docs/.vitepress/dist (Cloudflare should auto-detect this).

Click Save and Deploy.

Cloudflare will build the site and give you a *.pages.dev URL.