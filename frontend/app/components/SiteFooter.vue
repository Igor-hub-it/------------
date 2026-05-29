<template>
  <footer class="bg-[rgba(31,58,95,1)]">
    <div class="container-default px-6 py-14 sm:px-10 lg:px-14">
      <div class="grid gap-10 md:grid-cols-2 lg:grid-cols-4">
        <div class="max-w-[290px]">
          <h3 class="text-[18px] font-semibold leading-7 text-[rgba(255,255,255,1)] [font-family:Inter,sans-serif]">
            ОБЩЕСТВО С ОГРАНИЧЕННОЙ
            <br />
            ОТВЕТСТВЕННОСТЬЮ "ПЕРЭКС-ОЦЕНКА"
          </h3>
          <p class="mt-5 text-[14px] font-normal leading-6 text-[rgba(255,255,255,0.7)] [font-family:Inter,sans-serif]">
            Профессиональные услуги кадастровой оценки недвижимости с общенациональным охватом.
          </p>
        </div>

        <div>
          <h4 class="text-[20px] font-semibold leading-7 text-white [font-family:Inter,sans-serif]">Наши услуги</h4>
          <ul class="mt-4 space-y-2.5">
            <li><a class="text-[16px] font-normal text-[rgba(255,255,255,0.7)] transition hover:text-white [font-family:Inter,sans-serif]" href="#pricing">Оценка жилой недвижимости</a></li>
            <li><a class="text-[16px] font-normal text-[rgba(255,255,255,0.7)] transition hover:text-white [font-family:Inter,sans-serif]" href="#pricing">Оценка коммерческой недвижимости</a></li>
            <li><a class="text-[16px] font-normal text-[rgba(255,255,255,0.7)] transition hover:text-white [font-family:Inter,sans-serif]" href="#pricing">Оценка земли</a></li>
            <li><a class="text-[16px] font-normal text-[rgba(255,255,255,0.7)] transition hover:text-white [font-family:Inter,sans-serif]" href="#pricing">Движимое имущество</a></li>
            <li><a class="text-[16px] font-normal text-[rgba(255,255,255,0.7)] transition hover:text-white [font-family:Inter,sans-serif]" href="#pricing">Снижение кадастровой стоимости</a></li>
          </ul>
        </div>

        <div>
          <h4 class="text-[20px] font-semibold leading-7 text-white [font-family:Inter,sans-serif]">Быстрые ссылки</h4>
          <ul class="mt-4 space-y-2.5">
            <li><NuxtLink class="text-[16px] font-normal text-[rgba(255,255,255,0.7)] transition hover:text-white [font-family:Inter,sans-serif]" to="/#about">О нас</NuxtLink></li>
            <li><NuxtLink class="text-[16px] font-normal text-[rgba(255,255,255,0.7)] transition hover:text-white [font-family:Inter,sans-serif]" to="/#team">Наши эксперты</NuxtLink></li>
            <li><NuxtLink class="text-[16px] font-normal text-[rgba(255,255,255,0.7)] transition hover:text-white [font-family:Inter,sans-serif]" to="/#reviews">Отзывы клиентов</NuxtLink></li>
            <li><NuxtLink class="text-[16px] font-normal text-[rgba(255,255,255,0.7)] transition hover:text-white [font-family:Inter,sans-serif]" to="/#contacts">Часто задаваемые вопросы</NuxtLink></li>
            <li><NuxtLink class="text-[16px] font-normal text-[rgba(255,255,255,0.7)] transition hover:text-white [font-family:Inter,sans-serif]" to="/politika-obrabotki-personalnyh-dannyh">Политика конфиденциальности</NuxtLink></li>
          </ul>
        </div>

        <div>
          <h4 class="text-[20px] font-semibold leading-7 text-white [font-family:Inter,sans-serif]">Свяжитесь с нами</h4>
          <ul class="mt-4 space-y-3.5">
            <li class="flex items-start gap-3 text-[16px] text-[rgba(255,255,255,0.7)] [font-family:Inter,sans-serif]">
              <Icon class="mt-0.5 h-5 w-5 shrink-0 text-white" name="lucide:phone" />
              <div class="space-y-1">
                <a class="block transition hover:text-white" href="tel:+79231688810">8-923-168-88-10</a>
                <a class="block transition hover:text-white" href="tel:+79609488292">8-960-948-82-92</a>
                <a class="block transition hover:text-white" href="tel:+79231616913">8-923-161-69-13</a>
              </div>
            </li>
            <li class="flex items-start gap-3 text-[16px] text-[rgba(255,255,255,0.7)] [font-family:Inter,sans-serif]">
              <Icon class="mt-0.5 h-5 w-5 shrink-0 text-white" name="lucide:mail" />
              <div class="space-y-1">
                <a class="block transition hover:text-white" href="mailto:pereks79@mail.ru">pereks79@mail.ru</a>
                <a class="block transition hover:text-white" href="mailto:22isn@bk.ru">22isn@bk.ru</a>
              </div>
            </li>
            <li class="flex items-start gap-3 text-[16px] text-[rgba(255,255,255,0.7)] [font-family:Inter,sans-serif]">
              <Icon class="mt-0.5 h-5 w-5 shrink-0 text-white" name="lucide:map-pin" />
              <span>г.Барнаул, ул.Советской Армии, 171 в, оф.305</span>
            </li>
            <li class="flex items-start gap-3 text-[16px] text-[rgba(255,255,255,0.7)] [font-family:Inter,sans-serif]">
              <Icon class="mt-0.5 h-5 w-5 shrink-0 text-white" name="lucide:users" />
              <div class="space-y-1">
                <span class="block">Илларионов Сергей Николаевич</span>
                <span class="block">Куранда Любовь Николаевна</span>
              </div>
            </li>
          </ul>
        </div>
      </div>

      <div class="mt-10 border-t border-[rgba(255,255,255,0.12)] pt-6">
        <div class="flex flex-col gap-3 lg:flex-row lg:items-center lg:justify-between">
          <p class="text-[14px] font-normal text-[rgba(255,255,255,0.7)] [font-family:Inter,sans-serif]">
            © 2026 Перэкс оценка. Все права защищены.
          </p>
          <div class="flex flex-wrap gap-6">
            <a class="text-[14px] font-normal text-[rgba(255,255,255,0.7)] transition hover:text-white [font-family:Inter,sans-serif]" href="#">Условия предоставления услуг</a>
            <NuxtLink class="text-[14px] font-normal text-[rgba(255,255,255,0.7)] transition hover:text-white [font-family:Inter,sans-serif]" to="/politika-obrabotki-personalnyh-dannyh">Политика конфиденциальности</NuxtLink>
            <!-- <a class="text-[14px] font-normal text-[rgba(255,255,255,0.7)] transition hover:text-white [font-family:Inter,sans-serif]" href="#">Политика использования файлов cookie</a> -->
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>
