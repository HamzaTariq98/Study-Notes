let hideElements= function(hiddenElement){
  if (hiddenElement.style.display === "none" || hiddenElement.style.display === "") {
    hiddenElement.style.display = "block";
  } else {
    hiddenElement.style.display = "none";
  }
}


const clickMeButton = document.querySelector("#click-me");

clickMeButton.addEventListener("click", function () {
  let hiddenElements = []
  hiddenElements.push(document.querySelector("#myImage"))
  liList = document.querySelectorAll("div.container.footer ul li")
  liList.forEach(element => {
    hiddenElements.push(element)
    });

  hiddenElements.forEach(hiddenElement => {
    hideElements(hiddenElement);
  });

});


const input = document.querySelector('div.container.footer input')
const submit = document.querySelector('div.container.footer input.submit')
const ul = document.querySelector('div.container.footer ul')

submit.addEventListener("click", function(){
  const inputValue = input.value.trim(); // Trim leading/trailing spaces

  if (inputValue !== ''){
    let newLi = document.createElement('li');
    newLi.appendChild(document.createTextNode(input.value));
    ul.appendChild(newLi)
    input.value = ''
  }
})

input.addEventListener("keyup", function(event){
    const inputValue = input.value.trim(); // Trim leading/trailing spaces
    if (inputValue !== '' && event.key === "Enter"){
      let newLi = document.createElement('li');
      newLi.appendChild(document.createTextNode(input.value));
      ul.appendChild(newLi)
      input.value = ''
    }

})



myLi = document.querySelectorAll('li')
myList = []

myLi.forEach(element => {
  myList.push(element.innerText)
});

console.log(myList)