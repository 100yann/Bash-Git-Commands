// JS uses camelCase

var name = "value"; // str/int/bool/null variable

var array1 = [] // can be modified
const array2 = [] // cannot be modified
array1.push() // add to array
array1.splice(index, n) // index to start removing; n = num of items to be removed

const index = array1.indexOf(name) // get index of passed parameter

var condition = null 

// Control Flow
if (condition) {
    pass;
} else if (!condition){
    pass;
} else {
    pass;
}

// While loops
while (true){
    continue;
}

// For loops
for (var i=0; i<10; i++){
    continue;
}

for (var num of array){
    continue;
}
array.forEach(newFunction); // for each item in the array call function

// Functions
function newFunction(param1, param2) {
    return;
}

// Objects
var objectName = {key:'value'}; // the key is not a string when initializing
objectName['key'] // but when getting value at key it is passed as a string
objectName['key'] = 'new_value' // update value

// iterating through objects
for (key in carInfo){
    console.log(key);
    console.log(carInfo[key]);
}

var newObject = {
    name: 'Asd',
    greet: function(){
        console.log('Hello ' + this.name)
    }
}

// Repeatedly call a function or execute a code snippet, with a fixed time delay between each call.
setInterval('function()', 10000) // interval is in milliseconds (10000 = 10sec)


// Document attributes
document.URL // returns the URL of the website
document.body // everything inside the body
document.head // everything inside the head
document.links // all links on the page

// Document methods
document.getElementById('id') // returns the element with the specified id
document.getElementByClassName('class') // returns a list of all elements with specified class name
document.getElementByTagName('tag') // returns a list of all elements with specified tag
document.querySelector('css selector - .class/#id/tag') // returns the first element that matches the css selector
document.querySelectorAll('css selector - .class/#id/tag') // returns all objects matching the css selector

// You can store an element inside the variable and change its attributes 
// by calling variable.style.color = newColor for example


// Example HTML
// <p> This is some text </p>

var paragraph = document.querySelector('p') // select the first element with a paragraph tag

paragraph.textContent // show the text currently in the paragraph tag
paragraph.textContent = 'This is some NEW text' // change the text inside the paragraph tag
// textContent will treat everything as a string, so you cannot use HTML tags inside

paragraph.innerHTML // show the actual HTML
paragraph.innerHTML = 'This is some <strong>NEW</strong> text' // edit

// Example HTML
// <div id='special'> 
//    <a href='www.google.com'></a>
// </div>

var special = document.querySelector('#special') // get the entire div with id special
var specialA = special.querySelector('a') // get the <a> tag inside the div
specialA.getAttribute('href') // get the attribute
specialA.setAttribute('href', 'www.bing.com') // edit the attribute (sorry google)


// Event Listeners - call a function on click/hover/etc.
special.addEventListener('mouseover', function(){
    // Some code
})
// Different event listeners - mouseover, mouseout, click, dblclick


// Selecting with jQuery
$('a') // selects all a tags
$('.container') // selects elements with the class 
$('#id') // selects element with id

 // edit css with jQuery using .css
var x = $('a')
x.css('background', 'green') // css property, value
// You can pass an entire object with multiple key:value pairs
x.eq(index).css() // eq(index) will select only one element inside the variable x 
                 //if threre's a list of elements inside x

$('h1').text() // get the text inside the tag
$('h1').text('NEW TEXT') // update the text inside the tag
$('h1').html() // get html
$('h1').html('new html/text') // edit html

// edit attribute using .attr
$('input').attr('type', 'checkbox')

// edit value using .val
$('input').val('new val')

x.addClass('class') // adds a class to the tag
x.removeClass('class') // remove
x.toggleClass('class') // toggles on/off

// event handling with jQuery
$('h1').click(function(){
    $(this).text() // change the text of the passed tag 
})


// KEY PRESS
$('input').eq(0).keypress(function(event){
    console.log(event.which); // this will print which key was pressed (will return key code)
})

// on()
$('h1').on('dblclick', function(){
    $(this).toggleClass('class)
})

// animations
$('input').on('click', function(){
    $(this).fadeOut(3000)
})
