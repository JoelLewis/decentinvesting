<script lang="ts">
  let {
    value = $bindable(),
    label,
    min = 0,
    step = 100,
  }: {
    value: number;
    label: string;
    min?: number;
    step?: number;
  } = $props();

  let editing = $state(false);
  let editText = $state('');

  const display = $derived(`$${value.toLocaleString()}`);

  function startEdit(e: FocusEvent) {
    editing = true;
    editText = String(value);
    requestAnimationFrame(() => (e.target as HTMLInputElement).select());
  }

  function handleInput(e: Event) {
    const raw = (e.target as HTMLInputElement).value;
    const cleaned = raw.replace(/[^0-9.]/g, '');
    editText = cleaned;
    const parsed = Number(cleaned);
    if (!isNaN(parsed)) {
      value = Math.max(min, parsed);
    }
  }

  function endEdit() {
    editing = false;
  }
</script>

<label class="block">
  <span class="text-xs font-medium text-gray-600 dark:text-gray-400 block mb-1">{label}</span>
  <input
    type="text"
    inputmode="decimal"
    value={editing ? editText : display}
    oninput={handleInput}
    onfocus={startEdit}
    onblur={endEdit}
    {step}
    class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md text-sm
           bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100
           focus:ring-2 focus:ring-sage-400 focus:border-sage-400"
  />
</label>
