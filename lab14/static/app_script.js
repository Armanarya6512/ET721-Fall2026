console.log("Arman Arya")
// collect items from the form
const itemForm = document.querySelector("#itemForm") // Fixed: added space after const

// add an event to the form
itemForm.addEventListener("submit", async function(event) {
    event.preventDefault()
    const name = document.querySelector("#name").value
    const price =  document.querySelector("#price").value

    try {
        // await to pause request until the request finishes
        // fetch() sends an HTTP request to a server
        const res = await fetch("http://127.0.0.1:5000/items", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }, // Fixed: added closing brace and a comma
            body: JSON.stringify({ name: name, price: Number(price) })
        }) // Fixed: added closing brace for the options object
        
        const data = await res.json()
        document.querySelector('#response').innerText = "Response: " + JSON.stringify(data)
    }
    catch(error) {
        document.querySelector('#response').innerText = "Error: " + error
    }
})

// LOADING ALL ITEMS
async function loadItems() {
    const res = await fetch("http://127.0.0.1:5000/items")
    const data = await res.json()

    //collect the elements to print all items
    const list = document.querySelector('.itemslist')

    //use a loop to place item in the json data to a list
    for (const id in data){
        const item = data[id]
        const li = document.createElement('li')
        li.innerHTML = `ID = ${id}, Name = ${item.name}, Price = ${item.price}
        <button onclick="showupdateform('${id}', '${item.name}', '${item.price}')">Update</button>
        <button onclick="deleteItem('${id}')">Delete</button>`
        list.appendChild(li)
    }


}
// function to collect the selected items
function showupdateform(id, name, price){
    document.querySelector("#updatesection").style.display = "block"
    document.querySelector("#updateID").value = id
    document.querySelector("#updateName").value = name
    document.querySelector("#updatePrice").value = price
} 

//function to update the selected item
async function updateItem(){
    const id = document.querySelector("#updateID").value
    const name = document.querySelector("#updateName").value
    const price = document.querySelector("#updatePrice").value

    //update the json data in the local host
    const res = await fetch(`http://127.0.0.1:5000/items/${id}`, {
     method: 'PUT',
     headers: {"Content-type" : "application/json"},
     body: JSON.stringify({name: name, price: Number(price)})
    })
    const html = await res.text()
    document.body.innerHTML = html
}

//DETETE ITEM
async function deleteItem(id){
    const res = await fetch(`http://127.0.0.1:5000/items/${id}`, {
        method: "DELETE",
    })
    const html = await res.text()
    document.body.innerHTML = html
}