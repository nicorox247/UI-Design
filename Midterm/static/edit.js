$(document).ready(function () {
    $("#edit-form").submit(function (event) {
        event.preventDefault();

        let formData = {
            ticker: $("#ticker").val().trim(),
            logo: $("#logo").val().trim(),
            description: $("#description").val().trim(),
            share_price: $("#share_price").val().trim(),
            models: $("#models").val().split(",").map(item => item.trim())  // Convert string to list
        };

        $.ajax({
            url: window.location.pathname,  // Submits to `/edit/<id>`
            type: "POST",
            data: formData,
            success: function (response) {
                if (response.success) {
                    window.location.href = response.redirect;  // Redirect to updated company page
                }
            },
            error: function () {
                alert("Error updating company. Please try again.");
            }
        });
    });

    $("#discard-changes").click(function () {
        if (confirm("Are you sure you want to discard changes?")) {
            window.history.back();  // Go back to previous page
        }
    });

    document.addEventListener("DOMContentLoaded", function() {
        let descBox = document.querySelector(".auto-resize");
        if (descBox) {
            // Count number of lines based on newlines
            let lines = descBox.value.split('\n').length;
            
            // Provide a minimum row count so it's never too small
            if (lines < 5) lines = 5;
            
            descBox.setAttribute('rows', lines);
    
            // Optional: allow user to expand further with vertical resize
            descBox.style.resize = "vertical";
        }
    });

    // $("#edit-form").submit(function (event) {
    //     let sharePriceInput = $("#share_price");
    //     let sharePriceValue = sharePriceInput.val().trim();
    //     let sharePriceRegex = /^\$\d+\.\d{2}$/; // Matches $XX.XX format

    //     $(".error-message").remove(); // Remove old error messages

    //     // Validate share price
    //     if (!sharePriceRegex.test(sharePriceValue)) {
    //         event.preventDefault(); // Prevent form submission
    //         sharePriceInput.after('<span class="error-message text-danger">Price must be in $XX.XX format.</span>');
    //         return;
    //     }
    // });
       
    
    
});
