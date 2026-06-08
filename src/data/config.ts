export const config = {
    themeSetting: 'zeus' as const,
    siteInfo: {
        name: 'Hospital Vargas de Caracas',
        shortName: 'Hospital Vargas',
        url: 'https://hospitalvargas.gob.ve',
        logo: '/logo.svg',
        address: 'Monte Carmelo a San Pirito, Esq. del Hospital, Parroquia San José, Caracas',
        phone: '(0212) 862-9965',
        email: 'hospitalvargas@gmail.com',
    },
    seo: {
        title: 'Hospital Vargas de Caracas | Hospital Universitario Caracas',
        description:
            'Segundo centro de salud más importante de Venezuela. 134 años de historia médica, 35 especialidades, 132 programas de postgrado. Patrimonio histórico de Caracas.',
        keywords: [
            'Hospital Universitario Caracas',
            'Salud Pública Venezuela',
            'Patrimonio Histórico de Caracas',
            'Hospital Vargas',
            'Medicina Pública Venezuela',
            'Emergencia 24h Caracas',
        ],
        author: 'Hospital Vargas de Caracas',
        openGraph: {
            type: 'website',
            locale: 'es_VE',
            url: 'https://hospitalvargas.gob.ve',
            siteName: 'Hospital Vargas de Caracas',
        },
    },
    settings: {
        language: 'es',
        dateFormat: 'DD/MM/YYYY',
        analytics: {
            enabled: false,
        },
    },
};
