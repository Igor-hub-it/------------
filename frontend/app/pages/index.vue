<script setup lang="ts">
import { serviceLinks } from '~/utils/services'
import iconMain1 from '~/assets/icon/Icon-main-1.svg'
import iconMain2 from '~/assets/icon/Icon-main-2.svg'
import iconMain3 from '~/assets/icon/Icon-main-3.svg'
import iconMain4 from '~/assets/icon/Icon-main-4.svg'
import about1 from '~/assets/icon/about-1.svg'
import about2 from '~/assets/icon/about-2.svg'
import about3 from '~/assets/icon/about-3.svg'
import advantages1 from '~/assets/icon/advantages-1.svg'
import advantages2 from '~/assets/icon/advantages-2.svg'
import advantages3 from '~/assets/icon/advantages-3.svg'
import advantages4 from '~/assets/icon/advantages-4.svg'
import advantages5 from '~/assets/icon/advantages-5.svg'
import advantages6 from '~/assets/icon/advantages-6.svg'
import advantages7 from '~/assets/icon/advantages-7.svg'
import advantages8 from '~/assets/icon/advantages-8.svg'
import select1 from '~/assets/icon/select-1.svg'
import select2 from '~/assets/icon/select-2.svg'
import select3 from '~/assets/icon/select-3.svg'
import select4 from '~/assets/icon/select-4.svg'
import select5 from '~/assets/icon/select-5.svg'
import howWork1 from '~/assets/icon/how-work-1.svg'
import howWork2 from '~/assets/icon/how-work-2.svg'
import howWork3 from '~/assets/icon/how-work-3.svg'
import howWork4 from '~/assets/icon/how-work-4.svg'
import arrowRightIcon from '~/assets/icon/arrow-right.svg'
import directionsIcon from '~/assets/icon/directions.svg'
import team1 from '~/assets/icon/team-1.svg'
import team2 from '~/assets/icon/team-2.svg'
import team3 from '~/assets/icon/team-3.svg'
import team4 from '~/assets/icon/team-4.svg'
import starIcon from '~/assets/icon/star.svg'
import quoteIcon from '~/assets/icon/quote.svg'
import buildIcon from '~/assets/icon/builld.svg'
import factoryIcon from '~/assets/icon/factory.svg'
import clockIcon from '~/assets/icon/clock.svg'
import landIcon from '~/assets/icon/land.svg'
import dollarIcon from '~/assets/icon/ruble-teal.svg'
import carIcon from '~/assets/icon/car.svg'

useSeoMeta({
  title: 'Оценка недвижимости и кадастровой стоимости',
  description:
    'Лендинг компании по независимой оценке жилой и коммерческой недвижимости, земельных участков и кадастровой стоимости.'
})

const mainHeroStyle = {
  '--hero-banner-desktop': "url('/image/banner-main.webp')",
  '--hero-banner-mobile': "url('/image/banner-main-mobile.webp')"
}

const heroAdvantages = [
  {
    title: 'Лицензированные специалисты',
    description: 'Сертифицированные оценщики с большим опытом',
    icon: iconMain1
  },
  {
    title: 'Юридическая гарантия',
    description: 'Все отчёты соответствуют требованиям законодательства',
    icon: iconMain2
  },
  {
    title: 'Быстрое выполнение',
    description: 'Оперативная обработка без потери качества',
    icon: iconMain3
  },
  {
    title: 'Гарантия',
    description: 'Точность и достоверность наших экспертных оценок',
    icon: iconMain4
  }
]

const keyAdvantages = [
  {
    title: 'Обширный опыт',
    description: 'Более 15 лет профессионального опыта оценки всех типов недвижимости',
    icon: advantages1
  },
  {
    title: 'Квалифицированные специалисты',
    description: 'Лицензированные и сертифицированные оценщики с высокой квалификацией',
    icon: advantages2
  },
  {
    title: 'Онлайн-заказ',
    description: 'Подавайте заявки и отслеживайте прогресс из любого места в любое время',
    icon: advantages3
  },
  {
    title: 'Доступные цены',
    description: 'Конкурентные тарифы без ущерба качеству и соответствию требованиям',
    icon: advantages4
  },
  {
    title: 'Юридическое соответствие',
    description: 'Все отчёты соответствуют национальным стандартам и нормативным требованиям',
    icon: advantages5
  },
  {
    title: 'Безопасность данных',
    description: 'Ваша информация защищена шифрованием банковского уровня',
    icon: advantages6
  },
  {
    title: 'Гарантия',
    description: 'Мы гарантируем точность и достоверность наших экспертных оценок',
    icon: advantages7
  },
  {
    title: 'Быстрое выполнение',
    description: 'Быстрая обработка заявок',
    icon: advantages8
  }
]

const reasons = [
  {
    title: 'По всей стране',
    description: 'Мы работаем во всех регионах с местным рыночным опытом',
    icon: select1
  },
  {
    title: 'Онлайн-услуги',
    description: 'Полный процесс подачи заявки в цифровом формате из любого места',
    icon: select2
  },
  {
    title: 'Гибкие осмотры',
    description: 'Планируйте посещения объекта в удобное для вас время',
    icon: select3
  },
  {
    title: 'Широкая сеть экспертов',
    description: 'Доступ к специализированным оценщикам для любого типа недвижимости',
    icon: select4
  },
  {
    title: 'Все типы недвижимости',
    description: 'От жилой до коммерческой и земельных участков',
    icon: select5
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
    icon: howWork1
  },
  {
    step: '02',
    title: 'Визит специалиста',
    description: 'Наш оценщик осмотрит объект в удобное для вас время',
    icon: howWork2
  },
  {
    step: '03',
    title: 'Оценка',
    description: 'Экспертный анализ с использованием рыночных данных и профессиональной методологии',
    icon: howWork3
  },
  {
    step: '04',
    title: 'Доставка отчета',
    description: 'Получите полный отчёт об оценке, соответствующий всем юридическим требованиям',
    icon: howWork4
  }
]

const processStepsMobile = [
  {
    step: '1',
    title: 'Заявка',
    description: 'Оставьте заявку на сайте или позвоните нам'
  },
  {
    step: '2',
    title: 'Консультация',
    description: 'Специалист свяжется с вами для уточнения деталей'
  },
  {
    step: '3',
    title: 'Осмотр',
    description: 'Выездной осмотр объекта в удобное для вас время'
  },
  {
    step: '4',
    title: 'Отчет',
    description: 'Получение готового отчета об оценке в течение 3-5 дней'
  }
]

const directionPropertyGroups = [
  {
    title: 'Жилая недвижимость',
    items: [
      'Квартира, комната, гостиница, кухня-прихожая, в том числе доля в праве на них',
      'Дом, коттедж, дача, таунхаус с земельным участком, в том числе доля в праве на них',
      'Незавершенный строительством дом, коттедж, таунхаус, дача с зем. участком, в том числе доля'
    ]
  },
  {
    title: 'Нежилая недвижимость',
    items: [
      'Нежилые помещения',
      'Гараж, парк. место',
      'Нежилое здание с земельным участком',
      'Незавершенное стр. нежилое здание с земельным участком'
    ]
  },
  {
    title: 'Земельные участки',
    items: ['<10 соток', '10-50 сот', 'От 50 сот до 1 га', 'От 1 га до 100 га', 'От 100 до 1000 га', 'Более 1000 га']
  }
]

const directionCadastreItems = [
  'Земельный участок любого назначения',
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
    icon: team1
  },
  {
    title: 'Передовое обучение',
    description: 'Регулярное профессиональное развитие и образование',
    icon: team2
  },
  {
    title: 'Отраслевые аккредитации',
    description: 'Члены профессиональных оценочных ассоциаций',
    icon: team3
  },
  {
    title: 'Стандарты качества',
    description: 'Сертифицированные по ISO процессы оценки',
    icon: team4
  }
]

const team = [
  {
    initials: 'МК',
    name: 'Мария',
    role: 'Старший оценщик недвижимости',
    experience: 'Лицензированный оценщик • 15 лет опыта',
    specialty: 'Специализация: Жилая и коммерческая недвижимость'
  },
  {
    initials: 'ЯН',
    name: 'Сергей',
    role: 'Директор по оценке',
    experience: 'Сертифицированный мастер-оценщик • 20 лет опыта',
    specialty: 'Специализация: Сложные объекты и земля'
  },
  {
    initials: 'АВ',
    name: 'Екатерина',
    role: 'Специалист по коммерческой недвижимости',
    experience: 'Лицензированный оценщик • 12 лет опыта',
    specialty: 'Специализация: Торговые и офисные площади'
  },
  {
    initials: 'ПК',
    name: 'Павел',
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
    author: 'Иван Дубровский',
    role: 'Домовладелец',
    date: 'Январь 2026',
    rating: 5,
    text: '"Отличный сервис от начала до конца. Оценщик был профессиональным, тщательным и предоставил отчет раньше срока. Настоятельно рекомендую всем, кому нужна оценка недвижимости."'
  },
  {
    author: 'Елена Курчатова',
    role: 'Инвестор в недвижимость',
    date: 'Декабрь 2025',
    rating: 5,
    text: '"Я пользовалась их услугами несколько раз для своих инвестиционных объектов. Стабильно точные оценки и быстрая обработка. Процесс онлайн-заявки очень удобен."'
  },
  {
    author: 'Алексей Козлов',
    role: 'Владелец бизнеса',
    date: 'Ноябрь 2025',
    rating: 5,
    text: '"Нужна была оценка коммерческой недвижимости для банковского кредита. Команда была осведомлена о коммерческой недвижимости и предоставила полный отчет, соответствующий всем требованиям."'
  },
  {
    author: 'Мария Михайлова',
    role: 'Юридический представитель',
    date: 'Октябрь 2025',
    rating: 5,
    text: '"Профессиональный и надежный сервис для целей раздела наследства. Отчет об оценке был четким, хорошо задокументированным и принят всеми сторонами. Отличная коммуникация на протяжении всего процесса."'
  }
]

const reviewStats = [
  { value: '4.9', label: 'Средний рейтинг', icon: starIcon },
  { value: '500+', label: 'Отзывов клиентов' },
  { value: '98%', label: 'Рекомендуют нас' }
]

type PriceEntry = {
  name: string
  note: string
  price: string
}

type PriceItem = {
  title: string
  price: string
  description: string
  icon?: string
  groupLabel?: string
  entries?: PriceEntry[]
}

type PropertyType =
  | 'Жилая недвижимость'
  | 'Нежилые помещения'
  | 'Нежилые здания с земельным участком'
  | 'Гаражи и парковки'
  | 'Незавершённые нежилые здания'
  | 'Земельные участки'
  | 'Оценка для снижения кадастровой стоимости'
  | 'Движимое имущество'

const priceList = [
  {
    title: 'Оценка жилой недвижимости',
    price: 'от 5 000 руб.',
    description: 'Квартиры, дома, коттеджи, таунхаусы, дачи и иные жилые объекты.',
    icon: buildIcon,
    groupLabel: 'Жилая недвижимость',
    entries: [
      { name: 'Квартира / комната / гостинка / кухня-прихожая', note: 'рыночная стоимость', price: '5 000 ₽' },
      { name: 'Дом / коттедж / таунхаус / дача с земельным участком', note: 'рыночная стоимость', price: '10 000 ₽' },
      { name: 'Незавершенный строительством дом / коттедж / таунхаус / дача с земельным участком', note: 'рыночная стоимость', price: '12 000 ₽' }
    ]
  },
  {
    title: 'Оценка нежилых помещений',
    price: 'от 9 000 руб.',
    description: 'Офисы, склады, торговые площади и иные коммерческие помещения различной площади.',
    icon: factoryIcon,
    groupLabel: 'Нежилые помещения',
    entries: [
      { name: 'Нежилое помещение площадью до 50 м²', note: 'рыночная стоимость', price: '9 000 ₽' },
      { name: 'Нежилое помещение площадью от 50 до 100 м²', note: 'рыночная стоимость', price: '14 000 ₽' },
      { name: 'Нежилое помещение площадью от 100 до 300 м²', note: 'рыночная стоимость', price: '18 000 ₽' },
      { name: 'Нежилое помещение площадью от 300 до 500 м²', note: 'рыночная стоимость', price: '25 000 ₽' },
      { name: 'Нежилое помещение площадью от 500 до 1000 м²', note: 'рыночная стоимость', price: '30 000 ₽' },
      { name: 'Нежилое помещение площадью более 1000 м²', note: 'рыночная стоимость', price: '45 000 ₽' }
    ]
  },
  {
    title: 'Оценка нежилых зданий',
    price: 'от 18 000 руб.',
    description: 'Нежилые здания различной площади с земельными участками.',
    icon: factoryIcon,
    groupLabel: 'Нежилые здания с земельным участком',
    entries: [
      { name: 'Нежилое здание площадью менее 100 м² с земельным участком', note: 'рыночная стоимость', price: '18 000 ₽' },
      { name: 'Нежилое здание площадью от 100 до 500 м² с земельным участком', note: 'рыночная стоимость', price: '25 000 ₽' },
      { name: 'Нежилое здание площадью от 500 до 1000 м² с земельным участком', note: 'рыночная стоимость', price: '32 000 ₽' },
      { name: 'Нежилое здание площадью от 1000 до 3000 м² с земельным участком', note: 'рыночная стоимость', price: '45 000 ₽' },
      { name: 'Нежилое здание площадью от 3000 до 5000 м² с земельным участком', note: 'рыночная стоимость', price: '72 000 ₽' },
      { name: 'Нежилое здание площадью более 5000 м² с земельным участком', note: 'рыночная стоимость', price: '90 000 ₽' }
    ]
  },
  {
    title: 'Оценка гаражей и парковок',
    price: 'от 7 000 руб.',
    description: 'Гаражи, парковочные места и незавершённые гаражи.',
    icon: carIcon,
    groupLabel: 'Гаражи и парковки',
    entries: [
      { name: 'Гараж / парковочное место', note: 'рыночная стоимость', price: '7 000 ₽' },
      { name: 'Незавершенный строительством гараж', note: 'рыночная стоимость', price: '9 000 ₽' }
    ]
  },
  {
    title: 'Оценка движимого имущества',
    price: 'от 8 000 руб.',
    description: 'Транспортные средства, оборудование, техника и другие движимые активы.',
    icon: carIcon,
    groupLabel: 'Движимое имущество',
    entries: [
      { name: 'Транспортные средства', note: 'рыночная стоимость', price: '' },
      { name: 'Оборудование и техника', note: 'рыночная стоимость', price: '' },
      { name: 'Прочие движимые активы', note: 'рыночная стоимость', price: '' }
    ]
  },
  {
    title: 'Оценка незавершённого строительства',
    price: 'от 21 000 руб.',
    description: 'Незавершённые нежилые здания различной площади с земельными участками.',
    icon: clockIcon,
    groupLabel: 'Незавершённые нежилые здания',
    entries: [
      { name: 'Незавершенное строительством нежилое здание площадью менее 100 м² с земельным участком', note: 'рыночная стоимость', price: '21 000 ₽' },
      { name: 'Незавершенное строительством нежилое здание площадью от 100 до 500 м² с земельным участком', note: 'рыночная стоимость', price: '27 000 ₽' },
      { name: 'Незавершенное строительством нежилое здание площадью от 500 до 1000 м² с земельным участком', note: 'рыночная стоимость', price: '43 000 ₽' },
      { name: 'Незавершенное строительством нежилое здание площадью от 1000 до 3000 м² с земельным участком', note: 'рыночная стоимость', price: '77 000 ₽' },
      { name: 'Незавершенное строительством нежилое здание площадью от 3000 до 5000 м² с земельным участком', note: 'рыночная стоимость', price: '82 000 ₽' },
      { name: 'Незавершенное строительством нежилое здание площадью более 5000 м² с земельным участком', note: 'рыночная стоимость', price: '95 000 ₽' }
    ]
  },
  {
    title: 'Оценка земельных участков',
    price: 'от 7 000 руб.',
    description: 'Земельные участки различной площади под любое использование.',
    icon: landIcon,
    groupLabel: 'Земельные участки',
    entries: [
      { name: 'Земельный участок площадью до 10 соток', note: 'рыночная стоимость', price: '7 000 ₽' },
      { name: 'Земельный участок площадью от 10 соток до 50 соток', note: 'рыночная стоимость', price: '12 000 ₽' },
      { name: 'Земельный участок площадью от 50 соток до 1 Га', note: 'рыночная стоимость', price: '18 000 ₽' },
      { name: 'Земельный участок площадью от 1 до 100 Га', note: 'рыночная стоимость', price: '23 000 ₽' },
      { name: 'Земельный участок площадью от 100 до 1000 Га', note: 'рыночная стоимость', price: '32 000 ₽' },
      { name: 'Земельный участок площадью от 1000 Га', note: 'рыночная стоимость', price: '45 000 ₽' }
    ]
  },
  {
    title: 'Снижение кадастровой стоимости',
    price: 'от 18 000 руб.',
    description: 'Оценка для целей оспаривания и снижения кадастровой стоимости объектов.',
    icon: dollarIcon,
    groupLabel: 'Оценка для снижения кадастровой стоимости',
    entries: [
      { name: 'Квартира / комната / гостинка / кухня-прихожая', note: 'для снижения кадастровой стоимости', price: '18 000 ₽' },
      { name: 'Жилое здание', note: 'для снижения кадастровой стоимости', price: '23 000 ₽' },
      { name: 'Нежилое помещение', note: 'для снижения кадастровой стоимости', price: '25 000 ₽' },
      { name: 'Земельный участок любой категории и назначения', note: 'для снижения кадастровой стоимости', price: '30 000 ₽' },
      { name: 'Нежилое здание', note: 'для снижения кадастровой стоимости', price: '32 000 ₽' }
    ]
  }
] as PriceItem[]

const pricingOpenStates = ref(priceList.map((_, index) => index === 1))

const togglePricingAccordion = (index: number) => {
  pricingOpenStates.value[index] = !pricingOpenStates.value[index]
}

const buildPricingComment = (item: PriceItem, entry: PriceEntry) =>
  [
    `Категория: ${item.groupLabel || item.title}`,
    `Название блока: ${item.title}`,
    `Цена: ${entry.price}`
  ].join('\n')

const isPropertyType = (value?: string): value is PropertyType =>
  !!value &&
  [
    'Жилая недвижимость',
    'Нежилые помещения',
    'Нежилые здания с земельным участком',
    'Гаражи и парковки',
    'Незавершённые нежилые здания',
    'Земельные участки',
    'Оценка для снижения кадастровой стоимости',
    'Движимое имущество'
  ].includes(value)

const getPricingPropertyType = (item: PriceItem): PropertyType =>
  isPropertyType(item.groupLabel) ? item.groupLabel : 'Жилая недвижимость'

const aboutFeatures = [
  {
    title: 'По всей стране',
    description: 'Работаем во всех регионах',
    icon: about1
  },
  {
    title: 'Онлайн-услуги',
    description: 'Подавайте заявки удалённо',
    icon: about2
  },
  {
    title: 'Гибкий график',
    description: 'Удобное время осмотра',
    icon: about3
  }
]

const companyStats = [
  { value: '15+', label: 'Лет опыта', large: true },
  { value: '10+\n000', mobileValue: '10 000+', label: 'Оценено объектов', large: true },
  { value: '50+', label: 'Экспертов-оценщиков' },
  { value: '100%', label: 'Юридическое соответствие' }
]
</script>

<template>
  <div class="4">
    <section
      id="services"
      class="main-hero-banner overflow-hidden py-4 sm:py-16 lg:flex lg:h-[620px] lg:items-center lg:py-0"
      :style="mainHeroStyle"
    >
      <div class="container-default">
        <div class="w-full sm:max-w-[65%] py-0">
          <h1 class="max-w-[520px] text-[36px] sm:text-[48px] font-semibold leading-[1.08] tracking-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
            Услуги по оценке недвижимости
          </h1>
          <p class="mt-2 sm:mt-8 text-[18px] font-normal leading-7 text-[rgba(31,58,95,0.9)] [font-family:Inter,sans-serif]">
            Юридическая, кадастровая и рыночная оценка
          </p>

          <div class="mt-4 sm:mt-8 grid gap-x-10 gap-y-5 sm:grid-cols-2 backdrop-blur-[6px] sm:backdrop-blur-none">
            <div v-for="item in heroAdvantages" :key="item.title" class="flex items-start gap-2 sm:gap-3 rounded-xl sm:bg-white/30 sm:p-3">
              <div class="flex h-8 w-8 shrink-0 items-center justify-center">
                <img :src="item.icon" alt="" class="h-6 w-6 object-contain" />
              </div>
              <div>
                <p class="text-[16px] font-medium leading-6 text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">{{ item.title }}</p>
                <p class="mt-1 text-[14px] font-normal leading-5 text-[rgba(31,58,95,0.7)] [font-family:Inter,sans-serif]">{{ item.description }}</p>
              </div>
            </div>
          </div>

          <div class="mt-4 sm:mt-10 flex flex-col gap-4 sm:flex-row sm:flex-wrap">
            <a
              class="inline-flex h-12 w-full items-center justify-center rounded-xl bg-[#37b5bd] px-8 text-[17px] font-semibold text-white transition hover:bg-[#2fa3aa] sm:w-auto"
              href="#contact-form"
            >
              Подать заявку
            </a>
            <a
              class="inline-flex h-12 w-full items-center justify-center rounded-xl border font-semibold border-slate-500/55 bg-white/30 px-8 text-[16px] font-medium text-[rgba(31,58,95,1)] transition backdrop-blur-[3px] hover:bg-white/50 [font-family:Inter,sans-serif] sm:w-auto"
              href="#pricing"
            >
              Наши услуги
            </a>
          </div>
        </div>
      </div>
    </section>

    <section id="about" class="bg-white py-8 sm:py-16 lg:py-20">
      <div class="container-default grid gap-12 lg:grid-cols-[0.95fr_1.05fr] lg:items-start">
        <article class="max-w-[470px]">
          <h2 class="text-[36px] font-semibold leading-tight tracking-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif] max-sm:text-3xl">
            О нашей компании
          </h2>
          <div class="mt-4 sm:mt-7 space-y-3 sm:space-y-5 text-[16px] font-normal leading-6 sm:leading-8 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
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

          <div class="mt-10 space-y-5">
            <div v-for="feature in aboutFeatures" :key="feature.title" class="flex items-start gap-4">
              <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-[rgba(233,237,242,1)] text-slate-500">
                <img :src="feature.icon" alt="" class="h-6 w-6 object-contain" />
              </div>
              <div>
                <h3 class="text-[16px] font-medium leading-6 text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">{{ feature.title }}</h3>
                <p class="mt-1 text-[14px] font-normal leading-6 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">{{ feature.description }}</p>
              </div>
            </div>
          </div>
        </article>

        <div class="grid grid-cols-2 gap-3 sm:gap-5">
          <article
            v-for="stat in companyStats"
            :key="stat.label"
            class="min-h-[138px] rounded-[16px] border border-slate-200 bg-white px-4 py-4 text-center shadow-[0_6px_18px_rgba(15,23,42,0.04)] sm:min-h-[215px] sm:rounded-[18px] sm:px-8 sm:py-6"
          >
            <p
              class="font-semibold leading-none tracking-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif] sm:text-[104px] sm:leading-[0.9]"
              :class="stat.mobileValue ? 'text-[30px] sm:text-[96px]' : 'text-[36px]'"
            >
              <template v-if="stat.mobileValue">
                <span class="sm:hidden">{{ stat.mobileValue }}</span>
                <span class="hidden whitespace-pre-line sm:inline">{{ stat.value }}</span>
              </template>
              <template v-else>
                {{ stat.value }}
              </template>
            </p>
            <p class="mt-3 text-[16px] font-normal leading-5 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif] sm:mt-6 sm:max-w-[160px] sm:leading-6">
              {{ stat.label }}
            </p>
          </article>
        </div>
      </div>
    </section>

    <section id="team" class="bg-[rgba(233,237,242,1)] py-6 lg:py-20">
      <div class="container-default">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-[28px] sm:text-[36px] font-semibold tracking-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
          Ключевые преимущества
        </h2>
        <p class="mt-2 sm:mt-4 text-[14px] sm:text-[18px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
          Почему клиенты доверяют нам оценку своей недвижимости
        </p>
      </div>

      <div class="mt-10 grid gap-4 xl:gap-6 md:grid-cols-2 xl:grid-cols-4">
        <article v-for="item in keyAdvantages" :key="item.title" class="rounded-[22px] border border-slate-200 bg-white p-5 shadow-sm">
          <div class="flex h-11 w-11 items-center justify-center rounded-full bg-[rgba(233,237,242,1)] text-slate-700">
            <img :src="item.icon" alt="" class="h-6 w-6 object-contain" />
          </div>
          <h3 class="mt-3 sm:mt-5 text-[18px] font-medium leading-7 text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">{{ item.title }}</h3>
          <p class="mt-1 sm:mt-3 text-[14px] font-normal leading-6 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
            {{ item.description }}
          </p>
        </article>
      </div>
      </div>
    </section>

    <section class="hidden py-8 sm:block sm:py-10 lg:py-14">
      <div class="container-default grid gap-10 lg:grid-cols-[0.94fr_1.06fr] lg:items-center">
      <div>
        <div class="max-w-2xl">
          <h2 class="text-[36px] font-semibold leading-tight tracking-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif] max-sm:text-3xl">
            Почему выбирают нас
          </h2>
          <p class="mt-5 max-w-[560px] text-[16px] font-normal leading-8 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
            Мы сочетаем технические знания, рыночную экспертизу и современные технологии для предоставления
            превосходных оценочных услуг, отвечающих вашим конкретным потребностям.
          </p>
        </div>

        <div class="mt-8 space-y-5">
          <div v-for="reason in reasons" :key="reason.title" class="flex items-start gap-4">
            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-[rgba(47,164,169,0.1)] text-[#5bc7ca]">
              <img :src="reason.icon" alt="" class="h-6 w-6 object-contain" />
            </div>

            <div>
              <h3 class="text-[18px] font-medium leading-6 text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">{{ reason.title }}</h3>
              <p class="mt-1 text-[14px] font-normal leading-6 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">{{ reason.description }}</p>
            </div>
          </div>
        </div>

        <div class="mt-10 w-full rounded-[16px] bg-[rgba(233,237,242,1)] px-7 py-6 shadow-[0_8px_20px_rgba(15,23,42,0.03)]">
          <div class="flex items-start gap-3.5">
            <div class="flex h-6 w-6 shrink-0 items-center justify-center text-emerald-500">
              <Icon class="h-6 w-6" name="lucide:check" />
            </div>
            <div>
              <h3 class="text-[16px] font-medium leading-6 text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">{{ reasonGuarantee.title }}</h3>
              <p class="mt-2 text-[14px] font-normal leading-6 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
                {{ reasonGuarantee.description }}
              </p>
            </div>
          </div>
        </div>
      </div>

      <div class="relative mx-auto w-full max-w-[320px] sm:max-w-[520px] sm:px-0 lg:mx-0">
        <div class="overflow-hidden rounded-[22px] shadow-sm">
          <img
            alt="Преимущества компании"
            class="h-[300px] sm:h-[420px] w-auto object-cover rounded-[22px]"
            src="/image/advantages.webp"
          />
        </div>

        <div class="absolute lg:w-[240px] bottom-[-14px] left-[-18px] rounded-[18px] bg-[rgba(47,164,169,1)] px-7 py-5 text-white shadow-[0_4px_6px_-4px_rgba(0,0,0,0.1),0_10px_15px_-3px_rgba(0,0,0,0.1)]">
          <p class="text-[64px] font-semibold leading-none [font-family:Inter,sans-serif]">98%</p>
          <p class="mt-2 text-right text-[14px] font-normal leading-5 text-white [font-family:Inter,sans-serif]">
            Удовлетворённость<br />
            клиентов
          </p>
        </div>
      </div>
      </div>
    </section>

    <section id="main-services" class="bg-[rgba(233,237,242,1)] py-6 sm:py-14 lg:py-20">
      <div class="container-default">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-[28px] sm:text-[36px] font-semibold tracking-tight text-center text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
          Наши услуги
        </h2>
        <p class="mt-2 sm:mt-4 text-[14px] sm:text-[18px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
          Комплексные оценочные решения для каждого типа недвижимости
        </p>
      </div>

      <div class="mt-10 grid grid-cols-1 gap-6 lg:grid-cols-2">
        <ServiceCard
          v-for="service in serviceLinks"
          :key="service.slug"
          :card-image="service.cardImage"
          :card-description="service.cardDescription"
          :description="service.description"
          :icon="service.icon"
          :title="service.title"
          :to="service.to"
          :use-cases="service.useCases"
          :use-cases-in-four-columns-on-lg="service.slug === 'kadastrovaya-stoimost'"
          :class="service.slug === 'kadastrovaya-stoimost' ? 'lg:col-span-2' : ''"
        />
      </div>
      </div>
    </section>

    <section id="reviews" class="bg-[rgba(233,237,242,1)] py-10 sm:bg-transparent sm:py-6">
      <div class="container-default">
        <div class="sm:hidden">
          <div class="mx-auto max-w-3xl text-center">
            <h2 class="text-[28px] sm:text-[36px] font-semibold leading-[1.05] tracking-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
              Как это работает
            </h2>
            <p class="mt-2 sm:mt-4 text-[14px] sm:text-[14px] sm:text-[18px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
              Простой процесс оценки в 4 шага
            </p>
          </div>

          <div class="mt-10 space-y-9">
            <article v-for="step in processStepsMobile" :key="step.step" class="flex items-start gap-4">
              <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-[#37b5bd] text-[18px] font-semibold leading-none text-white">
                {{ step.step }}
              </div>
              <div class="pt-1">
                <h3 class="text-[22px] font-semibold leading-[1.2] text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
                  {{ step.title }}
                </h3>
                <p class="mt-2 max-w-[520px] text-[17px] font-normal leading-[1.35] text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
                  {{ step.description }}
                </p>
              </div>
            </article>
          </div>
        </div>

        <div class="hidden sm:block">
          <div class="mx-auto max-w-3xl text-center">
            <h2 class="text-[28px] sm:text-[36px] font-semibold tracking-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
              Как это работает
            </h2>
            <p class="mt-2 sm:mt-4 text-[14px] sm:text-[18px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
              Простой и прозрачный процесс от заявки до финального отчета
            </p>
          </div>

          <div class="mt-12 grid grid-cols-1 items-stretch gap-6 md:grid-cols-2 xl:grid-cols-4">
            <div v-for="(step, index) in processSteps" :key="step.step" class="relative h-full">
              <div
                v-if="index < processSteps.length - 1"
                class="absolute left-[calc(100%)] top-1/2 z-10 hidden h-7 w-7 -translate-y-1/2 items-center justify-center rounded-full bg-[#37b5bd] text-white xl:flex"
              >
                <img :src="arrowRightIcon" alt="" class="h-6 w-6 object-contain" />
              </div>

              <article class="flex h-full flex-col rounded-[24px] border border-slate-200 bg-white px-6 pb-7 pt-5 text-center shadow-sm">
                <div class="mx-auto flex h-14 w-14 items-center justify-center rounded-full bg-[#37b5bd] text-xl font-semibold text-white">
                  {{ step.step }}
                </div>

                <div class="mx-auto mt-5 flex h-12 w-12 items-center justify-center rounded-full bg-slate-100 text-slate-700">
                  <img :src="step.icon" alt="" class="h-6 w-6 object-contain" />
                </div>

                <h3 class="mt-5 text-[18px] font-medium leading-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
                  {{ step.title }}
                </h3>
                <p class="mx-auto mt-3 max-w-[220px] flex-1 text-[14px] font-normal leading-6 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
                  {{ step.description }}
                </p>
              </article>
            </div>
          </div>

          <div class="mt-12 text-center">
            <p class="text-[16px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
              Готовы начать? Весь процесс обычно занимает 5-7 рабочих дней.
            </p>
            <a class="mt-5 inline-flex rounded-2xl bg-[#37b5bd] px-8 py-3 text-base font-semibold text-white transition hover:bg-[#2fa3aa]" href="#contact-form">
              Подать заявку
            </a>
          </div>
        </div>
      </div>
    </section>

    <section id="directions" class="hidden py-6 sm:block">
      <div class="container-default">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-[28px] sm:text-[36px] font-semibold tracking-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
          Наши направления
        </h2>
        <p class="mt-2 sm:mt-4 text-[14px] sm:text-[18px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
          Полный перечень всех работ по оценке
        </p>
      </div>

      <div class="mt-10 grid gap-6 lg:grid-cols-[1.05fr_0.95fr] lg:items-start">
        <article class="rounded-[26px] border border-l-4 border-slate-200 border-l-[rgba(44,111,140,1)] bg-white p-5 shadow-sm sm:p-6">
          <h3 class="text-[20px] font-medium leading-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">Недвижимое имущество</h3>

          <div class="mt-5 space-y-5">
            <section
              v-for="group in directionPropertyGroups"
              :key="group.title"
              class="rounded-[22px] border border-l-4 border-slate-200 border-l-[rgba(47,164,169,1)] bg-[#eef1f7] p-4 shadow-sm"
            >
              <div>
                <h4 class="text-[18px] font-medium leading-6 text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">{{ group.title }}</h4>

                <div class="mt-4 space-y-3">
                  <div
                    v-for="(item, itemIndex) in group.items"
                    :key="item"
                    class="rounded-2xl border border-slate-200 bg-white px-4 py-3 text-[14px] font-normal leading-6 text-[rgba(31,58,95,1)] shadow-[0_1px_3px_rgba(15,23,42,0.05)] [font-family:Inter,sans-serif]"
                  >
                    <div class="flex items-center justify-between gap-3">
                      <span>{{ item }}</span>
                      <span
                        v-if="group.title === 'Земельные участки'"
                        class="h-2.5 w-2.5 shrink-0 rounded-full"
                        :style="{
                          backgroundColor:
                            itemIndex < 3
                              ? 'rgba(47, 164, 169, 1)'
                              : itemIndex === 3
                                ? 'rgba(44, 111, 140, 1)'
                                : 'rgba(31, 58, 95, 1)'
                        }"
                      ></span>
                    </div>
                  </div>
                </div>
              </div>
            </section>
          </div>
        </article>

        <div class="space-y-5">
          <article class="rounded-[26px] border border-l-4 border-slate-200 border-l-[rgba(44,111,140,1)] bg-white p-5 shadow-sm sm:p-6">
            <h3 class="text-[20px] font-medium leading-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
              Снижение кадастр. стоимости недвижимости
            </h3>

            <div class="mt-5 rounded-[22px] border border-l-4 border-slate-200 border-l-[rgba(47,164,169,1)] bg-[#eef1f7] p-4 shadow-sm">
              <div>
                <h4 class="text-[18px] font-medium leading-6 text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">Типы объектов</h4>

                <div class="mt-4 space-y-3">
                  <div
                    v-for="item in directionCadastreItems"
                    :key="item"
                    class="rounded-2xl border border-slate-200 bg-white px-4 py-3 text-[14px] font-normal leading-6 text-[rgba(31,58,95,1)] shadow-[0_1px_3px_rgba(15,23,42,0.05)] [font-family:Inter,sans-serif]"
                  >
                    {{ item }}
                  </div>
                </div>
              </div>
            </div>
          </article>

          <article class="rounded-[26px] border border-l-4 border-slate-200 border-l-[rgba(44,111,140,1)] bg-white p-5 shadow-sm sm:p-6">
            <h3 class="text-[20px] font-medium leading-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">Движимое имущество</h3>

            <div class="mt-5 rounded-[22px] bg-[#eef1f7] px-6 py-8 text-center">
              <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-[#37b5bd] text-white">
                <img :src="directionsIcon" alt="" class="h-6 w-6 object-contain" />
              </div>
              <p class="mx-auto mt-4 max-w-[250px] text-[14px] font-normal leading-6 text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
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

    <section class="hidden bg-[rgba(233,237,242,1)] py-14 sm:block lg:py-20">
      <div class="container-default">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-[28px] sm:text-[36px] font-semibold tracking-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
          Наши эксперты и сертификация
        </h2>
        <p class="mx-auto mt-2 sm:mt-4 max-w-2xl text-[14px] sm:text-[18px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
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
            <img :src="item.icon" alt="" class="h-6 w-6 object-contain" />
          </div>
          <h3 class="mx-auto mt-5 max-w-[190px] text-[16px] font-medium leading-7 text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">{{ item.title }}</h3>
          <p class="mx-auto mt-3 max-w-[190px] text-[14px] font-normal leading-6 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">{{ item.description }}</p>
        </article>
      </div>

      <div class="mt-12 text-center">
        <h3 class="text-[28px] font-semibold tracking-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">Познакомьтесь с нашей командой</h3>
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
              <h4 class="text-[18px] font-medium text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">{{ member.name }}</h4>
              <p class="mt-1 text-sm font-medium text-[#37b5bd]">{{ member.role }}</p>
              <p class="mt-2 text-sm leading-6 text-slate-500">{{ member.experience }}</p>
              <p class="mt-1 text-sm leading-6 text-slate-500">{{ member.specialty }}</p>
            </div>
          </div>
        </article>
      </div>

      <article class="mt-8 rounded-[24px] border border-l-4 border-slate-200 border-l-[rgba(47,164,169,1)] bg-white px-6 py-6 shadow-sm">
        <div class="flex items-start gap-4">
          <div class="flex h-9 w-9 shrink-0 items-center justify-center rounded-full text-emerald-500">
            <img :src="team3" alt="" class="h-6 w-6 object-contain" />
          </div>
          <div>
            <h3 class="text-[18px] font-medium text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">{{ expertCertificationNote.title }}</h3>
            <p class="mt-2 text-[14px] font-normal leading-6 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">{{ expertCertificationNote.description }}</p>
          </div>
        </div>
      </article>
      </div>
    </section>

    <section class="hidden py-6 sm:block">
      <div class="container-default">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-[28px] sm:text-[36px] font-semibold tracking-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
          Отзывы клиентов
        </h2>
        <p class="mt-2 sm:mt-4 text-[14px] sm:text-[18px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
          Что наши клиенты говорят о наших услугах
        </p>
      </div>
      <!-- <div class="w-full h-px bg-[]"> -->
      <div class="mt-10 grid grid-cols-1 gap-5 lg:grid-cols-2">
        <article
          v-for="review in reviews"
          :key="review.author"
          class="relative flex h-full flex-col rounded-[24px] border border-slate-200 bg-white px-6 py-6 shadow-sm"
        >
          <img :src="quoteIcon" alt="" class="absolute right-6 top-6 h-16 w-16 object-contain" />
          <div class="flex items-start justify-between gap-4">
            <div class="flex items-center gap-1 text-amber-400">
              <img
                v-for="star in review.rating"
                :key="star"
                :src="starIcon"
                alt=""
                class="h-5 w-5 object-contain"
              />
            </div>
          </div>

          <p class="mt-2 w-[90%] text-[16px] font-normal pb-4 leading-7 text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif] md:w-[93%]">
            {{ review.text }}
          </p>

          <div class="mt-auto flex items-end justify-between gap-4 pt-4 border-t border-slate-200">
            <div>
              <p class="text-[16px] font-medium text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">{{ review.author }}</p>
              <p class="mt-1 text-[14px] font-normal text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">{{ review.role }}</p>
            </div>
            <p class="text-[14px] font-normal text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">{{ review.date }}</p>
          </div>
        </article>
      </div>

      <div class="mt-10 grid grid-cols-1 gap-4 md:grid-cols-3">
        <article
          v-for="stat in reviewStats"
          :key="stat.label"
          class="rounded-[22px] bg-[rgba(233,237,242,1)] px-6 py-6 text-center"
        >
          <div class="flex items-center justify-center gap-2">
            <img
              v-if="stat.icon"
              :src="stat.icon"
              alt=""
              class="h-8 w-8 object-contain"
            />
            <p class="text-[36px] font-semibold leading-none text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">{{ stat.value }}</p>
          </div>
          <p class="mt-3 text-[14px] font-normal text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">{{ stat.label }}</p>
        </article>
      </div>
      </div>
    </section>

    <section id="pricing" class="bg-[rgba(233,237,242,1)] py-14 lg:py-20">
      <div class="container-default">
      <div class="mx-auto max-w-3xl text-center">
        <h2 class="text-[28px] sm:text-[36px] font-semibold tracking-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
          Прайс
        </h2>
        <p class="mx-auto mt-2 sm:mt-4 max-w-2xl text-[14px] sm:text-[18px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
          Лицензированные профессионалы с подтвержденным опытом и признанием в отрасли
        </p>
      </div>

      <div class="mx-auto mt-10 space-y-5">
        <div
          v-for="(item, index) in priceList"
          :key="item.title"
          class="group relative overflow-hidden rounded-[14px] transition-all duration-200"
          :class="
            pricingOpenStates[index]
              ? 'p-[4px]'
              : 'border border-slate-200 border-l-[4px] border-l-[rgba(47,164,169,1)] bg-white sm:hover:border-l-[8px]'
          "
          :style="
            pricingOpenStates[index]
              ? { background: 'linear-gradient(180deg, rgba(47,164,169,1) 10%, rgba(233,237,242,1) 19%)' }
              : undefined
          "
        >
          <div class="overflow-hidden bg-white shadow-sm" :class="pricingOpenStates[index] ? 'rounded-[13px]' : 'rounded-[14px]'">
            <button
              type="button"
              class="flex w-full cursor-pointer items-center justify-between gap-4 py-6 px-6 text-left sm:group-hover:pl-[20px]"
              @click="togglePricingAccordion(index)"
            >
              <span class="text-[24px] font-medium leading-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif] max-sm:text-xl">
                {{ item.title }}
              </span>
              <span class="shrink-0 text-[#37b5bd] transition" :class="pricingOpenStates[index] ? 'rotate-180' : ''">
                <Icon class="h-6 w-6" name="lucide:chevron-down" />
              </span>
            </button>

            <div v-if="pricingOpenStates[index]" class=" bg-[rgba(233,237,242,1)]">
              <div class="h-[40px] w-full bg-[linear-gradient(180deg,#FFFFFF_21.94%,rgba(255,255,255,0)_100%)]"></div>

              <div class="px-4 pb-5 sm:px-5">
                <p v-if="item.groupLabel" class="px-1 text-[22px] font-medium leading-7 text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
                  {{ item.groupLabel }}
                </p>
                <p class="mt-2 px-1 text-[14px] font-normal leading-6 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
                  {{ item.description }}
                </p>

                <div class="mt-4 space-y-2.5">
                  <div
                    v-for="entry in item.entries || []"
                    :key="`${item.title}-${entry.name}`"
                    class="flex flex-wrap items-center justify-between gap-4 rounded-[12px] border-l-4 border-l-[#2fa4a9] bg-white px-5 py-4"
                  >
                    <div class="flex min-w-[220px] flex-1 items-start gap-3">
                      <div v-if="item.icon" class="flex h-6 w-6 shrink-0 items-center justify-center rounded-full">
                        <img :src="item.icon" alt="" class="h-6 w-6 object-contain" />
                      </div>
                      <div class="min-w-0 flex-1">
                        <p class="text-[16px] font-medium leading-6 text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
                          {{ entry.name }}
                        </p>
                        <p class="mt-1 text-[13px] font-normal leading-5 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
                          {{ entry.note }}
                        </p>
                      </div>
                    </div>
                    <p class="min-w-[90px] text-[32px] font-medium leading-none text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
                      {{ entry.price }}
                    </p>
                    <NuxtLink
                      class="inline-flex h-12 items-center justify-center gap-2 rounded-xl bg-[#2fa4a9] px-6 text-[16px] font-medium text-white transition sm:hover:bg-[#289299]"
                      :to="{
                        path: '/',
                        hash: '#contact-form',
                        query: {
                          presetComment: buildPricingComment(item, entry),
                          presetPropertyType: getPricingPropertyType(item)
                        }
                      }"
                    >
                      Подать заявку
                      <Icon class="h-5 w-5" name="lucide:arrow-right" />
                    </NuxtLink>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      </div>
    </section>

    <ContactSection />
  </div>
</template>

<style scoped>
.main-hero-banner {
  background-image: linear-gradient(90deg, rgba(15, 23, 42, 0) 0%, rgba(15, 23, 42, 0) 42%, rgba(15, 23, 42, 0) 100%), var(--hero-banner-desktop);
  background-size: cover;
  background-position: center bottom;
  background-repeat: no-repeat;
}

@media (max-width: 639px) {
  .main-hero-banner {
    background-image: linear-gradient(90deg, rgba(15, 23, 42, 0) 0%, rgba(15, 23, 42, 0) 42%, rgba(15, 23, 42, 0) 100%), var(--hero-banner-mobile);
  }
}
</style>
