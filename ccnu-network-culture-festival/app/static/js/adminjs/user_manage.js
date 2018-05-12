$(function () {

    //User 3
    //Moderator 1
    //Admin 2
     $(".User").click(function () {
        var ID=$(this).parent().parent().parent().parent().siblings().eq(0).text();
        var jurisdiction=3;
        var url="/admin/api/user/"+ID+"/manage/";
        $.ajax({
            url: url,
            type:"PATCH",
            data: {"jurisdiction":jurisdiction},
            success: function( result ) {
                window.location.reload();
            }
        });
    });

     $(".Moderator").click(function () {
        var ID=$(this).parent().parent().parent().parent().siblings().eq(0).text();
        var jurisdiction=1;
        var url="/admin/api/user/"+ID+"/manage/";
        $.ajax({
            url: url,
            type:"PATCH",
            data: {"jurisdiction":jurisdiction},
            success: function( result ) {
                window.location.reload();
            }
        });
    });

     $(".Admin").click(function () {
        var ID=$(this).parent().parent().parent().parent().siblings().eq(0).text();
        var jurisdiction=2;
        var url="/admin/api/user/"+ID+"/manage/";
        $.ajax({
            url: url,
            type:"PATCH",
            data: {"jurisdiction":jurisdiction},
            success: function( result ) {
                window.location.reload();
            }
        });
    });

     //删除按钮被点击
     $(".btn-danger").click(function () {
         var ID=$(this).parent().siblings().eq(0).text();
         var url="/admin/api/user/"+ID+"/manage/";
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
