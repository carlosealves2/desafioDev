function login() {
    fetch('/auth/token/login/',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "username": "admin",
            "password": "041295"
        })
    })
    .then(data => {
        if (data.status === 200) {
            return data.json()
        } else if (data.status === 400) {
            alert('Invalid request')
        }
    })
    .then(json => {
        localStorage.setItem("token", json.auth_token)
    })
    .catch(err => {
        alert(err)
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
    .then(d => d.json())
    .then(json => console.log(json))

}


function isAuth() {
    let token = localStorage.getItem('token')
    if (token) {
        fetch("/auth/users/me/", {
            method: "POST",
            headers: {
                "Authorization": `Token ${token}`
            }
        })
        .then(data => {
            if (data.status === 401) {
                localStorage.removeItem('token')
                ToastNotification("Auth status", "Your login has expired.")
            }
        })
    }
}