import { Doughnut } from 'react-chartjs-2';
import { Chart, ArcElement, CategoryScale, Title, Tooltip, Legend } from 'chart.js';

Chart.register(ArcElement, CategoryScale, Title, Tooltip, Legend);

function BloodChart({ bloodData }: { bloodData: Record<string, number> }) {
    
    const capitalizeFirstLetter = (str: string) => {
        return str.charAt(0).toUpperCase() + str.slice(1);
    };

    const data = {
        labels: Object.keys(bloodData).map((key) => capitalizeFirstLetter(key)),
        datasets: [{
            data: Object.values(bloodData),
            backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)'],
            borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)'],
            borderWidth: 1,
        }],
    };

    return (
        <Doughnut
            className="flex flex-col items-center justify-center p-24"
            data={data}
            options={{
                plugins: {
                    legend: {
                        display: true,
                        position: 'top',
                    },
                },
                aspectRatio: 1, // Adjust the value to make the chart smaller or larger
            }}
        />
    )
}

export default BloodChart;