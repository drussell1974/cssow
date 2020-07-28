(function() { 
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        var invalid_tokens = document.querySelectorAll(".tokenfield .invalid");
        if (form.checkValidity() === false || Array.from(invalid_tokens).length > 0) {
          event.preventDefault();
          event.stopPropagation();
        } else {
            // get token data from token feild
            var keyword_tokens = $("#keywords-tokenfield").tokenfield('getTokens');
            console.log(`add keyword tokens for form POST (${JSON.stringify(keyword_tokens)})`);
            $("#hdn-key_words").val(JSON.stringify(keyword_tokens));
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
}());