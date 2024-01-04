// custom_script.js

// Scroll to top functionality using arrow function
document.querySelector('.btt-link').addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Sorting selector functionality using arrow function and template literals
document.querySelector('#sort-selector').addEventListener('change', () => {
    const selector = document.querySelector('#sort-selector');
    const currentUrl = new URL(window.location);
    const selectedVal = selector.value;

    if (selectedVal !== "reset") {
        const [sort, direction] = selectedVal.split("_");

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
});
