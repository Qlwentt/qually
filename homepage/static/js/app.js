
$(document).ready(function(){

	$('.keyword').first().attr('id', 'first'); 
	$('.keyword').last().attr('id', 'last'); 

	$('.keyword:not(#first):not(#last)').append(",\u00A0")


});
  

$.getJSON("/get_resume_json", 
    function(response){
    	var resume_text = response
		$('#use-saved').click(function(){
	 		$('#id_resume').val(resume_text);
		});       
	}
);  

