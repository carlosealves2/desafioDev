let timeout = null

function ToastNotification(title, message) {
    let toast = document.querySelector('#toastNotification')
    let toast_title = toast.querySelector(".toast-header strong.me-auto")
    let toast_body = toast.querySelector(".toast-body")

    toast_title.innerHTML = title
    toast_body.innerHTML = message

    toast.classList.remove('hide')
    toast.classList.add("fade")
    toast.classList.add("show")

    timeout = setTimeout(() => {
        toast.classList.remove("fade")
        toast.classList.remove("show")

        toast.classList.add('hide')
    }, 4000)
}

function closeToast() {
    let toast = document.querySelector('#toastNotification')

    toast.classList.remove("fade")
    toast.classList.remove("show")
    toast.classList.add('hide')

    clearTimeout(timeout)

}

function hidden_offcanva() {
    var offcanva = document.querySelector('#offcanvaSideMenu')
    let canva = bootstrap.Offcanvas.getInstance(offcanva)
    canva.hide()

}