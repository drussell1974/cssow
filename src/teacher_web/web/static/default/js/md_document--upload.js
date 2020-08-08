 //scheme_of_work_id, 
 const md_document_control_group = document.querySelector("#md_document--control-group");
 const md_file_control = document.querySelector("#ctl-md_file");
 const md_document_name_control = document.querySelector("#ctl-md_document_name");
 const type_field = document.querySelector("#ctl-type_id");    
 
 function showHideMarkdownUpload(value) {
     // get comparison value from settings
     if (value != 10) {
         md_document_control_group.style.display = "none";
         md_file_control.required = false;
         md_document_name_control.required = false;
     } else if (md_document_name_control != null && md_document_name_control.value == "") {
         md_document_control_group.style.display = "block";
         md_file_control.required = true;
         md_document_name_control.required = false;
     } else {
         md_document_control_group.style.display = "block";
         md_file_control.required = false;
         md_document_name_control.required = true;
     }
 }

 type_field.addEventListener('change', (e) => {
     showHideMarkdownUpload(e.target.value);
 })

 window.addEventListener('load', () => {
     showHideMarkdownUpload(type_field.value);
 })