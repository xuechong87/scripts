//.recruit-sidebar{position:fixed;display:none;}
$(window,document).on("scroll",function(){
    var totalH = $(document).height();//文档总高度
    var eleH = 550;//元素高度
    var originPadTop = 420;//初始高度
    var btmH = 452;//元素在最底部时 元素底部与文档底部高度差
    var floationPadTop = 80;//悬浮时顶部高度

    function ch(scT){

        if(scT<=originPadTop-floationPadTop){
            return originPadTop-scT;
        }

        if((totalH-scT) <= (btmH + eleH + originPadTop)){
            return originPadTop -((btmH + eleH + originPadTop)-(totalH-scT));
        }

        return floationPadTop;
    }
    var topV = ch($(window).scrollTop());

    $(".recruit-sidebar").css({
        top:topV
    });

});

$(window).scroll();

$(".recruit-sidebar").show();