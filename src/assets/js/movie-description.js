const cards = document.querySelectorAll('.card');

// Does the card in the parameter contain the class "highlight"?
function checkIfHighlighted(card) {
  return card.classList.contains('highlight');
}

// If the user clicks on the card and it is in the front, the description will appear
cards.forEach(card => {
  card.addEventListener('click', () => {
    if (checkIfHighlighted(card)) {
      card.classList.toggle('show-description');
    }
  });
});

// If any of the cards is no longer in the front, the description will disappear
function updateDescriptions() {
  cards.forEach(card => {
    if (!checkIfHighlighted(card)) {
      card.classList.remove('show-description');
    }
  });
}

// Llamar a la función cada vez que el estado del carrusel cambie (cuando la clase 'highlight' se cambie)
setInterval(updateDescriptions, 100); // Actualiza cada 100 ms (ajusta según sea necesario)
