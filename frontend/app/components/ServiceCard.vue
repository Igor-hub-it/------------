<script setup lang="ts">
import services1 from '~/assets/icon/services-1.svg'
import services2 from '~/assets/icon/services-2.svg'
import services3 from '~/assets/icon/services-3.svg'
import services4 from '~/assets/icon/services-4.svg'
import services5 from '~/assets/icon/services-5.svg'

const iconMap = {
  car: services1,
  home: services2,
  building: services3,
  map: services4,
  bank: services5
} as const

defineProps<{
  title: string
  description: string
  cardImage?: string
  cardDescription?: string
  useCases?: string[]
  useCasesInFourColumnsOnLg?: boolean
  icon?: 'car' | 'home' | 'building' | 'map' | 'bank'
  to: string
}>()
</script>

<template>
  <article class="flex h-full flex-col overflow-hidden rounded-[24px] border border-slate-200 bg-white shadow-sm">
    <div
      class="relative h-[130px] sm:h-[200px] bg-slate-200 bg-cover bg-bottom"
      :style="cardImage ? { backgroundImage: `url('${cardImage}')` } : undefined"
    >
      <div class="absolute inset-0 bg-[radial-gradient(circle_at_30%_30%,rgba(255,255,255,0.2),transparent_35%),linear-gradient(180deg,rgba(15,23,42,0.04),rgba(15,23,42,0.18))]"></div>
      <div class="absolute left-6 top-6 flex h-14 w-14 items-center justify-center rounded-full bg-white text-slate-700 shadow-sm">
        <img :src="iconMap[icon || 'bank']" alt="" class="h-6 w-6 object-contain" />
      </div>
    </div>

    <div class="flex flex-1 flex-col p-8 gap-4">
      <h3 class="text-[22px] font-medium leading-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
        {{ title }}
      </h3>
      <p class="text-[14px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
        {{ cardDescription || description }}
      </p>

      <div class="">
        <p class="text-[14px] font-medium text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">Частые случаи использования:</p>
        <ul
          class="mt-3 text-[14px] font-normal leading-6 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]"
          :class="useCasesInFourColumnsOnLg ? 'space-y-2 lg:grid lg:grid-cols-4 lg:gap-4 lg:space-y-0' : 'space-y-2'"
        >
          <li v-for="item in useCases || []" :key="item" class="flex items-start gap-3">
            <span class="mt-[9px] h-2 w-2 shrink-0 rounded-full bg-[#37b5bd]"></span>
            <span>{{ item }}</span>
          </li>
        </ul>
      </div>

      <NuxtLink
        :to="to"
        class="mt-auto inline-flex items-center justify-center gap-3 rounded-2xl bg-[#37b5bd] px-6 py-4 mt-6 text-lg font-semibold text-white transition hover:bg-[#2fa3aa]"
      >
        Узнать подробнее
        <Icon aria-hidden="true" class="h-6 w-6" name="lucide:arrow-right" />
      </NuxtLink>
    </div>
  </article>
</template>
