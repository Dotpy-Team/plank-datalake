document.getElementById('open_btn').addEventListener('click', function () {
  const sidebar = document.getElementById('sidebar');
  const searchButton = document.querySelector('.search-button');
  
  sidebar.classList.toggle('open-sidebar');

  searchButton.classList.toggle('expanded');
});

document.addEventListener('DOMContentLoaded', function() {
  const items = document.querySelectorAll('.side-item');

  items.forEach(item => {
      const icon = item.querySelector('.icon');
      const originalSrc = icon.src; // Armazena o src original
      const hoverSrc = icon.getAttribute('data-hover-src'); // Obtém o src de hover do atributo data

      item.addEventListener('mouseover', function() {
          icon.src = hoverSrc; // Troca para a imagem de hover
      });

      item.addEventListener('mouseout', function() {
          icon.src = originalSrc; // Volta para a imagem original
      });
  });
});
