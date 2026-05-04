export const config = {
  themeSetting: 'zeus' as const,
  siteInfo: {
    name: 'Hospital José María Vargas',
    shortName: 'Hospital Vargas',
    url: 'https://hospitalvargas.gob.ve',
    logo: '/logo.svg',
    address: 'Monte Carmelo a San Pirito, Esq. del Hospital, Parroquia San José, Caracas',
    phone: '(0212) 862-9965',
    email: 'hospitalvargas@gmail.com'
  },
  seo: {
    title: 'Hospital José María Vargas | Hospital Universitario Caracas',
    description: 'Segundo centro de salud más importante de Venezuela. 134 años de historia médica, 35 especialidades, 132 programas de postgrado. Patrimonio histórico de Caracas.',
    keywords: [
      'Hospital Universitario Caracas',
      'Salud Pública Venezuela',
      'Patrimonio Histórico de Caracas',
      'Hospital Vargas',
      'Medicina Pública Venezuela',
      'Emergencia 24h Caracas'
    ],
    author: 'Hospital José María Vargas',
    openGraph: {
      type: 'website',
      locale: 'es_VE',
      url: 'https://hospitalvargas.gob.ve',
      siteName: 'Hospital José María Vargas'
    }
  },
  settings: {
    language: 'es',
    dateFormat: 'DD/MM/YYYY',
    analytics: {
      enabled: false
    }
  }
};
