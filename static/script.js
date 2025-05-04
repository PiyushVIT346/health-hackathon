function uploadImage() {
    let fileInput = document.getElementById("fileInput");
    let file = fileInput.files[0];

    if (!file) {
        alert("Please select an image file.");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    fetch("/brainTumor", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = "Error: " + data.error;
        } else {
            document.getElementById("result").innerText = 
                `Prediction: ${data.class} (Confidence: ${(data.confidence * 100).toFixed(2)}%)`;
            
            let reader = new FileReader();
            reader.onload = function (e) {
                let img = document.getElementById("previewImage");
                img.src = e.target.result;
                img.style.display = "block";
            };
            reader.readAsDataURL(file);
        }
    })
    .catch(error => console.error("Error:", error));
}
