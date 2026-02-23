<script lang="ts">
  import type { Snippet } from 'svelte';

  let { title, children }: { title: string; children: Snippet } = $props();
  let open = $state(false);
</script>

<div class="my-4 overflow-hidden rounded-lg border border-sage-200 dark:border-sage-800">
  <button
    onclick={() => (open = !open)}
    class="flex w-full cursor-pointer items-center justify-between gap-3 bg-sage-50/70 px-4 py-3 text-left
           text-sm font-medium
           text-sage-800 transition-colors
           hover:bg-sage-100 dark:bg-sage-950/40
           dark:text-sage-200 dark:hover:bg-sage-900/60"
    aria-expanded={open}
  >
    <span class="flex items-center gap-2">
      <svg
        class="h-4 w-4 shrink-0 text-sage-500 transition-transform duration-200 dark:text-sage-400"
        class:rotate-90={open}
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        stroke-width="2.5"
      >
        <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
      </svg>
      {title}
    </span>
    <span class="shrink-0 text-xs text-sage-500 dark:text-sage-500">
      {open ? 'collapse' : 'expand'}
    </span>
  </button>

  {#if open}
    <div
      class="border-t border-sage-200 bg-white px-4 py-3 text-sm dark:border-sage-800 dark:bg-gray-950"
    >
      {@render children()}
    </div>
  {/if}
</div>
