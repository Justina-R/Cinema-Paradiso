const hamburger = document.querySelector('.hamburger');
const mobileNav = document.querySelector('.mobile-nav');
const menuItems = document.querySelectorAll('.mobile-nav li');

hamburger.addEventListener('click', () => {
  mobileNav.classList.toggle('hidden');
});

menuItems.forEach(item => {
  item.addEventListener('click', () => {
    mobileNav.classList.add('hidden');
  });
});