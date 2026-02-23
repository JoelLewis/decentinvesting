<script lang="ts">
  import { feeImpact } from '@/lib/calculations';
  import FeeErosionChart from '@/components/visualizations/FeeErosionChart.svelte';
  import CurrencyInput from '@/components/ui/CurrencyInput.svelte';

  let principal = $state(100000);
  let annualReturn = $state(8);
  let years = $state(30);
  let feeA = $state(0.03);
  let feeB = $state(0.75);

  const data = $derived(feeImpact(principal, annualReturn / 100, years, feeA / 100, feeB / 100));
  const finalRow = $derived(data[data.length - 1]);
  const difference = $derived((finalRow?.valueA ?? 0) - (finalRow?.valueB ?? 0));
</script>

<div
  class="my-8 rounded-xl border border-gray-200 bg-gray-50 p-6 dark:border-gray-700 dark:bg-gray-900"
>
  <h4 class="mb-4 text-lg font-semibold text-gray-900 dark:text-gray-100">Fee Impact Calculator</h4>

  <div class="mb-6 grid grid-cols-2 gap-4 sm:grid-cols-5">
    <CurrencyInput bind:value={principal} label="Starting amount" step={10000} />
    <label class="block">
      <span class="mb-1 block text-xs font-medium text-gray-600 dark:text-gray-400"
        >Annual return (%)</span
      >
      <input
        type="number"
        bind:value={annualReturn}
        min="0"
        max="15"
        step="0.5"
        class="w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm text-gray-900 focus:border-sage-400 focus:ring-2 focus:ring-sage-400 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-100"
      />
    </label>
    <label class="block">
      <span class="mb-1 block text-xs font-medium text-gray-600 dark:text-gray-400">Years</span>
      <input
        type="number"
        bind:value={years}
        min="1"
        max="50"
        class="w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm text-gray-900 focus:border-sage-400 focus:ring-2 focus:ring-sage-400 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-100"
      />
    </label>
    <label class="block">
      <span class="mb-1 block text-xs font-medium text-gray-600 dark:text-gray-400"
        >Low fee (%)</span
      >
      <input
        type="number"
        bind:value={feeA}
        min="0"
        max="3"
        step="0.01"
        class="w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm text-gray-900 focus:border-sage-400 focus:ring-2 focus:ring-sage-400 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-100"
      />
    </label>
    <label class="block">
      <span class="mb-1 block text-xs font-medium text-gray-600 dark:text-gray-400"
        >High fee (%)</span
      >
      <input
        type="number"
        bind:value={feeB}
        min="0"
        max="3"
        step="0.01"
        class="w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm text-gray-900 focus:border-sage-400 focus:ring-2 focus:ring-sage-400 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-100"
      />
    </label>
  </div>

  <FeeErosionChart {data} {feeA} {feeB} />

  <div class="mt-4 grid grid-cols-3 gap-4 text-center">
    <div>
      <p class="text-xs text-gray-500 dark:text-gray-400">Low fee ({feeA}%) final</p>
      <p class="text-lg font-bold text-sage-600 dark:text-sage-400">
        ${(finalRow?.valueA ?? 0).toLocaleString()}
      </p>
    </div>
    <div>
      <p class="text-xs text-gray-500 dark:text-gray-400">High fee ({feeB}%) final</p>
      <p class="text-lg font-bold text-red-500 dark:text-red-400">
        ${(finalRow?.valueB ?? 0).toLocaleString()}
      </p>
    </div>
    <div>
      <p class="text-xs text-gray-500 dark:text-gray-400">Lost to fees</p>
      <p class="text-lg font-bold text-red-600 dark:text-red-400">${difference.toLocaleString()}</p>
    </div>
  </div>
</div>
