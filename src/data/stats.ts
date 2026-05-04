export interface Stat {
    value: string | number;
    label: string;
    prefix?: string;
    suffix?: string;
}

export interface StatsList {
    id: string;
    stats: Stat[];
}

export const statsLists: Record<string, StatsList> = {
    main: {
        id: 'main',
        stats: [
            {
                value: '134',
                label: 'Años de Historia',
            },
            {
                value: '35',
                label: 'Especialidades Médicas',
                suffix: '+'
            },
            {
                value: '132',
                label: 'Programas de Postgrado',
            }
        ]
    }
};
