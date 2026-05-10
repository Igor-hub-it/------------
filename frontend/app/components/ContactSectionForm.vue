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
        property_type: form.propertyType.trim() || 'Не указано',
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
      'Не удалось отправить сообщение. Проверьте, что backend запущен и почтовый API настроен.'
  } finally {
    pending.value = false
  }
}
</script>

<template>
  <section class="rounded-[24px] border border-slate-200 bg-white p-6 shadow-sm sm:p-8">
    <div class="sm:hidden">
      <h2 class="text-[30px] sm:text-[46px] font-semibold leading-[1.1] text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
        Свяжитесь с нами
      </h2>
      <p class="mt-4 text-[17px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
        Оставьте заявку и мы перезвоним вам в течение 15 минут
      </p>
    </div>

    <h3 class="hidden text-[22px] font-medium leading-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif] sm:block">
      Отправьте нам сообщение
    </h3>

    <form class="mt-6 grid gap-4 md:grid-cols-2" @submit.prevent="submitForm">
      <label class="block md:col-span-2">
        <span class="mb-2 block text-[16px] font-medium text-[rgba(31,58,95,1)]">Ваше имя *</span>
        <input v-model="form.name" class="input-base rounded-[12px] border-slate-300" minlength="2" placeholder="Введите ваше имя" required type="text" />
      </label>

      <label class="block">
        <span class="mb-2 block text-[16px] font-medium text-[rgba(31,58,95,1)]">Телефон *</span>
        <input v-model="form.phone" class="input-base rounded-[12px] border-slate-300" minlength="6" placeholder="+7 (__) ___-_-__" required type="tel" />
      </label>

      <label class="block md:col-span-2">
        <span class="mb-2 block text-[16px] font-medium text-[rgba(31,58,95,1)]">Email *</span>
        <input v-model="form.email" class="input-base rounded-[12px] border-slate-300" placeholder="example@mail.com" required type="email" />
      </label>

      <label class="block md:col-span-2">
        <span class="mb-2 block text-[16px] font-medium text-[rgba(31,58,95,1)]">Тип недвижимости *</span>
        <select v-model="form.propertyType" class="input-base rounded-[12px] border-slate-300" required>
          <option disabled value="">Выберите тип объекта</option>
          <option v-for="item in propertyTypes" :key="item" :value="item">
            {{ item }}
          </option>
        </select>
      </label>

      <label class="block md:col-span-2">
        <span class="mb-2 block text-[16px] font-medium text-[rgba(31,58,95,1)]">Комментарий *</span>
        <textarea
          v-model="form.message"
          class="input-base min-h-[140px] resize-y rounded-[12px] border-slate-300"
          minlength="5"
          placeholder="Расскажите о вашем объекте недвижимости"
          required
        ></textarea>
      </label>

      <div class="md:col-span-2">
        <button
          class="inline-flex w-full items-center justify-center gap-3 rounded-[12px] bg-[#37b5bd] px-6 py-4 text-[18px] font-semibold text-white transition sm:hover:bg-[#2fa3aa] disabled:cursor-not-allowed disabled:opacity-70"
          :disabled="pending"
          type="submit"
        >
          <Icon class="hidden h-6 w-6 sm:block" name="lucide:send" />
          {{ pending ? 'Отправка...' : 'Подать заявку' }}
        </button>

        <p class="mx-auto mt-4 max-w-[290px] text-center text-[13px] leading-5 text-slate-500">
          Нажимая кнопку, вы соглашаетесь с политикой конфиденциальности
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
