$(document).ready(function () {

    // Seach logic
    let searchInput = $("#search-input");

    // Prevent searching empty whitespace
    $("#search-form").submit(function (event) {
        let query = searchInput.val().trim();
        if (query === "") {
            event.preventDefault();
            searchInput.val("");
            searchInput.focus();
            return;
        }
    });

    function highlightMatch(text, query) {
        if (!query || !text) return text; // Ensure valid inputs
    
        try {
            let regex = new RegExp(`(${query})`, "gi"); // Case-insensitive match
            return text.replace(regex, '<span class="highlight">$1</span>');
        } catch (error) {
            console.error("Regex error in highlightMatch:", error);
            return text;
        }
    }

    // Function to load Cards (Used for both Home and Search)
    function loadCards(data, containerId) {
        let cardContainer = $(`#${containerId}`);
        cardContainer.empty();  // Clear previous content

        data.forEach(company => {
            let card = `
                <div class="col-md-4">
                    <div class="card mb-4 shadow-sm">
                        <img src="${company.logo}" class="card-img-top" alt="${company.id} Logo">
                        <div class="card-body">
                            <h5 class="card-title">${company.name}</h5>
                            <p class="card-text">${company.description.substring(0, 100)}...</p>
                            <a href="/view/${company.id}" class="btn btn-primary">View Details</a>
                        </div>
                    </div>
                </div>
            `;
            cardContainer.append(card);
        });
    }

    // Function to load Search Results (List or Card View)
    function loadResults(data, viewType) {
        let listContainer = $("#results-list");
        let cardContainer = $("#results-cards");
    
        listContainer.empty();
        cardContainer.empty();
    
        if (viewType === "list") {
            console.log("Loading List View with", data.length, "results"); // Debugging
    
            data.forEach(company => {
                let highlightedName = highlightMatch(company.name, searchQuery);
                let highlightedTicker = highlightMatch(company.ticker, searchQuery);
                let highlightedDesc = highlightMatch(company.description.substring(0, 150), searchQuery);
    
                let listItem = `
                    <li class="list-group-item">
                        <strong>${highlightedName}</strong> (${highlightedTicker})<br>
                        <span class="description">${highlightedDesc}...</span><br>
                        <a href="/view/${company.id}" class="btn btn-primary btn-sm mt-2">View Details</a>
                    </li>
                `;
    
                console.log("Appending List Item:", listItem); // Debugging
                listContainer.append(listItem);
            });
    
            listContainer.removeClass("d-none");
            cardContainer.addClass("d-none");
        } else {
            console.log("Loading Card View...");
            loadCards(data, "results-cards");
            cardContainer.removeClass("d-none");
            listContainer.addClass("d-none");
        }
    }
    

    // Handle View Toggle on Search Page
    $("#toggle-view").click(function () {
        let isListView = $("#results-list").hasClass("d-none");

        if (isListView) {
            loadResults(results, "list");
            $(this).text("Switch to Card View");
        } else {
            loadResults(results, "card");
            $(this).text("Switch to List View");
        }
    });

    // ✅ Load Home Page Favorites if `favorites` exists
    if (typeof favorites !== "undefined") {
        loadCards(favorites, "card-element");
    }

    // ✅ Load Search Results if `results` exists
    if (typeof results !== "undefined") {
        loadResults(results, "list");
    }

    //Battery Animation logic
    let battery = $("#battery");
    let charge = $("#charge");
    let statusText = $("#battery-status");

    let isCharging = false; // Tracks if charging is in progress
    let isFull = false; // Tracks if battery is fully charged
    let chargeLevel = 0;
    let chargeInterval;

    battery.click(function () {
        if (isFull) {
            // Reset battery only if it is FULLY CHARGED
            clearInterval(chargeInterval); 
            chargeLevel = 0;
            charge.css({ "width": "0%", "transition": "none" }); // Instantly reset
            statusText.text("Click to Charge ⚡");
            isFull = false;
            return;
        }

        if (isCharging) {
            return; // If currently charging, ignore clicks
        }

        // ⚡ Shock effect
        battery.addClass("shock");

        setTimeout(() => {
            battery.removeClass("shock");

            isCharging = true;
            charge.css("transition", "width 2s ease-in-out");

            chargeInterval = setInterval(() => {
                chargeLevel += 10;
                charge.css("width", chargeLevel + "%");

                if (chargeLevel >= 100) {
                    clearInterval(chargeInterval);
                    statusText.text("Fully Charged 🔋✅");
                    isCharging = false;
                    isFull = true; // Mark battery as fully charged
                } else {
                    statusText.text(`Charging... ${chargeLevel}% ⚡`);
                }
            }, 500);
        }, 500);
    });

});
