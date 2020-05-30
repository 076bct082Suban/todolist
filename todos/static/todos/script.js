
document.addEventListener("DOMContentLoaded", () => {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');


    document.querySelectorAll(".add_new_todo").forEach(todo_form => {
        todo_form.onsubmit = function() {
            console.log(this.new_todo.value)
            const new_todo = this.new_todo.value
            console.log(this.dataset.todolist_id)
            const todolist_id = this.dataset.todolist_id

            const url = 'http://127.0.0.1:8000/api/todo-create/'

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json', 
                    'X-CSTFToken': csrftoken
                },
                mode: 'same-origin' ,
                body: JSON.stringify({
                    "id": 1,
                    "title": new_todo,
                    "description": "",
                    "difficulty": 1,
                    "is_complete": false,
                    "todolist": todolist_id
                })
            }
            ).then(function(response){
                console.log(response)
            })
            return false
        }
    });

    document.querySelectorAll('.todo-checkbox').forEach(checkbox => {
        checkbox.addEventListener('change', (e) => {

            if(checkbox.checked){
                console.log("checked")
            }else{
                console.log('unchecked')
            }
        })

    })

});