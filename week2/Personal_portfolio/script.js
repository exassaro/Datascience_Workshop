const menuIcon = document.querySelector('#menu-icon');
const navLinks = document.querySelector('.nav-links');

menuIcon.onclick = () =>{
    navLinks.classList.toggle('active');
}

//Typing effect

document.addEventListener("DOMContentLoaded", () => {
    const professions = ["Web Designer ", "Web Developer ", "Graphic Designer ", "AI Engineer ", "Data Scientist "];
    let index = 0; // Current profession index
    let charIndex = 0; // Current character index
    let isDeleting = false; // Flag for typing or deleting
    const typingSpeed = 100; // Typing speed in ms
    const erasingSpeed = 50; // Erasing speed in ms
    const delayBetweenWords = 1500; // Pause before deleting
    const typedTextElement = document.getElementById("typed-text");

    function typeEffect() {
        const currentText = professions[index];

        if (!isDeleting && charIndex <= currentText.length) {
            // Add characters
            typedTextElement.textContent = currentText.substring(0, charIndex++);
        } else if (isDeleting && charIndex >= 0) {
            // Remove characters
            typedTextElement.textContent = currentText.substring(0, charIndex--);
        }

        // Transition between typing and deleting
        if (!isDeleting && charIndex === currentText.length) {
            // Pause when fully typed
            isDeleting = true;
            setTimeout(typeEffect, delayBetweenWords);
            return;
        } else if (isDeleting && charIndex === 0) {
            // Move to the next word
            isDeleting = false;
            index = (index + 1) % professions.length; // Loop to the next profession
        }

        // Continue the effect
        setTimeout(typeEffect, isDeleting ? erasingSpeed : typingSpeed);
    }

    // Start the typing effect
    typeEffect();
});
