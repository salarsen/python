$(document).ready(function(){
    console.log("Jquery seems to exist");
    // process_notes("");
    $.get('/load_notes',function(res){
        process_notes(res);
    });
});


function process_notes(notes){
    console.log("loaded function");
    $('#notes').html(notes);

    //unbind submit to prevent duplicate submits (goes exponential if not careful)
    $('form').unbind('submit');

    //wipe new note input
    $('#new_note').children('[name*="title"]').val("");

    $('form').submit(function(){
        console.log("form submitted");
        if($(this).attr('name') == "new_note"){
            console.log("adding new note");
            $.post('/new_note',$(this).serialize(),function(res){
                process_notes(res);
            });
        } else if ($(this).attr('name') == "update"){
            console.log("updating note");
            console.log($(this).serialize());
            $.post('/update',$(this).serialize(),function(res){
                process_notes(res);
            });
        } else if ($(this).attr('name') == "delete"){
            console.log("removing note");
            $.post('/delete',$(this).serialize(),function(res){
                process_notes(res);
            });
        }
        return false;
    });

    $('p').click(function(){
        if ($(this).attr('name') == "title"){
            $(this).replaceWith('<p><input type="text" name="title" value="'+$(this).html()+'" /></p>')
        }else if($(this).attr('name') == "description"){
            $(this).replaceWith('<p><textarea name="description">'+$(this).html()+'</textarea></p>');
        }
    })
}
