




var intervalId; // Variable to hold the interval ID

function sendPostRequest() {
    var canvas = document.getElementById("canvas_data").value;
    var prompt = document.getElementById("prompt").value;
    var url = "pch-home-server3143.iptime.org:8000/save"; // Replace with your server endpoint URL

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ canvas_data:canvas, prompt:prompt })
    })
    .then(response => {
        if (response.ok) {
            startPeriodicGetRequest(response.col); // Start periodic GET requests
        }
        return response.json();
    })
    .then(result => {
        // Handle the response from the server
        console.log(result);
    })
    .catch(error => {
        // Handle any errors that occur during the request
        console.error("Error:", error);
    });
}
function startPeriodicGetRequest() {
    var url = "pch-home-server3143.iptime.org:8000/queue"; // Replace with your server endpoint URL

    intervalId = setInterval(() => {
        fetch(url)
        .then(response => response.json())
        .then(result => {
            // Handle the response from the server
            console.log(result);
            if (result === -1) {
                stopPeriodicGetRequest();
                window.location.href = "pch-home-server3143.iptime.org:8000/result"; // Replace with the redirect URL
            }
        })
        .catch(error => {
            // Handle any errors that occur during the request
            console.error("Error:", error);
        });
    }, 1000); // Send GET request every second (1000 milliseconds)
}

function stopPeriodicGetRequest() {
    clearInterval(intervalId); // Stop the interval
}