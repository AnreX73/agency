

document.addEventListener('DOMContentLoaded', function() {
const swiper = new Swiper('.object-gallery', {
  // Optional parameters
//  direction: 'vertical',

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

});

document.addEventListener('DOMContentLoaded', function() {

const tabLinks = document.querySelectorAll('.logo-and-title');
const tabsContent = document.querySelectorAll('.apartments-container');

tabLinks.forEach(function(item){
  item.addEventListener('click',function(){
    currentTab = item;
    tabId = currentTab.getAttribute('data-tab');
    currentTabContent = document.querySelector(tabId)
    if ( ! currentTab.classList.contains('active')) {
      tabLinks.forEach(function(item){
        item .classList.remove('active');
      });
        tabsContent.forEach(function(item){
        item .classList.remove('active');
      });
         currentTab.classList.add('active');
         currentTabContent.classList.add('active')
      
    }

   
  });
});
// const navLinks = document.querySelectorAll('nav li ul li')

// navLinks.forEach(function(item){
//   item.addEventListener('click',function(){
    
//     currentLink = item;
//     linkName = currentLink.getAttribute('data-link');
//     linkId = '#' + linkName;
   
//     currentLinkContent = document.querySelector(linkId);
//     console.log(currentLinkContent);
  
    
   
    
//   })
// })


});