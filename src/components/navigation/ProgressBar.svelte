<script lang="ts">
  let { currentIndex, totalPages }: { currentIndex: number; totalPages: number } = $props();

  const progress = $derived(((currentIndex + 1) / totalPages) * 100);
</script>

<div
  class="sticky top-14 z-30 h-1 bg-gray-100 dark:bg-gray-800"
  role="progressbar"
  aria-valuenow={currentIndex + 1}
  aria-valuemin={1}
  aria-valuemax={totalPages}
  aria-label="Guide progress: step {currentIndex + 1} of {totalPages}"
>
  <div
    class="h-full bg-sage-500 transition-all duration-500 ease-out dark:bg-sage-400"
    style="width: {progress}%"
  ></div>
</div>
