<script setup lang="ts">
const contactIconMap = {
  phone: 'lucide:phone',
  mail: 'lucide:mail',
  pin: 'lucide:map-pin',
  clock: 'lucide:clock-3'
} as const

defineProps<{
  presetPropertyType?: string
}>()

const contacts = [
  {
    title: 'Телефон',
    value: '+7 913 000 00 00',
    note: 'Пн-Пт: 9:00 - 18:00',
    href: 'tel:+79130000000',
    icon: 'phone'
  },
  {
    title: 'Электронная почта',
    value: 'info@example.com',
    note: 'Ответ в течение 24 часов',
    href: 'mailto:info@example.com',
    icon: 'mail'
  },
  {
    title: 'Адрес офиса',
    value: 'г. Новосибирск, ул. Примерная, 12',
    note: 'Офис для консультаций по записи',
    icon: 'pin'
  },
  {
    title: 'Часы работы',
    value: 'Понедельник - Пятница: 9:00 - 18:00',
    note: 'Суббота: 10:00 - 14:00',
    icon: 'clock'
  }
]

const urgentService = {
  title: 'Срочная оценка?',
  description: 'Нужна срочная оценка недвижимости? Мы предлагаем экспресс-услугу с выполнением за 48 часов.',
  action: 'Запросить срочную услугу'
}
</script>

<template>
  <section id="contacts" class="bg-[#eef2f6] px-6 py-14 sm:px-10 lg:px-14 lg:py-20">
    <div class="container-default">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl">Свяжитесь с нами</h2>
        <p class="mt-4 text-base leading-7 text-slate-500">
          Готовы начать оценку недвижимости? Свяжитесь с нами сегодня
        </p>
      </div>

      <div class="mt-10 grid gap-6 lg:grid-cols-[0.9fr_1.1fr]">
        <div class="space-y-5">
          <article class="rounded-[24px] border border-slate-200 bg-white p-6 shadow-sm sm:p-8">
            <h3 class="text-[28px] font-semibold leading-tight text-slate-900">Контактная информация</h3>

            <div class="mt-6 space-y-6">
              <div v-for="item in contacts" :key="item.title" class="flex items-start gap-4">
                <div class="flex h-11 w-11 shrink-0 items-center justify-center rounded-full bg-emerald-50 text-emerald-500">
                  <Icon :name="contactIconMap[item.icon]" class="h-5 w-5" />
                </div>

                <div>
                  <p class="text-base font-semibold text-slate-900">{{ item.title }}</p>
                  <a
                    v-if="item.href"
                    :href="item.href"
                    class="mt-1 block text-base leading-7 text-slate-600 hover:text-slate-900"
                  >
                    {{ item.value }}
                  </a>
                  <p v-else class="mt-1 text-base leading-7 text-slate-600">
                    {{ item.value }}
                  </p>
                  <p class="text-sm leading-6 text-slate-400">{{ item.note }}</p>
                </div>
              </div>
            </div>
          </article>

          <article class="rounded-[24px] bg-[#37b5bd] px-6 py-6 text-white shadow-sm sm:px-8">
            <h3 class="text-[26px] font-semibold leading-tight">{{ urgentService.title }}</h3>
            <p class="mt-3 max-w-md text-sm leading-6 text-white/90">{{ urgentService.description }}</p>
            <a
              class="mt-5 inline-flex rounded-2xl bg-white px-6 py-3 text-sm font-semibold text-[#37b5bd] transition hover:bg-slate-100"
              href="#contact-form"
            >
              {{ urgentService.action }}
            </a>
          </article>
        </div>

        <div id="contact-form">
          <ContactSectionForm :preset-property-type="presetPropertyType" />
        </div>
      </div>
    </div>
  </section>
</template>
