var data;
var user = 'harrison';
console.log(1)
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


function convertDate( timestamp ) {
  var _dateObj = $.parseJSON( '{"created": ' + timestamp + '}' );
  var _date = new Date( 1000 * _dateObj.created );

  return _date.toString();
}