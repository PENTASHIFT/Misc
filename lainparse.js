// An extension to filter through the censoring nonsense on lainchan.

// The class name of each post.
var elements = document.getElementsByClassName("body");

// Looping through each post and filtering.
for(var i=0; i<elements.length; i++){
	let content = elements[i].textContent;
	let parsed = content.replace(/fuarrrk/g, "fuck");
	elements[i].innerHTML = parsed;
}
