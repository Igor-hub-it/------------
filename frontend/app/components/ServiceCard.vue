<script setup lang="ts">
defineProps<{
  title: string
  description: string
  cardDescription?: string
  useCases?: string[]
  icon?: 'car' | 'home' | 'building' | 'map' | 'bank'
  to: string
}>()
</script>

<template>
  <article class="overflow-hidden rounded-[24px] border border-slate-200 bg-white shadow-sm">
    <div class="relative h-[245px] bg-[linear-gradient(180deg,#dfe7ef_0%,#c8d2dc_100%)]">
      <div class="absolute inset-0 bg-[radial-gradient(circle_at_30%_30%,rgba(255,255,255,0.45),transparent_40%),linear-gradient(180deg,rgba(255,255,255,0.15),rgba(15,23,42,0.08))]"></div>
      <div class="absolute left-6 top-6 flex h-14 w-14 items-center justify-center rounded-full bg-white text-slate-700 shadow-sm">
        <svg
          v-if="icon === 'car'"
          class="h-6 w-6"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="1.8"
        >
          <path d="M5 16h14l-1.3-4.1A2 2 0 0 0 15.8 10H8.2a2 2 0 0 0-1.9 1.4L5 16Z" />
          <path d="M4 16v2a1 1 0 0 0 1 1h1m13-3v2a1 1 0 0 1-1 1h-1M7.5 19v-1m9 1v-1" />
          <circle cx="8" cy="16.5" r="1.5" />
          <circle cx="16" cy="16.5" r="1.5" />
        </svg>
        <svg
          v-else-if="icon === 'home'"
          class="h-6 w-6"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="1.8"
        >
          <path d="M4 11.5 12 5l8 6.5" />
          <path d="M6.5 10.5V19h11v-8.5" />
          <path d="M10 19v-4.5h4V19" />
        </svg>
        <svg
          v-else-if="icon === 'building'"
          class="h-6 w-6"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="1.8"
        >
          <path d="M4 20h16M7 20V6h10v14M10 9h1m3 0h1m-5 4h1m3 0h1m-5 4h1m3 0h1" />
        </svg>
        <svg
          v-else-if="icon === 'map'"
          class="h-6 w-6"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="1.8"
        >
          <path d="m3 6 6-2 6 2 6-2v14l-6 2-6-2-6 2V6Z" />
          <path d="M9 4v14M15 6v14" />
        </svg>
        <svg
          v-else
          class="h-6 w-6"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="1.8"
        >
          <path d="M4 20h16M6 17V9l6-4 6 4v8M9 20v-6h6v6" />
          <path d="M10 10h4" />
        </svg>
      </div>
    </div>

    <div class="flex h-full flex-col p-8">
      <h3 class="text-[22px] font-semibold leading-tight text-slate-900">
        {{ title }}
      </h3>
      <p class="mt-4 text-[15px] leading-7 text-slate-500">
        {{ cardDescription || description }}
      </p>

      <div class="mt-6">
        <p class="text-base font-semibold text-slate-900">Частые случаи использования:</p>
        <ul class="mt-3 space-y-2 text-[15px] leading-6 text-slate-500">
          <li v-for="item in useCases || []" :key="item" class="flex items-start gap-3">
            <span class="mt-[9px] h-2 w-2 shrink-0 rounded-full bg-[#37b5bd]"></span>
            <span>{{ item }}</span>
          </li>
        </ul>
      </div>

      <NuxtLink
        :to="to"
        class="mt-8 inline-flex items-center justify-center gap-3 rounded-2xl bg-[#37b5bd] px-6 py-4 text-lg font-semibold text-white transition hover:bg-[#2fa3aa]"
      >
        Узнать подробнее
        <span aria-hidden="true" class="text-2xl leading-none">→</span>
      </NuxtLink>
    </div>
  </article>
</template>
