$(function() {

    var hashtags = false;

    $(document).on('keydown', '#myInputField', function (e) {
        arrow = {
            hashtag: 51,
            space: 32
        };

        var input_field = $(this);
        switch (e.which) {
            case arrow.hashtag:
                input_field.val(input_field.val() + "<span class='highlight'>");
                hashtags = true;
                break;
            case arrow.space:
                if(hashtags) {
                    input_field.val(input_field.val() + "</span>");
                    hashtags = false;
                }
                break;
        }

    });

});

      $('#tags_1').tagsInput({width:'auto'});
      $('#tags_2').tagsInput({
        width: 'auto',
        onChange: function(elem, elem_tags)
        {
          var languages = ['php','ruby','javascript'];
          $('.tag', elem_tags).each(function()
          {
            if($(this).text().search(new RegExp('\\b(' + languages.join('|') + ')\\b')) >= 0)
              $(this).css('background-color', 'yellow');
          });
        }
      });