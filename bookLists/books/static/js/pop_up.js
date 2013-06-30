//log in page:
$(function() {
    $(".tooltip").hover(function() {
        var tooltip = $("> div", this).show();
        var pos = tooltip.offset();
        tooltip.hide();
        var right = pos.left + tooltip.width();
        var pageWidth = $(document).width();
        if (pos.left < 0) {
            tooltip.css("marginLeft", "+=" + (-pos.left) + "px");
        }
        else if (right > pageWidth) {
            tooltip.css("marginLeft", "-=" + (right - pageWidth));
        }
        tooltip.fadeIn();
    }, function() {
        $("> div", this).fadeOut(function() {$(this).css("marginLeft", "");});
    });
});

//html : <br></br><br></br>
<span class="tooltip"><a href="#">log in</a><div>
<div class="tooltipContent"> user+password+sign </div></div></span> 

//css : .tooltip {
    position: relative;
}
.tooltip > div {
    display: none;
    position: absolute;
    bottom: 100%;
    left: 50%;
    margin-left: -150px;
    width: 300px;
    
}
.tooltipContent {
    background-color: #eee;
    border: 1px solid #555;
    border-radius: 5px;
    padding: 5px;
} 


//books page:

