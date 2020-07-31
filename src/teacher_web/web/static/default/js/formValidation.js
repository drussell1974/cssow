
(function() { 
  'use strict';
  window.addEventListener('load', function() {
    
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');

    function onCancelPressed(event) {           
      // do not submit
      event.preventDefault();
      event.stopPropagation();
    
      $("#cancelModal").on("hidden.bs.modal", function() {
        Array.prototype.filter.call(forms, function(form) {
          form.removeAttribute('novalidate');
        })
      })
    
      $("#cancelModal").modal("show");
    
      $("#cancelModalContinueButton").click(function() {
        window.history.back();
      })
    }
    
    function onDeletePressed(event) {           
      // do not submit
      event.preventDefault();
      //event.stopPropagation();
    
      // contains href button

      $("#deleteModal").modal("show");

      $("#deleteModalContinueButton").click(function() {
        form.submit();
      })
    }

    // prevent validation when cancel button is clicked 

    document.getElementById('cancelButton').addEventListener('click', function(event) {
      // set all forms to cancel validation
      Array.prototype.filter.call(forms, function(form) {
        form.setAttribute('novalidate', "");
      })
    });

    // prevent validation when delete button is clicked 
    var deleteButtonElem = document.getElementById('deleteButton');
    if (deleteButtonElem != undefined) { 
      deleteButtonElem.addEventListener('click', function(event) {
        // set all forms to cancel validation
        Array.prototype.filter.call(forms, function(form) {
          form.setAttribute('novalidate', "");
        })
      });
    }

    // Get validation errors from hidden field
    function showValidationErrors() {
      // get validation errors
      var dangerClassName = "help-block text-danger invalid-feedback";

      var string_errors = document.getElementById("hdn-validation_errors") || "{}";
      if (string_errors != "{}"){
        var dict_errors = JSON.parse(string_errors.value.replace(new RegExp("'","g"),"\""));
        console.log(typeof dict_errors)
        for (var key in dict_errors) {
          var inputElem = document.querySelector(`input[name='${key}']`);
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
    
        let submitter = event.submitter;
        let handler = submitter.id;
        

        if (handler == "cancelButton") {
    
          // Cancel button was pressed
    
          onCancelPressed(event);

        } else if (handler == "deleteButton") {
          
          // Delete button was pressed
        
          onDeletePressed(event);

        } else {

          // validate anything else

          if (form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
          }
          form.classList.add('was-validated');
        }

      }, false);
    });

    showValidationErrors();

  }, false);
}());