// Função para criar um gráfico de barras
function createBarChart(labels, data) {
    const ctx = document.getElementById('barChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Bar Chart',
                data: data,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Função para criar um gráfico de pizza
function createPieChart(labels, data) {
    const ctx = document.getElementById('pieChart').getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                label: 'Pie Chart',
                data: data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        }
    });
}

// Função para criar um gráfico de linha
function createLineChart(labels, dataSets) {
    const ctx = document.getElementById('lineChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: dataSets.map((dataSet) => ({
                label: dataSet.label,
                data: dataSet.data,
                borderColor: dataSet.borderColor || 'rgba(75, 192, 192, 1)',
                backgroundColor: dataSet.backgroundColor || 'rgba(75, 192, 192, 0.2)',
                fill: false
            }))
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Função para mostrar o slide com base no índice
function showSlide(index) {
    const slides = document.querySelectorAll('.slide');
    slides.forEach((slide, i) => {
        slide.classList.toggle('hidden', i !== index);
    });
}

// Variável para rastrear o slide atual
let currentSlide = 0;

// Função para avançar para o próximo slide
function nextSlide(event) {
    event.preventDefault(); // Impede o comportamento padrão do evento
    const slides = document.querySelectorAll('.slide');
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

// Função para voltar ao slide anterior
function prevSlide(event) {
    event.preventDefault(); // Impede o comportamento padrão do evento
    const slides = document.querySelectorAll('.slide');
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
}

// Inicializa Interact.js para elementos redimensionáveis e arrastáveis
interact('.resize-drag')
  .draggable({
    onmove: dragMoveListener,
  })
  .resizable({
    edges: { left: true, right: true, bottom: true, top: true },
    listeners: {
      move(event) {
        let { x, y } = event.target.dataset;

        x = (parseFloat(x) || 0) + event.deltaRect.left;
        y = (parseFloat(y) || 0) + event.deltaRect.top;

        Object.assign(event.target.style, {
          width: `${event.rect.width}px`,
          height: `${event.rect.height}px`,
          transform: `translate(${x}px, ${y}px)`,
        });

        Object.assign(event.target.dataset, { x, y });
      },
    },
    modifiers: [
      interact.modifiers.restrictEdges({
        outer: 'parent',
      }),
      interact.modifiers.restrictSize({
        min: { width: 100, height: 50 },
        max: { width: '100%', height: '100%' },
      }),
    ],
    inertia: true,
  });

// Função de callback para movimentar os elementos
function dragMoveListener(event) {
  let { x, y } = event.target.dataset;

  x = (parseFloat(x) || 0) + event.dx;
  y = (parseFloat(y) || 0) + event.dy;

  event.target.style.transform = `translate(${x}px, ${y}px)`;

  Object.assign(event.target.dataset, { x, y });
}
