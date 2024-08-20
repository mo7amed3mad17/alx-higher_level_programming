#!/usr/bin/node

$(document).ready(function() {
  $('#toggle_header').on('click', function() {
    // Check if header has red class
    if ($('header').hasClass('red')) {
      // If red class exists, remove it and add green class
      $('header').removeClass('red').addClass('green');
    } else {
      // If red class doesn't exist, remove green class and add red class
      $('header').removeClass('green').addClass('red');
    }
  });
});
