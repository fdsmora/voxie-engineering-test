$(document).ready(
  function(){
    $("form input").click(function(){ 
        if ($(this).val()=="Edit"){
            var closestParentRow = $(this).parent().closest('div').eq(0);
            closestParentRow.find(".viewmode").hide();
            closestParentRow.find(".editmode").show();
        }else if ($(this).val()=="Cancel"){
            var closestParentRow = $(this).parent().closest('div').eq(0);
            closestParentRow.find(".viewmode").show();
            closestParentRow.find(".editmode").hide();
        }
    });
});
