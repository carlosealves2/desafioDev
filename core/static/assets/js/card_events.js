function toggleActionButtons() {
    let list_btn_toggle = [
        document.querySelector("#btn_delete"),
        document.querySelector("#btn_edit")
    ]
    let total_checkbox_selected = document.querySelectorAll("input[type='checkbox']:checked").length
    
    switch (true) {
        case total_checkbox_selected == 0:
            list_btn_toggle.forEach(ele => {
                ele.classList.add("disabled")
            })
            break;
        case total_checkbox_selected == 1:
            list_btn_toggle.forEach(ele => {
                ele.classList.remove("disabled")
            })
            break;
        case total_checkbox_selected > 1:
            document.querySelector("#btn_edit").classList.add("disabled")
            break;
        default:
            break;
    }

    

}

function deleteChecked() {
    let payload = {
        ids: [],
    }

    document.querySelectorAll("input[type='checkbox']:checked").forEach(ele => {
        payload.ids.push(ele.dataset.productId)
    })

    fetch('/product/', {
        method: 'DELETE',
        headers: {
            "Authorization": `Token ${localStorage.getItem("token")}`
        },
        body: JSON.stringify(payload)
    })
    .then(data => {
        if (data.status === 401) {
            alert("Make login to execute this action")
        } else if (data.status === 200) {
            return data.json()
        }
    })
    .then(json => {
        json.deleted.forEach(id => {
            document.querySelector(`#prod_id_${id}`).remove()
        })
        if (document.querySelectorAll('.card').length === 0) {
            window.location.reload()

        }
    })
    .catch(err => console.error(err))
}


