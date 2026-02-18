<script lang="ts">
  type Heading = { depth: number; slug: string; text: string };

  let { headings }: { headings: Heading[] } = $props();
</script>

<nav class="text-xs" aria-label="On this page">
  <h3 class="font-semibold text-gray-900 dark:text-gray-100 mb-3 uppercase tracking-wider">
    On this page
  </h3>
  <ul class="space-y-1.5">
    {#each headings as heading}
      <li style="padding-left: {(heading.depth - 2) * 0.75}rem">
        <a
          href="#{heading.slug}"
          class="block text-gray-500 dark:text-gray-400 no-underline hover:text-sage-600 dark:hover:text-sage-300 transition-colors leading-snug"
        >
          {heading.text}
        </a>
      </li>
    {/each}
  </ul>
</nav>
