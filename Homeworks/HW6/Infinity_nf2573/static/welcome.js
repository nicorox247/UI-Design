$(document).ready(function () {

    $("#search-form").submit(function (event) {
        let searchInput = $("#search-input"); // Get the input field
        let query = searchInput.val().trim(); // Trim whitespace

        if (query === "") {
            event.preventDefault(); // Stop form submission
            searchInput.val(""); // Clear the input field
            searchInput.focus(); // Keep focus on the search bar
            return;
        }
    });

    function loadCards(data, containerId) {
        let cardContainer = $(`#${containerId}`);
        cardContainer.empty();  // Clear previous content

        data.forEach(company => {
            let card = `
                <div class="col-md-4">
                    <div class="card mb-4 shadow-sm">
                        <img src="${company.logo}" class="card-img-top" alt="${company.id} Logo">
                        <div class="card-body">
                            <h5 class="card-title">${company.ticker}</h5>
                            <p class="card-text">${company.description.substring(0, 100)}...</p>
                            <a href="/view/${company.id}" class="btn btn-primary">View Details</a>
                        </div>
                    </div>
                </div>
            `;
            cardContainer.append(card);
        });
    }

    // Check which page we're on and load the appropriate data
    if (typeof favorites !== "undefined") {
        loadCards(favorites, "card-element");
    } else if (typeof results !== "undefined") {
        loadCards(results, "search-results");
    }

});
