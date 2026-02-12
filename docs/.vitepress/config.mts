import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Decent Investing",
  description: "Simple steps to help most people start and stay safe.",
  
  // Clean URLs (no .html extensions) look more professional
  cleanUrls: true,

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    
    // Top navigation bar (optional, good if you add more pages later)
    nav: [
      { text: 'Home', link: '/' }
    ],

    // Sidebar navigation - automatically generates based on your H2 headers
    sidebar: [
      {
        text: 'Guide',
        items: [
          { text: 'Start Here', link: '/' },
          { text: '1. Build Your Cash Cushion', link: '/#_1-build-your-cash-cushion' },
          { text: '2. Which Accounts to Use First', link: '/#_2-which-investment-accounts-to-use-first' },
          { text: '3. Simple Investment Choices', link: '/#_3-simple-investment-choices' },
          { text: 'Next Steps', link: '/#next-steps' },
          { text: 'Disclaimer', link: '/#disclaimer' },
        ]
      }
    ],

    socialLinks: [
      // Add your GitHub or Twitter if you want, otherwise delete this block
      // { icon: 'github', link: 'https://github.com/yourusername/project' }
    ],

    // Footer copyright
    footer: {
      message: 'Not financial advice. Read the disclaimer.',
      copyright: 'Copyright © 2024'
    },
    
    // Search functionality (runs locally, no server needed)
    search: {
      provider: 'local'
    }
  }
})