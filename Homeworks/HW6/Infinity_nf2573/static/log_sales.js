
const SALESPERSON = "Nick";

$(document).ready(function(){
    $("#client-input").autocomplete({
        source: clients
    });

    display_sales_list(sales);

    $("#submit-btn").click(function(){
        
        let client_name = $("#client-input").val().trim();
        let reams = $("#ream-input").val().trim();

        //if Client box empty
        if(client_name === ""){
            $("#client-input").addClass("error");
            $("#client-input").focus();
            return;
        }

        //if ream box empty or is not a number
        if(reams === "" || isNaN(reams) || Number(reams) <= 0){
            $("#ream-input").addClass("error");
            $("#ream-input").css("color", "red");
            $("#ream-input").focus();
            return;
        }

        if(client_name && !clients.includes(client_name)){
            clients.push(client_name)
            $("#client-input").autocomplete("option", "source", clients);
        }

        let new_sale = {
            salesperson: SALESPERSON,
            client: client_name,
            reams: reams
        };

        // save sale and refresh view
        save_sale(new_sale);

        $("#client-input").val("").focus();
        $("#ream-input").val("");

    });

    //error handling:
    // input changes in the client box
    $("#client-input").on("input", function() {
        if ($(this).val().trim() !== "") {
            $(this).removeClass("error");
        }
    });

    //input changes for ream box
    $("#ream-input").on("input", function() {
        let input = $(this).val().trim()
        if ( input !== "" && !isNaN(input) && Number(input) > 0) {
            $(this).removeClass("error");
            $(this).css("color", "black");
        }
    });

    //enter key
    $("#ream-input").keydown(function(event){
        if(event.key === "Enter"){
            $("#submit-btn").click();
        }
    })
});

function delete_sale(id){
    $.post('/delete_sale', { id: id }, function(response) {
        sales = response.sales; // Update sales list
        display_sales_list(sales); // Refresh UI
    }, "json");
}

function save_sale(new_sale){
    $.post('/save_sale', new_sale, function(response) {
        sales = response.sales;   // Update sales list
        clients = response.clients; // Update clients list

        // Update autocomplete with new client list
        $("#client-input").autocomplete("option", "source", clients);

        // Refresh UI with updated sales
        display_sales_list(sales);
    }, "json");
}

function display_sales_list(sales) {
$("#sales-records").empty(); // Clear existing list

    sales.forEach((sale) => {
        let saleEntry = $(`
            <div class="row sale-entry" data-id="${sale.id}">
                <div class="col-3">${sale.salesperson}</div>
                <div class="col-4">${sale.client}</div>
                <div class="col-3">${sale.reams}</div>
                <div class="col-1">
                    <button class="btn btn-danger btn-sm delete-btn" data-id="${sale.id}">X</button>
                </div>
            </div>
        `);
        $("#sales-records").append(saleEntry);

        // Make sales rows draggable
        saleEntry.draggable({
            revert: "invalid",
            helper: "clone", 
            cursor: "move",
            start: function() {
                $(this).css("opacity", "0.5");
            },
            stop: function() {
                $(this).css("opacity", "1");
            }
        });
    });

    // delete buttons
    $(".delete-btn").click(function(){
        let saleId = $(this).data("id");
        delete_sale(saleId);
    });

        // Make the trash bin droppable
        $("#trash").droppable({
            accept: ".sale-entry",
            over: function() {
                $(this).addClass("highlight"); 
            },
            out: function() {
                $(this).removeClass("highlight");
            },
            drop: function(event, ui) {
                $(this).removeClass("highlight");

                let saleId = ui.draggable.data("id");
                delete_sale(saleId);
            }
        });

}