export interface HistoryEvent {
    year: string;
    title: string;
    description: string;
}

export interface FounderInfo {
    name: string;
    title: string;
    bio: string;
    imageUrl?: string;
}

export const founderInfo: FounderInfo = {
    name: 'Dr. José María Vargas',
    title: 'Médico y Educador Venezolano',
    bio: 'El Hospital José María Vargas lleva su nombre en honor al ilustre médico venezolano del cual lleva su nombre. Fue un reconocido médico y educador que sentó las bases para una medicina pública, accesible y de calidad en Venezuela.',
    imageUrl: ''
};

export const historicalTimeline: HistoryEvent[] = [
    {
        year: '1891',
        title: 'Fundación del Hospital',
        description: 'El Hospital José María Vargas fue fundado en la ciudad de Caracas el 5 de julio de 1891.'
    },
    {
        year: '1895',
        title: 'Inicio de la Enseñanza Médica',
        description: 'Un grupo de jóvenes médicos liderizados por Luis Razetti y Santos Dominici, constituyen la "Generación Renovadora", bajo la influencia de la Escuela Francesa, reformando profundamente los estudios médicos y el ejercicio de la medicina.'
    },
    {
        year: '1959',
        title: 'Cesión del Local',
        description: 'La Facultad cede el antiguo local del Instituto Anatómico de San Lorenzo, en la plaza del mismo nombre, construido sobre el cementerio de La Merced e inaugurado por Luis Razetti en 1911.'
    },
    {
        year: '1960',
        title: 'Apertura del Primer Curso',
        description: 'El 1º de Noviembre de 1960 se abrió el Primer Curso en la Nueva Escuela, aún sin edificio, con los locales improvisados en el Hospital Vargas. En la Morgue funcionaba la sala de disección.'
    },
    {
        year: '1961',
        title: 'Solicitud Formal',
        description: 'El Decano, durante la conmemoración de los 70 años del Hospital Vargas, informó que había solicitado la creación de la nueva Escuela ante el Consejo Universitario.'
    },
    {
        year: '1962',
        title: 'Conclusión del Edificio',
        description: 'Se concluyó el edificio de la Escuela Vargas, albergando durante el año lectivo 1962-1963 los 3 primeros años de la carrera. La promoción Ricardo Archila (62-68) fue la que comenzó sus estudios en este edificio.'
    },
    {
        year: '1965',
        title: 'Aprobación Oficial',
        description: 'El informe aprobatorio del Consejo Nacional de Universidades (CNU) se recibió 4 años después de la solicitud (agosto, 1965), oficializando la creación de la Escuela.'
    },
    {
        year: '1967',
        title: 'Terremoto del 29 de Julio',
        description: 'El terremoto ocasionó fuertes deterioros en el recién construido edificio: grietas en fachadas y paredes internas, columnas de carga dañadas. Las reparaciones comenzaron tres meses después.'
    },
    {
        year: '1981-1988',
        title: 'Reparaciones Post-Terremoto',
        description: 'Se realizaron trabajos de inyección de resinas epóxicas en las grietas (1981) y el apantallamiento y rigidización de la estructura (1985 y 1988), incluyendo la construcción de pantallas laterales de concreto.'
    },
    {
        year: '1988',
        title: 'Regreso al Edificio',
        description: 'El regreso de las Cátedras al Edificio se hizo en forma progresiva finalizando en septiembre de 1988.'
    },
    {
        year: 'Actualidad',
        title: 'Centro de Referencia Nacional',
        description: 'El Hospital Vargas es el segundo centro de salud más importante del Ministerio del Poder Popular para la Salud (MPPS), después del Hospital Universitario de Caracas, con un área de influencia de más de 400 mil habitantes.'
    }
];

export const keyFigures = [
    {
        name: 'Dr. José María Vargas',
        role: 'Eponímous - Médico Ilustre',
        description: 'En honor al cual lleva su nombre el hospital.'
    },
    {
        name: 'Dr. Luis Razetti',
        role: 'Líder de la Generación Renovadora',
        description: 'Junto con Santos Dominici, liderizó la reforma de los estudios médicos.'
    },
    {
        name: 'Dr. Francisco Montbrun',
        role: 'Impulsor de la Escuela',
        description: 'Decidido a mantener la tradición docente del Hospital Vargas.'
    },
    {
        name: 'Dra. Jacinto Convit',
        role: 'Médico Distinguido',
        description: 'Miembro del grupo de profesores que mantuvo la tradición docente.'
    }
];

export const hospitalStats = {
    founded: '1891',
    yearsOfHistory: '134',
    bedCapacity: '400',
    influenceArea: '400 mil habitantes',
    specialties: '35+',
    postgradPrograms: '132'
};
