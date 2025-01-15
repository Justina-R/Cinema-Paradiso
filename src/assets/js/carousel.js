let index = 0;
mover(0);

function mover(n) {
  const images = document.querySelector('.carousel-images');
  const totalImages = images.children.length;

  index = (index + n + totalImages) % totalImages;
  const movement = -index * 100;
  images.style.transform = `translateX(${movement}%)`;
}