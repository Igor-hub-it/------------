<script setup lang="ts">
import { serviceLinks } from '~/utils/services'

useSeoMeta({
  title: 'Оценка недвижимости и кадастровой стоимости',
  description:
    'Лендинг компании по независимой оценке жилой и коммерческой недвижимости, земельных участков и кадастровой стоимости.'
})

const mainHeroStyle = {
  backgroundImage:
    "linear-gradient(90deg, rgba(15, 23, 42, 0.0) 0%, rgba(15, 23, 42, 0.0) 42%, rgba(15, 23, 42, 0.0) 100%), url('/image/banner-main.webp')",
  backgroundSize: 'cover',
  backgroundPosition: 'center'
}

const aboutFeatureIconMap = {
  pin: 'lucide:map-pin',
  globe: 'lucide:globe',
  calendar: 'lucide:calendar-days'
} as const

const keyAdvantageIconMap = {
  user: 'lucide:user-round',
  users: 'lucide:users-round',
  monitor: 'lucide:monitor',
  money: 'lucide:circle-dollar-sign',
  document: 'lucide:file-check-2',
  lock: 'lucide:lock-keyhole',
  shield: 'lucide:shield-check',
  flash: 'lucide:zap'
} as const

const reasonIconMap = {
  pin: 'lucide:map-pinned',
  phone: 'lucide:smartphone',
  clock: 'lucide:clock-3',
  users: 'lucide:users-round',
  building: 'lucide:building-2'
} as const

const processStepIconMap = {
  document: 'lucide:file-text',
  pin: 'lucide:map-pin',
  calculator: 'lucide:calculator',
  send: 'lucide:send'
} as const

const expertHighlightIconMap = {
  badge: 'lucide:badge-check',
  cap: 'lucide:graduation-cap',
  document: 'lucide:file-badge',
  star: 'lucide:star'
} as const

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
  <div class="space-y-20 py-10 sm:py-14">
    <section
      id="services"
      class="overflow-hidden py-16 sm:py-20 lg:flex lg:h-[620px] lg:items-center lg:py-0"
      :style="mainHeroStyle"
    >
      <div class="container-default grid gap-8 lg:grid-cols-[1.15fr_0.85fr] lg:items-center">
        <div>
          <p class="text-sm font-semibold uppercase tracking-[0.22em] text-cyan-100">Услуги по оценке недвижимости</p>
          <h1 class="mt-4 max-w-4xl text-4xl font-bold tracking-tight text-white sm:text-5xl">
            Проводим независимую оценку недвижимости для сделок, суда, банков и снижения кадастровой нагрузки
          </h1>
          <p class="mt-6 max-w-3xl text-base leading-7 text-slate-100 sm:text-lg">
            Работаем с жилой и коммерческой недвижимостью, земельными участками и задачами по кадастровой стоимости.
            Подготавливаем отчёты и сопровождаем клиента от первой консультации до готового результата.
          </p>

          <div class="mt-8 flex flex-wrap gap-4">
            <a class="button-primary" href="#contact-form">Подать заявку</a>
            <NuxtLink class="button-secondary border-white/40 bg-white/10 text-white hover:border-white hover:bg-white/20 hover:text-white" to="/uslugi/kadastrovaya-stoimost">
              Подробнее об услугах
            </NuxtLink>
          </div>
        </div>

        <div class="rounded-[28px] border border-white/20 bg-white/88 p-8 shadow-xl backdrop-blur-sm">
          <p class="section-label">Что входит в услугу</p>
          <ul class="mt-6 space-y-4 text-sm leading-6 text-slate-700">
            <li>Отчёт об оценке под конкретную задачу: сделка, суд, залог, наследство или пересмотр кадастровой стоимости.</li>
            <li>Понятный план работ с перечнем документов, сроками и ответственным специалистом.</li>
            <li>Поддержка по вопросам оформления заявки и передачи исходных данных онлайн.</li>
          </ul>
        </div>
      </div>
    </section>

    <section id="about" class="container-default grid gap-10 lg:grid-cols-[1.08fr_0.92fr] lg:items-stretch">
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
              <Icon :name="aboutFeatureIconMap[feature.icon]" class="h-5 w-5" />
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

    <section class="bg-[#eef2f6] px-6 py-14 sm:px-10 lg:px-14 lg:py-20">
      <div class="container-default">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl">Ключевые преимущества</h2>
        <p class="mt-4 text-base leading-7 text-slate-500">
          Почему клиенты доверяют нам оценку своей недвижимости
        </p>
      </div>

      <div class="mt-10 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <article v-for="item in keyAdvantages" :key="item.title" class="rounded-[22px] border border-slate-200 bg-white p-5 shadow-sm">
          <div class="flex h-11 w-11 items-center justify-center rounded-full bg-slate-100 text-slate-700">
            <Icon :name="keyAdvantageIconMap[item.icon]" class="h-5 w-5" />
          </div>
          <h3 class="mt-5 text-[22px] font-medium leading-7 text-slate-900">{{ item.title }}</h3>
          <p class="mt-3 text-sm leading-6 text-slate-500">
            {{ item.description }}
          </p>
        </article>
      </div>
      </div>
    </section>

    <section class="container-default grid gap-10 lg:grid-cols-[0.94fr_1.06fr] lg:items-center">
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
              <Icon :name="reasonIconMap[reason.icon]" class="h-5 w-5" />
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
              <Icon class="h-4 w-4" name="lucide:check" />
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

    <section class="bg-[#eef2f6] px-6 py-14 sm:px-10 lg:px-14 lg:py-20">
      <div class="container-default">
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
      </div>
    </section>

    <section class="px-2 py-6 sm:px-4">
      <div class="container-default">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl">Как это работает</h2>
        <p class="mt-4 text-base leading-7 text-slate-500">
          Простой и прозрачный процесс от заявки до финального отчета
        </p>
      </div>

      <div class="mt-12 grid grid-cols-1 items-stretch gap-6 md:grid-cols-2 xl:grid-cols-4">
        <div v-for="(step, index) in processSteps" :key="step.step" class="relative h-full">
          <div
            v-if="index < processSteps.length - 1"
            class="absolute left-[calc(100%)] top-1/2 z-10 hidden h-7 w-7 -translate-y-1/2 items-center justify-center rounded-full bg-[#37b5bd] text-white xl:flex"
          >
            <Icon class="h-7 w-7" name="lucide:arrow-right" />
          </div>

          <article class="flex h-full flex-col rounded-[24px] border border-slate-200 bg-white px-6 pb-7 pt-5 text-center shadow-sm">
            <div class="mx-auto flex h-14 w-14 items-center justify-center rounded-full bg-[#37b5bd] text-xl font-semibold text-white">
              {{ step.step }}
            </div>

            <div class="mx-auto mt-5 flex h-12 w-12 items-center justify-center rounded-full bg-slate-100 text-slate-700">
              <Icon :name="processStepIconMap[step.icon]" class="h-5 w-5" />
            </div>

            <h3 class="mt-5 text-[26px] font-semibold leading-tight text-slate-900">
              {{ step.title }}
            </h3>
            <p class="mx-auto mt-3 max-w-[220px] flex-1 text-sm leading-6 text-slate-500">
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
      </div>
    </section>

    <section id="directions" class="px-2 py-6 sm:px-4">
      <div class="container-default">
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
                <Icon class="h-7 w-7" name="lucide:car-front" />
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
      </div>
    </section>

    <section class="bg-[#eef2f6] px-6 py-14 sm:px-10 lg:px-14 lg:py-20">
      <div class="container-default">
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
            <Icon :name="expertHighlightIconMap[item.icon]" class="h-5 w-5" />
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
            <Icon class="h-4 w-4" name="lucide:file-check-2" />
          </div>
          <div>
            <h3 class="text-lg font-semibold text-slate-900">{{ expertCertificationNote.title }}</h3>
            <p class="mt-2 text-sm leading-6 text-slate-500">{{ expertCertificationNote.description }}</p>
          </div>
        </div>
      </article>
      </div>
    </section>

    <section class="px-2 py-6 sm:px-4">
      <div class="container-default">
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
              <Icon
                v-for="star in review.rating"
                :key="star"
                class="h-4 w-4 fill-current"
                name="lucide:star"
              />
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
            <Icon
              v-if="stat.icon === 'star'"
              class="h-6 w-6 fill-amber-400 text-amber-400"
              name="lucide:star"
            />
            <p class="text-[44px] font-semibold leading-none text-slate-900">{{ stat.value }}</p>
          </div>
          <p class="mt-3 text-sm text-slate-500">{{ stat.label }}</p>
        </article>
      </div>
      </div>
    </section>

    <section id="pricing" class="bg-[#eef2f6] px-6 py-14 sm:px-10 lg:px-14 lg:py-20">
      <div class="container-default">
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
              <Icon class="h-7 w-7" name="lucide:chevron-down" />
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
      </div>
    </section>

    <ContactSection />
  </div>
</template>
