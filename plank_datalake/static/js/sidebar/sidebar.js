document.getElementById('open_btn').addEventListener('click', function () {
  const sidebar = document.getElementById('sidebar');
  const searchButton = document.querySelector('.search-button');
  
  sidebar.classList.toggle('open-sidebar');

  searchButton.classList.toggle('expanded');
});