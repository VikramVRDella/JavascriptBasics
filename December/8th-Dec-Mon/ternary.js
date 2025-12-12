const fname = "Raj";
var age = 21;
var age=13;


const result = age>=18? "Eliglible":"Not Eligible"

console.log(result)


function welcome(name)
{
    const result = name?name:"Stranger"
    console.log("Welcome "+result)
}

welcome()
welcome(fname)


const great=()=>{
    return "Hello"
}

console.log(great())

const user={
    // "name":"Hendry",
    "age":18
}
console.log(user)
console.log(user.name? user.name : "No Name")

const rsult = user.age>=18 ?`${user.name?user.name:"No Name"} Eligible to Vote`:`${user.name?user.name:"No Name"} Not Eligible to Vote` 
console.log(rsult)


avg = 80

const grade = avg>=90 ?"A" :avg>=80 ?"B" :"C" 
console.log("Grade : ",grade)