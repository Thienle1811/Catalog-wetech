// main.js for simple interactions

// This file can be used to add JavaScript for features like:
// - A simple carousel for the feedback section
// - Mobile menu toggle
// - Active state handling for navigation links

console.log("main.js loaded");

// Example: Simple carousel logic (conceptual)
// You would need a more robust implementation for a real carousel.
document.addEventListener('DOMContentLoaded', function() {
    // Tab functionality for product detail page
    const tabLinks = document.querySelectorAll('.tab-link');
    if (tabLinks.length > 0) {
        const tabContents = document.querySelectorAll('.tab-content');

        tabLinks.forEach(link => {
            link.addEventListener('click', () => {
                const tabId = link.getAttribute('data-tab');

                tabLinks.forEach(l => l.classList.remove('active'));
                tabContents.forEach(c => c.classList.remove('active'));

                link.classList.add('active');
                document.getElementById(tabId).classList.add('active');
            });
        });
    }

    // Thumbnail click functionality for product detail page
    const thumbnails = document.querySelectorAll('.thumbnail');
    if (thumbnails.length > 0) {
        const mainImage = document.querySelector('.main-image img');
        thumbnails.forEach(thumb => {
            thumb.addEventListener('click', function() {
                thumbnails.forEach(t => t.classList.remove('active'));
                this.classList.add('active');
                mainImage.src = this.querySelector('img').src.replace('80x80', '480x480');
            });
        });
    }
});
