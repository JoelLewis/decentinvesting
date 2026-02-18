<script lang="ts">
  type Page = { slug: string; title: string; number: number };

  let { pages, currentSlug }: { pages: Page[]; currentSlug: string } = $props();
</script>

<nav class="text-sm" aria-label="Guide navigation">
  <h3 class="font-semibold text-gray-900 dark:text-gray-100 mb-3 text-xs uppercase tracking-wider">
    The Guide
  </h3>
  <ul class="space-y-1">
    {#each pages as page}
      <li>
        <a
          href="/guide/{page.slug}"
          class="block px-3 py-1.5 rounded-md no-underline transition-colors
            {currentSlug === page.slug
              ? 'bg-sage-100 dark:bg-sage-900/40 text-sage-700 dark:text-sage-300 font-medium'
              : 'text-gray-600 dark:text-gray-400 hover:text-sage-600 dark:hover:text-sage-300 hover:bg-sage-50 dark:hover:bg-sage-900/20'}"
          aria-current={currentSlug === page.slug ? 'page' : undefined}
        >
          {page.number > 0 ? `${page.number}. ` : ''}{page.title}
        </a>
      </li>
    {/each}
  </ul>

  <h3 class="font-semibold text-gray-900 dark:text-gray-100 mt-6 mb-3 text-xs uppercase tracking-wider">
    Reference
  </h3>
  <ul class="space-y-1">
    <li>
      <a
        href="/reference/glossary"
        class="block px-3 py-1.5 rounded-md no-underline text-gray-600 dark:text-gray-400 hover:text-sage-600 dark:hover:text-sage-300 hover:bg-sage-50 dark:hover:bg-sage-900/20 transition-colors"
      >
        Glossary
      </a>
    </li>
    <li>
      <a
        href="/reference/disclaimer"
        class="block px-3 py-1.5 rounded-md no-underline text-gray-600 dark:text-gray-400 hover:text-sage-600 dark:hover:text-sage-300 hover:bg-sage-50 dark:hover:bg-sage-900/20 transition-colors"
      >
        Disclaimer
      </a>
    </li>
  </ul>
</nav>
