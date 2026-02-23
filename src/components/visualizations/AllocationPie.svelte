<script lang="ts">
  import { onMount } from 'svelte';
  import * as d3 from 'd3';

  let {
    slices,
  }: {
    slices: { label: string; value: number; color: string }[];
  } = $props();

  let container: HTMLElement;

  function isDark() {
    return document.documentElement.classList.contains('dark');
  }

  onMount(() => {
    const themeObserver = new MutationObserver(() => {
      // Trigger re-render on theme change by reassigning slices reference
      render();
    });
    themeObserver.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['class'],
    });
    return () => themeObserver.disconnect();
  });

  function render() {
    if (!container) return;

    const dark = isDark();

    const svg = d3.select(container).select('svg');
    svg.selectAll('*').remove();

    const size = 192;
    const radius = size / 2;
    const innerRadius = radius * 0.55;

    const g = svg.append('g').attr('transform', `translate(${radius},${radius})`);

    const pie = d3
      .pie<{ label: string; value: number; color: string }>()
      .value((d) => d.value)
      .sort(null)
      .padAngle(0.02);

    const arc = d3
      .arc<d3.PieArcDatum<{ label: string; value: number; color: string }>>()
      .innerRadius(innerRadius)
      .outerRadius(radius - 4)
      .cornerRadius(3);

    g.selectAll('path')
      .data(pie(slices))
      .join('path')
      .attr('d', arc)
      .attr('fill', (d) => d.data.color)
      .attr('stroke', dark ? '#030712' : 'white')
      .attr('stroke-width', 2);

    // Center label
    const total = slices.reduce((sum, s) => sum + s.value, 0);
    const stockPct = slices
      .filter((s) => s.label.includes('Stock'))
      .reduce((sum, s) => sum + s.value, 0);
    g.append('text')
      .attr('text-anchor', 'middle')
      .attr('dy', '-0.2em')
      .attr('font-size', '24px')
      .attr('font-weight', 'bold')
      .attr('fill', dark ? '#f3f4f6' : '#1f2937')
      .text(`${stockPct}/${total - stockPct}`);

    g.append('text')
      .attr('text-anchor', 'middle')
      .attr('dy', '1.2em')
      .attr('font-size', '11px')
      .attr('fill', dark ? '#9ca3af' : '#6b7280')
      .text('stocks / bonds');
  }

  $effect(() => {
    render();
  });
</script>

<div bind:this={container}>
  <svg width="192" height="192" role="img" aria-label="Portfolio allocation donut chart"> </svg>
</div>
