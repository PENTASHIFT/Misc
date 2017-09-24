// An extension to filter through the censoring nonsense on lainchan.

var elements = document.getElementsByClassName("body");

var i;
for(i=0; i<elements.length; i++){
	var content = elements[i].textContent;
	var parsed = content.replace(/fuarrrk/g, "fuck");
	elements[i].innerHTML = parsed;
}
