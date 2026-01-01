// 1. Data Store: A collection of quotes to pull from
const quotes = [
    {
        text: "The best way to predict the future is to create it.",
        author: "Abraham Lincoln"
    },
    {
        text: "Don't watch the clock; do what it does. Keep going.",
        author: "Sam Levenson"
    },
    {
        text: "Everything you've ever wanted is on the other side of fear.",
        author: "George Addair"
    },
    {
        text: "Hardships often prepare ordinary people for an extraordinary destiny.",
        author: "C.S. Lewis"
    },
    {
        text: "Believe you can and you're halfway there.",
        author: "Theodore Roosevelt"
    },
    {
        text: "Your talent determines what you can do. Your motivation determines how much you are willing to do.",
        author: "Lou Holtz"
    }
];

/**
 * 2. New Quote Generator
 * This function selects a random quote and updates the DOM
 */
function generateQuote() {
    const quoteElement = document.getElementById('main-quote');
    const authorElement = document.getElementById('main-author');
    const quoteBox = document.querySelector('.quote-box');

    // Step A: Start Fade Out
    quoteBox.style.opacity = '0';
    quoteBox.style.transform = 'translateY(10px)';
    
    // Step B: Wait for fade out animation (300ms), then swap text
    setTimeout(() => {
        // Pick a random index from the array
        const randomIndex = Math.floor(Math.random() * quotes.length);
        const selectedQuote = quotes[randomIndex];

        // Update the text
        quoteElement.innerText = `"${selectedQuote.text}"`;
        authorElement.innerText = `— ${selectedQuote.author}`;

        // Step C: Fade back in
        quoteBox.style.opacity = '1';
        quoteBox.style.transform = 'translateY(0)';
        quoteBox.style.transition = 'all 0.5s ease';
    }, 400);
}

// 3. Auto-update Copyright Year
// Instead of manually changing 2023 to 2024, JS does it for you.
document.addEventListener('DOMContentLoaded', () => {
    const footerYear = document.querySelector('footer p');
    const currentYear = new Date().getFullYear();
    footerYear.innerHTML = `&copy; ${currentYear} Inspiria Quotes. All rights reserved.`;
});

// 4. Mobile Menu Toggle (Bonus)
// If you add a "Hamburger" icon later, this script will handle opening the menu
const toggleMenu = () => {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
};

document.getElementById("share-btn").addEventListener("click", function() {
    const quote = document.getElementById("main-quote").innerText;
    const author = document.getElementById("main-author").innerText;
    const textToShare = `${quote} ${author}`;

    if (navigator.share) {
        navigator.share({
            title: "Daily Motivation Quote",
            text: textToShare,
        }).then(() => console.log("Shared successfully"))
          .catch((err) => console.log("Error sharing", err));
    } else {
        // fallback: copy to clipboard
        navigator.clipboard.writeText(textToShare).then(() => {
            alert("Quote copied to clipboard!");
        });
    }
});
