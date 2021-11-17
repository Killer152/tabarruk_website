const swiper = new Swiper('.swiper', {
  // Optional parameters
  // direction: 'vertical',
  loop: true,
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: "auto",
  coverflowEffect: {
    rotate: 50,
    stretch: 0,
    depth: 100,
    modifier: 1,
    slideShadows: true,
  },
  pagination: {
    el: ".swiper-pagination",
  },
  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  slidesPerView: 3,


});


let headerMenu = document.querySelector('.header__menu')
let navList = document.querySelector('.nav__card-list')
let headerMenuLine = document.querySelector('.header__menu-line')

headerMenu.addEventListener('click', () => {
  // if (navList.classList.has(".active")) {
  //   navList.classList.remove(".active")
  // }
  // else{
  //   navList.classList.add(".active")
  // }
  navList.classList.toggle("active")
  headerMenuLine.classList.toggle("active1")

})

let btns = document.querySelectorAll(".link_wrapper-a")
let form = document.querySelector(".form")

for (let i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function (e) {
    e.preventDefault()
    form.classList.add("active")
  })
}

form.addEventListener("click", function (e) {
  if (e.target === e.currentTarget) {
    form.classList.remove("active")
  }
})
let formClose = document.querySelector(".form__close")
formClose.addEventListener("click", function (e) {
    form.classList.remove("active")
})
