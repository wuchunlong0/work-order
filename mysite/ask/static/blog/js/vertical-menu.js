
$(document).ready(function(){
    dropdownOpen();//调用
});
/**
 * 鼠标划过就展开子菜单，免得需要点击才能展开
 */
function dropdownOpen() {
    var $dropdownLi = $('li.dropdown');
    $dropdownLi.mouseover(function() {
        $(this).addClass('open');
    }).mouseout(function() {
        $(this).removeClass('open');
    });
}


/*自定义垂直菜单  与菜单vertical-menu.css class="active" 配合使用   放入最后 */
$('.vertical-menu a').click(function(){
  $(this).addClass("active").siblings("a").removeClass("active");
})