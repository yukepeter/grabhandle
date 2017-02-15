// receive data via REST API
var getUrl = function(event) {
    //Clicking on a "Submit" button, prevent it from submitting a form
	event.preventDefault();
    console.log('yuke') 
    // Interact with REST API
    var data = JSON.stringify($("#submit").serializeObject());
    $.ajax({
        type: "POST",
        crossDomain: true,
        contentType: "application/json; charset=UTF-8",
        data: data,
        url: "/api/geturl",
        success: function(data) {
        console.log(data)         
        },
        error: function(error) {
            // turn json back to js object, a bit tricky here
            var err_obj = JSON.parse(error.responseText);
            for (var i in err_obj['errors']) {
                // console.log(err_obj['errors'][i]);
                $(".error").append(err_obj['errors'][i]['message'].concat('</br>'));
            }
        }
    })
}
