<script lang="ts">
  import { onMount } from 'svelte';
  import * as d3 from 'd3';

  const drawdowns = [
    { name: 'Oil Crisis', year: 1973, drop: -48, recovery: 1980 },
    { name: 'Black Monday', year: 1987, drop: -34, recovery: 1989 },
    { name: 'Dot-com', year: 2000, drop: -49, recovery: 2007 },
    { name: '2008 Crisis', year: 2007, drop: -57, recovery: 2013 },
    { name: 'COVID', year: 2020, drop: -34, recovery: 2020 },
  ];

  let container: HTMLElement;
  let width = $state(600);
  const height = 220;
  const margin = { top: 20, right: 20, bottom: 30, left: 50 };

  function isDark() {
    return document.documentElement.classList.contains('dark');
  }

  onMount(() => {
    const observer = new ResizeObserver((entries) => {
      width = entries[0].contentRect.width;
    });
    observer.observe(container);

    const themeObserver = new MutationObserver(() => {
      width = container.getBoundingClientRect().width;
    });
    themeObserver.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });

    return () => { observer.disconnect(); themeObserver.disconnect(); };
  });

  $effect(() => {
    if (!container) return;

    const dark = isDark();
    const axisColor = dark ? '#4b5563' : '#e5e7eb';
    const tickColor = dark ? '#9ca3af' : '#6b7280';
    const redColor = dark ? '#f87171' : '#ef4444';
    const labelColor = dark ? '#9ca3af' : '#6b7280';

    const svg = d3.select(container).select('svg');
    svg.selectAll('*').remove();

    const innerW = width - margin.left - margin.right;
    const innerH = height - margin.top - margin.bottom;

    const x = d3.scaleLinear().domain([1970, 2025]).range([0, innerW]);
    const y = d3.scaleLinear().domain([-60, 0]).range([innerH, 0]);

    const g = svg.append('g').attr('transform', `translate(${margin.left},${margin.top})`);

    // Zero line
    g.append('line')
      .attr('x1', 0).attr('x2', innerW)
      .attr('y1', y(0)).attr('y2', y(0))
      .attr('stroke', axisColor)
      .attr('stroke-width', 1);

    // Drawdown bars
    drawdowns.forEach((d) => {
      const barWidth = Math.max(x(d.recovery) - x(d.year), 8);

      g.append('rect')
        .attr('x', x(d.year))
        .attr('y', y(0))
        .attr('width', barWidth)
        .attr('height', y(d.drop) - y(0))
        .attr('fill', redColor)
        .attr('opacity', dark ? 0.25 : 0.3)
        .attr('rx', 2);

      g.append('text')
        .attr('x', x(d.year) + barWidth / 2)
        .attr('y', y(d.drop) + 14)
        .attr('text-anchor', 'middle')
        .attr('font-size', '10px')
        .attr('fill', redColor)
        .attr('font-weight', 'bold')
        .text(`${d.drop}%`);

      g.append('text')
        .attr('x', x(d.year) + barWidth / 2)
        .attr('y', y(0) - 6)
        .attr('text-anchor', 'middle')
        .attr('font-size', '9px')
        .attr('fill', labelColor)
        .text(d.name);
    });

    // Axes
    g.append('g')
      .attr('transform', `translate(0,${innerH})`)
      .call(d3.axisBottom(x).ticks(6).tickFormat((d) => String(d)))
      .call((sel) => { sel.select('.domain').attr('stroke', axisColor); sel.selectAll('.tick text').attr('fill', tickColor); sel.selectAll('.tick line').attr('stroke', axisColor); });

    g.append('g')
      .call(d3.axisLeft(y).ticks(4).tickFormat((d) => `${d}%`))
      .call((sel) => { sel.select('.domain').attr('stroke', axisColor); sel.selectAll('.tick text').attr('fill', tickColor); sel.selectAll('.tick line').attr('stroke', axisColor); });
  });
</script>

<div bind:this={container} class="w-full my-6">
  <svg {width} {height} class="overflow-visible" role="img" aria-label="Historical market drawdowns timeline showing major crashes and recovery periods">
  </svg>
  <p class="text-xs text-gray-500 dark:text-gray-400 text-center mt-2">
    Every major crash was followed by full recovery and new highs. S&P 500 data.
  </p>
</div>
