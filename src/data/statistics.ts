export interface Statistic {
    id: string;
    title: string;
    value: string;
    description: string;
}

export interface ExternalLink {
    name: string;
    url: string;
}

export const hospitalStatistics: Statistic[] = [
    {
        id: 'vih',
        title: 'Pacientes con VIH',
        value: 'En atención',
        description: 'Seguimiento y tratamiento antiretroviral'
    },
    {
        id: 'diabetes',
        title: 'Diabetes Tipo 2',
        value: 'En tratamiento',
        description: 'Control metabólico y complicaciones'
    },
    {
        id: 'hipertension',
        title: 'Hipertensión',
        value: 'Casos registrados',
        description: 'Monitorización y manejo clínico'
    }
];

export const bulletins: ExternalLink[] = [
    {
        name: 'Alerta Epidemiológica - MPPS',
        url: 'http://www.mpps.gob.ve'
    },
    {
        name: 'Anuario Epidemiológico',
        url: 'http://www.mpps.gob.ve'
    }
];

export const performanceIndicators = {
    emergencyResponse: '< 30 minutos',
    labResults: '24-48 horas',
    imagingResults: '48-72 horas',
    bedOccupancy: '85%',
    patientSatisfaction: '92%'
};
