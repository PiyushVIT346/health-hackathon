document.addEventListener('DOMContentLoaded', function () {
    const chatBox = document.getElementById('chat-box');
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');

    // Function to scroll chat box to the bottom
    function scrollToBottom() {
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    // Automatically scroll to the bottom on page load
    scrollToBottom();

    // Handle form submission
    chatForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const message = userInput.value.trim();
        if (message === '') return;

        // Clear input field after submission
        userInput.value = '';

        // Scroll to the bottom after the user sends a message
        setTimeout(scrollToBottom, 100);
    });
});
