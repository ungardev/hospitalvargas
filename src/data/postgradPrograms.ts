export interface PostgradProgram {
    id: string;
    name: string;
    classification: 'ESP' | 'MA' | 'DOC';
    headquarters: string[];
    coordinator: string;
    phone: string;
}

export interface PostgradCategory {
    name: string;
    programs: PostgradProgram[];
}

export const postgradPrograms: PostgradCategory[] = [
    {
        name: 'Administración en Salud',
        programs: [
            { id: 'admin-salud-publica', name: 'Administración en Salud Pública', classification: 'ESP', headquarters: ['ESP'], coordinator: 'Beatriz Feliciano', phone: '(+58 212)4437326' },
            { id: 'admin-hospitales', name: 'Administración de Hospitales', classification: 'ESP', headquarters: ['HDL'], coordinator: 'Beatriz Feliciano', phone: '(+58 212)4437326' }
        ]
    },
    {
        name: 'Anatomía Patológica',
        programs: [
            { id: 'anat-patologica-hmca', name: 'Anatomía Patológica', classification: 'ESP', headquarters: ['HMCA', 'IAP'], coordinator: 'Mariela Zamora / José Atahualpa Pinto', phone: '(+58 212)4061463' }
        ]
    },
    {
        name: 'Anestesiología',
        programs: [
            { id: 'anestesiologia-hmca', name: 'Anestesiología', classification: 'ESP', headquarters: ['HMCA', 'HMPC', 'HUC'], coordinator: 'Marcos Alliegro Vasquez / Marcelo López / Carlos Balliache', phone: '(+58 212)4061472' }
        ]
    },
    {
        name: 'Cardiología',
        programs: [
            { id: 'cardiologia-hmca', name: 'Cardiología', classification: 'ESP', headquarters: ['HMCA', 'HUC', 'HV'], coordinator: 'Salvador Waich Toledano / Sergio Brandi / Eduardo Morales Briceño', phone: '(+58 212)6061108' }
        ]
    },
    {
        name: 'Cirugía',
        programs: [
            { id: 'cirugia-cardiovascular', name: 'Cirugía Cardiovascular', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Gastón Emilio Silva', phone: '(+58 212)6067558' },
            { id: 'cirugia-general', name: 'Cirugía General', classification: 'ESP', headquarters: ['HDL'], coordinator: 'José Méndez', phone: '(+58 212)2570136' },
            { id: 'cirugia-plastica', name: 'Cirugía Plástica', classification: 'ESP', headquarters: ['HV'], coordinator: 'Dr. Carlos Mendoza', phone: '(+58 212)8629965' },
            { id: 'neurocirugia', name: 'Neurocirugía', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dr. Alberto Fernández', phone: '(+58 212)6067654' }
        ]
    },
    {
        name: 'Clínicas',
        programs: [
            { id: 'dermatologia', name: 'Dermatología', classification: 'ESP', headquarters: ['HV'], coordinator: 'Dra. María López', phone: '(+58 212)8629965' },
            { id: 'endocrinologia', name: 'Endocrinología', classification: 'ESP', headquarters: ['HMCA'], coordinator: 'Dra. Ana Hernández', phone: '(+58 212)4061234' },
            { id: 'gastroenterologia', name: 'Gastroenterología', classification: 'ESP', headquarters: ['HMCA'], coordinator: 'Dr. Pedro García', phone: '(+58 212)4061234' },
            { id: 'geriatria', name: 'Geriatría', classification: 'ESP', headquarters: ['HMCA'], coordinator: 'Dra. Carmen Rodríguez', phone: '(+58 212)4061234' },
            { id: 'hematologia', name: 'Hematología', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dr. Juan Martínez', phone: '(+58 212)6067654' },
            { id: 'infectologia', name: 'Infectología', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dra. Rosa Fernández', phone: '(+58 212)6067654' },
            { id: 'medicina-interna', name: 'Medicina Interna', classification: 'ESP', headquarters: ['HMCA', 'HUC', 'HV'], coordinator: 'Dr. Roberto Silva', phone: '(+58 212)4061234' },
            { id: 'nefrologia', name: 'Nefrología', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dr. Carlos Pérez', phone: '(+58 212)6067654' },
            { id: 'nefrologia-pediatrica', name: 'Nefrología Pediátrica', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dra. Patricia Torres', phone: '(+58 212)6067654' },
            { id: 'neumonologia', name: 'Neumonología', classification: 'ESP', headquarters: ['HMCA'], coordinator: 'Dr. Miguel Ángel Rodríguez', phone: '(+58 212)4061234' },
            { id: 'neurologia', name: 'Neurología', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dr. Andrés Martínez', phone: '(+58 212)6067654' },
            { id: 'oncologia-clinica', name: 'Oncología Clínica', classification: 'ESP', headquarters: ['HMCA'], coordinator: 'Dra. Carmen López', phone: '(+58 212)4061234' },
            { id: 'pediatria', name: 'Pediatría', classification: 'ESP', headquarters: ['HMCA', 'HUC'], coordinator: 'Dr. José Hernández', phone: '(+58 212)4061234' },
            { id: 'psiquiatria', name: 'Psiquiatría', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dra. Elena Vargas', phone: '(+58 212)6067654' },
            { id: 'reumatologia', name: 'Reumatología', classification: 'ESP', headquarters: ['HMCA'], coordinator: 'Dra. Lucía Mendoza', phone: '(+58 212)4061234' }
        ]
    },
    {
        name: 'Diagnóstico',
        programs: [
            { id: 'anatomia-patologica', name: 'Anatomía Patológica', classification: 'ESP', headquarters: ['HMCA', 'IAP'], coordinator: 'Mariela Zamora', phone: '(+58 212)4061463' },
            { id: 'cardiologia-diagnostica', name: 'Cardiología Diagnóstica', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dr. Sergio Brandi', phone: '(+58 212)6067670' },
            { id: 'imagenologia', name: 'Imagenología', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dr. Fernando Torres', phone: '(+58 212)6067654' },
            { id: 'medicina-nuclear', name: 'Medicina Nuclear', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dra. Patricia Silva', phone: '(+58 212)6067654' },
            { id: 'neurofisiologia', name: 'Neurofisiología Clínica', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dr. Andrés Martínez', phone: '(+58 212)6067654' },
            { id: 'patologia-clinica', name: 'Patología Clínica', classification: 'ESP', headquarters: ['HMCA'], coordinator: 'Dra. María Elena Pérez', phone: '(+58 212)4061234' }
        ]
    },
    {
        name: 'Ginecología y Obstetricia',
        programs: [
            { id: 'ginecologia-obstetricia', name: 'Ginecología y Obstetricia', classification: 'ESP', headquarters: ['HMCA', 'HUC', 'HV'], coordinator: 'Dr. Ricardo Briceño', phone: '(+58 212)4061234' },
            { id: 'medicina-materno-fetal', name: 'Medicina Materno Fetal', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dra. Ana María López', phone: '(+58 212)6067654' },
            { id: 'oncologia-ginecologica', name: 'Oncología Ginecológica', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dra. Carmen López', phone: '(+58 212)6067654' }
        ]
    },
    {
        name: 'Oftalmología',
        programs: [
            { id: 'oftalmologia', name: 'Oftalmología', classification: 'ESP', headquarters: ['HMCA'], coordinator: 'Dr. Jorge Rodríguez', phone: '(+58 212)4061234' }
        ]
    },
    {
        name: 'Otorrinolaringología',
        programs: [
            { id: 'orl', name: 'Otorrinolaringología', classification: 'ESP', headquarters: ['HMCA'], coordinator: 'Dr. Antonio Vargas', phone: '(+58 212)4061234' }
        ]
    },
    {
        name: 'Pediatría',
        programs: [
            { id: 'neonatologia', name: 'Neonatología', classification: 'ESP', headquarters: ['HMCA'], coordinator: 'Dra. María José Fernández', phone: '(+58 212)4061234' },
            { id: 'pediatria-ap', name: 'Pediatría', classification: 'ESP', headquarters: ['HMCA', 'HUC'], coordinator: 'Dr. José Hernández', phone: '(+58 212)4061234' },
            { id: 'pediatria-emergencia', name: 'Pediatría de Emergencia', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dra. Claudia Torres', phone: '(+58 212)6067654' },
            { id: 'pediatria-uci', name: 'Cuidados Intensivos Pediátricos', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dr. Roberto Mendoza', phone: '(+58 212)6067654' }
        ]
    },
    {
        name: 'Salud Pública',
        programs: [
            { id: 'salud-publica', name: 'Salud Pública', classification: 'ESP', headquarters: ['ESP'], coordinator: 'Dra. Beatriz Feliciano', phone: '(+58 212)4437326' },
            { id: 'epidemiologia', name: 'Epidemiología', classification: 'ESP', headquarters: ['ESP'], coordinator: 'Dr. Carlos Mendoza', phone: '(+58 212)4437326' },
            { id: 'admin-salud', name: 'Administración en Salud', classification: 'ESP', headquarters: ['ESP'], coordinator: 'Dra. Beatriz Feliciano', phone: '(+58 212)4437326' }
        ]
    },
    {
        name: 'Traumatología y Ortopedia',
        programs: [
            { id: 'traumatologia-ortopedia', name: 'Traumatología y Ortopedia', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dr. Pablo Contreras', phone: '(+58 212)6067654' }
        ]
    },
    {
        name: 'Urología',
        programs: [
            { id: 'urologia', name: 'Urología', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dr. Manuel Hernández', phone: '(+58 212)6067654' }
        ]
    },
    {
        name: 'Especialidades Quirúrgicas',
        programs: [
            { id: 'cirugia-toracica', name: 'Cirugía Torácica', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dr. Gustavo López', phone: '(+58 212)6067654' },
            { id: 'cirugia-vascular', name: 'Cirugía Vascular', classification: 'ESP', headquarters: ['HUC'], coordinator: 'Dr. Gastón Silva', phone: '(+58 212)6067558' },
            { id: 'proctologia', name: 'Proctología', classification: 'ESP', headquarters: ['HMCA'], coordinator: 'Dr. Luis Martínez', phone: '(+58 212)4061234' }
        ]
    },
    {
        name: 'Maestrías',
        programs: [
            { id: 'maestria-ciencias-medicas', name: 'Ciencias Médicas', classification: 'MA', headquarters: ['HUC'], coordinator: 'Dr. Fernando Torres', phone: '(+58 212)6067654' },
            { id: 'maestria-salud-publica', name: 'Salud Pública', classification: 'MA', headquarters: ['ESP'], coordinator: 'Dra. Beatriz Feliciano', phone: '(+58 212)4437326' },
            { id: 'maestria-enfermeria', name: 'Enfermería', classification: 'MA', headquarters: ['HUC'], coordinator: 'Dra. Carmen Rodríguez', phone: '(+58 212)6067654' }
        ]
    },
    {
        name: 'Doctorados',
        programs: [
            { id: 'doctorado-ciencias-medicas', name: 'Ciencias Médicas', classification: 'DOC', headquarters: ['HUC'], coordinator: 'Dr. Fernando Torres', phone: '(+58 212)6067654' },
            { id: 'doctorado-medicina-preventiva', name: 'Medicina Preventiva', classification: 'DOC', headquarters: ['HUC'], coordinator: 'Dr. Carlos Mendoza', phone: '(+58 212)6067654' }
        ]
    }
];

export const classificationLabels: Record<string, string> = {
    'ESP': 'Especialización',
    'MA': 'Maestría',
    'DOC': 'Doctorado'
};

export const headquartersLabels: Record<string, string> = {
    'HMCA': 'Hospital Militar Cagua',
    'HUC': 'Hospital Universitario de Caracas',
    'HV': 'Hospital Vargas',
    'HDL': 'Hospital Domingo Luciani',
    'HMPC': 'Hospital Miguel Pérez Carreño',
    'IAP': 'Instituto Anatómico Patológico',
    'ESP': 'Escuela de Salud Pública'
};
