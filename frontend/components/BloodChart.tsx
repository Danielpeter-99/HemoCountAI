import { Doughnut } from 'react-chartjs-2';
import { Chart, ArcElement, CategoryScale, Title, Tooltip } from 'chart.js';

Chart.register(ArcElement, CategoryScale, Title, Tooltip);


function BloodChart({ bloodData }: { bloodData: Record<string, number> }) {
    // const bloodData = {
    //     'blood': 84,
    //     'eosinophils': 2,
    //     'red': 82,
    // }

    const data = {
        labels: Object.keys(bloodData),
        datasets: [{
            data: Object.values(bloodData),
            backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)'],
            borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)'],
            borderWibloodDatah: 1,
        }],
    };

    return (
        <div className="flex flex-col items-center justify-center p-24">
        <Doughnut
            data={data}
            // ...props
        />
        </div>
    )
}

export default BloodChart;