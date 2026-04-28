<script setup lang="ts">
import { getServiceBySlug } from '~/utils/services'

const route = useRoute()
const slug = computed(() => String(route.params.slug || ''))
const service = computed(() => getServiceBySlug(slug.value))

if (!service.value) {
  throw createError({
    statusCode: 404,
    statusMessage: 'Страница услуги не найдена'
  })
}

useSeoMeta({
  title: service.value.title,
  description: service.value.description
})

const heroStyle = computed(() => ({
  backgroundImage: `linear-gradient(90deg, rgba(15, 23, 42, 0.72) 0%, rgba(15, 23, 42, 0.46) 42%, rgba(15, 23, 42, 0.24) 100%), url('${service.value?.heroBanner || ''}')`,
  backgroundSize: 'cover',
  backgroundPosition: 'center'
}))
</script>

<template>
  <div class="space-y-12 py-10 sm:py-14">
    <section
      class="overflow-hidden py-16 sm:py-20 lg:flex lg:h-[620px] lg:items-center lg:py-0"
      :style="heroStyle"
    >
      <div class="container-default grid gap-6 lg:grid-cols-[1.15fr_0.85fr]">
        <div>
          <p class="mb-4 text-sm font-semibold uppercase tracking-[0.2em] text-cyan-100">Услуги</p>
          <h1 class="text-4xl font-bold tracking-tight text-white sm:text-5xl">
            {{ service?.title }}
          </h1>
          <p class="mt-6 max-w-3xl text-base leading-7 text-slate-100 sm:text-lg">
            {{ service?.intro }}
          </p>
        </div>

        <div class="rounded-[28px] border border-white/20 bg-white/88 p-6 shadow-xl backdrop-blur-sm">
          <h2 class="text-xl font-semibold text-slate-900">Кому подходит услуга</h2>
          <ul class="mt-4 space-y-3 text-sm leading-6 text-slate-700">
            <li v-for="item in service?.audience" :key="item">
              {{ item }}
            </li>
          </ul>
        </div>
      </div>
    </section>

    <section class="container-default grid gap-6 lg:grid-cols-2">
      <article class="section-card p-6">
        <h2 class="text-2xl font-semibold text-slate-900">Что входит в работу</h2>
        <p class="mt-4 text-sm leading-6 text-slate-600">
          Проводим анализ документов и характеристик объекта, проверяем исходные данные, подбираем аналоги и готовим
          отчёт об оценке в соответствии с задачей клиента.
        </p>
      </article>

      <article class="section-card p-6">
        <h2 class="text-2xl font-semibold text-slate-900">Этапы оценки</h2>
        <ol class="mt-4 space-y-3 text-sm leading-6 text-slate-600">
          <li v-for="(step, index) in service?.steps" :key="step">
            {{ index + 1 }}. {{ step }}
          </li>
        </ol>
      </article>
    </section>

    <ContactSection :preset-property-type="service?.shortTitle" />
  </div>
</template>
