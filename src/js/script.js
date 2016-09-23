(function(){

var data;
var user = 'harrison';

$.get( 'data.json', function( data ) {
  data = JSON.parse( data );

  $.each( data, function() {
    var tr = $('<tr/>');

    tr.append( $('<td/>').text( convertDate( this.date ) ) );
    tr.append( $('<td/>').text( this.description ) );

    if ( this.donor == user ) {
      tr.append( $('<td/>').text( this.value * -1 ) );
      tr.append( $('<td/>').text( this.receiver ) );
    } else {
      tr.append( $('<td/>').text( this.value ) );
      tr.append( $('<td/>').text( this.donor ) );
    }

    $( '.transitions' ).append( tr );
  });
});

$('#form-add').submit(function(e) {
  e.preventDefault();

  var form = $(this);
  var data = form.serialize();

  $.post('http://192.168.1.29:5000/transaction/', data, function(response) {
    form.find('.feedback').text('Adicionado :) |||| ' + data.toString() + ' |||| ' + response);
  })

});

$('.delete').on('click', function(e) {
  var button = $(e.currentTarget);
  var id = button.attr('transaction-id');

  $.post('.', id, function(response) {
    console.log(response);
    console.log(button.closest('tr').remove());
  })
});

$('#add-button').on('click', function() {
  $('#form-add').addClass('show');
})

function convertDate( timestamp ) {
  var _dateObj = $.parseJSON( '{"created": ' + timestamp + '}' );
  var _date = new Date( 1000 * _dateObj.created );

  return _date.toString();
}

})();