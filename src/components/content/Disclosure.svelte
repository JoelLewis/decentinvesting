<script lang="ts">
  import type { Snippet } from 'svelte';

  let { title, children }: { title: string; children: Snippet } = $props();
  let open = $state(false);
</script>

<div class="my-4 border border-sage-200 dark:border-sage-800 rounded-lg overflow-hidden">
  <button
    onclick={() => open = !open}
    class="w-full flex items-center justify-between gap-3 px-4 py-3 text-left text-sm font-medium
           text-sage-800 dark:text-sage-200
           bg-sage-50/70 dark:bg-sage-950/40
           hover:bg-sage-100 dark:hover:bg-sage-900/60
           transition-colors cursor-pointer"
    aria-expanded={open}
  >
    <span class="flex items-center gap-2">
      <svg
        class="w-4 h-4 text-sage-500 dark:text-sage-400 transition-transform duration-200 shrink-0"
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
    <span class="text-xs text-sage-500 dark:text-sage-500 shrink-0">
      {open ? 'collapse' : 'expand'}
    </span>
  </button>

  {#if open}
    <div class="px-4 py-3 text-sm border-t border-sage-200 dark:border-sage-800 bg-white dark:bg-gray-950">
      {@render children()}
    </div>
  {/if}
</div>
