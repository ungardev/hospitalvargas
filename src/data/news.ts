export interface NewsItem {
    id: string;
    title: string;
    date: string;
    excerpt: string;
    content: string;
    category: string;
    imageUrl?: string;
}

export const newsItems: NewsItem[] = [
    {
        id: 'charla-anticonceptivos',
        title: 'Charla sobre métodos anticonceptivos hormonales',
        date: '16 de abril de 2013',
        excerpt: 'Actividad educativa sobre métodos anticonceptivos hormonales dirigida a la comunidad.',
        content: 'Son hormonas sintéticas que inhiben la ovulación y espesan el moco cervical para impedir el paso de los espermatozoides. Son de uso exclusivo para la mujer y para ello es necesario realizar una consulta médica que oriente acerca de cuál es el método más adecuado para cada organismo. No Previenen de las infecciones de transmisión sexual.',
        category: 'Educación'
    },
    {
        id: 'obesidad-venezuela',
        title: 'En Venezuela, 65,2% de la población mayor de 15 años tiene sobrepeso',
        date: 'Julio 2013',
        excerpt: 'El país ocupa el vigésimo cuarto lugar mundial por cantidad de obesos según la OMS.',
        content: 'En el ranking mundial ocupa el vigésimo cuarto lugar por cantidad de obesos, de acuerdo con el informe más reciente de la Organización Mundial de la Salud (OMS). De esa cifra, 13,5% son menores de 15 años.',
        category: 'Salud Pública'
    },
    {
        id: 'convenio-china',
        title: 'Nuevos equipos médicos gracias al Convenio China-Venezuela',
        date: '2013',
        excerpt: 'Equipamiento de alta tecnología para diagnóstico avanzado.',
        content: 'Gracias a los convenios China-Venezuela se han adquirido equipos de alta tecnología como laparoscopia, broncofibroscopía, eco doppler, eco vaginal y ecocardiograma.',
        category: 'Tecnología'
    },
    {
        id: 'hospital-122-anos',
        title: 'Hospital Vargas cumple 122 años',
        date: '24 de mayo de 2013',
        excerpt: 'Celebración del 122 aniversario del centro de salud más importante del país.',
        content: 'Considerado el segundo centro de salud más importante del país, este nosocomio tiene un área de influencia de 400 mil habitantes y ofrece servicios de endocrinología, neumonología, medicina interna, ginecología, cardiología, radiología, pediatría, neurología, laboratorio y rayos X.',
        category: 'Institución'
    },
    {
        id: 'banco-sangre',
        title: 'Banco Municipal de Sangre: Salvando vidas',
        date: '2013',
        excerpt: 'Centro de referencia nacional para la donación de sangre.',
        content: 'El Banco Municipal de Sangre del Hospital Vargas es un centro de referencia nacional que garantiza la disponibilidad de sangre segura para todos los pacientes que lo requieran.',
        category: 'Servicios'
    }
];

export const newsCategories = [
    'Todos',
    'Educación',
    'Salud Pública',
    'Tecnología',
    'Institución',
    'Servicios'
];
