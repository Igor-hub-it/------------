<script setup lang="ts">
import logo from '~/assets/icon/logo.svg'
import logoMobile from '~/assets/icon/logo-mobile.svg'

const navigation = [
  { label: 'О компании', to: '/#about' },
  // { label: 'Услуги оценки', to: '/#services' },
  { label: 'Услуги', to: '/#main-services' },
  { label: 'Цены', to: '/#pricing' },
  { label: 'Контакты', to: '/#contacts' }
]

const isMobileMenuOpen = ref(false)
const route = useRoute()

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

const closeMobileMenu = () => {
  isMobileMenuOpen.value = false
}

watch(isMobileMenuOpen, (isOpen) => {
  if (import.meta.client) {
    document.body.style.overflow = isOpen ? 'hidden' : ''
  }
})

watch(
  () => route.fullPath,
  () => {
    closeMobileMenu()
  }
)

onBeforeUnmount(() => {
  if (import.meta.client) {
    document.body.style.overflow = ''
  }
})
</script>

<template>
  <header class="sticky top-0 z-50 border-b border-white/20 bg-[rgba(31,58,95,1)] lg:border-slate-300 lg:bg-white">
    <div class="mx-auto flex h-[53px] sm:h-[75px] w-full max-w-[1260px] items-center gap-8 px-4 sm:px-6">
      <div class="flex min-w-0 flex-1 items-center gap-8 xl:gap-10">
        <NuxtLink to="/" aria-label="На главную" class="flex h-[53px] w-[170px] shrink-0 items-center" @click="closeMobileMenu">
          <img :src="logoMobile" alt="ПЕРАКС-ОЦЕНКА" class="h-[40px] w-[110px] object-contain lg:hidden" />
          <img :src="logo" alt="ПЕРАКС-ОЦЕНКА" class="hidden h-[53px] w-[131px] object-contain lg:block" />
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

      <div class="ml-auto hidden shrink-0 items-center gap-4 lg:flex lg:gap-5">
        <a
          href="tel:+79609488292"
          class="hidden items-center gap-2 text-[14px] font-medium text-[rgba(107,119,133,1)] transition hover:text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif] md:flex"
        >
          <Icon class="h-4 w-4 text-[rgba(107,119,133,1)]" name="lucide:phone" />
          +7 960 948 82 92
        </a>
        <NuxtLink
          class="inline-flex h-10 items-center justify-center rounded-[10px] bg-[#37b5bd] px-7 text-[13px] font-semibold text-white transition hover:bg-[#2fa3aa]"
          to="/#contact-form"
        >
          Подать заявку
        </NuxtLink>
      </div>

      <button
        :aria-expanded="isMobileMenuOpen"
        aria-label="Открыть меню"
        class="ml-auto inline-flex h-11 w-11 items-center justify-center lg:hidden"
        type="button"
        @click="toggleMobileMenu"
      >
        <span class="relative h-5 w-6">
          <span
            class="absolute left-0 top-0 h-[2px] w-6 rounded bg-white transition-all duration-300"
            :class="isMobileMenuOpen ? 'top-2 rotate-45' : ''"
          ></span>
          <span
            class="absolute left-0 top-2 h-[2px] w-6 rounded bg-white transition-all duration-300"
            :class="isMobileMenuOpen ? 'opacity-0' : ''"
          ></span>
          <span
            class="absolute left-0 top-4 h-[2px] w-6 rounded bg-white transition-all duration-300"
            :class="isMobileMenuOpen ? '!top-2 -rotate-45' : ''"
          ></span>
        </span>
      </button>
    </div>

    <div
      class="fixed inset-x-0 bottom-0 top-[53px] sm:top-[75px] lg:hidden"
      :class="isMobileMenuOpen ? 'pointer-events-auto' : 'pointer-events-none'"
    >
      <button
        aria-label="Закрыть меню"
        class="absolute inset-0 bg-black/40 transition-opacity duration-300"
        :class="isMobileMenuOpen ? 'opacity-100' : 'opacity-0'"
        type="button"
        @click="closeMobileMenu"
      ></button>

      <aside
        class="relative h-full w-full max-w-none bg-[rgba(31,58,95,1)] px-5 pb-5 pt-4 shadow-xl transition-transform duration-300 ease-out"
        :class="isMobileMenuOpen ? 'translate-x-0' : '-translate-x-full'"
      >
        <nav aria-label="Мобильная навигация">
          <ul class="space-y-1">
            <li v-for="item in navigation" :key="item.to">
              <NuxtLink
                :to="item.to"
                class="block rounded-lg px-3 py-2 text-[15px] font-medium text-white transition hover:bg-white/10"
                @click="closeMobileMenu"
              >
                {{ item.label }}
              </NuxtLink>
            </li>
          </ul>
        </nav>

        <a
          href="tel:+79609488292"
          class="mt-4 inline-flex w-full items-center justify-center gap-2 rounded-[10px] border border-white/25 px-4 py-3 text-[15px] font-medium text-white transition hover:bg-white/10 [font-family:Inter,sans-serif]"
          @click="closeMobileMenu"
        >
          <Icon class="h-4 w-4" name="lucide:phone" />
          +7 960 948 82 92
        </a>

        <NuxtLink
          class="mt-4 inline-flex h-11 w-full items-center justify-center rounded-[10px] bg-[#37b5bd] px-7 text-[14px] font-semibold text-white transition hover:bg-[#2fa3aa]"
          to="/#contact-form"
          @click="closeMobileMenu"
        >
          Подать заявку
        </NuxtLink>
      </aside>
    </div>
  </header>
</template>
