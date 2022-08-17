document.addEventListener('DOMContentLoaded', function() {
const swiper = new Swiper('.object-gallery', {
  // Optional parameters
//  direction: 'vertical',
//  loop: true,

  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
    clickable:true,
    dynamicBullets: true,
   
  },
  effect:'flip',
  speed:600,
  loop: true,
  grabCursor:true,

        mousewheel:{
          eventTarget:".object-gallery",
        },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  // And if we need scrollbar
  scrollbar: {
    el: '.swiper-scrollbar',
  },
});
});