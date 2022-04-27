import { bs } from './modules/bsComponents.js'
import { shadow } from './modules/shadow.js'
import { wowAnimate } from './modules/wowAnimate.js'
import { scroll } from './modules/scroll.js'
import { naverMap } from './modules/naverMap.js'

// dogimg에서 그림자 효과
bs()
if (document.querySelector('#shadow-box')) {
  shadow()
}

if (document.querySelector('.wow')) {
  wowAnimate()
}

if (document.querySelector('#scrolltoTop')) {
  scroll()
}

if (document.querySelector('#map')) {
  naverMap()
}


const slickSlide = jQuery('#slick-slide')

if (slickSlide) {
  slickSlide.slick({
    dots: true,
    arrows: false,
    slidesToShow: 3,
    slideToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
    responsive: [{
        breakpoint: 768,
        settings: {
          slidesToShow: 2
        }
      },
      {
        breakpoint: 576,
        settings: {
          slidesToShow: 1
        }
      }
    ]
  })
}


var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

const mapDiv = document.querySelector('#map')
const options = {
  center: new daum.maps.LatLng(37.57599184507025, 126.9769613271878),
  scrollwheel: false,
  level: 3
}
const imageSrc = '/static/img/logo.png'
const imageSize = new kakao.maps.Size(48, 48)

const marker = new daum.maps.Marker({
  image: new kakao.maps.MarkerImage(imageSrc, imageSize),
  position: new daum.maps.LatLng(37.57599184507025, 126.9769613271878)
})

const map = new daum.maps.Map(mapDiv, options)
marker.setMap(map)


