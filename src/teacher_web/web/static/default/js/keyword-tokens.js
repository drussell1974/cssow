function keyword_token_handler(get_keywords_url, token_input_css_selector, invalid_tokens_css_selector, invalid_classes, modal_id, modal_id_id, modal_title_id, modal_definition_id, modal_save_button_id, on_remove_token) {
  
  keyword_options = [];
  has_initialized = false;
  suppress_modal = false;
  
  function transform_keyword_options(result) {
    result.keywords.map(x => { 
      keyword_options.push({ value: x.term, term: x.term, id: x.id, definition: x.definition, number_of_lessons: x.number_of_lessons, is_valid: x.is_valid, published: x.published, is_new: false }); 
    }); 
  }

  function get_keyword_data(active_token_attrs) {        
    var found = keyword_options.find(x => x.value == active_token_attrs.value);
    if (found != undefined) { // item has been found
      
      active_token_attrs.id = found.id;
      active_token_attrs.term = found.value;
      active_token_attrs.definition = found.definition;
      active_token_attrs.is_valid = found.is_valid;
      active_token_attrs.number_of_lessons = found.number_of_lessons;
      active_token_attrs.published = found.published;
      active_token_attrs.is_new = found.is_new;
    } else {

      // set defaults (not valid)
      active_token_attrs.id = 0;
      active_token_attrs.term = active_token_attrs.value;
      active_token_attrs.definition = "";
      active_token_attrs.is_valid = false;
      active_token_attrs.number_of_lessons = 0;
      active_token_attrs.published = 1;
      active_token_attrs.is_new = true;
    }
  }

  function invalidator(target, keyword_data) {
    var invalid_tokens = document.querySelectorAll(invalid_tokens_css_selector);
    // handle no is_valid varialbe
    if (invalid_tokens.length == 1 && keyword_data.is_valid === false) {
      // there is one invalid token and this 
      // one being removed is invalid then
      // we can assume everything is valid
      target.removeClass(invalid_classes);
    }
  }

  function validate(target, form_control, active_token_attrs) {

    var re = /[^0-9,!-/)]([A-Za-z0-9 ]+)?/g
    
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

  function target_modal(target, active_token_attrs) {
    // assign modal class to token and store data
    target.attr("data-toggle", "modal");
    target.attr("data-target",modal_id);
    target.attr("data-keyword_id", active_token_attrs.id);
    target.attr("data-keyword_term", active_token_attrs.term);
    target.attr("data-keyword_defintion", active_token_attrs.definition);
    target.attr("data-number_of_lessons", active_token_attrs.number_of_lessons);
    target.attr("data-published", active_token_attrs.published);
    target.attr("data-is_new", active_token_attrs.is_new);

    // handle open and close dialog
    target.click(function(e) {
      // do not open if modal has been suppress (e.g. when token is being removed)
      if (suppress_modal == true) {
        suppress_modal = false;
        return false;
      }   

      if(active_token_attrs !== undefined && active_token_attrs !== null) {
        $(modal_id_id).val(active_token_attrs.id);
        $(modal_title_id).val(active_token_attrs.term);
        $(modal_definition_id).val(active_token_attrs.definition);
        // update keyword definitions when finished
        $(modal_save_button_id).click(function (e) {

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
            // stop modal from closing from save button
            $(modal_title_id).addClass(invalid_classes);
          } else {
            
            // update active token
            active_token_attrs.id = modal_data.id;
            active_token_attrs.value = modal_data.value;
            active_token_attrs.term = modal_data.value;
            active_token_attrs.definition = modal_data.definition;
            
            // close the modal
            $(modal_id).modal('hide');
          }
        })
      }
    });
  }

  function fetch_keywords_from_service(show_all) {
    $.ajax({url:get_keywords_url + `?show_all=${show_all}`,
      success: function(result){   
    
        transform_keyword_options(result);
    
        $(token_input_css_selector).tokenfield({
          autocomplete: {
            source: keyword_options,
            delay: 100
          },
          showAutocompleteOnFocus: true,
        })
      },
      error: function(){
          $("#token-error").html('Could not get keywords at this time');
      }
    });
  }
  // events

  $(token_input_css_selector).on('tokenfield:initialize', function (e) {
    has_initialized = true;    
  });

  $(token_input_css_selector).on('tokenfield:removetoken', function (e) {
    suppress_modal = true;
    
    return on_remove_token(e);
  });

  $(token_input_css_selector).on('tokenfield:removetoken tokenfield:edittoken', function (e) {
    invalidator($(e.relatedTarget).parent(), e.attrs);
  });

  $(token_input_css_selector).on('tokenfield:createtoken', function (e) {
    // look up in the list of keywords (find gets the first item)
    if(e.attrs.id === undefined){
      // assign as invalid
      e.attrs.is_valid = false;
      // check if exists and update values accordingly
      get_keyword_data(e.attrs);
    } 
    // any new terms marked new
    if (has_initialized == true) {
      e.attrs.is_new = true;
    }
  });

  $(token_input_css_selector).on('tokenfield:createdtoken tokenfield:editedtoken', function (e) {
    var target = $(e.relatedTarget);
    
    validate(target, target.parent(), e.attrs);
    
    if(e.attrs.is_valid) {
      target_modal(target, e.attrs);
    }
  })

  fetch_keywords_from_service();
}
