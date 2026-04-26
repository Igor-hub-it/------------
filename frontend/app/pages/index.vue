<script setup lang="ts">
import { serviceLinks } from '~/utils/services'

useSeoMeta({
  title: 'Оценка недвижимости и кадастровой стоимости',
  description:
    'Лендинг компании по независимой оценке жилой и коммерческой недвижимости, земельных участков и кадастровой стоимости.'
})

const keyAdvantages = [
  {
    title: 'Обширный опыт',
    description: 'Более 15 лет профессионального опыта оценки всех типов недвижимости',
    icon: 'user'
  },
  {
    title: 'Профессиональный персонал',
    description: 'Лицензированные и сертифицированные оценщики с высокой квалификацией',
    icon: 'users'
  },
  {
    title: 'Онлайн-заказ',
    description: 'Подавайте заявки и отслеживайте прогресс из любого места в любое время',
    icon: 'monitor'
  },
  {
    title: 'Доступные цены',
    description: 'Конкурентные тарифы без ущерба качеству и соответствию требованиям',
    icon: 'money'
  },
  {
    title: 'Юридическое соответствие',
    description: 'Все отчёты соответствуют национальным стандартам и нормативным требованиям',
    icon: 'document'
  },
  {
    title: 'Безопасность данных',
    description: 'Ваша информация защищена шифрованием банковского уровня',
    icon: 'lock'
  },
  {
    title: 'Гарантия 3 года',
    description: 'Мы гарантируем наши оценки всеобъемлющей гарантией',
    icon: 'shield'
  },
  {
    title: 'Быстрое выполнение',
    description: 'Быстрая обработка для соблюдения ваших сроков',
    icon: 'flash'
  }
]

const reasons = [
  {
    title: 'По всей стране',
    description: 'Мы работаем во всех регионах с местным рыночным опытом',
    icon: 'pin'
  },
  {
    title: 'Онлайн-услуги',
    description: 'Полный процесс подачи заявки в цифровом формате из любого места',
    icon: 'phone'
  },
  {
    title: 'Гибкие осмотры',
    description: 'Планируйте посещения объекта в удобное для вас время',
    icon: 'clock'
  },
  {
    title: 'Широкая сеть экспертов',
    description: 'Доступ к специализированным оценщикам для любого типа недвижимости',
    icon: 'users'
  },
  {
    title: 'Все типы недвижимости',
    description: 'От жилой до коммерческой и земельных участков',
    icon: 'building'
  }
]

const reasonGuarantee = {
  title: 'Гарантия качества',
  description: 'Каждая оценка проверяется старшими оценщиками для обеспечения точности и соответствия отраслевым стандартам.'
}

const processSteps = [
  {
    step: '01',
    title: 'Заявка',
    description: 'Подайте заявку онлайн или по телефону с базовыми данными о недвижимости',
    icon: 'document'
  },
  {
    step: '02',
    title: 'Визит специалиста',
    description: 'Наш оценщик осмотрит объект в удобное для вас время',
    icon: 'pin'
  },
  {
    step: '03',
    title: 'Оценка',
    description: 'Экспертный анализ с использованием рыночных данных и профессиональной методологии',
    icon: 'calculator'
  },
  {
    step: '04',
    title: 'Доставка отчета',
    description: 'Получите полный отчёт об оценке, соответствующий всем юридическим требованиям',
    icon: 'send'
  }
]

const directionPropertyGroups = [
  {
    title: 'Жилая недвижимость',
    items: [
      'Квартира, комната, гостиница, кухня-прихожая, в т.ч доля в праве на них',
      'Дом, коттедж, дача, таунхаус с земельным участком, в т.ч. доля в праве на них',
      'Незавершенный строительством дом, коттедж, таунхаус, дача с зем. участком, в т.ч доля'
    ]
  },
  {
    title: 'Нежилая недвижимость',
    items: [
      'Нежилые помещения',
      'Гараж, парк. место',
      'Нежилое здание с зем. уч.',
      'Незавершенное стр. нежилое здание с зем уч.'
    ]
  },
  {
    title: 'Земельные участки',
    items: ['<10 соток', '10-50 сот', 'От 50 сот до 1 га', 'От 1 га до 100 га', 'От 100 до 1000 га', 'Более 1000 га']
  }
]

const directionCadastreItems = [
  'Зем уч любого назначения',
  'Нежилое здание',
  'Жилое помещение: квартира, комната, гостиница, кухня-прихожая',
  'Нежилое помещение',
  'Жилое здание: дом, коттедж, таунхаус, дача'
]

const directionMovableLabel = 'Транспорт, оборудование, прочие активы'

const expertHighlights = [
  {
    title: 'Национальная сертификация оценщиков',
    description: 'Все оценщики имеют действующие национальные лицензии',
    icon: 'badge'
  },
  {
    title: 'Передовое обучение',
    description: 'Регулярное профессиональное развитие и образование',
    icon: 'cap'
  },
  {
    title: 'Отраслевые аккредитации',
    description: 'Члены профессиональных оценочных ассоциаций',
    icon: 'document'
  },
  {
    title: 'Стандарты качества',
    description: 'Сертифицированные по ISO процессы оценки',
    icon: 'star'
  }
]

const team = [
  {
    initials: 'МК',
    name: 'Мария Ковальски',
    role: 'Старший оценщик недвижимости',
    experience: 'Лицензированный оценщик • 15 лет опыта',
    specialty: 'Специализация: Жилая и коммерческая недвижимость'
  },
  {
    initials: 'ЯН',
    name: 'Ян Новак',
    role: 'Главный директор по оценке',
    experience: 'Сертифицированный мастер-оценщик • 20 лет опыта',
    specialty: 'Специализация: Сложные объекты и земля'
  },
  {
    initials: 'АВ',
    name: 'Анна Вишневская',
    role: 'Специалист по коммерческой недвижимости',
    experience: 'Лицензированный оценщик • 12 лет опыта',
    specialty: 'Специализация: Торговые и офисные площади'
  },
  {
    initials: 'ПК',
    name: 'Пётр Ковальчик',
    role: 'Специалист по земле и сельскому хозяйству',
    experience: 'Лицензированный оценщик • 18 лет опыта',
    specialty: 'Специализация: Земельные участки и фермы'
  }
]

const expertCertificationNote = {
  title: 'Сертифицированное превосходство',
  description:
    'Наше агентство и все оценщики лицензированы и сертифицированы национальным регулирующим органом. Мы поддерживаем профессиональное страхование ответственности и придерживаемся высочайших этических стандартов в отрасли.'
}

const reviews = [
  {
    author: 'Роберт Левандовски',
    role: 'Домовладелец',
    date: 'Январь 2026',
    rating: 5,
    text: '"Отличный сервис от начала до конца. Оценщик был профессиональным, тщательным и предоставил отчет раньше срока. Настоятельно рекомендую всем, кому нужна оценка недвижимости."'
  },
  {
    author: 'Елена Ковальска',
    role: 'Инвестор в недвижимость',
    date: 'Декабрь 2025',
    rating: 5,
    text: '"Я пользовалась их услугами несколько раз для своих инвестиционных объектов. Стабильно точные оценки и быстрая обработка. Процесс онлайн-заявки очень удобен."'
  },
  {
    author: 'Томаш Новицкий',
    role: 'Владелец бизнеса',
    date: 'Ноябрь 2025',
    rating: 5,
    text: '"Нужна была оценка коммерческой недвижимости для банковского кредита. Команда была осведомлена о коммерческой недвижимости и предоставила полный отчет, соответствующий всем требованиям."'
  },
  {
    author: 'Магдалена Войчик',
    role: 'Юридический представитель',
    date: 'Октябрь 2025',
    rating: 5,
    text: '"Профессиональный и надежный сервис для целей раздела наследства. Отчет об оценке был четким, хорошо задокументированным и принят всеми сторонами. Отличная коммуникация на протяжении всего процесса."'
  }
]

const reviewStats = [
  { value: '4.9', label: 'Средний рейтинг', icon: 'star' },
  { value: '500+', label: 'Отзывов клиентов' },
  { value: '98%', label: 'Рекомендуют нас' }
]

const priceList = [
  {
    title: 'Оценка жилой недвижимости',
    price: 'от 5 000 руб.',
    description: 'Квартиры, дома, комнаты, таунхаусы и иные жилые объекты.'
  },
  {
    title: 'Оценка нежилой недвижимости',
    price: 'от 12 000 руб.',
    description: 'Офисы, склады, торговые площади, производственные и иные коммерческие объекты.'
  },
  {
    title: 'Оценка незавершенных зданий',
    price: 'от 15 000 руб.',
    description: 'Объекты незавершённого строительства для сделок, суда и инвестиционного анализа.'
  },
  {
    title: 'Оценка земельных участков',
    price: 'от 8 000 руб.',
    description: 'Участки под ИЖС, сельхозназначение, коммерческое и иное использование.'
  },
  {
    title: 'Оценка движимого имущества',
    price: 'от 6 000 руб.',
    description: 'Транспорт, оборудование, техника и другие движимые активы.'
  },
  {
    title: 'Снижение кадастровой стоимости',
    price: 'по запросу',
    description: 'Предварительный анализ, отчёт и сопровождение для снижения налоговой нагрузки.'
  }
]

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

const aboutFeatures = [
  {
    title: 'По всей стране',
    description: 'Работаем во всех регионах',
    icon: 'pin'
  },
  {
    title: 'Онлайн-услуги',
    description: 'Подавайте заявки удалённо',
    icon: 'globe'
  },
  {
    title: 'Гибкий график',
    description: 'Удобное время осмотра',
    icon: 'calendar'
  }
]

const companyStats = [
  { value: '15+', label: 'Лет опыта', large: true },
  { value: '10+\n000', label: 'Оценено объектов', large: true },
  { value: '50+', label: 'Экспертов-оценщиков' },
  { value: '100%', label: 'Юридическое соответствие' }
]
</script>

<template>
  <div class="container-default space-y-20 py-10 sm:py-14">
    <section id="services" class="grid gap-8 lg:grid-cols-[1.15fr_0.85fr] lg:items-center">
      <div>
        <p class="section-label">Услуги по оценке недвижимости</p>
        <h1 class="mt-4 max-w-4xl text-4xl font-bold tracking-tight text-slate-900 sm:text-5xl">
          Проводим независимую оценку недвижимости для сделок, суда, банков и снижения кадастровой нагрузки
        </h1>
        <p class="mt-6 max-w-3xl text-base leading-7 text-slate-600 sm:text-lg">
          Работаем с жилой и коммерческой недвижимостью, земельными участками и задачами по кадастровой стоимости.
          Подготавливаем отчёты и сопровождаем клиента от первой консультации до готового результата.
        </p>

        <div class="mt-8 flex flex-wrap gap-4">
          <a class="button-primary" href="#contact-form">Подать заявку</a>
          <NuxtLink class="button-secondary" to="/uslugi/kadastrovaya-stoimost">
            Подробнее об услугах
          </NuxtLink>
        </div>
      </div>

      <div class="section-card p-8">
        <p class="section-label">Что входит в услугу</p>
        <ul class="mt-6 space-y-4 text-sm leading-6 text-slate-600">
          <li>Отчёт об оценке под конкретную задачу: сделка, суд, залог, наследство или пересмотр кадастровой стоимости.</li>
          <li>Понятный план работ с перечнем документов, сроками и ответственным специалистом.</li>
          <li>Поддержка по вопросам оформления заявки и передачи исходных данных онлайн.</li>
        </ul>
      </div>
    </section>

    <section id="about" class="grid gap-10 lg:grid-cols-[1.08fr_0.92fr] lg:items-stretch">
      <article class="section-card p-8 lg:p-10">
        <h2 class="text-[40px] font-semibold leading-tight tracking-tight text-slate-900 max-sm:text-3xl">
          О нашей компании
        </h2>
        <div class="mt-6 space-y-5 text-[17px] leading-8 text-slate-500">
          <p>
            Мы - профессиональное кадастровое агентство по оценке недвижимости с проверенным опытом предоставления
            точных, юридически обоснованных оценок всех типов недвижимости. Наша команда лицензированных оценщиков
            сочетает технический опыт с рыночными знаниями для предоставления комплексных услуг оценки.
          </p>
          <p>
            Благодаря общенациональному охвату и возможности обработки заявок онлайн, мы делаем профессиональную
            оценку недвижимости доступной, эффективной и прозрачной.
          </p>
        </div>

        <div class="mt-8 space-y-5 border-t border-slate-200 pt-6">
          <div v-for="feature in aboutFeatures" :key="feature.title" class="flex items-start gap-4">
            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full border border-slate-300 bg-slate-50 text-slate-700">
              <svg
                v-if="feature.icon === 'pin'"
                class="h-5 w-5"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="1.8"
              >
                <path d="M12 21s6-5.2 6-11a6 6 0 1 0-12 0c0 5.8 6 11 6 11Z" />
                <circle cx="12" cy="10" r="2.5" />
              </svg>
              <svg
                v-else-if="feature.icon === 'globe'"
                class="h-5 w-5"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="1.8"
              >
                <circle cx="12" cy="12" r="9" />
                <path d="M3 12h18M12 3a15 15 0 0 1 0 18M12 3a15 15 0 0 0 0 18" />
              </svg>
              <svg
                v-else
                class="h-5 w-5"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="1.8"
              >
                <rect x="4" y="5" width="16" height="15" rx="2" />
                <path d="M8 3v4M16 3v4M4 10h16" />
              </svg>
            </div>
            <div>
              <h3 class="text-lg font-semibold text-slate-900">{{ feature.title }}</h3>
              <p class="mt-1 text-sm text-slate-500">{{ feature.description }}</p>
            </div>
          </div>
        </div>
      </article>

      <div class="grid gap-4 sm:grid-cols-2">
        <article
          v-for="stat in companyStats"
          :key="stat.label"
          class="rounded-[28px] border border-slate-200 bg-white p-8 shadow-sm"
          :class="stat.large ? 'min-h-[210px]' : 'min-h-[130px]'"
        >
          <p
            class="font-semibold tracking-tight text-slate-900 whitespace-pre-line"
            :class="stat.large ? 'text-[72px] leading-[0.95]' : 'text-[44px] leading-none'"
          >
            {{ stat.value }}
          </p>
          <p class="mt-5 text-base leading-6 text-slate-500 max-w-[170px]">
            {{ stat.label }}
          </p>
        </article>
      </div>
    </section>

    <section class="rounded-[36px] bg-[#eef2f6] px-6 py-14 sm:px-10 lg:px-14 lg:py-20">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl">Ключевые преимущества</h2>
        <p class="mt-4 text-base leading-7 text-slate-500">
          Почему клиенты доверяют нам оценку своей недвижимости
        </p>
      </div>

      <div class="mt-10 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <article v-for="item in keyAdvantages" :key="item.title" class="rounded-[22px] border border-slate-200 bg-white p-5 shadow-sm">
          <div class="flex h-11 w-11 items-center justify-center rounded-full bg-slate-100 text-slate-700">
            <svg
              v-if="item.icon === 'user'"
              class="h-5 w-5"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.8"
            >
              <circle cx="12" cy="8" r="3.2" />
              <path d="M6.5 19a5.5 5.5 0 0 1 11 0" />
            </svg>
            <svg
              v-else-if="item.icon === 'users'"
              class="h-5 w-5"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.8"
            >
              <circle cx="9" cy="9" r="2.5" />
              <circle cx="16.5" cy="8" r="2" />
              <path d="M4.5 18a4.5 4.5 0 0 1 9 0M14 17a3.5 3.5 0 0 1 6 0" />
            </svg>
            <svg
              v-else-if="item.icon === 'monitor'"
              class="h-5 w-5"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.8"
            >
              <rect x="4" y="5" width="16" height="11" rx="2" />
              <path d="M10 19h4M12 16v3" />
            </svg>
            <svg
              v-else-if="item.icon === 'money'"
              class="h-5 w-5"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.8"
            >
              <path d="M12 4v16M15.5 7.5a3.5 3.5 0 0 0-7 0c0 5 7 2.5 7 7a3.5 3.5 0 0 1-7 0" />
            </svg>
            <svg
              v-else-if="item.icon === 'document'"
              class="h-5 w-5"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.8"
            >
              <path d="M8 3h6l4 4v11a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2Z" />
              <path d="M14 3v5h5M9 13l2 2 4-4" />
            </svg>
            <svg
              v-else-if="item.icon === 'lock'"
              class="h-5 w-5"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.8"
            >
              <rect x="5" y="10" width="14" height="10" rx="2" />
              <path d="M8 10V7a4 4 0 1 1 8 0v3" />
            </svg>
            <svg
              v-else-if="item.icon === 'shield'"
              class="h-5 w-5"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.8"
            >
              <path d="M12 3 5.5 6v5.5c0 4.2 2.6 7.2 6.5 9.5 3.9-2.3 6.5-5.3 6.5-9.5V6L12 3Z" />
              <path d="m9.5 12 1.7 1.7 3.6-3.6" />
            </svg>
            <svg
              v-else
              class="h-5 w-5"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.8"
            >
              <path d="M13 3 6 14h5l-1 7 8-11h-5l1-7Z" />
            </svg>
          </div>
          <h3 class="mt-5 text-[22px] font-medium leading-7 text-slate-900">{{ item.title }}</h3>
          <p class="mt-3 text-sm leading-6 text-slate-500">
            {{ item.description }}
          </p>
        </article>
      </div>
    </section>

    <section class="grid gap-10 lg:grid-cols-[0.94fr_1.06fr] lg:items-center">
      <div>
        <div class="max-w-2xl">
          <h2 class="text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl">Почему выбирают нас</h2>
          <p class="mt-5 text-base leading-7 text-slate-500">
            Мы сочетаем технические знания, рыночную экспертизу и современные технологии для предоставления
            превосходных оценочных услуг, отвечающих вашим конкретным потребностям.
          </p>
        </div>

        <div class="mt-8 space-y-5">
          <div v-for="reason in reasons" :key="reason.title" class="flex items-start gap-4">
            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-emerald-50 text-emerald-500">
              <svg
                v-if="reason.icon === 'pin'"
                class="h-5 w-5"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="1.8"
              >
                <path d="M12 21s6-5.2 6-11a6 6 0 1 0-12 0c0 5.8 6 11 6 11Z" />
                <circle cx="12" cy="10" r="2.5" />
              </svg>
              <svg
                v-else-if="reason.icon === 'phone'"
                class="h-5 w-5"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="1.8"
              >
                <rect x="7" y="3.5" width="10" height="17" rx="2.5" />
                <path d="M11 17.5h2" />
              </svg>
              <svg
                v-else-if="reason.icon === 'clock'"
                class="h-5 w-5"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="1.8"
              >
                <circle cx="12" cy="12" r="8" />
                <path d="M12 7.5v4.8l3 1.7" />
              </svg>
              <svg
                v-else-if="reason.icon === 'users'"
                class="h-5 w-5"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="1.8"
              >
                <circle cx="8.5" cy="9" r="2.5" />
                <circle cx="15.5" cy="9" r="2.5" />
                <path d="M3.5 18a5 5 0 0 1 10 0M10.5 18a5 5 0 0 1 10 0" />
              </svg>
              <svg
                v-else
                class="h-5 w-5"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="1.8"
              >
                <path d="M4 20h16M6 20V9l6-4 6 4v11M10 13h4M10 16h4" />
              </svg>
            </div>

            <div>
              <h3 class="text-xl font-semibold text-slate-900">{{ reason.title }}</h3>
              <p class="mt-1 text-sm leading-6 text-slate-500">{{ reason.description }}</p>
            </div>
          </div>
        </div>

        <div class="mt-8 rounded-[24px] bg-[#eef1f7] px-6 py-5">
          <div class="flex items-start gap-4">
            <div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-white text-emerald-500">
              <svg class="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="m5 12 4 4L19 6" />
              </svg>
            </div>
            <div>
              <h3 class="text-lg font-semibold text-slate-900">{{ reasonGuarantee.title }}</h3>
              <p class="mt-2 text-sm leading-6 text-slate-500">{{ reasonGuarantee.description }}</p>
            </div>
          </div>
        </div>
      </div>

      <div class="relative mx-auto w-full max-w-[520px] lg:mx-0">
        <div class="relative h-[440px] overflow-hidden rounded-[26px] bg-[linear-gradient(180deg,#eef4f7_0%,#d4dde4_52%,#a8b4bc_100%)] shadow-sm">
          <div class="absolute inset-x-0 bottom-0 h-[42%] bg-[linear-gradient(180deg,rgba(44,83,71,0.14)_0%,rgba(35,62,54,0.72)_100%)]"></div>
          <div class="absolute bottom-0 left-0 h-[52%] w-[44%] rounded-tr-[120px] bg-[radial-gradient(circle_at_30%_40%,rgba(82,120,98,0.9),rgba(40,71,58,0.96)_65%,rgba(29,53,45,1)_100%)] blur-[1px]"></div>
          <div class="absolute bottom-0 left-[18%] h-[48%] w-[18%] rounded-t-[80px] bg-[radial-gradient(circle_at_40%_30%,rgba(78,120,98,0.95),rgba(38,71,57,1)_70%)]"></div>
          <div class="absolute bottom-0 left-[28%] h-[56%] w-[16%] rounded-t-[90px] bg-[radial-gradient(circle_at_40%_30%,rgba(92,132,108,0.95),rgba(42,74,61,1)_70%)]"></div>
          <div class="absolute -right-[2%] top-0 h-full w-[54%] rounded-l-[28px] bg-[linear-gradient(180deg,#e9ecef_0%,#c9d0d6_100%)] shadow-[-20px_0_40px_rgba(15,23,42,0.12)]"></div>
          <div class="absolute right-[5%] top-0 h-full w-[8%] bg-[#24434e]"></div>
          <div class="absolute right-[16%] top-0 h-full w-[2px] bg-slate-600/25"></div>
          <div class="absolute right-[28%] top-0 h-full w-[2px] bg-slate-600/25"></div>
          <div class="absolute right-[40%] top-0 h-full w-[2px] bg-slate-600/20"></div>
          <div class="absolute right-[6%] top-[11%] h-[2px] w-[48%] bg-slate-600/15"></div>
          <div class="absolute right-[6%] top-[28%] h-[2px] w-[48%] bg-slate-600/15"></div>
          <div class="absolute right-[6%] top-[45%] h-[2px] w-[48%] bg-slate-600/15"></div>
          <div class="absolute right-[6%] top-[62%] h-[2px] w-[48%] bg-slate-600/15"></div>
          <div class="absolute right-[11%] top-[8%] h-[18%] w-[10%] bg-cyan-200/80"></div>
          <div class="absolute right-[24%] top-[14%] h-[15%] w-[9%] bg-cyan-200/75"></div>
          <div class="absolute right-[11%] top-[34%] h-[16%] w-[10%] bg-cyan-200/80"></div>
          <div class="absolute right-[24%] top-[40%] h-[15%] w-[9%] bg-cyan-200/75"></div>
          <div class="absolute right-[11%] top-[60%] h-[16%] w-[10%] bg-cyan-200/80"></div>
          <div class="absolute right-[24%] top-[66%] h-[15%] w-[9%] bg-cyan-200/75"></div>
        </div>

        <div class="absolute bottom-[-14px] left-[-18px] rounded-[18px] bg-[#2eb5bf] px-7 py-5 text-white shadow-[0_16px_32px_rgba(46,181,191,0.28)]">
          <p class="text-[58px] font-semibold leading-none">98%</p>
          <p class="mt-2 text-right text-sm leading-5 text-white/90">
            Удовлетворённость<br />
            клиентов
          </p>
        </div>
      </div>
    </section>

    <section class="rounded-[36px] bg-[#eef2f6] px-6 py-14 sm:px-10 lg:px-14 lg:py-20">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl">Наши услуги</h2>
        <p class="mt-4 text-base leading-7 text-slate-500">
          Комплексные оценочные решения для каждого типа недвижимости
        </p>
      </div>

      <div class="mt-10 grid grid-cols-1 gap-6 lg:grid-cols-2">
        <ServiceCard
          v-for="service in serviceLinks"
          :key="service.slug"
          :card-description="service.cardDescription"
          :description="service.description"
          :icon="service.icon"
          :title="service.title"
          :to="service.to"
          :use-cases="service.useCases"
          :class="service.slug === 'kadastrovaya-stoimost' ? 'lg:col-span-2' : ''"
        />
      </div>
    </section>

    <section class="px-2 py-6 sm:px-4">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl">Как это работает</h2>
        <p class="mt-4 text-base leading-7 text-slate-500">
          Простой и прозрачный процесс от заявки до финального отчета
        </p>
      </div>

      <div class="mt-12 grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-4">
        <div v-for="(step, index) in processSteps" :key="step.step" class="relative">
          <div
            v-if="index < processSteps.length - 1"
            class="absolute left-[calc(100%-10px)] top-1/2 z-10 hidden h-5 w-5 -translate-y-1/2 items-center justify-center rounded-full bg-[#37b5bd] text-white xl:flex"
          >
            <span class="text-xs leading-none">›</span>
          </div>

          <article class="rounded-[24px] border border-slate-200 bg-white px-6 pb-7 pt-5 text-center shadow-sm">
            <div class="mx-auto flex h-14 w-14 items-center justify-center rounded-full bg-[#37b5bd] text-xl font-semibold text-white">
              {{ step.step }}
            </div>

            <div class="mx-auto mt-5 flex h-12 w-12 items-center justify-center rounded-full bg-slate-100 text-slate-700">
              <svg
                v-if="step.icon === 'document'"
                class="h-5 w-5"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="1.8"
              >
                <path d="M8 3h6l4 4v11a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2Z" />
                <path d="M14 3v5h5M9 13h6M9 17h4" />
              </svg>
              <svg
                v-else-if="step.icon === 'pin'"
                class="h-5 w-5"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="1.8"
              >
                <path d="M12 21s6-5.2 6-11a6 6 0 1 0-12 0c0 5.8 6 11 6 11Z" />
                <circle cx="12" cy="10" r="2.5" />
              </svg>
              <svg
                v-else-if="step.icon === 'calculator'"
                class="h-5 w-5"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="1.8"
              >
                <rect x="6" y="3.5" width="12" height="17" rx="2" />
                <path d="M9 7.5h6M9 12h1m4 0h1M9 15.5h1m4 0h1" />
              </svg>
              <svg
                v-else
                class="h-5 w-5"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="1.8"
              >
                <path d="M14 4h6v6M20 4l-8 8" />
                <path d="M20 14v4a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h4" />
              </svg>
            </div>

            <h3 class="mt-5 text-[26px] font-semibold leading-tight text-slate-900">
              {{ step.title }}
            </h3>
            <p class="mx-auto mt-3 max-w-[220px] text-sm leading-6 text-slate-500">
              {{ step.description }}
            </p>
          </article>
        </div>
      </div>

      <div class="mt-12 text-center">
        <p class="text-base leading-7 text-slate-500">
          Готовы начать? Весь процесс обычно занимает 5-7 рабочих дней.
        </p>
        <a class="mt-5 inline-flex rounded-2xl bg-[#37b5bd] px-8 py-3 text-base font-semibold text-white transition hover:bg-[#2fa3aa]" href="#contact-form">
          Подать заявку
        </a>
      </div>
    </section>

    <section id="directions" class="px-2 py-6 sm:px-4">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl">Наши направления в виде схемы</h2>
        <p class="mt-4 text-base leading-7 text-slate-500">
          Полный перечень всех работ по оценке
        </p>
      </div>

      <div class="mt-10 grid gap-6 lg:grid-cols-[1.05fr_0.95fr] lg:items-start">
        <article class="rounded-[26px] border border-slate-200 bg-white p-5 shadow-sm sm:p-6">
          <h3 class="text-[28px] font-semibold leading-tight text-slate-900">Недвижимое имущество</h3>

          <div class="mt-5 space-y-5">
            <section
              v-for="group in directionPropertyGroups"
              :key="group.title"
              class="rounded-[22px] border border-slate-200 bg-[#eef1f7] p-4 shadow-sm"
            >
              <div class="border-l-[3px] border-[#37b5bd] pl-3">
                <h4 class="text-lg font-semibold text-slate-900">{{ group.title }}</h4>

                <div class="mt-4 space-y-3">
                  <div
                    v-for="item in group.items"
                    :key="item"
                    class="rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm leading-6 text-slate-600 shadow-[0_1px_3px_rgba(15,23,42,0.05)]"
                  >
                    <div class="flex items-center justify-between gap-3">
                      <span>{{ item }}</span>
                      <span
                        v-if="group.title === 'Земельные участки'"
                        class="h-2.5 w-2.5 shrink-0 rounded-full"
                        :class="item === 'От 100 до 1000 га' || item === 'Более 1000 га' ? 'bg-slate-900' : 'bg-[#37b5bd]'"
                      ></span>
                    </div>
                  </div>
                </div>
              </div>
            </section>
          </div>
        </article>

        <div class="space-y-5">
          <article class="rounded-[26px] border border-slate-200 bg-white p-5 shadow-sm sm:p-6">
            <h3 class="text-[26px] font-semibold leading-tight text-slate-900">
              Снижение кадастр. стоимости недвижимости
            </h3>

            <div class="mt-5 rounded-[22px] border border-slate-200 bg-[#eef1f7] p-4 shadow-sm">
              <div class="border-l-[3px] border-[#37b5bd] pl-3">
                <h4 class="text-lg font-semibold text-slate-900">Типы объектов</h4>

                <div class="mt-4 space-y-3">
                  <div
                    v-for="item in directionCadastreItems"
                    :key="item"
                    class="rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm leading-6 text-slate-600 shadow-[0_1px_3px_rgba(15,23,42,0.05)]"
                  >
                    {{ item }}
                  </div>
                </div>
              </div>
            </div>
          </article>

          <article class="rounded-[26px] border border-slate-200 bg-white p-5 shadow-sm sm:p-6">
            <h3 class="text-[26px] font-semibold leading-tight text-slate-900">Движимое имущество</h3>

            <div class="mt-5 rounded-[22px] bg-[#eef1f7] px-6 py-8 text-center">
              <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-[#37b5bd] text-white">
                <svg class="h-7 w-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                  <path d="M5 16h14l-1.3-4.1A2 2 0 0 0 15.8 10H8.2a2 2 0 0 0-1.9 1.4L5 16Z" />
                  <path d="M4 16v2a1 1 0 0 0 1 1h1m13-3v2a1 1 0 0 1-1 1h-1M7.5 19v-1m9 1v-1" />
                  <circle cx="8" cy="16.5" r="1.5" />
                  <circle cx="16" cy="16.5" r="1.5" />
                </svg>
              </div>
              <p class="mx-auto mt-4 max-w-[250px] text-sm leading-6 text-slate-600">
                {{ directionMovableLabel }}
              </p>
            </div>
          </article>

          <a
            class="inline-flex w-full items-center justify-center gap-3 rounded-2xl bg-[#37b5bd] px-6 py-4 text-lg font-semibold text-white transition hover:bg-[#2fa3aa]"
            href="#contact-form"
          >
            Подать заявку
            <span aria-hidden="true" class="text-2xl leading-none">→</span>
          </a>
        </div>
      </div>
    </section>

    <section class="rounded-[36px] bg-[#eef2f6] px-6 py-14 sm:px-10 lg:px-14 lg:py-20">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl">Наши эксперты и сертификация</h2>
        <p class="mx-auto mt-4 max-w-2xl text-base leading-7 text-slate-500">
          Лицензированные профессионалы с подтвержденным опытом и признанием в отрасли
        </p>
      </div>

      <div class="mt-10 grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4">
        <article
          v-for="item in expertHighlights"
          :key="item.title"
          class="rounded-[22px] border border-slate-200 bg-white px-5 py-6 text-center shadow-sm"
        >
          <div class="mx-auto flex h-11 w-11 items-center justify-center rounded-full bg-emerald-50 text-emerald-500">
            <svg
              v-if="item.icon === 'badge'"
              class="h-5 w-5"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.8"
            >
              <circle cx="12" cy="8" r="3" />
              <path d="M7 20v-4.5A4.5 4.5 0 0 1 11.5 11h1A4.5 4.5 0 0 1 17 15.5V20l-5-2-5 2Z" />
            </svg>
            <svg
              v-else-if="item.icon === 'cap'"
              class="h-5 w-5"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.8"
            >
              <path d="m3 9 9-4 9 4-9 4-9-4Z" />
              <path d="M7 11.5V15c0 1.7 2.2 3 5 3s5-1.3 5-3v-3.5" />
            </svg>
            <svg
              v-else-if="item.icon === 'document'"
              class="h-5 w-5"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.8"
            >
              <path d="M8 3h6l4 4v11a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2Z" />
              <path d="M14 3v5h5" />
            </svg>
            <svg
              v-else
              class="h-5 w-5"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.8"
            >
              <path d="m12 3 2.8 5.6 6.2.9-4.5 4.4 1 6.1-5.5-2.9-5.5 2.9 1-6.1L3 9.5l6.2-.9L12 3Z" />
            </svg>
          </div>
          <h3 class="mx-auto mt-5 max-w-[190px] text-lg font-semibold leading-7 text-slate-900">{{ item.title }}</h3>
          <p class="mx-auto mt-3 max-w-[190px] text-sm leading-6 text-slate-500">{{ item.description }}</p>
        </article>
      </div>

      <div class="mt-12 text-center">
        <h3 class="text-3xl font-semibold tracking-tight text-slate-900">Познакомьтесь с нашей командой</h3>
      </div>

      <div class="mt-8 grid grid-cols-1 gap-4 lg:grid-cols-2">
        <article
          v-for="member in team"
          :key="member.name"
          class="rounded-[22px] border border-slate-200 bg-white px-5 py-5 shadow-sm"
        >
          <div class="flex items-start gap-4">
            <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-emerald-50 text-lg font-semibold text-[#37b5bd]">
              {{ member.initials }}
            </div>
            <div>
              <h4 class="text-xl font-semibold text-slate-900">{{ member.name }}</h4>
              <p class="mt-1 text-sm font-medium text-[#37b5bd]">{{ member.role }}</p>
              <p class="mt-2 text-sm leading-6 text-slate-500">{{ member.experience }}</p>
              <p class="mt-1 text-sm leading-6 text-slate-500">{{ member.specialty }}</p>
            </div>
          </div>
        </article>
      </div>

      <article class="mt-8 rounded-[24px] border border-slate-200 bg-white px-6 py-6 shadow-sm">
        <div class="flex items-start gap-4 border-l-[3px] border-[#37b5bd] pl-4">
          <div class="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-emerald-50 text-emerald-500">
            <svg class="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
              <path d="M8 3h6l4 4v11a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2Z" />
              <path d="M14 3v5h5M9 13l2 2 4-4" />
            </svg>
          </div>
          <div>
            <h3 class="text-lg font-semibold text-slate-900">{{ expertCertificationNote.title }}</h3>
            <p class="mt-2 text-sm leading-6 text-slate-500">{{ expertCertificationNote.description }}</p>
          </div>
        </div>
      </article>
    </section>

    <section class="px-2 py-6 sm:px-4">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl">Отзывы клиентов</h2>
        <p class="mt-4 text-base leading-7 text-slate-500">
          Что наши клиенты говорят о наших услугах
        </p>
      </div>

      <div class="mt-10 grid grid-cols-1 gap-5 lg:grid-cols-2">
        <article
          v-for="review in reviews"
          :key="review.author"
          class="rounded-[24px] border border-slate-200 bg-white px-6 py-6 shadow-sm"
        >
          <div class="flex items-start justify-between gap-4">
            <div class="flex items-center gap-1 text-amber-400">
              <svg
                v-for="star in review.rating"
                :key="star"
                class="h-4 w-4 fill-current"
                viewBox="0 0 24 24"
              >
                <path d="m12 3 2.8 5.6 6.2.9-4.5 4.4 1 6.1-5.5-2.9-5.5 2.9 1-6.1L3 9.5l6.2-.9L12 3Z" />
              </svg>
            </div>
            <div class="text-[64px] font-semibold leading-none text-slate-200">”</div>
          </div>

          <p class="mt-2 text-base leading-7 text-slate-600">
            {{ review.text }}
          </p>

          <div class="mt-8 flex items-end justify-between gap-4">
            <div>
              <p class="text-base font-semibold text-slate-900">{{ review.author }}</p>
              <p class="mt-1 text-sm text-slate-500">{{ review.role }}</p>
            </div>
            <p class="text-sm text-slate-400">{{ review.date }}</p>
          </div>
        </article>
      </div>

      <div class="mt-10 grid grid-cols-1 gap-4 md:grid-cols-3">
        <article
          v-for="stat in reviewStats"
          :key="stat.label"
          class="rounded-[22px] bg-[#eef1f7] px-6 py-6 text-center"
        >
          <div class="flex items-center justify-center gap-2">
            <svg
              v-if="stat.icon === 'star'"
              class="h-6 w-6 fill-amber-400 text-amber-400"
              viewBox="0 0 24 24"
            >
              <path d="m12 3 2.8 5.6 6.2.9-4.5 4.4 1 6.1-5.5-2.9-5.5 2.9 1-6.1L3 9.5l6.2-.9L12 3Z" />
            </svg>
            <p class="text-[44px] font-semibold leading-none text-slate-900">{{ stat.value }}</p>
          </div>
          <p class="mt-3 text-sm text-slate-500">{{ stat.label }}</p>
        </article>
      </div>
    </section>

    <section id="pricing" class="rounded-[36px] bg-[#eef2f6] px-6 py-14 sm:px-10 lg:px-14 lg:py-20">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl">Прейскурант</h2>
        <p class="mx-auto mt-4 max-w-2xl text-base leading-7 text-slate-500">
          Лицензированные профессионалы с подтвержденным опытом и признанием в отрасли
        </p>
      </div>

      <div class="mx-auto mt-10 max-w-5xl space-y-5">
        <details
          v-for="item in priceList"
          :key="item.title"
          class="group overflow-hidden rounded-[22px] border border-slate-200 bg-white shadow-sm"
        >
          <summary class="flex cursor-pointer list-none items-center justify-between gap-4 px-6 py-6 text-left marker:content-none">
            <span class="border-l-[3px] border-[#37b5bd] pl-5 text-[28px] font-semibold leading-tight text-slate-900 max-sm:text-xl">
              {{ item.title }}
            </span>
            <span class="shrink-0 text-[#37b5bd] transition group-open:rotate-180">
              <svg class="h-7 w-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                <path d="m6 9 6 6 6-6" />
              </svg>
            </span>
          </summary>

          <div class="border-t border-slate-200 px-6 pb-6 pt-4">
            <div class="pl-5">
              <p class="text-2xl font-semibold text-slate-900">{{ item.price }}</p>
              <p class="mt-3 text-base leading-7 text-slate-500">{{ item.description }}</p>
            </div>
          </div>
        </details>
      </div>
    </section>

    <section id="contacts" class="rounded-[36px] bg-[#eef2f6] px-6 py-14 sm:px-10 lg:px-14 lg:py-20">
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
                  <svg
                    v-if="item.icon === 'phone'"
                    class="h-5 w-5"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="1.8"
                  >
                    <path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.4 19.4 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7l.5 3.1a2 2 0 0 1-.6 1.8l-2 2a16 16 0 0 0 6.1 6.1l2-2a2 2 0 0 1 1.8-.6l3.1.5A2 2 0 0 1 22 16.9Z" />
                  </svg>
                  <svg
                    v-else-if="item.icon === 'mail'"
                    class="h-5 w-5"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="1.8"
                  >
                    <rect x="3" y="5" width="18" height="14" rx="2" />
                    <path d="m4 7 8 6 8-6" />
                  </svg>
                  <svg
                    v-else-if="item.icon === 'pin'"
                    class="h-5 w-5"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="1.8"
                  >
                    <path d="M12 21s6-5.2 6-11a6 6 0 1 0-12 0c0 5.8 6 11 6 11Z" />
                    <circle cx="12" cy="10" r="2.5" />
                  </svg>
                  <svg
                    v-else
                    class="h-5 w-5"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="1.8"
                  >
                    <circle cx="12" cy="12" r="8" />
                    <path d="M12 7.5v4.8l3 1.7" />
                  </svg>
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
          <ContactSectionForm />
        </div>
      </div>
    </section>
  </div>
</template>
