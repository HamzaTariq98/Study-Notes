// var students = ['hamza','ahmad','fadi']


// value = students.length
// for (var x = 0; x<value; x++){
//     console.log(students[x],students.length)
    
// }


// function area_find(rectangle){
//     return rectangle[0]*rectangle[1] // width*length
// }

// function area_print(rectangle_area){
//     console.log(rectangle_area)
//     return 'hi'
// }

// var operations = [area_find,area_print]

// var rectangle = [10,2]
// console.log(operations[1](operations[0](rectangle)))


// var student1 = {
//     name: 'hamza',
//     age: 25,
//     score: 80,
//     sayHi: function(){
//         return 'Hi my name is '+ this.name + ', my age is '+ this.age
//     }
// }

// var student2 = new Object() 
// student2.name = 'ali'
// student2.age = 26
// student2.score = 80

// var student3 = {}
// student3.name = 'mohammad'
// student3.age = 16
// student3.score = 70


// students = [student1,student2,student3]
// console.log(students)
// console.log(student1.sayHi())





// OOP




// function Student(fistName,lastName,age){
//     this.fistName = fistName
//     this.lastName = lastName
//     this.age = age
//     this.sayHi = function(){
//                 return 'Hi my name is '+ this.fistName + ', my age is '+ this.age
//         }
// }

// students = []
// students.push(new Student('hamza','mustafa',26))
// students.push(new Student('ali','shafiq',30))
// students.push(new Student('fathi','mousa',6))


// for (var index=0; index<students.length; index++){
//     console.log(students[index].sayHi())
// }

// // Binding: set the function or (this) for certain scope

// this.car = 'hello'
// var my_cars = {
//     car: 'Avanti96',
//     getCar: function(){
//         return this.car
//     }
// }

// console.log(my_cars.getCar())

// var storeGetCarFunction = my_cars.getCar

// console.log(storeGetCarFunction()) // this will only work for same scope

// var realGetCarFunction = storeGetCarFunction.bind(my_cars)

// console.log(realGetCarFunction())

// // Simpler way of binding

// var storeGetCarFunction = my_cars.getCar.bind(my_cars)
// console.log(storeGetCarFunction())




// form.addEventListener('submit', function(event){
//     var x = parseFloat(x_input.value)
//     var y = parseFloat(y_input.value)
//     if (!x || !y){
//         alert('Please enter values')
//     }
//     else {
//         var _result = (x/y) *100
//         result.innerText = "Result is: " + _result + "%"
//         event.preventDefault()
//     }
    
// })

var form = document.getElementById('calculator-form')
var result = document.getElementById('result')

// Predefined using ChatGPT
function calculate(expression) {
    try {
        // Create a Function constructor with the expression and return the result
        return new Function('return ' + expression)();
    } catch (error) {
        return 'Error'; // Handle invalid expressions gracefully
    }
}


result.innerText = []
var buttons = form.querySelectorAll('button');

console.log(buttons.forEach(function(button){
    button.addEventListener('click', function(){
        var _value = button.value
        if (result.innerText === "-Infinity" || /^[^\d\+\-\(\)]/.test(result.innerText)){ //Regular expression predefined by ChatGPT
            console.log('i am heter')
            result.innerText = []
        }
        if (_value === 'C'){
            result.innerText = []
        }
        else if (_value === 'del'){
            result.innerText = result.innerText.slice(0,-1)
        }
        else if(_value === '='){
            result.innerText = calculate(result.innerText)
        }
        else{
            result.innerText += _value
        }
        
    })
}))

form.addEventListener('submit',function(event){
    event.preventDefault()
})