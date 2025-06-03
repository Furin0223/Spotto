const carousel = document.getElementById('carousel');
const nextBtn = document.getElementById('nextBtn');
const prevBtn = document.getElementById('prevBtn');

const itemWidth = 300;

nextBtn.addEventListener('click', () => {
  carousel.scrollBy({ left: itemWidth, behavior: 'smooth' });
});

prevBtn.addEventListener('click', () => {
  carousel.scrollBy({ left: -itemWidth, behavior: 'smooth' });
});
