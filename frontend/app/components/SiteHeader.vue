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
  <header class="sticky top-0 z-40 border-b border-slate-300 bg-white">
    <div class="mx-auto flex h-[75px] w-full max-w-[1260px] items-center gap-8 px-5 sm:px-6 lg:px-8">
      <div class="flex min-w-0 flex-1 items-center gap-8 xl:gap-10">
        <NuxtLink to="/" aria-label="На главную" class="flex h-[53px] w-[130px] shrink-0 items-center gap-2.5">
          <div class="flex h-10 w-10 items-center justify-center rounded-full border-[3px] border-[#37b5bd] text-[#2a8f96]">
            <div class="relative flex h-5 w-5 items-center justify-center text-[12px] font-bold uppercase">
              <!-- Текстовый логотип стилизован под макет -->
                <span>П</span>
                <span class="absolute left-[9px] top-[1px]">О</span>
            </div>
          </div>
          <div class="leading-none text-[#2a8f96]">
            <span class="block text-[16px] font-semibold uppercase tracking-[0.02em]">ПЕРЭКС</span>
            <span class="mt-1 block text-[16px] font-semibold uppercase tracking-[0.02em]">ОЦЕНКА</span>
          </div>
        </NuxtLink>

        <nav aria-label="Основная навигация" class="hidden min-w-0 flex-1 lg:block">
          <ul class="flex w-full items-center justify-evenly text-[14px] font-medium text-slate-600 [font-family:Inter,sans-serif]">
            <li v-for="item in navigation" :key="item.to">
              <NuxtLink :to="item.to" class="transition hover:text-slate-900">
                {{ item.label }}
              </NuxtLink>
            </li>
          </ul>
        </nav>
      </div>

      <div class="ml-auto flex shrink-0 items-center gap-4 lg:gap-5">
        <a
          href="tel:+79609489292"
          class="hidden items-center gap-2 text-[12px] font-normal text-slate-500 transition hover:text-slate-900 md:flex"
        >
          <Icon class="h-6 w-6 text-slate-400" name="lucide:phone" />
          +7 960 948 92 92
        </a>
        <NuxtLink
          class="inline-flex h-10 items-center justify-center rounded-[10px] bg-[#37b5bd] px-7 text-[13px] font-semibold text-white transition hover:bg-[#2fa3aa]"
          to="/#contact-form"
        >
          Подать заявку
        </NuxtLink>
      </div>
    </div>
  </header>
</template>
