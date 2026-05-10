<script setup lang="ts">
import { getServiceBySlug } from '~/utils/services'
import serviceHandsIcon from '~/assets/icon/service-hands.svg'
import serviceLightIcon from '~/assets/icon/service-ligth.svg'
import serviceDocumentIcon from '~/assets/icon/service-document.svg'
import serviceDollarIcon from '~/assets/icon/service-dollar.svg'
import howWork1 from '~/assets/icon/how-work-1.svg'
import howWork2 from '~/assets/icon/how-work-2.svg'
import howWork3 from '~/assets/icon/how-work-3.svg'
import howWork4 from '~/assets/icon/how-work-4.svg'
import arrowRightIcon from '~/assets/icon/arrow-right.svg'

const route = useRoute()
const slug = computed(() => String(route.params.slug || ''))
const service = computed(() => getServiceBySlug(slug.value))
const mobileHeroBannerBySlug: Record<string, string> = {
  'zhilaya-nedvizhimost': '/image/banner-zhilaya-mobile.webp',
  'nezhilaya-nedvizhimost': '/image/banner-nezhilaya-mobile.webp',
  'zemelnyj-uchastok': '/image/banner-zemlya-mobile.webp',
  'kadastrovaya-stoimost': '/image/banner-kadastr-mobile.webp'
}

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
  '--hero-banner-desktop': `url('${service.value?.heroBanner || ''}')`,
  '--hero-banner-mobile': `url('${mobileHeroBannerBySlug[service.value?.slug || ''] || service.value?.heroBanner || ''}')`
}))

const heroTitle = computed(() => {
  switch (service.value?.slug) {
    case 'dvizhimoe-imushchestvo':
      return 'Оценка движимого имущества'
    case 'nezhilaya-nedvizhimost':
      return 'Оценка нежилой недвижимости'
    case 'zhilaya-nedvizhimost':
      return 'Оценка жилой недвижимости'
    case 'zemelnyj-uchastok':
      return 'Оценка земельного участка'
    case 'kadastrovaya-stoimost':
      return 'Снижение кадастровой стоимости'
    default:
      return 'Оценка жилой недвижимости'
  }
})

const heroUseCases = [
  {
    title: 'Гражданско-правовые сделки',
    description: 'Для точного определения стоимости имущества в сделках.',
    icon: serviceHandsIcon
  },
  {
    title: 'Раздел имущества',
    description: 'Для справедливого раздела имущества, определяя его стоимость.',
    icon: serviceLightIcon
  },
  {
    title: 'Бухгалтерские операции',
    description: 'Для обеспечения точных данных для учета активов и налогов.',
    icon: serviceDocumentIcon
  },
  {
    title: 'Получение страховки',
    description: 'Для определения стоимости страхования, давая защиту и уверенность в качестве.',
    icon: serviceDollarIcon
  }
]

const servicePurposeContent = computed(() => {
  switch (service.value?.slug) {
    case 'dvizhimoe-imushchestvo':
      return {
        title: 'Зачем нужна оценка движимого имущества?',
        paragraphs: [
          'Выяснение стоимости собственности требуется при заключении гражданско-правовых сделок, проведении бухгалтерских операций, разделе имущества, получении страховки, оформлении кредита или возмещении нанесенного ущерба.',
          'Это только краткий перечень ситуаций, в которых вам могут понадобиться оценочные услуги. По результатам работы вы получите отчет об оценке стоимости движимого имущества, который можно будет предоставить в суд, банк или другую организацию.',
          'Знание объективной стоимости автомобиля помогает более рационально использовать собственность. Получить такие знания хотят многие владельцы частных и коммерческих авто любого назначения. Наша компания решает эту задачу с помощью проведения оценки рыночной стоимости транспортных средств и выдает отчет с результатами работы.'
        ],
        bullets: [] as string[]
      }
    case 'nezhilaya-nedvizhimost':
      return {
        title: 'Зачем нужна оценка нежилой недвижимости?',
        paragraphs: [
          'Оценивать стоимость нежилой недвижимости чаще всего приходится предпринимателям, так как к этой категории относятся постройки для производства и хранения товаров, торговли, отдыха, офисных задач и других целей. Наша компания «Перэкс Оценка» определит реальную стоимость вашей собственности. Вы получите документ с окончательной ценой и детальным описанием всех факторов, которые на нее повлияли.',
          'Как и другие постройки, эти объекты оценивают перед куплей-продажей. Также их цену приходится рассчитывать при дарении, получении в наследство и разделе имущества. Помимо этого, нежилые здания оценивают для получения займов, сдачи в аренду, с целью бухгалтерского учета, обжалования кадастровой стоимости и в других случаях. Мы проводим оценку объектов с учетом их индивидуальных особенностей. В результате клиент получает отчет, который служит официальным документом в любой государственной инстанции или коммерческой организации.'
        ],
        bullets: [] as string[]
      }
    case 'zhilaya-nedvizhimost':
      return {
        title: 'Зачем нужна оценка жилой недвижимости?',
        paragraphs: [
          'Цены на недвижимость постоянно меняются, поэтому стоимость ее продажи нужно определять методом экспертной оценки. Она распространяется на земельные участки, частные дома и квартиры, офисные, коммерческие и промышленные постройки, незавершенные объекты, паи в сельском хозяйстве, гаражи и прочую собственность.',
          'Компания «Перэкс Оценка» занимается оценкой недвижимого имущества с предоставлением отчета и с гарантией качества. Наши услуги могут быть полезны частным лицам и предпринимателям.',
          'Рассчитывать стоимость недвижимой собственности необходимо при ее продаже или передаче под залог для оформления кредита. Также от цены объекта зависят налоговые сборы и платежи. При имущественных спорах тоже проводят оценку недвижимости, чтобы разделить наследство или совместно нажитую в браке собственность. После оценки стоимости недвижимого имущества выдается отчет, который служит официальным документом в государственных и коммерческих структурах.'
        ],
        bullets: [] as string[]
      }
    case 'zemelnyj-uchastok':
      return {
        title: 'Зачем нужна оценка стоимости земельного участка?',
        paragraphs: [
          'Рыночная стоимость земельного участка — это полезная информация для владельцев наделов любого назначения и категории. С помощью проведения независимой оценки стоимости земельного участка можно более выгодно распоряжаться собственностью.',
          'Наша компания «Перэкс Оценка» оказывает услугу оценки недвижимого имущества и выдает клиентам официальный отчет по ее результатам.',
          'Также стоимость земли определяют при сдаче ее под залог и перед привлечением инвесторов (или вложением денег в развитие чужого участка).'
        ],
        bullets: ['перед куплей-продажей надела;', 'при наследовании;', 'при разрешении споров относительно общего имущества.']
      }
    case 'kadastrovaya-stoimost':
      return {
        title: 'Зачем нужно снижение кадастровой стоимости?',
        paragraphs: [
          'От кадастровой цены объекта зависит стоимость его аренды и выплачиваемые налоги. Поэтому владельцы земельных участков, а также жилых и нежилых зданий и помещений заказывают оценку недвижимости для снижения кадастровой стоимости.',
          'Предлагаем заказать эту услугу в нашей компании «Перэкс Оценка». По завершению оценки недвижимого имущества вы получите отчет, соответствующий государственным требованиям.'
        ],
        bullets: [] as string[]
      }
    default:
      return {
        title: 'Зачем нужна оценка недвижимости?',
        paragraphs: ['Помогаем определить объективную стоимость имущества и подготовить официальный отчет для любых целей.'],
        bullets: [] as string[]
      }
  }
})

const servicePurposeImage = computed(() => {
  switch (service.value?.slug) {
    case 'dvizhimoe-imushchestvo':
      return '/image/why-car.webp'
    case 'nezhilaya-nedvizhimost':
      return '/image/why-non-apart.webp'
    default:
      return '/image/why-apart.webp'
  }
})

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

type ServiceExtraBlock = {
  title: string
  paragraphs: string[]
  image: string
  imageLeft?: boolean
  showCtaAfter?: boolean
  bullets?: string[]
}

const nonResidentialExtraBlocks: ServiceExtraBlock[] = [
  {
    title: '',
    paragraphs: [
      'Реальная стоимость жилья зависит от его площади, состояния, этажности постройки, благоустроенности придомовой территории и других факторов. Поэтому правильную оценку могут выполнить только оценщики. Они помогают рассчитывать цены на собственность для владельцев жилых объектов. К таким объектам относятся [квартиры и доли в квартирах], [дома и коттеджи], комнаты в коммуналках. Наша компания оказывает услуги по оценке жилой недвижимости с выдачей отчета после завершения работ.',
      'Эта процедура востребована при купле-продаже и сдаче в аренду нежилых объектов. Она помогает продавцу объективно рассчитать цену, а покупателю - избежать переплат. Также услугу заказывают при оформлении ипотеки или кредита под жилую собственность, получении страховки на жилье и разделе наследства. Отчет об оценке стоимости жилой недвижимости служит официальным документом, который можно предоставить в суд, страховую компанию или банк.'
    ],
    image: '/image/non-apart-1.webp',
    imageLeft: true
  },
  {
    title: 'Оценка нежилого помещения',
    paragraphs: [
      'Нежилые помещения расположены в многоквартирных домах, но используются не для проживания и не для технического обеспечения эксплуатации здания, а для получения прибыли. В них размещаются офисы, магазины, рестораны или кафе, салоны услуг, образовательные или медицинские заведения и т.д.',
      'Такие объекты часто переходят из рук в руки, а для этого необходима рыночная оценка нежилого помещения, которая помогает установить его стоимость.',
      'Наша компания «Перэкс Оценка» оказывает оценочные услуги и предоставляет клиенту официальный отчет об оценке.'
    ],
    image: '/image/non-apart-2.webp',
    showCtaAfter: true
  },
  {
    title: 'Оценка нежилого здания с земельным участком',
    paragraphs: [
      'Нежилые строения используются в производственных, коммерческих, административных, логистических и прочих целях. Они принадлежат физическим или юридическим лицам.',
      'Чтобы совершать любые сделки, решать споры имущественного характера с ними, необходима оценка нежилого здания с земельным участком, которая позволит определить стоимость объекта.',
      'Компания «Перэкс Оценка» проводит оценку нежилой недвижимости и предоставляет клиенту отчет, в котором учтены все факторы, влияющие на цену.'
    ],
    image: '/image/non-apart-3.webp',
    imageLeft: true
  },
  {
    title: 'Незавершенный строительством дом, коттедж, таунхаус, дача с земельным участком',
    paragraphs: [
      'Не достроенный по каким-либо причинам и не введенный в эксплуатацию жилой дом может быть предметом имущественных отношений или споров. Для совершения юридически значимых действий с ним необходимо знать его стоимость. Наша компания «Перэкс Оценка» оказывает услуги оценки незавершенного строительства жилого дома и предоставляет заказчикам отчет по ее итогам.',
      'Недостроенный дом можно купить, завещать или получить в наследство, подарить, использовать в качестве залога или как часть уставного капитала. Также его стоимость нужно знать, чтобы решить вопрос о возобновлении строительства или сносе здания и использовании земельного участка по другому назначению. Для определения цены необходимо выяснить его состояние, степень износа.'
    ],
    image: '/image/non-apart-4.webp',
    showCtaAfter: true
  }
]

const residentialExtraBlocks: ServiceExtraBlock[] = [
  {
    title: '',
    paragraphs: [
      'Реальная стоимость жилья зависит от его площади, состояния, этажности постройки, благоустроенности придомовой территории и других факторов. Поэтому правильную оценку могут выполнить только оценщики. Они помогают рассчитывать цены на собственность для владельцев жилых объектов. К таким объектам относятся [квартиры и доли в квартирах], [дома и коттеджи], комнаты в коммуналках. Наша компания оказывает услуги по оценке жилой недвижимости с выдачей отчета после завершения работ.',
      'Эта процедура востребована при купле-продаже жилых объектов. Она помогает продавцу объективно рассчитать цену, а покупателю -- избежать переплат. Также услугу заказывают при оформлении ипотеки или кредита под жилую собственность, получении страховки на жилье и разделе наследства. Отчет об оценке стоимости жилой недвижимости служит официальным документом, который можно предоставить в суд, страховую компанию или банк.'
    ],
    image: '/image/non-apart-1.webp',
    imageLeft: true
  },
  {
    title: 'Квартира, комната, кухня-прихожая, в том числе доля в праве на них',
    paragraphs: [
      'Жилая недвижимость чаще всего становится предметом сделок купли-продажи и имущественных споров независимо от её размеров, статуса, принадлежности. Для совершения любых юридических действий необходимо знать, сколько стоит объект недвижимости. Наша компания в Барнауле предлагает провести оценку рыночной стоимости квартиры, комнаты, гостинки, кухни-прихожей и подготовить отчет по ее результатам.',
      'Услуга оценки квартиры необходима для продажи, наследования, страхования недвижимости, оформления залога, разделения прав. Отчет по оценке комнаты в квартире потребуется при выкупе доли. Для решения споров, связанных с недвижимостью, в суде необходимо иметь подтверждение рыночной стоимости.'
    ],
    image: '/image/non-apart-5.webp',
    showCtaAfter: true
  },
  {
    title: 'Дом, коттедж, таунхаус, дачи с земельным участком',
    paragraphs: [
      'Отдельно стоящий дом часто выступает предметом имущественных отношений. Для юридически значимых действий с ним необходимо знать, сколько он стоит. Для этого производится оценка рыночной стоимости жилой недвижимости -- дома, коттеджа, таунхауса, дачи с земельным участком. Компания «Перэкс Оценка» оказывает такие услуги и составляет по итогам оценочных мероприятий отчет об оценке дома, коттеджа, дачи.',
      'Независимая оценка частного дома, дачи помогает определить цену недвижимости для купли-продажи, дарения, наследования, использования в качестве залога, страхования, определения сумы ущерба, при разделе имущества, а также при судебных разбирательствах. В ходе оценочных работ рассматриваются ценообразующие факторы: местоположение, площадь участка и здания, наличие инженерных сетей и подъездных путей, материалы, износ и другое.'
    ],
    image: '/image/non-apart-6.webp',
    imageLeft: true
  }
]

const cadastreExtraBlocks: ServiceExtraBlock[] = [
  {
    title: 'Зачем нужно снижение кадастровой стоимости?',
    paragraphs: [
      'Эта услуга позволяет оспаривать кадастровую стоимость объекта, если она рассчитывалась на основании неправильных данных:',
      'Пересмотр кадастровой стоимости также возможен при завышенной цене постройки или земельного участка в сравнении с рыночными предложениями. Но для доказательства вашей правоты необходимо оценить собственность.',
      'Наш оценщик сделает это с соблюдением требований законодательства.'
    ],
    bullets: ['о площади постройки;', 'об использованных строительных материалах'],
    image: '/image/kadastr-1.webp',
    imageLeft: true
  }
]

const serviceExtraBlocks = computed<ServiceExtraBlock[]>(() => {
  if (service.value?.slug === 'nezhilaya-nedvizhimost') {
    return nonResidentialExtraBlocks
  }

  if (service.value?.slug === 'zhilaya-nedvizhimost') {
    return residentialExtraBlocks
  }

  if (service.value?.slug === 'kadastrovaya-stoimost') {
    return cadastreExtraBlocks
  }

  return []
})

const landAreaDetails = [
  {
    title: 'Земельный участок площадью\nменее 10 соток',
    description: 'Оценка небольших земельных наделов для личного пользования, садоводства или ИЖС.',
    image: '/image/land-1.webp'
  },
  {
    title: 'Земельный участок площадью\nот 10 до 50 соток',
    description: 'Оценка участков среднего размера под индивидуальное жилищное строительство, фермерское хозяйство или коммерческое использование.',
    image: '/image/land-2.webp'
  },
  {
    title: 'Земельный участок площадью\nот 50 соток до 1 Га',
    description: 'Оценка крупных наделов под сельскохозяйственные нужды, коттеджные поселки или коммерческую застройку.',
    image: '/image/land-3.webp'
  },
  {
    title: 'Земельный участок площадью\nот 1 до 100 Га',
    description: 'Оценка значительных территорий под сельскохозяйственное производство, инвестиционные проекты или промышленное освоение.',
    image: '/image/land-4.webp'
  },
  {
    title: 'Земельный участок площадью\nот 100 до 1000 Га',
    description: 'Оценка масштабных земельных массивов для агропромышленных комплексов, крупных инвестиционных проектов или перераспределения земель.',
    image: '/image/land-5.webp'
  },
  {
    title: 'Земельный участок площадью\nболее 1000 Га',
    description: 'Оценка обширных территорий для стратегических инвестиций, крупных агрохолдингов или государственных нужд.',
    image: '/image/land-6.webp'
  }
]

const cadastreObjectDetails = [
  {
    title: 'Земельный участок\n(любой категории и назначения)',
    description:
      'Оценка земельного участка для оспаривания кадастровой стоимости позволяет существенно снизить налоговую нагрузку и арендные платежи.',
    image: '/image/kadastr-2.webp'
  },
  {
    title: 'Нежилое здание',
    description:
      'Оценка нежилого здания для снижения кадастровой стоимости необходима, если кадастровая оценка была проведена с ошибками или не учитывает фактическое состояние объекта.',
    image: '/image/kadastr-3.webp'
  },
  {
    title: 'Жилое помещение\n(квартира/комната/гостинка/кухня-прихожая)',
    description:
      'Для владельцев квартир и комнат снижение кадастровой стоимости означает уменьшение налога на имущество и снижение сопутствующих расходов.',
    image: '/image/kadastr-4.webp'
  },
  {
    title: 'Нежилое помещение',
    description:
      'Нежилые помещения в многоквартирных домах также могут быть переоценены, если их кадастровая стоимость завышена и не отражает рыночных условий.',
    image: '/image/kadastr-5.webp'
  },
  {
    title: 'Жилое здание\n(дом/коттедж/таунхаус/дача)',
    description:
      'Для владельцев индивидуальных жилых домов снижение кадастровой стоимости позволяет уменьшить земельный и имущественный налог.',
    image: '/image/kadastr-6.webp'
  }
]
</script>

<template>
  <div class="">
    <section
      class="service-hero-banner overflow-hidden py-2 sm:py-20 mb-10 lg:flex lg:h-[620px] lg:items-center lg:py-0"
      :style="heroStyle"
    >
      <div class="container-default">
        <div class="max-w-[900px] rounded-[28px] border border-white/20 bg-[rgba(15,23,42,0.35)] p-4 shadow-xl backdrop-blur-[4px] sm:p-8 lg:p-10">
          <h1 class="text-[24px] sm:text-[48px] font-semibold leading-[1.1] text-[rgba(255,255,255,1)] [font-family:Inter,sans-serif]">
            {{ heroTitle }}
          </h1>
          <p class="mt-2 sm:mt-6 max-w-4xl text-[14px] sm:text-[18px] font-normal leading-5 sm:leading-7 text-[rgba(233,237,242,1)] [font-family:Inter,sans-serif]">{{ service?.description }}</p>

          <div class="mt-4 sm:mt-8 grid gap-2 sm:gap-4 md:grid-cols-2">
            <article
              v-for="item in heroUseCases"
              :key="item.title"
              class="flex items-start gap-3 rounded-[16px] bg-[rgba(233,237,242,0)]  sm:p-4"
            >
              <div class="flex h-5 w-5 sm:h-6 sm:w-6 shrink-0 items-center justify-center rounded-full">
                <img :src="item.icon" alt="" class="h-5 w-5 sm:h-6 sm:w-6 object-contain" />
              </div>
              <div>
                <p class="text-[16px] font-medium leading-5 sm:leading-6 text-white [font-family:Inter,sans-serif]">{{ item.title }}</p>
                <p class="mt-1 text-[12px] sm:text-[14px] font-normal leading-5 sm:leading-6 text-white [font-family:Inter,sans-serif]">{{ item.description }}</p>
              </div>
            </article>
          </div>

          <div class="mt-8 flex flex-col gap-4 sm:flex-row sm:flex-wrap">
            <a
              class="inline-flex h-12 w-full items-center justify-center rounded-xl bg-[#37b5bd] px-8 text-[16px] font-semibold text-white transition hover:bg-[#2fa3aa] [font-family:Inter,sans-serif] sm:w-auto"
              href="#contact-form"
            >
              Подать заявку
            </a>
            <NuxtLink
              class="inline-flex h-12 w-full items-center justify-center gap-3 rounded-xl border border-white/50 bg-white/20 px-8 text-[16px] font-medium text-white transition backdrop-blur-[8px] hover:bg-white/30 [font-family:Inter,sans-serif] sm:w-auto"
              to="/#main-services"
            >
              другие услуги
              <Icon aria-hidden="true" class="h-5 w-5" name="lucide:arrow-right" />
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>

    <section class="container-default">
      <article class="rounded-[24px]">
        <h2 class="text-center text-[28px] sm:text-[36px] font-semibold leading-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
          {{ servicePurposeContent.title }}
        </h2>

        <div class="mt-8 grid gap-8 lg:grid-cols-[1.05fr_0.95fr] lg:items-start">
          <div class="lg:w-[95%] space-y-5 text-[17px] font-normal leading-6 sm:leading-8 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
            <p v-for="paragraph in servicePurposeContent.paragraphs" :key="paragraph">
              {{ paragraph }}
            </p>
            <div v-if="servicePurposeContent.bullets.length">
              <p>Узнать цену будет полезно:</p>
              <ul class="mt-2 space-y-1">
                <li v-for="bullet in servicePurposeContent.bullets" :key="bullet">
                  • {{ bullet }}
                </li>
              </ul>
            </div>
          </div>

          <div class="overflow-hidden rounded-[18px] shadow-sm lg:justify-self-end">
            <img :src="servicePurposeImage" :alt="servicePurposeContent.title" class=" sm:h-[480px] sm:w-[480px] w-full h-auto object-cover" />
          </div>
        </div>
      </article>
    </section>

    <section class="bg-[rgba(233,237,242,1)] py-10 sm:bg-transparent sm:py-6">
      <div class="container-default">
        <div class="sm:hidden">
          <div class="mx-auto max-w-3xl text-center">
            <h2 class="text-[28px] sm:text-[36px] font-semibold leading-[1.05] tracking-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
              Как это работает
            </h2>
            <p class="mt-2 sm:mt-4 text-[14px] sm:text-[18px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
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
                <img :src="arrowRightIcon" alt="" class="h-4 w-4 object-contain" />
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

    <section v-if="service?.slug === 'kadastrovaya-stoimost' && serviceExtraBlocks.length" class="container-default space-y-8">
      <div v-for="(block, index) in serviceExtraBlocks" :key="`kadastr-${block.title || 'intro'}-${index}`" class="space-y-8">
        <article class="rounded-[24px]">
          <h2
            v-if="block.title"
            class="text-[28px] sm:text-[36px] sm:w-[85%] w-full mx-auto font-semibold text-center mb-8 mt-24 leading-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]"
          >
            {{ block.title }}
          </h2>
          <div class="grid gap-8 lg:grid-cols-[1.05fr_0.95fr] lg:items-start">
            <div
              class="space-y-5 text-[17px] w-[95%] font-normal leading-6 sm:leading-8 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]"
              :class="block.imageLeft ? 'text-right lg:order-2 lg:justify-self-end' : 'lg:order-1'"
            >
              <p v-for="paragraph in block.paragraphs" :key="paragraph">
                {{ paragraph }}
              </p>
              <ul v-if="block.bullets?.length" class="space-y-1">
                <li v-for="bullet in block.bullets" :key="bullet">
                  • {{ bullet }}
                </li>
              </ul>
            </div>

            <div class="overflow-hidden shadow-sm" :class="block.imageLeft ? 'lg:order-1' : 'lg:order-2 lg:justify-self-end'">
              <img :src="block.image" :alt="block.title || 'Оценка нежилой недвижимости'" class="sm:h-[480px] sm:w-[480px] w-full h-auto object-cover rounded-[18px]" />
            </div>
          </div>
        </article>

        <div v-if="block.showCtaAfter" class="text-center">
          <p class="text-[16px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
            Готовы начать? Весь процесс занимает от 1 рабочего дня
          </p>
          <a class="mt-5 inline-flex rounded-2xl bg-[#37b5bd] px-8 py-3 text-base font-semibold text-white transition sm:hover:bg-[#2fa3aa]" href="#contact-form">
            Подать заявку
          </a>
        </div>
      </div>
    </section>

    <section v-if="service?.slug === 'kadastrovaya-stoimost'" class="bg-[rgba(233,237,242,1)] py-10 sm:py-12">
      <div class="container-default">
        <div class="mx-auto max-w-3xl text-center">
          <h2 class="text-[28px] sm:text-[36px] font-semibold tracking-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
            Выберите объект для снижения кадастровой стоимости
          </h2>
          <p class="mt-2 sm:mt-4 text-[14px] sm:text-[18px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
            Любых категорий и назначения
          </p>
        </div>

        <div class="mt-10 grid gap-6 md:grid-cols-2">
          <article
            v-for="item in cadastreObjectDetails"
            :key="item.title"
            class="flex h-full flex-col overflow-hidden rounded-[16px] border border-slate-200 bg-white shadow-sm"
          >
            <img :src="item.image" :alt="item.title.replace('\n', ' ')" class="h-[170px] w-full object-cover" />
            <div class="flex flex-1 flex-col gap-4 p-5">
              <h3 class="whitespace-pre-line text-[32px] font-medium leading-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
                {{ item.title }}
              </h3>
              <p class="text-[14px] font-normal leading-6 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
                {{ item.description }}
              </p>
              <a
                class="mt-auto inline-flex h-12 w-full items-center justify-center rounded-xl bg-[#37b5bd] px-6 text-[16px] font-medium text-white transition sm:hover:bg-[#2fa3aa]"
                href="#contact-form"
              >
                Подать заявку
              </a>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section v-if="serviceExtraBlocks.length && service?.slug !== 'kadastrovaya-stoimost'" class="container-default space-y-8">
      <div v-for="(block, index) in serviceExtraBlocks" :key="`${block.title || 'intro'}-${index}`" class="space-y-8">
        <article class="rounded-[24px]">
          <h2
            v-if="block.title"
            class="text-[28px] sm:text-[36px] sm:w-[85%] w-full mx-auto font-semibold text-center mb-8 mt-24 leading-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]"
          >
            {{ block.title }}
          </h2>
          <div class="grid gap-8 lg:grid-cols-[1.05fr_0.95fr] lg:items-start">
            <div
              class="space-y-5 text-[17px] w-[95%] font-normal leading-6 sm:leading-8 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]"
              :class="block.imageLeft ? 'text-right lg:order-2 lg:justify-self-end' : 'lg:order-1'"
            >
              <p v-for="paragraph in block.paragraphs" :key="paragraph">
                {{ paragraph }}
              </p>
              <ul v-if="block.bullets?.length" class="space-y-1">
                <li v-for="bullet in block.bullets" :key="bullet">
                  • {{ bullet }}
                </li>
              </ul>
            </div>

            <div class="overflow-hidden shadow-sm" :class="block.imageLeft ? 'lg:order-1' : 'lg:order-2 lg:justify-self-end'">
              <img :src="block.image" :alt="block.title || 'Оценка нежилой недвижимости'" class="sm:h-[480px] sm:w-[480px] w-full h-auto object-cover rounded-[18px]" />
            </div>
          </div>
        </article>

        <div v-if="block.showCtaAfter" class="text-center">
          <p class="text-[16px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
            Готовы начать? Весь процесс занимает от 1 рабочего дня
          </p>
          <a class="mt-5 inline-flex rounded-2xl bg-[#37b5bd] px-8 py-3 text-base font-semibold text-white transition sm:hover:bg-[#2fa3aa]" href="#contact-form">
            Подать заявку
          </a>
        </div>
      </div>
    </section>

    <section v-if="service?.slug === 'zemelnyj-uchastok'" class="bg-[rgba(233,237,242,1)] py-10 sm:py-12">
      <div class="container-default">
        <div class="mx-auto max-w-3xl text-center">
          <h2 class="text-[28px] sm:text-[36px] font-semibold tracking-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
            Детализация по площади земельных участков
          </h2>
          <p class="mt-2 sm:mt-4 text-[14px] sm:text-[18px] font-normal leading-7 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
            Решения для участков любой площади
          </p>
        </div>

        <div class="mt-10 grid gap-6 md:grid-cols-2">
          <article
            v-for="item in landAreaDetails"
            :key="item.title"
            class="flex h-full flex-col overflow-hidden rounded-[16px] border border-slate-200 bg-white shadow-sm"
          >
            <img :src="item.image" :alt="item.title.replace('\n', ' ')" class="h-[170px] w-full object-cover" />
            <div class="flex flex-1 flex-col gap-4 p-5">
              <h3 class="whitespace-pre-line text-[28px] sm:text-[32px] font-medium leading-tight text-[rgba(31,58,95,1)] [font-family:Inter,sans-serif]">
                {{ item.title }}
              </h3>
              <p class="text-[14px] font-normal leading-6 text-[rgba(107,119,133,1)] [font-family:Inter,sans-serif]">
                {{ item.description }}
              </p>
              <a
                class="mt-auto inline-flex h-12 w-full items-center justify-center rounded-xl bg-[#37b5bd] px-6 text-[16px] font-medium text-white transition sm:hover:bg-[#2fa3aa]"
                href="#contact-form"
              >
                Подать заявку
              </a>
            </div>
          </article>
        </div>
      </div>
    </section>

    <ContactSection :preset-property-type="service?.shortTitle" />
  </div>
</template>

<style scoped>
.service-hero-banner {
  background-image: linear-gradient(90deg, rgba(15, 23, 42, 0.72) 0%, rgba(15, 23, 42, 0.46) 42%, rgba(15, 23, 42, 0.24) 100%), var(--hero-banner-desktop);
  background-size: cover;
  background-position: center;
}

@media (max-width: 639px) {
  .service-hero-banner {
    background-image: linear-gradient(90deg, rgba(15, 23, 42, 0.72) 0%, rgba(15, 23, 42, 0.46) 42%, rgba(15, 23, 42, 0.24) 100%), var(--hero-banner-mobile);
  }
}
</style>
