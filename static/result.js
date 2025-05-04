document.addEventListener("DOMContentLoaded", function () {
    const resultBox = document.querySelector(".result-box");
    const uploadButton = document.querySelector(".btn");

    // Add fade-in animation
    resultBox.style.opacity = "0";
    setTimeout(() => {
        resultBox.style.transition = "opacity 1s ease-in-out";
        resultBox.style.opacity = "1";
    }, 300);

    // Button hover effect
    uploadButton.addEventListener("mouseover", function () {
        uploadButton.style.transform = "scale(1.05)";
    });

    uploadButton.addEventListener("mouseout", function () {
        uploadButton.style.transform = "scale(1)";
    });

    // Add a simple error alert if classification data is missing
    const classificationText = document.querySelector("h3").textContent.trim();
    if (!classificationText || classificationText.includes("None")) {
        alert("Warning: No valid classification found. Please try uploading a different image.");
    }
});
