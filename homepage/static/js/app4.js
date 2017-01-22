
$(document).ready(function(){

	$('.keyword').first().attr('id', 'first'); 
	$('.keyword').last().attr('id', 'last'); 

	$('.keyword:not(#first):not(#last)').append(",\u00A0")

});