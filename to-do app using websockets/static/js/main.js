// connecting to websocket server
const socket = IO();

//DOM ELEMENTS
const taskform = document.getElementById("myform");
const taskinput = document.getElementById("task-input");
const list_input = document.getElementById("todoList");

//handling form submission
taskform.addEventListener("submit", (e) => {
  e.preventDefault();
  const text = taskinput.value;
  if (text) {
    //emit addtask to the server
    socket.emit("add_task", { text });
    taskinput.value = "";
  }
});

//listern for task events
