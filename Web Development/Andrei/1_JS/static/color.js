
const color1 = document.querySelector('#color1')
const color2 = document.querySelector('#color2')
const body = document.querySelector('body')
const text = document.querySelector('p.result')


let changeColor = function(){
  body.style.background = `linear-gradient(90deg, ${color1.value}, ${color2.value})`;
  text.innerHTML = body.style.background+';'
}

color1.addEventListener('input',changeColor)
color2.addEventListener('input',changeColor)
