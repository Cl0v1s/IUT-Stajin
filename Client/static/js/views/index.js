var sliding = false;
var sliderTime;

$(document).ready(function()
{
	prepareSlider();
	$(window).resize(prepareSlider);
	$(window).resize(manageScroll);
	sliderTime = setInterval(slider, 3500);
	$("#slider-next").click(function(){ if(!sliding){sliderNext();} });
	$("#slider-previous").click(function(){ if(!sliding){sliderPrevious();} } );
	$(window).mousewheel(manageScroll);
});

//Gère le scrolling
function manageScroll(event)
{
	var s = $(window).scrollTop();
	s = s - event.deltaY * event.deltaFactor;
	var r = 250;
	if($(window).height()<690)
	{
		r += 690-$(window).height();
	}
	if(s < r)
		$(window).scrollTop(s);
}



//Remet le timer à zéro
function resetSliderTime()
{
	clearInterval(sliderTime);
    sliderTime= null;
}

//Adapte le slider à l'écran
function prepareSlider()
{
	var wheight=$(window).height();
	$("#slider").css("height", wheight);
	$("#slider ul").css("height", wheight);
	$("#slider ul").css("width", $(window).width() * 3 - 300);
	$("#slider ul .slider-item").css("width", $(window).width()-100);
	$("#slider ul .slider-item").css("min-height", wheight);
}

//Gère le slider et ses animations
function slider()
{
	sliding = true;
	resetSliderTime();
	$("#slider li:first").animate({marginLeft:-$(window).width()}, 800, function()
	{
		resetSliderTime();
		$(this).css("margin-left", "0px");
		sliding = false;
		$(this).parent().find("li:last").after($(this));
	});
}

//Fait passer le slider à la prochaine image
function sliderNext()
{
	clearInterval(sliderTime);
	sliderTime = null;
	slider();
}

function sliderPrevious()
{
	clearInterval(sliderTime);
	sliderTime = null;
	sliding = true;
	resetSliderTime();
	$("#slider ul li:last").css("margin-left", -$(window).width());
	$("#slider ul").find("li:first").before($("#slider ul li:last"));
	$("#slider li:first").animate({marginLeft:0}, 800, function(){sliding = false;resetSliderTime();});
}
