<script lang="ts">
  import { debtPayoff } from '@/lib/calculations';
  import CurrencyInput from '@/components/ui/CurrencyInput.svelte';

  type DebtEntry = { name: string; balance: number; rate: number; minimum: number };

  let debts = $state<DebtEntry[]>([
    { name: 'Credit card', balance: 6000, rate: 0.22, minimum: 150 },
    { name: 'Car loan', balance: 4000, rate: 0.06, minimum: 200 },
    { name: 'Student loan', balance: 12000, rate: 0.05, minimum: 150 },
  ]);

  let extraPayment = $state(500);

  const avalanche = $derived(debtPayoff(debts, extraPayment, 'avalanche'));
  const snowball = $derived(debtPayoff(debts, extraPayment, 'snowball'));
  const interestDiff = $derived(Math.abs(avalanche.totalInterest - snowball.totalInterest));

  function updateDebt(index: number, field: keyof DebtEntry, value: string) {
    const parsed = field === 'name' ? value : Number(value);
    debts[index] = { ...debts[index], [field]: parsed };
    // force reactivity
    debts = [...debts];
  }

  function addDebt() {
    debts = [...debts, { name: `Debt ${debts.length + 1}`, balance: 1000, rate: 0.10, minimum: 50 }];
  }

  function removeDebt(index: number) {
    debts = debts.filter((_, i) => i !== index);
  }

  // Track which cell is being edited for currency formatting
  let editingCell = $state<string | null>(null);
  let editText = $state('');

  function currencyDisplay(val: number): string {
    return `$${val.toLocaleString()}`;
  }

  function startCellEdit(key: string, val: number, e: FocusEvent) {
    editingCell = key;
    editText = String(val);
    requestAnimationFrame(() => (e.target as HTMLInputElement).select());
  }

  function handleCellInput(index: number, field: 'balance' | 'minimum', e: Event) {
    const raw = (e.target as HTMLInputElement).value;
    const cleaned = raw.replace(/[^0-9.]/g, '');
    editText = cleaned;
    const parsed = Number(cleaned);
    if (!isNaN(parsed)) {
      updateDebt(index, field, String(parsed));
    }
  }

  function endCellEdit() {
    editingCell = null;
  }
</script>

<div class="my-8 p-6 bg-gray-50 dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-700">
  <h4 class="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-4">Debt Payoff Comparison</h4>

  <!-- Debt inputs -->
  <div class="space-y-2 mb-4">
    {#each debts as debt, i}
      <div class="grid grid-cols-5 gap-2 items-end">
        <label class="block">
          {#if i === 0}<span class="text-xs font-medium text-gray-600 dark:text-gray-400 block mb-1">Name</span>{/if}
          <input
            type="text"
            value={debt.name}
            oninput={(e) => updateDebt(i, 'name', (e.target as HTMLInputElement).value)}
            class="w-full px-2 py-1.5 border border-gray-300 dark:border-gray-600 rounded text-sm bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100"
          />
        </label>
        <label class="block">
          {#if i === 0}<span class="text-xs font-medium text-gray-600 dark:text-gray-400 block mb-1">Balance</span>{/if}
          <input
            type="text"
            inputmode="decimal"
            value={editingCell === `balance-${i}` ? editText : currencyDisplay(debt.balance)}
            oninput={(e) => handleCellInput(i, 'balance', e)}
            onfocus={(e) => startCellEdit(`balance-${i}`, debt.balance, e)}
            onblur={endCellEdit}
            class="w-full px-2 py-1.5 border border-gray-300 dark:border-gray-600 rounded text-sm bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100"
          />
        </label>
        <label class="block">
          {#if i === 0}<span class="text-xs font-medium text-gray-600 dark:text-gray-400 block mb-1">Rate</span>{/if}
          <input
            type="number"
            value={debt.rate * 100}
            oninput={(e) => updateDebt(i, 'rate', String(Number((e.target as HTMLInputElement).value) / 100))}
            min="0"
            max="100"
            step="0.5"
            class="w-full px-2 py-1.5 border border-gray-300 dark:border-gray-600 rounded text-sm bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100"
          />
        </label>
        <label class="block">
          {#if i === 0}<span class="text-xs font-medium text-gray-600 dark:text-gray-400 block mb-1">Minimum</span>{/if}
          <input
            type="text"
            inputmode="decimal"
            value={editingCell === `minimum-${i}` ? editText : currencyDisplay(debt.minimum)}
            oninput={(e) => handleCellInput(i, 'minimum', e)}
            onfocus={(e) => startCellEdit(`minimum-${i}`, debt.minimum, e)}
            onblur={endCellEdit}
            class="w-full px-2 py-1.5 border border-gray-300 dark:border-gray-600 rounded text-sm bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100"
          />
        </label>
        <div>
          {#if debts.length > 1}
            <button
              onclick={() => removeDebt(i)}
              class="px-2 py-1.5 text-sm text-red-500 dark:text-red-400 hover:text-red-700 dark:hover:text-red-300 cursor-pointer"
              aria-label="Remove {debt.name}"
            >&times;</button>
          {/if}
        </div>
      </div>
    {/each}
  </div>

  <div class="flex items-center gap-4 mb-6">
    <button
      onclick={addDebt}
      class="text-sm text-sage-600 dark:text-sage-400 hover:text-sage-700 dark:hover:text-sage-300 font-medium cursor-pointer"
    >+ Add debt</button>
    <div class="ml-auto w-48">
      <CurrencyInput bind:value={extraPayment} label="Extra monthly payment" step={50} />
    </div>
  </div>

  <!-- Comparison results -->
  <div class="grid grid-cols-2 gap-4">
    <div class="p-4 bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700">
      <h5 class="font-semibold text-gray-900 dark:text-gray-100 mb-1">Avalanche</h5>
      <p class="text-xs text-gray-500 dark:text-gray-400 mb-3">Highest rate first — saves the most money</p>
      <p class="text-2xl font-bold text-gray-900 dark:text-gray-100">{avalanche.months} months</p>
      <p class="text-lg font-semibold text-sage-700 dark:text-sage-400 mt-1">${avalanche.totalInterest.toLocaleString()} <span class="text-xs font-normal text-gray-500 dark:text-gray-400">in interest</span></p>
    </div>
    <div class="p-4 bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700">
      <h5 class="font-semibold text-gray-900 dark:text-gray-100 mb-1">Snowball</h5>
      <p class="text-xs text-gray-500 dark:text-gray-400 mb-3">Smallest balance first — faster psychological wins</p>
      <p class="text-2xl font-bold text-gray-900 dark:text-gray-100">{snowball.months} months</p>
      <p class="text-lg font-semibold text-gray-700 dark:text-gray-300 mt-1">${snowball.totalInterest.toLocaleString()} <span class="text-xs font-normal text-gray-500 dark:text-gray-400">in interest</span></p>
    </div>
  </div>

  <!-- Difference callout -->
  {#if interestDiff < 100}
    <div class="mt-4 p-3 rounded-lg bg-sage-50 dark:bg-sage-950/40 border border-sage-200 dark:border-sage-800 text-center">
      <p class="text-sm text-sage-800 dark:text-sage-300">
        <strong>${interestDiff.toLocaleString()}</strong> difference — practically identical.
        Pick whichever keeps you motivated.
      </p>
    </div>
  {:else}
    <div class="mt-4 p-3 rounded-lg bg-sage-50 dark:bg-sage-950/40 border border-sage-200 dark:border-sage-800 text-center">
      <p class="text-sm font-medium text-sage-800 dark:text-sage-300">
        Avalanche saves <strong class="text-sage-700 dark:text-sage-300 text-base">${interestDiff.toLocaleString()}</strong> more in interest.
      </p>
      <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">
        But the snowball gives faster wins — pick what fits your psychology.
      </p>
    </div>
  {/if}
</div>
