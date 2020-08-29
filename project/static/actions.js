$(document).ready(
  function(){
    $("form a").click(function(){ 
        if ($(this).text()=="Edit"){
            var closestParentRow = $(this).parent().closest('div').eq(0);
            closestParentRow.find(".viewmode").hide();
            closestParentRow.find(".editmode").show();
        }else if ($(this).text()=="Cancel"){
            var closestParentRow = $(this).parent().closest('div').eq(0);
            closestParentRow.find(".viewmode").show();
            closestParentRow.find(".editmode").hide();
        }
    });
});
