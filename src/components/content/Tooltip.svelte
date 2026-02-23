<script lang="ts">
  let { term, definition, href }: { term: string; definition: string; href?: string } = $props();
  let visible = $state(false);
</script>

<span
  class="relative inline-block"
  role="term"
  onmouseenter={() => (visible = true)}
  onmouseleave={() => (visible = false)}
  onfocusin={() => (visible = true)}
  onfocusout={() => (visible = false)}
>
  <button
    class="font-inherit cursor-help border-b border-dashed border-sage-400 bg-transparent p-0 text-sage-700 dark:border-sage-500 dark:text-sage-400"
    aria-describedby="{term}-tooltip"
    type="button"
  >
    {term}
  </button>

  {#if visible}
    <span
      id="{term}-tooltip"
      role="tooltip"
      class="absolute bottom-full left-1/2 z-50 mb-2 max-w-xs -translate-x-1/2 whitespace-normal rounded-lg bg-gray-800 px-3 py-2 text-xs text-white shadow-lg"
    >
      {definition}
      {#if href}
        <a {href} class="ml-1 text-sage-300 no-underline hover:text-sage-200">→ glossary</a>
      {/if}
    </span>
  {/if}
</span>
