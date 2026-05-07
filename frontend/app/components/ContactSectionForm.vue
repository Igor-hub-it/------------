<script setup lang="ts">
const props = defineProps<{
  presetPropertyType?: string
}>()

const config = useRuntimeConfig()

const propertyTypes = [
  'Жилая недвижимость',
  'Нежилая недвижимость',
  'Земельный участок',
  'Движимое имущество',
  'Кадастровая стоимость'
]

const form = reactive({
  name: '',
  email: '',
  phone: '',
  propertyType: props.presetPropertyType || '',
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
    await $fetch('/api/applications', {
      baseURL: config.public.apiBase,
      method: 'POST',
      body: {
        name: form.name.trim(),
        email: form.email.trim(),
        phone: form.phone.trim(),
        property_type: form.propertyType.trim(),
        message: form.message.trim()
      }
    })

    successMessage.value = 'Сообщение отправлено. Мы свяжемся с вами в ближайшее время.'
    form.name = ''
    form.email = ''
    form.phone = ''
    form.propertyType = props.presetPropertyType || ''
    form.message = ''
  } catch (error: any) {
    console.error(error)
    errorMessage.value =
      error?.data?.detail ||
      'Не удалось отправить сообщение. Проверьте, что backend запущен и SMTP настроен.'
  } finally {
    pending.value = false
  }
}
</script>

<template>
  <section class="rounded-[24px] border border-slate-200 bg-white p-6 shadow-sm sm:p-8">
    <h3 class="text-[28px] font-semibold leading-tight text-slate-900">Отправьте нам сообщение</h3>

    <form class="mt-6 grid gap-4 md:grid-cols-2" @submit.prevent="submitForm">
      <label class="block md:col-span-2">
        <span class="mb-2 block text-sm font-medium text-slate-700">Полное имя *</span>
        <input v-model="form.name" class="input-base" minlength="2" placeholder="Иван Иванов" required type="text" />
      </label>

      <label class="block">
        <span class="mb-2 block text-sm font-medium text-slate-700">Электронная почта *</span>
        <input v-model="form.email" class="input-base" placeholder="ivan@example.com" required type="email" />
      </label>

      <label class="block">
        <span class="mb-2 block text-sm font-medium text-slate-700">Телефон</span>
        <input v-model="form.phone" class="input-base" minlength="6" placeholder="+7 913 000 00 00" required type="tel" />
      </label>

      <label class="block md:col-span-2">
        <span class="mb-2 block text-sm font-medium text-slate-700">Тип недвижимости *</span>
        <select v-model="form.propertyType" class="input-base" required>
          <option disabled value="">Выберите тип объекта</option>
          <option v-for="item in propertyTypes" :key="item" :value="item">
            {{ item }}
          </option>
        </select>
      </label>

      <label class="block md:col-span-2">
        <span class="mb-2 block text-sm font-medium text-slate-700">Сообщение *</span>
        <textarea
          v-model="form.message"
          class="input-base min-h-[140px] resize-y"
          minlength="5"
          placeholder="Пожалуйста, предоставьте подробности о вашей недвижимости"
          required
        ></textarea>
      </label>

      <div class="md:col-span-2">
        <button
          class="inline-flex w-full items-center justify-center gap-3 rounded-2xl bg-[#37b5bd] px-6 py-4 text-base font-semibold text-white transition hover:bg-[#2fa3aa] disabled:cursor-not-allowed disabled:opacity-70"
          :disabled="pending"
          type="submit"
        >
          <Icon class="h-6 w-6" name="lucide:send" />
          {{ pending ? 'Отправка...' : 'Отправить сообщение' }}
        </button>

        <p class="mt-4 text-center text-xs leading-5 text-slate-400">
          Отправляя эту форму, вы соглашаетесь с нашей политикой конфиденциальности и условиями предоставления услуг.
        </p>

        <p v-if="successMessage" class="mt-3 text-sm text-emerald-600">
          {{ successMessage }}
        </p>
        <p v-else-if="errorMessage" class="mt-3 text-sm text-rose-600">
          {{ errorMessage }}
        </p>
      </div>
    </form>
  </section>
</template>
