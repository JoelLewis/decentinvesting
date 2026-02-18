<script lang="ts">
  import { rothVsTraditional } from '@/lib/calculations';
  import CurrencyInput from '@/components/ui/CurrencyInput.svelte';

  let annualContribution = $state(7000);
  let currentRate = $state(22);
  let futureRate = $state(24);
  let annualReturn = $state(8);
  let years = $state(30);

  const result = $derived(
    rothVsTraditional(annualContribution, currentRate / 100, futureRate / 100, annualReturn / 100, years)
  );

  const recommendation = $derived(
    result.rothAdvantage > 0 ? 'Roth' : 'Traditional'
  );
</script>

<div class="my-8 p-6 bg-gray-50 dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-700">
  <h4 class="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-4">Roth vs Traditional Comparison</h4>

  <div class="grid grid-cols-2 sm:grid-cols-5 gap-4 mb-6">
    <CurrencyInput bind:value={annualContribution} label="Annual contribution" step={500} />
    <label class="block">
      <span class="text-xs font-medium text-gray-600 dark:text-gray-400 block mb-1">Current tax rate (%)</span>
      <input
        type="number"
        bind:value={currentRate}
        min="0"
        max="50"
        step="1"
        class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md text-sm bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-sage-400 focus:border-sage-400"
      />
    </label>
    <label class="block">
      <span class="text-xs font-medium text-gray-600 dark:text-gray-400 block mb-1">Future tax rate (%)</span>
      <input
        type="number"
        bind:value={futureRate}
        min="0"
        max="50"
        step="1"
        class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md text-sm bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-sage-400 focus:border-sage-400"
      />
    </label>
    <label class="block">
      <span class="text-xs font-medium text-gray-600 dark:text-gray-400 block mb-1">Annual return (%)</span>
      <input
        type="number"
        bind:value={annualReturn}
        min="0"
        max="15"
        step="0.5"
        class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md text-sm bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-sage-400 focus:border-sage-400"
      />
    </label>
    <label class="block">
      <span class="text-xs font-medium text-gray-600 dark:text-gray-400 block mb-1">Years to retirement</span>
      <input
        type="number"
        bind:value={years}
        min="1"
        max="50"
        class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md text-sm bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-sage-400 focus:border-sage-400"
      />
    </label>
  </div>

  <!-- Comparison bars -->
  <div class="space-y-3 mb-4">
    <div>
      <div class="flex justify-between text-sm mb-1">
        <span class="font-medium text-sage-700 dark:text-sage-300">Roth (after-tax value)</span>
        <span class="font-bold text-gray-900 dark:text-gray-100">${result.rothFinal.toLocaleString()}</span>
      </div>
      <div class="h-6 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden">
        <div
          class="h-full bg-sage-500 dark:bg-sage-400 rounded-full transition-all duration-500"
          style="width: {Math.min(100, (result.rothFinal / Math.max(result.rothFinal, result.traditionalFinal)) * 100)}%"
        ></div>
      </div>
    </div>
    <div>
      <div class="flex justify-between text-sm mb-1">
        <span class="font-medium text-blue-700 dark:text-blue-300">Traditional (after-tax value)</span>
        <span class="font-bold text-gray-900 dark:text-gray-100">${result.traditionalFinal.toLocaleString()}</span>
      </div>
      <div class="h-6 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden">
        <div
          class="h-full bg-blue-500 dark:bg-blue-400 rounded-full transition-all duration-500"
          style="width: {Math.min(100, (result.traditionalFinal / Math.max(result.rothFinal, result.traditionalFinal)) * 100)}%"
        ></div>
      </div>
    </div>
  </div>

  <div class="p-3 rounded-lg text-sm text-center {recommendation === 'Roth'
    ? 'bg-sage-50 dark:bg-sage-950/40 text-sage-700 dark:text-sage-300'
    : 'bg-blue-50 dark:bg-blue-950/30 text-blue-700 dark:text-blue-300'}">
    <strong>{recommendation}</strong> comes out ahead by
    <strong>${Math.abs(result.rothAdvantage).toLocaleString()}</strong>
    in this scenario.
    {#if currentRate === futureRate}
      When tax rates are equal, Roth and Traditional are mathematically identical — but Roth offers more flexibility (penalty-free contribution withdrawals).
    {:else if currentRate < futureRate}
      Since your future rate is higher, paying taxes now (Roth) saves money overall.
    {:else}
      Since your current rate is higher, deferring taxes (Traditional) saves money overall.
    {/if}
  </div>

  <p class="text-xs text-gray-500 dark:text-gray-400 mt-3">
    This is a simplified comparison. Real-world factors (state taxes, deduction changes, RMDs, Social Security taxation) add complexity. Consider consulting a tax professional.
  </p>
</div>
