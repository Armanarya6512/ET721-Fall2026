// load all tasks
function loadTasks() {
    fetch("/get_tasks")
        .then(response => response.json())
        .then(tasks => {
            const list = document.querySelector("#tasklist");
            list.innerHTML = "";

            tasks.forEach(task => {
                const li = document.createElement("li");
                li.textContent = task.task;
                list.appendChild(li);

                // create delete button for each task
const btn = document.createElement("button");
btn.innerHTML = "&#10060;"; 
btn.classList.add("btndeletetask");
btn.onclick = () => {
    fetch("/delete_task", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({task: task.task})
    })
    .then(() => loadTasks());
};
li.appendChild(btn);
});
});
}

// load all tasks when the page loads
window.onload = loadTasks;
// add a new task
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

// run loadTasks when the page opens
loadTasks();
