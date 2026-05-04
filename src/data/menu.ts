export const headerMenu = [
    { name: 'Inicio', link: '/' },
    { name: 'Historia', link: '/historia' },
    { 
        name: 'Servicios', 
        link: '/servicios',
        children: [
            { name: 'Servicios Médicos', link: '/servicios' },
            { name: 'Banco de Sangre', link: '/banco-de-sangre' },
            { name: 'Estadísticas', link: '/estadisticas' }
        ]
    },
    { name: 'Pregrado', link: '/pregrado' },
    { name: 'Postgrado', link: '/postgrado' },
    { name: 'Noticias', link: '/noticias' }
];

export const footerMenu = [
    { name: 'Historia', link: '/historia' },
    { name: 'Servicios', link: '/servicios' },
    { name: 'Postgrado', link: '/postgrado' },
    { name: 'Banco de Sangre', link: '/banco-de-sangre' },
    { name: 'Estadísticas', link: '/estadisticas' },
    { name: 'Noticias', link: '/noticias' }
];

export const legalMenu = [];
