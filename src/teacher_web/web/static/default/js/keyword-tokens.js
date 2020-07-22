var keywordservice = {
    dict: [],
    init: (results) => {
      results.map(x => { 
        keywordservice.dict.push({ key:x.term, value: x }); 
      });
    },
    getkeywordsonly: () => {
        return keywordservice.dict.map(x => x.key);
    },
    getid_or_term: (search_term) => {
        item = keywordservice.dict.find(x => x.key === search_term);
        if(item === undefined || item.length === 0) {
          return search_term; // treat as a new object
        } else {
          return item.value.id // return first result
        }
    }
}

function init_keyword_tokens(get_keywords_url, token_input_css_selector, all_tokens_css_selector, form_field_selector, error_css_selector) {
      $.ajax({url:get_keywords_url,
        success: function(result){
          keywordservice.init(result.keywords);

          $(token_input_css_selector).tokenfield({
            autocomplete: {
              source: keywordservice.getkeywordsonly(),
              delay: 100
            },
            showAutocompleteOnFocus: true,
          })
        },
        error: function(){
            $("#token-error").html('Could not get keywords at this time');
        }
      });

    $("#keywords-tokenfield").on('tokenfield:createdtoken tokenfield:editedtoken tokenfield:removedtoken', function (e) {
        // create array to turn into comma-seperated list
        var labels = document.querySelectorAll(all_tokens_css_selector);
        var labelsArr = Array.prototype.slice.call(labels);
        var keywordsArr = labelsArr.map(x => { return x.innerText }).join(",");
        document.querySelector(form_field_selector).value = keywordsArr.split(",").map(kw => keywordservice.getid_or_term(kw));
        console.log(form_field_selector + ":-" + document.querySelector("#hdn-key_words").value)
    })
}