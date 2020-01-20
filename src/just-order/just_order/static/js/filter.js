$("#select_tag").change(function(){
    var selected = $(this).children("option:selected").val();
    var tags = $(".tags");
    if(selected === "---"){
        show(tags);
        return;
    }

    for (let i in tags){
        var tag = tags[i].innerHTML;
        if(tag == undefined){
            continue;
        }

        if (tag.indexOf(selected) === -1){
            hideParent(tags[i]);
        }else{
            showParent(tags[i]);
        }
    }
});


function show(tags){
    for (let i in tags){
        showParent(tags[i]);
    }
}

function showParent(tag){
    $(tag).parent().parent().removeClass("d-none");
    $(tag).parent().parent().addClass("d-flex");
}

function hideParent(tag){
    $(tag).parent().parent().removeClass("d-flex");
    $(tag).parent().parent().addClass("d-none");
}
