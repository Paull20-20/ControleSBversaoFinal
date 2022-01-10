$(document).ready(function(){
    
    //Evento para o botão excluir, não deletar direto, após isso faremos uma verificação para saber se o user deseja mesmo excluir
    var deleteBtn = $('.delete-btn');


    $(deleteBtn).on('click', function(e){
        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer mesmo deletar o item solicitado ?');

        if(result){
            window.location.href = delLink;
        }

    });




})
