<script setup lang="ts">
import applicationPhoneIcon from '~/assets/icon/aplication-phone.svg'
import applicationMailIcon from '~/assets/icon/aplication-mail.svg'
import applicationMapIcon from '~/assets/icon/aplication-map.svg'
import applicationClockIcon from '~/assets/icon/aplication-clock.svg'

const contactIconMap = {
  phone: applicationPhoneIcon,
  mail: applicationMailIcon,
  pin: applicationMapIcon,
  clock: applicationClockIcon
} as const

const getContactIcon = (icon: string) =>
  contactIconMap[icon as keyof typeof contactIconMap]

defineProps<{
  presetPropertyType?: string
}>()

const contacts = [
  {
    title: 'Название компании',
    value: 'ООО "ПЕРЭКС-ОЦЕНКА"',
    note: 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ПЕРЭКС-ОЦЕНКА"',
    icon: 'pin'
  },
  {
    title: 'Телефоны',
    value: '8-923-168-88-10',
    note: '8-960-948-82-92 • 8-923-161-69-13',
    href: 'tel:+79231688810',
    icon: 'phone'
  },
  {
    title: 'E-mail',
    value: 'pereks79@mail.ru',
    note: '22isn@bk.ru',
    href: 'mailto:pereks79@mail.ru',
    icon: 'mail'
  },
  {
    title: 'Адрес и контактные лица',
    value: 'г.Барнаул, ул.Советской Армии, 171 в, оф.305',
    note: 'Илларионов Сергей Николаевич • Куранда Любовь Николаевна',
    icon: 'clock'
  }
]

const urgentService = {
  title: 'Срочная оценка?',
  description: 'Нужна срочная оценка недвижимости? Мы предлагаем экспресс-услугу с выполнением за 48 часов.',
  action: 'Запросить срочную услугу',
  href: 'tel:+79231688810'
}
</script>

<template>
  <section id="contacts" class="bg-[#eef2f6] px-0 py-8 sm:py-14 lg:py-20">
    <div class="container-default">
      <div class="mx-auto hidden max-w-3xl text-center sm:block">
        <h2 class="text-[36px] font-semibold tracking-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
          Свяжитесь с нами
        </h2>
        <p class="mt-4 text-[18px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
          Готовы начать оценку недвижимости? Свяжитесь с нами сегодня
        </p>
      </div>

      <div class="mt-10 grid gap-6 lg:grid-cols-[0.9fr_1.1fr]">
        <div class="hidden space-y-5 sm:block">
          <article class="rounded-[24px] border border-slate-200 bg-white p-6 shadow-sm sm:p-8">
            <h3 class="text-[22px] font-medium leading-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
              Контактная информация
            </h3>

            <div class="mt-6 space-y-6">
              <div v-for="item in contacts" :key="item.title" class="flex items-start gap-4">
                <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-[rgba(47,164,169,0.1)]">
                  <img :src="getContactIcon(item.icon)" alt="" class="h-6 w-6 object-contain" />
                </div>

                <div>
                  <p class="text-[16px] font-medium text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">{{ item.title }}</p>
                  <a
                    v-if="item.href"
                    :href="item.href"
                    class="mt-1 block text-[16px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif] hover:text-[rgba(31,58,95,1)]"
                  >
                    {{ item.value }}
                  </a>
                  <p v-else class="mt-1 text-[16px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
                    {{ item.value }}
                  </p>
                  <p class="text-[14px] font-normal leading-6 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">{{ item.note }}</p>
                </div>
              </div>
            </div>
          </article>

          <article class="rounded-[24px] bg-[#37b5bd] px-6 py-6 text-white shadow-sm sm:px-8">
            <h3 class="text-[26px] font-semibold leading-tight">{{ urgentService.title }}</h3>
            <p class="mt-3 max-w-md text-sm leading-6 text-white/90">{{ urgentService.description }}</p>
            <a
              class="mt-5 inline-flex rounded-2xl bg-white px-6 py-3 text-sm font-semibold text-[#37b5bd] transition hover:bg-slate-100"
              :href="urgentService.href"
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
