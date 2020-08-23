
(function() { 
  'use strict';
  window.addEventListener('load', function() {
    
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');

    // Get validation errors from hidden field
    function showValidationErrors() {
      // get validation errors
      var dangerClassName = "help-block text-danger invalid-feedback";

      var string_errors = document.getElementById("hdn-validation_errors") || "{}";
      if (string_errors.value.length > 2) {
        var dict_errors = JSON.parse(string_errors.value.replace(new RegExp("'","g"),"\""));
        console.log(dict_errors)
        console.log(typeof dict_errors)
        for (var key in dict_errors) {
          var inputElem = document.querySelector(`input[name='${key}'], select[name='${key}']`);
          if (inputElem != null) {   
            var dangerElem = inputElem.parentNode.getElementsByClassName(dangerClassName);
            if (dangerElem != null) {
              dangerElem[0].innerText = dict_errors[key];
              dangerElem[0].setAttribute("style", "display:block");
              dangerElem[0].innerText = dict_errors[key];
            } else {
              dangerElem = document.createElement("div");        
              dangerElem.className = dangerClassName;
              dangerElem.innerText = dict_errors[key];
              inputElem.parentNode.appendChild(dangerElem);
            }
          }
        }
      }
    }
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
    
    
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      

      }, false);
    });

    showValidationErrors();

  }, false);
}());