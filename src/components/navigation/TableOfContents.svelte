<script lang="ts">
  type Heading = { depth: number; slug: string; text: string };

  let { headings }: { headings: Heading[] } = $props();
</script>

<nav class="text-xs" aria-label="On this page">
  <h3 class="mb-3 font-semibold uppercase tracking-wider text-gray-900 dark:text-gray-100">
    On this page
  </h3>
  <ul class="space-y-1.5">
    {#each headings as heading}
      <li style="padding-left: {(heading.depth - 2) * 0.75}rem">
        <a
          href="#{heading.slug}"
          class="block leading-snug text-gray-500 no-underline transition-colors hover:text-sage-600 dark:text-gray-400 dark:hover:text-sage-300"
        >
          {heading.text}
        </a>
      </li>
    {/each}
  </ul>
</nav>
