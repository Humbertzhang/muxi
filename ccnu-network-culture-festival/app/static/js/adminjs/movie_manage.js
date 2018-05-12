$(function () {
     //通过按钮被点击
     $(".btn-success").click(function () {
        var ID=$(this).parent().siblings().eq(0).text();
        var url="/admin/api/movie/"+ID+"/manage/";
        $.ajax({
            url: url,
            type:"PATCH",
            data: {},
            success: function( result ) {
                window.location.reload();
            }
        });
    });

     //删除按钮被点击
     $(".btn-danger").click(function () {
         var ID=$(this).parent().siblings().eq(0).text();
         var url="/admin/api/movie/"+ID+"/manage/";

         $.ajax({
             url: url,
             type:"DELETE",
             data: {},
             success: function( result ) {
                window.location.reload();
            }
        });
     });
});
