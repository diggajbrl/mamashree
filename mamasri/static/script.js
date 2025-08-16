function resetDropdowns() {
    document.querySelectorAll('.pagination, .articles').forEach(el => el.style.display = 'none');
    document.querySelectorAll('.index').forEach(item => {
        item.style.color = '';
        const icon = item.querySelector('i');
        if (icon) icon.className = 'bi bi-chevron-compact-down';
    });
}

document.querySelectorAll('.index').forEach(item => {
    item.addEventListener('click', () => {
        const container = item.parentElement;
        const dropdown = container.querySelector('.pagination');
        const icon = item.querySelector('i');
        const isOpen = dropdown.style.display === 'block';

        resetDropdowns();

        if (!isOpen) {
            dropdown.style.display = 'block';
            item.style.color = '#666687';
            if (icon) icon.className = 'bi bi-chevron-compact-up';
            if (container.classList.contains('articles')) container.style.display = 'block';
        } else if (container.classList.contains('articles')) {
            container.style.display = 'none';
        }
    });
});

const showArticlesBtn = document.getElementById('showArticles');
if (showArticlesBtn) {
    showArticlesBtn.addEventListener('click', (e) => {
        e.preventDefault();
        const articles = document.querySelector('.articles');
        const isVisible = articles.style.display === 'block';

        resetDropdowns();

        articles.style.display = isVisible ? 'none' : 'block';
        if (!isVisible) {
            articles.querySelector('.pagination').style.display = 'block';
            articles.querySelector('.index').style.color = '#666687';
            const icon = articles.querySelector('.index i');
            if (icon) icon.className = 'bi bi-x-lg';
        }
    });
}

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".readMore").forEach(btn => {
        btn.addEventListener("click", () => {
            document.querySelectorAll(btn.getAttribute("data-target") + " .hidden")
                .forEach(item => item.classList.remove("hidden"));
            btn.style.display = "none";
        });
    });
});

const openPopup = document.getElementById('openPopup');
const closePopup = document.getElementById('closePopup');
const popupOverlay = document.getElementById('popupOverlay');

openPopup.addEventListener('click', () => {
    popupOverlay.classList.add('active');
    document.body.classList.add('no-scroll');
});

closePopup.addEventListener('click', () => {
    popupOverlay.classList.remove('active');
    document.body.classList.remove('no-scroll');
});

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".left .docs table").forEach(function (table) {
        const wrapper = document.createElement("div");
        wrapper.classList.add("table-wrapper");
        wrapper.style.overflowX = "auto";
        wrapper.style.webkitOverflowScrolling = "touch";

        table.parentNode.insertBefore(wrapper, table);
        wrapper.appendChild(table);
    });
});

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".showMore").forEach(function (btn) {
        btn.style.cursor = "pointer";

        btn.addEventListener("click", function () {
            const container = btn.closest("ul");
            const hiddenItems = container.querySelectorAll(".extra-item");

            if (hiddenItems.length === 0) return;

            const isHidden = hiddenItems[0].style.display === "none" || hiddenItems[0].style.display === "";

            hiddenItems.forEach(item => {
                item.style.display = isHidden ? "list-item" : "none";
            });

            btn.textContent = isHidden ? ". . . Show Less" : ". . . Show More";
        });
    });
});