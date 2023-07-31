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
