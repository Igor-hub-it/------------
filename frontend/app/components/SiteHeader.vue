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
  <header class="sticky top-0 z-40 h-[75px] border-b border-slate-200 bg-[rgba(233,237,242,0.96)] backdrop-blur">
    <div class="container-default flex h-full items-center justify-between gap-6">
      <div class="flex items-center gap-8">
        <NuxtLink to="/" aria-label="На главную" class="block h-[53px] w-[130px] shrink-0 rounded-2xl bg-slate-900 px-4 py-3 text-white">
          <span class="block text-[10px] uppercase tracking-[0.24em] text-slate-300">Эксперт</span>
          <span class="mt-1 block text-sm font-semibold leading-4">Оценка недвижимости</span>
        </NuxtLink>

        <nav aria-label="Основная навигация" class="hidden lg:block">
          <ul class="flex flex-wrap gap-2 text-sm font-medium text-slate-700">
            <li v-for="item in navigation" :key="item.to">
              <NuxtLink :to="item.to" class="rounded-full px-4 py-2 hover:bg-white hover:text-slate-900">
                {{ item.label }}
              </NuxtLink>
            </li>
          </ul>
        </nav>
      </div>

      <div class="flex items-center gap-3">
        <a href="tel:+79130000000" class="text-base font-semibold text-slate-900 hover:text-slate-700">
          +7 913 000 00 00
        </a>
        <NuxtLink class="button-primary" to="/#contact-form">Подать заявку</NuxtLink>
      </div>
    </div>
  </header>
</template>
