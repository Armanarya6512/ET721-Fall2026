function loadTasks() {
    fetch("/get_tasks")
        .then(response => response.json())
        .then(tasks => {
            const list = document.querySelector("#tasklist");
            list.innerHTML = "";

            tasks.forEach(task => {
                const li = document.createElement("li");
                li.textContent = task.task;
                li.classList.add("task_item");

                const btn = document.createElement("button");
                btn.innerHTML = "&#10060;";
                btn.classList.add("btndeletetask");
                btn.onclick = () => deleteTask(task.id);

                li.appendChild(btn);
                list.appendChild(li);
            });
        });
}

function addTask() {
    const inputtask = document.querySelector("#task-input");
    const task = inputtask.value.trim();
    if (task === "") return;

    fetch("/add_task", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task: task })
    })
    .then(() => {
        inputtask.value = "";
        loadTasks();
    });
}

function deleteTask(id) {
    fetch("/delete_task", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: id })
    })
    .then(() => loadTasks());
}

loadTasks();