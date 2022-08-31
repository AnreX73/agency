/* библиотека для закрытия модальных окон без гемора*/
!function(e){"function"!=typeof e.matches&&(e.matches=e.msMatchesSelector||e.mozMatchesSelector||e.webkitMatchesSelector||function(e){for(var t=this,o=(t.document||t.ownerDocument).querySelectorAll(e),n=0;o[n]&&o[n]!==t;)++n;return Boolean(o[n])}),"function"!=typeof e.closest&&(e.closest=function(e){for(var t=this;t&&1===t.nodeType;){if(t.matches(e))return t;t=t.parentNode}return null})}(window.Element.prototype);

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
  speed:1000,
  loop: true,
  grabCursor:true,

        // mousewheel:{
        //   eventTarget:".object-gallery",
        // },

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

openDropNav = document.querySelectorAll('.header-nav-item');
dropNav = document.querySelectorAll('.header-open-nav');

openDropNav.forEach(function(item){
  /* Назначаем каждой ссылке обработчик клика */
  item.addEventListener('mouseover', function(e) {
      e.preventDefault();
      /* ищем подменю по атрибуту ссылки */
      var openDrop = this.getAttribute('data-open');

      navWindow = document.querySelector('.header-open-nav[data-open ="' + openDrop + '"]');
      navWindow.classList.add('active');
   });

  });

dropNav.forEach(function(item){
  /* Назначаем каждой ссылке обработчик клика */
  item.addEventListener('mouseout', function(e) {
      // e.preventDefault();
      /* ищем подменю по атрибуту ссылки */
      // var openDrop = this.getAttribute('data-open');

      // navWindow = document.querySelector('.header-open-nav[data-open ="' + openDrop + '"]');
      var parentModal = this.closest('.header-open-nav');
             parentModal.classList.remove('active');
   });

  });


});