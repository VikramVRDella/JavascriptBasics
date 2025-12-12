var age =25;
var fname="Hendry";
var phone=true;

const s1= Symbol()
const s2 = Symbol()

console.log(typeof phone, phone);
console.log(typeof age , age);
console.log(typeof fname, fname);
console.log(typeof s1, s1);
console.log(typeof s2, s2);

if (s1===s2)
{
    console.log(true);
}
else
{
    console.log(false)
}

var languages= ["C","C++","Javascript"]
var Student={
    "name":"Hello",
    "age":22
}

var dt=Date()

console.log(languages, typeof languages)
console.log(Student, typeof Student)
console.log(dt, typeof dt)