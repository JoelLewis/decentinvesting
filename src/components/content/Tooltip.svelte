<script lang="ts">
  let { term, definition, href }: { term: string; definition: string; href?: string } = $props();
  let visible = $state(false);
</script>

<span
  class="relative inline-block"
  role="term"
  onmouseenter={() => visible = true}
  onmouseleave={() => visible = false}
  onfocusin={() => visible = true}
  onfocusout={() => visible = false}
>
  <button
    class="border-b border-dashed border-sage-400 dark:border-sage-500 text-sage-700 dark:text-sage-400 bg-transparent p-0 font-inherit cursor-help"
    aria-describedby="{term}-tooltip"
    type="button"
  >
    {term}
  </button>

  {#if visible}
    <span
      id="{term}-tooltip"
      role="tooltip"
      class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 px-3 py-2 text-xs text-white bg-gray-800 rounded-lg shadow-lg max-w-xs z-50 whitespace-normal"
    >
      {definition}
      {#if href}
        <a href={href} class="text-sage-300 ml-1 no-underline hover:text-sage-200">→ glossary</a>
      {/if}
    </span>
  {/if}
</span>
