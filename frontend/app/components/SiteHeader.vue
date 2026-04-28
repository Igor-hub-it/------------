<script setup lang="ts">
const navigation = [
  { label: 'О компании', to: '/#about' },
  { label: 'Услуги оценки', to: '/#services' },
  { label: 'Направления работы', to: '/#directions' },
  { label: 'Цены', to: '/#pricing' },
  { label: 'Контакты', to: '/#contacts' }
]
</script>

<template>
  <header class="sticky top-0 z-40 bg-[rgba(233,237,242,0.96)] py-3 backdrop-blur">
    <div class="px-3 sm:px-4 lg:px-5">
      <div class="flex min-h-[49px] items-center justify-between gap-6 rounded-[4px] border border-slate-100 bg-white px-5 shadow-[0_1px_3px_rgba(15,23,42,0.04)]">
        <div class="flex items-center gap-8">
          <NuxtLink to="/" aria-label="На главную" class="flex shrink-0 items-center gap-3">
            <div class="flex h-10 w-10 items-center justify-center rounded-full border-[3px] border-[#37b5bd] text-[#2a8f96]">
              <div class="relative flex h-5 w-5 items-center justify-center text-[12px] font-bold uppercase">
                <span>П</span>
                <span class="absolute left-[9px] top-[1px]">О</span>
              </div>
            </div>
            <div class="leading-none text-[#2a8f96]">
              <span class="block text-[10px] font-semibold uppercase tracking-[0.14em]">ПЕРЭКС</span>
              <span class="mt-1 block text-[11px] font-semibold uppercase tracking-[0.14em]">ОЦЕНКА</span>
            </div>
          </NuxtLink>

          <nav aria-label="Основная навигация" class="hidden lg:block">
            <ul class="flex flex-wrap gap-1 text-[12px] font-medium text-slate-500">
            <li v-for="item in navigation" :key="item.to">
                <NuxtLink :to="item.to" class="rounded-full px-3 py-2 hover:text-slate-900">
                  {{ item.label }}
                </NuxtLink>
            </li>
          </ul>
        </nav>
        </div>

        <div class="flex items-center gap-5">
          <a href="tel:+79130000000" class="hidden items-center gap-2 text-[13px] font-medium text-slate-600 hover:text-slate-900 md:flex">
            <Icon class="h-4 w-4 text-slate-500" name="lucide:phone" />
            +7 913 000 00 00
          </a>
          <NuxtLink
            class="inline-flex h-10 items-center justify-center rounded-xl bg-[#37b5bd] px-6 text-[13px] font-semibold text-white transition hover:bg-[#2fa3aa]"
            to="/#contact-form"
          >
            Подать заявку
          </NuxtLink>
        </div>
      </div>
    </div>
  </header>
</template>
