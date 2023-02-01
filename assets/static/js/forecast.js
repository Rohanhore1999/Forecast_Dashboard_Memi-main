let ctx = document.getElementById("chart2").getContext("2d");

console.log(JSON.parse(`{{datasets|escapejs}}`));
var config = {
  type: "line",
  data: {
    labels: JSON.parse(`{{labels}}`),
    datasets: JSON.parse(`{{datasets|escapejs}}`),
  },
  options: {
    maintainAspectRatio: false,
    responsive: true,
    legend: {
      position: "top",
    },
    title: {
      position: "top",
      display: true,
    },
    tooltips: {
      mode: "index",
      intersect: false,
    },
    hover: {
      mode: "nearest",
      intersect: true,
    },
    elements: {
      point: {
        radius: 0,
        hoverRadius: 0,
      },
    },

    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
};

new Chart(ctx, config);
