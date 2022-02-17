const name = document.getElementById('name')
const form = document.getElementById('form')
const errorElement = document.getElementById('emailerror')
var intonumber = parseInt(document.getElementById('name'))
const uname = document.getElementById('username')
const phnnumber = document.getElementById('number')
const email = document.getElementById('email')
const pword = document.getElementById('password')



form.addEventListener('submit' ,(e)  => {
    let messages =[]
    if( name.value.trim() ==""){
        messages.push("Non of the field should be empty.")
        name.style.border= "solid 4px tomato"
    }
    else if(username.value.trim() ==""){
        messages.push("Usename shouldn't be empty.")
        username.style.border="solid 4px tomato"
    }
    else if(email.value.trim()==""){
        messages.push("Please enter your email address.")
        email.style.border="solid 4px tomato"
    }
    else if(number.value.trim()==""){
        messages.push("Please enter your number.")
        number.style.border="solid 4px tomato"
    }
    else if(number.value.length<10 || number.value.length>10){
        messages.push("The number should be 10 digits.")
        number.style.border="solid 4px tomato"
    }
    else if(password.value.trim()==""){
        messages.push("The password fiels should not be empty.")
        password.style.border="solid 4px tomato"
    }
    else if(password.value.length<=8){
        messages.push("Password too short.")
        password.style.border="solid 4px tomato"
    }
    if(messages.length >0){
        e.preventDefault()
        errorElement.innerHTML = messages.join(' , ' )
    }
    else{
        alert("Registered Successfully")
    }
})
$(window).on('load',function(){
    $(".container").fadeIn(1000);
});
