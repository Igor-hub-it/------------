<template>
  <footer class="border-t border-slate-200 bg-white">
    <div class="container-default flex flex-col gap-4 py-8 text-sm text-slate-600 md:flex-row md:items-center md:justify-between">
      <div>
        <p class="font-medium text-slate-900">Оценка недвижимости</p>
        <p>Независимая оценка жилой, коммерческой недвижимости и земельных участков.</p>
      </div>

      <div class="flex flex-col gap-2 text-left md:text-right">
        <a class="font-medium text-slate-900 hover:text-slate-700" href="tel:+79130000000">+7 913 000 00 00</a>
        <NuxtLink class="hover:text-slate-900" to="/politika-obrabotki-personalnyh-dannyh">
          Политика обработки персональных данных
        </NuxtLink>
        <a class="hover:text-slate-900" href="mailto:info@example.com">info@example.com</a>
      </div>
    </div>
  </footer>
</template>
