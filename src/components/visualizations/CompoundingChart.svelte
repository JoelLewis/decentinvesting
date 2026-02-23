<script lang="ts">
  import { onMount } from 'svelte';
  import * as d3 from 'd3';

  let {
    data,
    totalContributed,
  }: {
    data: { year: number; balance: number }[];
    totalContributed: number;
  } = $props();

  let container: HTMLElement;
  let width = $state(600);
  const height = 300;
  const margin = { top: 20, right: 20, bottom: 40, left: 70 };

  function isDark() {
    return document.documentElement.classList.contains('dark');
  }

  onMount(() => {
    const observer = new ResizeObserver((entries) => {
      width = entries[0].contentRect.width;
    });
    observer.observe(container);

    const themeObserver = new MutationObserver(() => {
      // Re-trigger effect on theme change
      width = container.getBoundingClientRect().width;
    });
    themeObserver.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['class'],
    });

    return () => {
      observer.disconnect();
      themeObserver.disconnect();
    };
  });

  $effect(() => {
    if (!container || data.length === 0) return;

    const dark = isDark();
    const axisColor = dark ? '#4b5563' : '#e5e7eb';
    const tickColor = dark ? '#9ca3af' : '#6b7280';

    const svg = d3.select(container).select('svg');
    svg.selectAll('*').remove();

    const innerW = width - margin.left - margin.right;
    const innerH = height - margin.top - margin.bottom;

    const x = d3
      .scaleLinear()
      .domain([0, data[data.length - 1].year])
      .range([0, innerW]);
    const y = d3
      .scaleLinear()
      .domain([0, d3.max(data, (d) => d.balance) ?? 0])
      .nice()
      .range([innerH, 0]);

    const g = svg.append('g').attr('transform', `translate(${margin.left},${margin.top})`);

    // Contribution area
    const contribLine = data.map((d) => {
      const contributed =
        totalContributed > 0
          ? Math.min(d.balance, totalContributed * (d.year / (data[data.length - 1].year || 1)))
          : 0;
      return { year: d.year, value: contributed };
    });

    const areaContrib = d3
      .area<{ year: number; value: number }>()
      .x((d) => x(d.year))
      .y0(innerH)
      .y1((d) => y(d.value))
      .curve(d3.curveMonotoneX);

    g.append('path')
      .datum(contribLine)
      .attr('d', areaContrib)
      .attr('fill', '#a8c2af')
      .attr('opacity', dark ? 0.3 : 0.5);

    // Growth area
    const areaGrowth = d3
      .area<{ year: number; balance: number }>()
      .x((d) => x(d.year))
      .y0(innerH)
      .y1((d) => y(d.balance))
      .curve(d3.curveMonotoneX);

    g.append('path')
      .datum(data)
      .attr('d', areaGrowth)
      .attr('fill', dark ? '#6aad7a' : '#4a7c59')
      .attr('opacity', 0.3);

    // Balance line
    const line = d3
      .line<{ year: number; balance: number }>()
      .x((d) => x(d.year))
      .y((d) => y(d.balance))
      .curve(d3.curveMonotoneX);

    g.append('path')
      .datum(data)
      .attr('d', line)
      .attr('fill', 'none')
      .attr('stroke', dark ? '#6aad7a' : '#4a7c59')
      .attr('stroke-width', 2.5);

    // Axes
    g.append('g')
      .attr('transform', `translate(0,${innerH})`)
      .call(
        d3
          .axisBottom(x)
          .ticks(Math.min(data.length - 1, 10))
          .tickFormat((d) => `${d}y`),
      )
      .call((g) => {
        g.select('.domain').attr('stroke', axisColor);
        g.selectAll('.tick text').attr('fill', tickColor);
        g.selectAll('.tick line').attr('stroke', axisColor);
      });

    g.append('g')
      .call(
        d3
          .axisLeft(y)
          .ticks(5)
          .tickFormat((d) => `$${d3.format('.2s')(d as number)}`),
      )
      .call((g) => {
        g.select('.domain').attr('stroke', axisColor);
        g.selectAll('.tick text').attr('fill', tickColor);
        g.selectAll('.tick line').attr('stroke', axisColor);
      });
  });
</script>

<div bind:this={container} class="w-full">
  <svg {width} {height} class="overflow-visible" role="img" aria-label="Compound growth chart">
  </svg>
</div>
