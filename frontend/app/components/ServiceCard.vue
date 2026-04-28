<script setup lang="ts">
const iconMap = {
  car: 'lucide:car-front',
  home: 'lucide:house',
  building: 'lucide:building-2',
  map: 'lucide:map',
  bank: 'lucide:landmark'
} as const

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
        <Icon :name="iconMap[icon || 'bank']" class="h-6 w-6" />
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
