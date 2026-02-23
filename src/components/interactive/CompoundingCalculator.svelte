<script lang="ts">
  import { compoundGrowth } from '@/lib/calculations';
  import CompoundingChart from '@/components/visualizations/CompoundingChart.svelte';
  import CurrencyInput from '@/components/ui/CurrencyInput.svelte';

  let principal = $state(10000);
  let monthly = $state(500);
  let rate = $state(8);
  let years = $state(30);

  const data = $derived(compoundGrowth(principal, monthly, rate / 100, years));
  const finalBalance = $derived(data[data.length - 1]?.balance ?? 0);
  const totalContributed = $derived(principal + monthly * 12 * years);
  const totalGrowth = $derived(finalBalance - totalContributed);
</script>

<div
  class="my-8 rounded-xl border border-gray-200 bg-gray-50 p-6 dark:border-gray-700 dark:bg-gray-900"
>
  <h4 class="mb-4 text-lg font-semibold text-gray-900 dark:text-gray-100">
    Compounding Calculator
  </h4>

  <div class="mb-6 grid grid-cols-2 gap-4 sm:grid-cols-4">
    <CurrencyInput bind:value={principal} label="Starting amount" step={1000} />
    <CurrencyInput bind:value={monthly} label="Monthly contribution" step={50} />
    <label class="block">
      <span class="mb-1 block text-xs font-medium text-gray-600 dark:text-gray-400"
        >Annual return (%)</span
      >
      <input
        type="number"
        bind:value={rate}
        min="0"
        max="20"
        step="0.5"
        class="w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm text-gray-900 focus:border-sage-400 focus:ring-2 focus:ring-sage-400 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-100"
      />
    </label>
    <label class="block">
      <span class="mb-1 block text-xs font-medium text-gray-600 dark:text-gray-400">Years</span>
      <input
        type="range"
        bind:value={years}
        min="1"
        max="50"
        class="mt-2 w-full accent-sage-600 dark:accent-sage-400"
      />
      <span class="text-xs text-gray-500 dark:text-gray-400">{years} years</span>
    </label>
  </div>

  <CompoundingChart {data} {totalContributed} />

  <div class="mt-4 grid grid-cols-3 gap-4 text-center">
    <div>
      <p class="text-xs text-gray-500 dark:text-gray-400">Total contributed</p>
      <p class="text-lg font-bold text-gray-700 dark:text-gray-200">
        ${totalContributed.toLocaleString()}
      </p>
    </div>
    <div>
      <p class="text-xs text-gray-500 dark:text-gray-400">Growth from returns</p>
      <p class="text-lg font-bold text-sage-600 dark:text-sage-400">
        ${Math.round(totalGrowth).toLocaleString()}
      </p>
    </div>
    <div>
      <p class="text-xs text-gray-500 dark:text-gray-400">Final balance</p>
      <p class="text-lg font-bold text-sage-700 dark:text-sage-300">
        ${Math.round(finalBalance).toLocaleString()}
      </p>
    </div>
  </div>
</div>
