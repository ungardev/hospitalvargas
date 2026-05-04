export interface Service {
    id: string;
    name: string;
    category: string;
    description: string;
    iconName: string;
}

export const serviceCategories = [
    'Clínicas',
    'Quirúrgicas',
    'Diagnóstico',
    'Apoyo Clínico',
    'Pediatría',
    'Especialidades de Adulto'
];

export const services: Service[] = [
    {
        id: 'cuidados-intensivos',
        name: 'Cuidados Intensivos',
        category: 'Clínicas',
        description: 'Unidad de terapia intensiva con equipamiento de última generación para pacientes críticos.',
        iconName: 'activity'
    },
    {
        id: 'anatomia-patologica',
        name: 'Anatomía Patológica',
        category: 'Diagnóstico',
        description: 'Diagnóstico histopatológico y citológico para diversas patologías.',
        iconName: 'microscope'
    },
    {
        id: 'anestesiologia',
        name: 'Anestesiología',
        category: 'Apoyo Clínico',
        description: 'Servicios anestésicos para procedimientos quirúrgicos de alta complejidad.',
        iconName: 'activity'
    },
    {
        id: 'cirugia-cardiovascular',
        name: 'Cirugía Cardiovascular',
        category: 'Quirúrgicas',
        description: 'Cirugías de corazón y sistema vascular con equipamiento de alta tecnología.',
        iconName: 'heart-pulse'
    },
    {
        id: 'cirugia-experimental',
        name: 'Cirugía Experimental',
        category: 'Quirúrgicas',
        description: 'Investigación y desarrollo de nuevas técnicas quirúrgicas.',
        iconName: 'flask-conical'
    },
    {
        id: 'cirugia-general',
        name: 'Cirugía General',
        category: 'Quirúrgicas',
        description: 'Cirugías generales y especializadas con equipamiento de alta tecnología incluyendo laparoscopia y broncofibroscopía.',
        iconName: 'stethoscope'
    },
    {
        id: 'cirugia-plastica',
        name: 'Cirugía Plástica',
        category: 'Quirúrgicas',
        description: 'Procedimientos de reconstructiva y estética.',
        iconName: 'activity'
    },
    {
        id: 'dermatologia',
        name: 'Dermatología',
        category: 'Clínicas',
        description: 'Diagnóstico y tratamiento de enfermedades de la piel.',
        iconName: 'activity'
    },
    {
        id: 'endocrinologia',
        name: 'Endocrinología',
        category: 'Clínicas',
        description: 'Atención en trastornos hormonales y metabólicos, incluyendo la Unidad de Diabetes.',
        iconName: 'activity'
    },
    {
        id: 'farmacia',
        name: 'Farmacia',
        category: 'Apoyo Clínico',
        description: 'Servicio de dispensación de medicamentos y orientación farmacológica.',
        iconName: 'flask-conical'
    },
    {
        id: 'hematologia',
        name: 'Hematología',
        category: 'Diagnóstico',
        description: 'Estudio de enfermedades de la sangre y trastornos hematológicos.',
        iconName: 'activity'
    },
    {
        id: 'infectologia',
        name: 'Infectología',
        category: 'Clínicas',
        description: 'Diagnóstico y tratamiento de enfermedades infecciosas.',
        iconName: 'activity'
    },
    {
        id: 'medicina-interna',
        name: 'Medicina Interna',
        category: 'Clínicas',
        description: 'Atención integral de enfermedades complejas en adultos.',
        iconName: 'stethoscope'
    },
    {
        id: 'medicina-nuclear',
        name: 'Medicina Nuclear',
        category: 'Diagnóstico',
        description: 'Estudios diagnósticos mediante radiofármacos.',
        iconName: 'activity'
    },
    {
        id: 'nefrologia',
        name: 'Nefrología',
        category: 'Clínicas',
        description: 'Tratamiento de enfermedades renales.',
        iconName: 'activity'
    },
    {
        id: 'neurocirugia',
        name: 'Neurocirugía',
        category: 'Quirúrgicas',
        description: 'Cirugías del sistema nervioso central y periférico.',
        iconName: 'activity'
    },
    {
        id: 'neurologia',
        name: 'Neurología',
        category: 'Clínicas',
        description: 'Diagnóstico y tratamiento de enfermedades del sistema nervioso.',
        iconName: 'activity'
    },
    {
        id: 'nutricion',
        name: 'Nutrición y Dietética',
        category: 'Apoyo Clínico',
        description: 'Evaluación y planificación nutricional para pacientes.',
        iconName: 'activity'
    },
    {
        id: 'orl',
        name: 'O.R.L.',
        category: 'Clínicas',
        description: 'Otorrinolaringología - enfermedades de oído, nariz y garganta.',
        iconName: 'activity'
    },
    {
        id: 'odontologia',
        name: 'Odontología',
        category: 'Clínicas',
        description: 'Salud bucodental y tratamientos odontológicos.',
        iconName: 'stethoscope'
    },
    {
        id: 'oftalmologia',
        name: 'Oftalmología',
        category: 'Clínicas',
        description: 'Diagnóstico y tratamiento de enfermedades de los ojos.',
        iconName: 'activity'
    },
    {
        id: 'oncologia',
        name: 'Oncología',
        category: 'Clínicas',
        description: 'Diagnóstico y tratamiento del cáncer.',
        iconName: 'activity'
    },
    {
        id: 'pediatria',
        name: 'Pediatría',
        category: 'Pediatría',
        description: 'Atención médica especializada para niños.',
        iconName: 'activity'
    },
    {
        id: 'psiquiatria',
        name: 'Psiquiatría',
        category: 'Clínicas',
        description: 'Salud mental y trastornos psiquiátricos.',
        iconName: 'activity'
    },
    {
        id: 'radiologia',
        name: 'Radiología y Diagnóstico por Imágenes',
        category: 'Diagnóstico',
        description: 'Estudios radiológicos, ecodoppler, ecocardiograma, eco vaginal y diagnóstico por imagen avanzado.',
        iconName: 'microscope'
    },
    {
        id: 'reumatologia',
        name: 'Reumatología',
        category: 'Clínicas',
        description: 'Enfermedades articulares y tejidos blandos.',
        iconName: 'activity'
    },
    {
        id: 'torax',
        name: 'Tórax y Neumonología',
        category: 'Clínicas',
        description: 'Enfermedades respiratorias y del tórax.',
        iconName: 'activity'
    },
    {
        id: 'traumatologia',
        name: 'Traumatología',
        category: 'Quirúrgicas',
        description: 'Tratamiento de lesiones traumáticas del sistema musculoesquelético.',
        iconName: 'activity'
    },
    {
        id: 'urologia',
        name: 'Urología',
        category: 'Quirúrgicas',
        description: 'Enfermedades del sistema urinario y genital.',
        iconName: 'activity'
    },
    {
        id: 'unidad-diabetes',
        name: 'Unidad de Diabetes',
        category: 'Clínicas',
        description: 'Centro de referencia para el manejo integral de la diabetes.',
        iconName: 'activity'
    },
    {
        id: 'unidad-dolor',
        name: 'Unidad del Dolor',
        category: 'Clínicas',
        description: 'Tratamiento especializado del dolor crónico.',
        iconName: 'activity'
    },
    {
        id: 'emergencia',
        name: 'Unidad de Emergencia',
        category: 'Clínicas',
        description: 'Servicio de emergencia permanente con 8 quirófanos equipados, sala de triaje, trauma shock, observación y unidad de terapia intermedia.',
        iconName: 'heart-pulse'
    }
];
