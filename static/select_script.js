window.onload = function() {
    generateRandomIcons();
}

function generateRandomIcons() {
    const iconTypes = ['fa-heart', 'fa-capsules', 'fa-stethoscope', 'fa-syringe', 'fa-user-md', 'fa-hand-holding-medical'];
    const floatingIconsContainer = document.querySelector('.floating-icons');

    for (let i = 0; i < 30; i++) {  // Generate 50 icons
        let icon = document.createElement('div');
        icon.classList.add('icon', 'fa-solid', iconTypes[Math.floor(Math.random() * iconTypes.length)]);
        
        // Randomly position the icons and give them a random direction
        icon.style.left = Math.random() * 100 + 'vw';
        icon.style.top = Math.random() * 100 + 'vh';
        
        // Randomize the animation duration and direction
        let randomDuration = (Math.random() * 10) + 5;  // Random duration between 5s to 15s
        icon.style.animationDuration = randomDuration + 's';
        icon.style.animationDirection = Math.random() > 0.5 ? 'normal' : 'reverse';

        // Remove the icon when hovered (simulate pop)
        icon.addEventListener('mouseenter', function() {
            icon.style.transform = 'scale(2)';
            setTimeout(() => icon.remove(), 300);  // Remove the icon after it pops
        });

        floatingIconsContainer.appendChild(icon);
    }
}
