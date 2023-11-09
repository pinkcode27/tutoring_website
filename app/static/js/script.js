// Get a reference to your navigation element
const nav = document.querySelector(".nav__list");

// Define the scroll threshold when you want the background color to change
const scrollThreshold = 50; // Adjust this value as needed - pixels

// Function to toggle the 'nav--scrolled' class
function toggleNavBackground() {
  if (window.scrollY > scrollThreshold) {
    nav.classList.add("nav__list--blur");
  } else {
    nav.classList.remove("nav__list--blur");
  }
}

// Add a scroll event listener to trigger the toggle function
window.addEventListener("scroll", toggleNavBackground);

// Call the toggle function once on page load to set the initial state
toggleNavBackground();

// To keep year up to date
const yearEl = document.querySelector(".year");
const currentYear = new Date().getFullYear();
console.log(currentYear);
yearEl.textContent = currentYear;
