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
        console.error("Error submitting item:", error)
    }
})
