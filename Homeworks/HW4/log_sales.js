let clients = [
    "Shake Shack",
    "Toast",
    "Computer Science Department",
    "Teacher's College",
    "Starbucks",
    "Subsconsious",
    "Flat Top",
    "Joe's Coffee",
    "Max Caffe",
    "Nussbaum & Wu",
    "Taco Bell",
];

let sales = [
	{
		"salesperson": "James D. Halpert",
		"client": "Shake Shack",
		"reams": 100
	},
	{
		"salesperson": "Stanley Hudson",
		"client": "Toast",
		"reams": 400
	},
	{
		"salesperson": "Michael G. Scott",
		"client": "Computer Science Department",
		"reams": 1000
	},
]

const SALESPERSON = "Nick";

$(document).ready(function(){
    $("#client-input").autocomplete({
        source: clients
    });

    renderSales();

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

        sales.unshift({
            salesperson: SALESPERSON,
            client: client_name,
            reams: reams
        });

        // Refresh view
        renderSales();

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

function renderSales() {
$("#sales-records").empty(); // Clear existing list

    sales.forEach((sale, index) => {
        let saleEntry = $(`
            <div class="row sale-entry">
                <div class="col-3">${sale.salesperson}</div>
                <div class="col-4">${sale.client}</div>
                <div class="col-3">${sale.reams}</div>
                <div class="col-1">
                    <button class="btn btn-danger btn-sm delete-btn" data-index="${index}">X</button>
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
        let index = $(this).data("index");
        sales.splice(index, 1); // Remove from model
        renderSales(); // Refresh view
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

                let index = ui.draggable.data("index");
                sales.splice(index, 1); // Remove from model
                renderSales(); // Refresh view
            }
        });

}