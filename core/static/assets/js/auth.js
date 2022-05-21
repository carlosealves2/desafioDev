document.querySelector("form#frm_login").addEventListener('submit', login)
document.querySelector("form#frm_register").addEventListener('submit', register)
function login(e) {
    e.preventDefault()
    
    let form_data = new FormData(e.target)
    let values = JSON.stringify(Object.fromEntries(form_data.entries()))
    fetch('/auth/token/login/',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: values
    })
    .then(data => {
        if (data.status === 200) {
            return data.json()
        } else if (data.status === 400) {
            alert('"username" or "password" invalid.')
        }
    })
    .then(json => {
        localStorage.setItem("token", json.auth_token)
        var auth_modal_ele = document.querySelector("#authModal")
        var modal = bootstrap.Modal.getInstance(auth_modal_ele)
        modal.hide()

        ToastNotification('login', "login success!")
        handle_menu(true)
    })
    .catch(err => {
        console.error(err)
    })
}

function logout() {
    fetch("/auth/token/logout/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "Authorization": `Token ${localStorage.getItem("token")}`
        },
    })
    .then(d => {
        if (d.status == 204) {
            handle_menu(false)
        }
    })

}


function isAuth() {
    let token = localStorage.getItem('token')
    if (token) {
        fetch("/auth/users/me/", {
            method: "GET",
            headers: {
                "Authorization": `Token ${token}`
            }
        })
        .then(data => {
            if (data.status === 401) {
                localStorage.removeItem('token')
                ToastNotification("Auth status", "Your login has expired.")
                handle_menu(false)
            } else if (data.status === 200) {
                handle_menu(true)
            }
        })
    }
}

function handle_menu(is_auth) {
    let side_menu = document.querySelector('.offcanvas-body .list-group ')
    
    if (is_auth) {
        let login_link = document.querySelector("#login_link")
        if (login_link) {
            login_link.remove()

            let logout_link = document.createElement('a')
            let text_link = document.createTextNode("Logout")
            logout_link.appendChild(text_link)
            logout_link.setAttribute('class', 'list-group-item list-group-item-action')
            logout_link.setAttribute("data-bs-toggle", "modal")
            logout_link.setAttribute("data-bs-target", "modal")
            logout_link.id = "logout_link"

            logout_link.addEventListener('click', logout)

            side_menu.appendChild(logout_link)
        }
    } else {
        let logout_link = document.querySelector("#logout_link")
        if (logout_link) {
            logout_link.remove()

            let login_link = document.createElement('a')
            let text_link = document.createTextNode("Login")
            login_link.appendChild(text_link)
            login_link.setAttribute('class', 'list-group-item list-group-item-action')
            login_link.setAttribute("data-bs-toggle", "modal")
            login_link.setAttribute("data-bs-target", "#authModal")
            login_link.id = "login_link"

            login_link.addEventListener('click', hidden_offcanva)

            side_menu.appendChild(login_link)
        }
    }
}

function register(e) {
    e.preventDefault()
    let form_data = new FormData(e.target)
    let values = JSON.stringify(Object.fromEntries(form_data.entries()))
    console.log(values)
    
    fetch('/auth/users/',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: values
    })
    .then(data => {
        if (data.status === 201) {
            var auth_modal_ele = document.querySelector("#authModal")
        var modal = bootstrap.Modal.getInstance(auth_modal_ele)
        modal.hide()

        ToastNotification('Register', "Success, now make login to use recurses!")
        } else {
            alert('Failure to register new user')
        }
    })
    .catch(err => {
        console.error(err)
    })
}