$(document).ready(function () {
    $("#add-company-form").submit(function (event) {
        event.preventDefault();

        let formData = {
            name: $("#name").val().trim(),
            ticker: $("#ticker").val().trim(),
            logo: $("#logo").val().trim(),
            description: $("#description").val().trim(),
            share_price: $("#share_price").val().trim(),
            models: $("#models").val().trim()
        };

        $(".error-message").text(""); // Clear previous errors

        $.ajax({
            url: "/add",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(formData),
            success: function (response) {
                // Show success message
                $("#success-message").removeClass("d-none");
                $("#view-link").attr("href", "/view/" + response.id);

                // Reset form fields
                $("#add-company-form")[0].reset();
                $("#name").focus();
            },
            error: function (xhr) {
                let errors = xhr.responseJSON.errors;
                if (errors) {
                    Object.keys(errors).forEach(field => {
                        $(`#${field}`).next(".error-message").text(errors[field]);
                    });
                }
            }
        });
    });
});
