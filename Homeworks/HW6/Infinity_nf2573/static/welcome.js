$(document).ready(function () {

    let cardContainer = $("#card-element");

    favorites.forEach(company => {
        let card = `
            <div class="col-md-4">
                <div class="card mb-4 shadow-sm">
                    <img src="${company.logo}" class="card-img-top" alt="${company.id} Logo">
                    <div class="card-body">
                        <h5 class="card-title">${company.ticker}</h5>
                        <p class="card-text">${company.description.substring(0, 100)}...</p>
                        <a href="#" class="btn btn-primary">View Details</a>
                    </div>
                </div>
            </div>
        `;
        cardContainer.append(card);
    });
});
