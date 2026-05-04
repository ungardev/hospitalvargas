export interface BloodBankInfo {
    name: string;
    description: string;
    mission: string;
}

export interface DonationRequirement {
    id: number;
    text: string;
}

export interface BloodType {
    type: string;
    compatible: string;
}

export const bloodBankInfo: BloodBankInfo = {
    name: 'Banco Municipal de Sangre del Hospital Vargas',
    description: 'Centro de referencia nacional para la donación y transfusion de sangre. Fundado como parte del compromiso del hospital con la salud de los venezolanos.',
    mission: 'Garantizar la disponibilidad de sangre segura y hemoderivados para todos los pacientes que lo requieran, promoviendo la donación voluntaria.'
};

export const donationRequirements: DonationRequirement[] = [
    { id: 1, text: 'Tener entre 18 y 65 años de edad' },
    { id: 2, text: 'Pesar más de 50 kilogramos' },
    { id: 3, text: 'Estar en buen estado de salud general' },
    { id: 4, text: 'No haber consumido alcohol en las últimas 24 horas' },
    { id: 5, text: 'No haber tomado medicamentos en los últimos 7 días' },
    { id: 6, text: 'No haberse realizado tatuajes o piercings en el último año' },
    { id: 7, text: 'No haber tenido relaciones sexuales de riesgo recientemente' },
    { id: 8, text: 'Apresentarse con identificación y en ayunas (mínimo 4 horas)' }
];

export const bloodTypes: BloodType[] = [
    { type: 'O-', compatible: 'Todos (Donante universal)' },
    { type: 'O+', compatible: 'O+, A+, B+, AB+' },
    { type: 'A-', compatible: 'A-, AB-' },
    { type: 'A+', compatible: 'A+, AB+' },
    { type: 'B-', compatible: 'B-, AB-' },
    { type: 'B+', compatible: 'B+, AB+' },
    { type: 'AB-', compatible: 'AB-' },
    { type: 'AB+', compatible: 'AB+ (Receptor universal)' }
];

export const schedule = {
    donation: {
        days: 'Lunes a Viernes',
        hours: '7:00 AM - 10:00 AM',
        note: 'Sábados de 7:00 AM a 9:00 AM'
    },
    specialDonations: {
        days: 'Con cita previa',
        hours: '24 horas para casos de emergencia',
        note: 'Para donaciones especiales, llamar al número del hospital'
    }
};

export const contactInfo = {
    phone: '(0212) 862-9965',
    extension: '1245',
    email: 'bancosangre@hospitalvargas.gob.ve'
};
