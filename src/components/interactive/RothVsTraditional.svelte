<script lang="ts">
  import { rothVsTraditional } from '@/lib/calculations';
  import CurrencyInput from '@/components/ui/CurrencyInput.svelte';

  let annualContribution = $state(7000);
  let currentRate = $state(22);
  let futureRate = $state(24);
  let annualReturn = $state(8);
  let years = $state(30);

  const result = $derived(
    rothVsTraditional(
      annualContribution,
      currentRate / 100,
      futureRate / 100,
      annualReturn / 100,
      years,
    ),
  );

  const recommendation = $derived(result.rothAdvantage > 0 ? 'Roth' : 'Traditional');
</script>

<div
  class="my-8 rounded-xl border border-gray-200 bg-gray-50 p-6 dark:border-gray-700 dark:bg-gray-900"
>
  <h4 class="mb-4 text-lg font-semibold text-gray-900 dark:text-gray-100">
    Roth vs Traditional Comparison
  </h4>

  <div class="mb-6 grid grid-cols-2 gap-4 sm:grid-cols-5">
    <CurrencyInput bind:value={annualContribution} label="Annual contribution" step={500} />
    <label class="block">
      <span class="mb-1 block text-xs font-medium text-gray-600 dark:text-gray-400"
        >Current tax rate (%)</span
      >
      <input
        type="number"
        bind:value={currentRate}
        min="0"
        max="50"
        step="1"
        class="w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm text-gray-900 focus:border-sage-400 focus:ring-2 focus:ring-sage-400 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-100"
      />
    </label>
    <label class="block">
      <span class="mb-1 block text-xs font-medium text-gray-600 dark:text-gray-400"
        >Future tax rate (%)</span
      >
      <input
        type="number"
        bind:value={futureRate}
        min="0"
        max="50"
        step="1"
        class="w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm text-gray-900 focus:border-sage-400 focus:ring-2 focus:ring-sage-400 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-100"
      />
    </label>
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
      <span class="mb-1 block text-xs font-medium text-gray-600 dark:text-gray-400"
        >Years to retirement</span
      >
      <input
        type="number"
        bind:value={years}
        min="1"
        max="50"
        class="w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm text-gray-900 focus:border-sage-400 focus:ring-2 focus:ring-sage-400 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-100"
      />
    </label>
  </div>

  <!-- Comparison bars -->
  <div class="mb-4 space-y-3">
    <div>
      <div class="mb-1 flex justify-between text-sm">
        <span class="font-medium text-sage-700 dark:text-sage-300">Roth (after-tax value)</span>
        <span class="font-bold text-gray-900 dark:text-gray-100"
          >${result.rothFinal.toLocaleString()}</span
        >
      </div>
      <div class="h-6 overflow-hidden rounded-full bg-gray-200 dark:bg-gray-700">
        <div
          class="h-full rounded-full bg-sage-500 transition-all duration-500 dark:bg-sage-400"
          style="width: {Math.min(
            100,
            (result.rothFinal / Math.max(result.rothFinal, result.traditionalFinal)) * 100,
          )}%"
        ></div>
      </div>
    </div>
    <div>
      <div class="mb-1 flex justify-between text-sm">
        <span class="font-medium text-blue-700 dark:text-blue-300"
          >Traditional (after-tax value)</span
        >
        <span class="font-bold text-gray-900 dark:text-gray-100"
          >${result.traditionalFinal.toLocaleString()}</span
        >
      </div>
      <div class="h-6 overflow-hidden rounded-full bg-gray-200 dark:bg-gray-700">
        <div
          class="h-full rounded-full bg-blue-500 transition-all duration-500 dark:bg-blue-400"
          style="width: {Math.min(
            100,
            (result.traditionalFinal / Math.max(result.rothFinal, result.traditionalFinal)) * 100,
          )}%"
        ></div>
      </div>
    </div>
  </div>

  <div
    class="rounded-lg p-3 text-center text-sm {recommendation === 'Roth'
      ? 'bg-sage-50 text-sage-700 dark:bg-sage-950/40 dark:text-sage-300'
      : 'bg-blue-50 text-blue-700 dark:bg-blue-950/30 dark:text-blue-300'}"
  >
    <strong>{recommendation}</strong> comes out ahead by
    <strong>${Math.abs(result.rothAdvantage).toLocaleString()}</strong>
    in this scenario.
    {#if currentRate === futureRate}
      When tax rates are equal, Roth and Traditional are mathematically identical — but Roth offers
      more flexibility (penalty-free contribution withdrawals).
    {:else if currentRate < futureRate}
      Since your future rate is higher, paying taxes now (Roth) saves money overall.
    {:else}
      Since your current rate is higher, deferring taxes (Traditional) saves money overall.
    {/if}
  </div>

  <p class="mt-3 text-xs text-gray-500 dark:text-gray-400">
    This is a simplified comparison. Real-world factors (state taxes, deduction changes, RMDs,
    Social Security taxation) add complexity. Consider consulting a tax professional.
  </p>
</div>
