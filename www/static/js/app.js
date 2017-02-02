// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


$(document).ready(function(){
	//key word commas
	console.log("I'm here")
	// // $('.keyword').first().attr('id', 'first'); 
	
	// // $('.job_result').each(function(index){
 // //       console.log(index);
 // //       $('.keyword').last().addClass('last');
 // //    }); 
	// // $( "div span:last-child" )
 // //  		.css({ color:"red", fontSize:"80%" })
	// $('.keyword').last().addClass('last');
	// $('.keyword:last-child').addClass('last');

	// $('.keyword:not(.last)').append(",\u00A0")
	// $('#update-profile p:nth-child(7)').attr('id', 'resume-box');
    $("#resume-input #id_resume").attr("rows","18")
	$(".star").click(function(e) {
	   
	    console.log("hi there");
	    var cached_job_key = $(this).closest('section').attr('id');
		var date = $(this).closest('section').data("date")
		var score =  $(this).closest('section').data("score")
		var company = $(this).closest('section').data("company")
		var location = $(this).closest('section').data("location")
		$.ajax({
		    url : "/favorite_job/",
		    type: "POST",
		    data : {"csrfmiddlewaretoken": csrftoken, 
		    		"cached_job_key": cached_job_key,
		    		"date": date,
		    		"score": score,
		    		"company": company,
		    		"location": location
		    		},		 	
		    success:  function(a) {console.log("hello")}
    	})
    	$(this).removeClass("glyphicon-star-empty").addClass("glyphicon-star");
	});	
});
	 



  

$.getJSON("/get_resume_json", 
    function(response){
    	var resume_text = response
		$('#use-saved').click(function(){
	 		$('#id_resume').val(resume_text);
		});       
	}
);  

