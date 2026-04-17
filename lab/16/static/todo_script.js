document.addEventListener("DOMContentLoaded", loadTasks);


function loadTasks() {
    fetch("get_tasks")
        .then(resp => resp.json())
        .then(data => {
            const list = document.getElementById("task_list");
            list.innerHTML = "";

            data.forEach(task => 
                createTaskElement(task)
            );
        });
}


function addtask() {
    const task_element = document.querySelector("#task_input");
    const task_info = task_element.value.trim();

    if ( task_info === "" ) return;

    fetch("add_task", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({task: task_info}),
    }).then(() => {
        task_element.value = "";
        loadTasks();
    });
}


function deleteTask(id) {
    fetch("delete_task", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({id: id})
    }).then(loadTasks);
}


function createTaskElement(task) {
    const list = document.getElementById("task_list");

    const item = document.createElement("li");

    item.textContent = task.task;
    item.classList.add("task-item");

    const button = document.createElement("button");

    button.innerHTML = "&#10060";
    button.onclick = () => deleteTask(task.id);
    button.classList.add("delete-item-button");

    item.append(button);
    list.appendChild(item);
}
