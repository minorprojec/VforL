// type writing heading
var TxtType = function(el, toRotate, period) {
    this.toRotate = toRotate;
    this.el = el;
    this.loopNum = 0;
    this.period = parseInt(period , 10) || 2000;
    this.txt = '';
    this.tick();
    this.isDeleting = false;
    };

    TxtType.prototype.tick =function() {
        var i = this.loopNum % this.toRotate.length;
        var fullTxt = this.toRotate[i];

        if(this.isDeleting) {
        this.txt = fullTxt.substring(0, this.txt.length - 1);
        }
        else {
        this.txt = fullTxt.substring(0, this.txt.length + 1);
        }
    
        this.el.innerHTML = '<span class="wrap">'+this.txt+'</span>';

        var that = this;
        var delta = 200 - Math.random() * 100;

        if (this.isDeleting) { delta /= 2; }

        if (!this.isDeleting && this.txt === fullTxt) {
        delta = this.period;
        this.isDeleting = true;
        } else if (this.isDeleting && this.txt=== '') {
        this.isDeleting = false;
        this.loopNum++;
        delta = 500;
        }
        setTimeout(function(){
            that.tick();
        }, delta);
        };
    
        window.onload = function() {
            var elements = document.getElementsByClassName('typewrite');
            for(var i=0; i<elements.length; i++){
                var toRotate = elements[i].getAttribute('data-type');
                var period = elements[i].getAttribute('data-period');
                if(toRotate){
                    new TxtType(elements[i], JSON.parse(toRotate) , period);
                }
            }
            //INJECT CSS
            var css= document.createElement("style");
            css.type = "text/css";
            css.innerHTML = ".typewrite > .wrap{ border-right : 0.08em solid #fff}";
            document.body.appendchild(css);
    
        };

//counter

(function($) {
        "use strict";
        function count($this){
        var current = parseInt($this.html(), 10);
        current = current + 1; /* Where 50 is increment */
        $this.html(++current);
            if(current > $this.data('count')){
                $this.html($this.data('count'));
            } else {
                setTimeout(function(){count($this)}, 50);
            }
        }
        $(".stat-count").each(function() {
          $(this).data('count', parseInt($(this).html(), 10));
          $(this).html('0');
          count($(this));
        });
    })(jQuery);
    
// smoth scroll

/*smoth scrolling*/

$(document).ready(function(){
    $('.menu a').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'')
        && location.hostname == this.hostname) {
            var $target = $(this.hash);
            $target = $target.length && $target
            || $('[name=' + this.hash.slice(1) +']');
            if ($target.length) {
                var targetoffset = $target.offset().top;
                $('html,body')
                .animate({scrollTop: targetoffset}, 1000);
                return false;
            }
        }
    });
});
    
// fixed header

jQuery(window).scroll(function() {
    if (jQuery(window).scrollTop() >= 10) {
        jQuery('#home').addClass('fixed-header');
    }
    else {
        jQuery('#home').removeClass('fixed-header');
    }
});

/*scroll to top*/

//Get the button:

/*Scroll to top when arrow up clicked BEGIN*/
$(window).scroll(function() {
    var height = $(window).scrollTop();
    if (height > 100) {
        $('#back2Top').fadeIn();
    } else {
        $('#back2Top').fadeOut();
    }
});
$(document).ready(function() {
    $("#back2Top").click(function(event) {
        event.preventDefault();
        $("html, body").animate({ scrollTop: 0 }, "slow");
        return false;
    });

});
