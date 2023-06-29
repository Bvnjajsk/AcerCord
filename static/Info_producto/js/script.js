$(document).ready(function(){
    $("#enviar").click(function(){
        $.get("https://deliciasmaullin-default-rtdb.firebaseio.com/1.json",
        function(data){
            $.each(data.categories,function(i,item){
                $("#categorias").append("<tr><td>" + item.idCategory + "</td><td>" + 
                item.strCategory + "</td><td><img src='" + item.strCategoryThumb+
                "'></td><td>" + item.strCategoryDescription+"</td></tr>");
            });
        });
    });
});