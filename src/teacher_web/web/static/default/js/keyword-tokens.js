function keyword_token_handler(get_keywords_url, token_input_css_selector, invalid_tokens_css_selector, invalid_classes, form_keyword_post, modal_id, modal_id_id, modal_title_id, modal_definition_id, modal_save_button_id) {

  keyword_options = [];
  
  function transform_keyword_options(result) {
    result.keywords.map(x => { 
      keyword_options.push({ value: x.term, term: x.term, id: x.id, definition: x.definition, is_valid: x.is_valid }); 
    }); 
  }

  function get_keyword_data(active_token_attrs) {        
    var found = keyword_options.find(x => x.value == active_token_attrs.value);
    if (found !== undefined) { // item has been found
      active_token_attrs.id = found.id;
      active_token_attrs.term = found.value;
      active_token_attrs.definition = found.definition;
      active_token_attrs.is_valid = found.is_valid;
    } else {
      // set defaults (not valid)
      active_token_attrs.id = 0;
      active_token_attrs.term = active_token_attrs.value;
      active_token_attrs.definition = "";
      active_token_attrs.is_valid = false;
    }
  }

  function invalidator(target, keyword_data) {
    var invalid_tokens = document.querySelectorAll(invalid_tokens_css_selector);
    console.log(`there are ${invalid_tokens.length} invalid tokens`);
    // handle no is_valid varialbe
    if (invalid_tokens.length == 1 && keyword_data.is_valid === false) {
      // there is one invalid token and this 
      // one being removed is invalid then
      // we can assume everything is valid
      target.removeClass(invalid_classes);
    }
  }

  function validate(target, form_control, active_token_attrs) {
    console.log(`validating keyword id:${active_token_attrs.id} value:${active_token_attrs.value} term:${active_token_attrs.term} definition:${active_token_attrs.definition} is_valid:${active_token_attrs.is_valid}`);

    var re = /[^0-9,!-)]([A-Za-z0-9 ]+)?/g
    
    active_token_attrs.is_valid = re.test(active_token_attrs.value);
    
    // display invalid
    if (!active_token_attrs.is_valid) {
      target.addClass(invalid_classes);
      form_control.addClass(invalid_classes);
    } else {
      target.removeClass(invalid_classes);
      form_control.removeClass(invalid_classes);
      //target.attr("data-keyword", JSON.stringify(keyword_data));
    }
    return active_token_attrs.is_valid;
  }

  function assign_modal(target, active_token_attrs) {
    // assign modal to token and store data
    target.attr("data-toggle", "modal");
    target.attr("data-target",modal_id);
    // handle open and close dialog
    target.click(function(e) {
      
      // get key_word
      //key_word = $(e.target).parent().data('keyword');
      
      if(active_token_attrs !== undefined && active_token_attrs !== null) {
        $(modal_id_id).val(active_token_attrs.id);
        $(modal_title_id).val(active_token_attrs.term);
        $(modal_definition_id).val(active_token_attrs.definition);
      
        // update keyword definitions when finished
        //$(modal_id).on('hidden.bs.modal', function(e) {
        $(modal_save_button_id).click(function (e) {

          //e.preventDefault();

          // update data on target
          console.log(`saving definition...`)
          
          // get values from modal form
          
          var modal_data = {
            id: $(modal_id_id).val(),
            value: $(modal_title_id).val(),
            definition: $(modal_definition_id).val(),
            is_valid: false
          }
            
          // validate form to show errors

          modal_data.is_valid = validate(target, $(modal_title_id), modal_data);
    
          if(!modal_data.is_valid){
            $(modal_title_id).addClass(invalid_classes);

            // stop modal from closing from save button
          } else {
            
            // update token data and close form

            console.log("modal updating token data...");

            // update active token
            active_token_attrs.id = modal_data.id;
            active_token_attrs.value = modal_data.value;
            active_token_attrs.term = modal_data.value;
            active_token_attrs.definition = modal_data.definition;
            
            // update label

            //active_token_attrs.label = modal_data.value;
         
            // close the modal
            $(modal_id).modal('hide');
         
          }
        })
      }
    });
  }

  $.ajax({url:get_keywords_url,
    success: function(result){   
      
      transform_keyword_options(result);

      $(token_input_css_selector).tokenfield({
        autocomplete: {
          source: keyword_options, //keywordservice.getkeywordsonly(),
          delay: 100
        },
        showAutocompleteOnFocus: true,
      })
    },
    error: function(){
        $("#token-error").html('Could not get keywords at this time');
    }
  });

  // events

  $(token_input_css_selector).on('tokenfield:createtoken', function (e) {
    console.log('tokenfield:createtoken:....')
  });

  $(token_input_css_selector).on('tokenfield:createdtoken', function (e) {
    console.log('tokenfield:createdtoken:....')
  });
  
  $(token_input_css_selector).on('tokenfield:edittoken', function (e) {
    console.log('tokenfield:edittoken:....')
  });

  $(token_input_css_selector).on('tokenfield:editedtoken', function (e) {
    console.log('tokenfield:editedtoken:....')
  });

  $(token_input_css_selector).on('tokenfield:removetoken', function (e) {
    console.log('tokenfield:removetoken:....')
  });

  $(token_input_css_selector).on('tokenfield:removedtoken', function (e) {
    console.log('tokenfield:removedtoken:....')
  });

  $(token_input_css_selector).on('tokenfield:removetoken tokenfield:edittoken', function (e) {
    console.log('tokenfield:removetoken tokenfield:edittoken: invalidating....')
    invalidator($(e.relatedTarget).parent(), e.attrs);
  });

  $(token_input_css_selector).on('tokenfield:createtoken', function (e) {
    console.log('tokenfield:createtoken: get existing data if new....')
    // on the form the Keywords are initially loaded with the value only...
    // look up in the list of keywords (find gets the first item)
    if(e.attrs.id === undefined){
      // assign as invalid
      e.attrs.is_valid = false;
      // check if exists and update values accordingly
      get_keyword_data(e.attrs);
    }
  });

  $(token_input_css_selector).on('tokenfield:createdtoken tokenfield:editedtoken', function (e) {
    console.log('tokenfield:createdtoken tokenfield:editedtoken: validate and allow modal....')
    var target = $(e.relatedTarget);
    
    validate(target, target.parent(), e.attrs);

    if(e.attrs.is_valid) {
      assign_modal(target, e.attrs);
    }
  })
}
