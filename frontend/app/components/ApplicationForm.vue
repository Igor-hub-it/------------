<script setup lang="ts">
const props = defineProps<{
  title?: string
  description?: string
  presetPropertyType?: string
}>()

const config = useRuntimeConfig()

const propertyTypes = [
  'Жилая недвижимость',
  'Нежилые помещения',
  'Нежилые здания с земельным участком',
  'Гаражи и парковки',
  'Незавершённые нежилые здания',
  'Земельные участки',
  'Оценка для снижения кадастровой стоимости',
  'Движимое имущество',
  'Нежилая недвижимость',
  'Земельный участок',
  'Кадастровая стоимость'
]
const defaultPropertyType = propertyTypes[0] ?? 'Жилая недвижимость'

const form = reactive({
  name: '',
  email: '',
  phone: '',
  propertyType: props.presetPropertyType || defaultPropertyType,
  message: ''
})

watch(
  () => props.presetPropertyType,
  (value) => {
    if (value) {
      form.propertyType = value
    }
  }
)

const pending = ref(false)
const successMessage = ref('')
const errorMessage = ref('')

async function submitForm() {
  pending.value = true
  successMessage.value = ''
  errorMessage.value = ''

  try {
    const payload = {
      name: form.name.trim(),
      email: form.email.trim(),
      phone: form.phone.trim(),
      property_type: form.propertyType.trim(),
      message: form.message.trim()
    }

    await $fetch('/api/applications', {
      baseURL: config.public.apiBase,
      method: 'POST',
      body: payload
    })

    successMessage.value = 'Заявка отправлена. Мы свяжемся с вами в ближайшее время.'
    form.name = ''
    form.email = ''
    form.phone = ''
    form.message = ''
    form.propertyType = props.presetPropertyType || defaultPropertyType
  } catch (error: any) {
    console.error(error)
    errorMessage.value =
      error?.data?.detail ||
      'Не удалось отправить заявку. Проверьте, что backend запущен и SMTP настроен.'
  } finally {
    pending.value = false
  }
}
</script>

<template>
  <section class="section-card p-6 sm:p-8">
    <div class="mb-6">
      <h2 class="text-2xl font-semibold text-slate-900">
        {{ title || 'Оставить заявку' }}
      </h2>
      <p class="mt-2 max-w-2xl text-sm leading-6 text-slate-600">
        {{ description || 'Заполните форму, и мы свяжемся с вами для уточнения задачи, сроков и стоимости работ.' }}
      </p>
    </div>

    <form class="grid gap-4 md:grid-cols-2" @submit.prevent="submitForm">
      <label class="block">
        <span class="mb-2 block text-sm text-slate-600">Имя</span>
        <input v-model="form.name" class="input-base" minlength="2" name="name" required type="text" />
      </label>

      <label class="block">
        <span class="mb-2 block text-sm text-slate-600">Email</span>
        <input v-model="form.email" class="input-base" name="email" required type="email" />
      </label>

      <label class="block">
        <span class="mb-2 block text-sm text-slate-600">Телефон</span>
        <input v-model="form.phone" class="input-base" minlength="6" name="phone" required type="tel" />
      </label>

      <label class="block">
        <span class="mb-2 block text-sm text-slate-600">Объект оценки</span>
        <select v-model="form.propertyType" class="input-base" name="propertyType" required>
          <option v-for="item in propertyTypes" :key="item" :value="item">
            {{ item }}
          </option>
        </select>
      </label>

      <label class="block md:col-span-2">
        <span class="mb-2 block text-sm text-slate-600">Сообщение</span>
        <textarea
          v-model="form.message"
          class="input-base min-h-36 resize-y"
          minlength="5"
          name="message"
          required
        ></textarea>
      </label>

      <div class="md:col-span-2 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <button class="button-primary" :disabled="pending" type="submit">
          {{ pending ? 'Отправка...' : 'Отправить заявку' }}
        </button>

        <p v-if="successMessage" class="text-sm text-emerald-600">
          {{ successMessage }}
        </p>
        <p v-else-if="errorMessage" class="text-sm text-rose-600">
          {{ errorMessage }}
        </p>
      </div>
    </form>
  </section>
</template>
