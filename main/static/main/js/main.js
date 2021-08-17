$(".confirm").on("click",function(e){
    if(confirm("O'chirishni xohlaysizmi?")){
        return true;
    }
    e.preventDefault();
    return false;
});