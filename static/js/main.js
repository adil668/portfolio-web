const navbar = document.getElementById("mainNav");
const menuToggle = document.getElementById("menuToggle");
const navLinks = document.getElementById("navLinks");
const backToTop = document.getElementById("backToTop");
const sections = document.querySelectorAll("header[id], section[id]");
const links = document.querySelectorAll(".nav-link");
const revealItems = document.querySelectorAll(".reveal");
const skillBars = document.querySelectorAll(".progress-bar");
const form = document.getElementById("contactForm");
const formNote = document.getElementById("formNote");

function updateNavbarState() {
    const scrolled = window.scrollY > 24;
    navbar.classList.toggle("scrolled", scrolled);
    backToTop.classList.toggle("visible", window.scrollY > 550);
}

function updateActiveLink() {
    let current = "page-top";

    sections.forEach((section) => {
        const sectionTop = section.offsetTop - 140;
        if (window.scrollY >= sectionTop) {
            current = section.getAttribute("id");
        }
    });

    links.forEach((link) => {
        link.classList.toggle("active", link.getAttribute("href") === `#${current}`);
    });
}

const revealObserver = new IntersectionObserver(
    (entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                revealObserver.unobserve(entry.target);
            }
        });
    },
    { threshold: 0.18 }
);

const skillObserver = new IntersectionObserver(
    (entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                const bar = entry.target;
                bar.style.width = `${bar.dataset.width}%`;
                skillObserver.unobserve(bar);
            }
        });
    },
    { threshold: 0.65 }
);

menuToggle.addEventListener("click", () => {
    const isOpen = navLinks.classList.toggle("open");
    menuToggle.classList.toggle("open", isOpen);
    menuToggle.setAttribute("aria-expanded", String(isOpen));
});

links.forEach((link) => {
    link.addEventListener("click", () => {
        navLinks.classList.remove("open");
        menuToggle.classList.remove("open");
        menuToggle.setAttribute("aria-expanded", "false");
    });
});

backToTop.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
});

if (form) {
    form.addEventListener("submit", (event) => {
        event.preventDefault();
        formNote.textContent = "Thanks. Your message is ready to connect to a backend handler.";
        form.reset();
    });
}

window.addEventListener("scroll", () => {
    updateNavbarState();
    updateActiveLink();
});

document.getElementById("currentYear").textContent = new Date().getFullYear();
revealItems.forEach((item) => revealObserver.observe(item));
skillBars.forEach((bar) => skillObserver.observe(bar));
updateNavbarState();
updateActiveLink();
