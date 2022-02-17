const form = document.getElementById('form')
const errorElement = document.getElementById('emailerror')
const email = document.getElementById('email')
const password = document.getElementById('password')



form.addEventListener('submit' ,(e)  => {
    let messages =[]
    if(email.value.trim()==""){
        messages.push("Please enter your email address.")
        email.style.border="solid 4px red"
    }
    else if(password.value.trim()==""){
        messages.push("The password fiels should not be empty.")
        password.style.border="solid 4px red"
    }
    if(messages.length >0){
        e.preventDefault()
        errorElement.innerHTML = messages.join(' , ' )
    }
    else{
        alert("Login Successfully")
    }
})

