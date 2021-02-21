 //course_id, 
const md_document_control_group = document.querySelector("#md_document--control-group");
const md_file_control = document.querySelector("#ctl-md_file");
const page_uri_control_group = document.querySelector("#page_uri--control-group");
const page_uri_control = document.querySelector("#ctl-uri");
const md_document_name_control = document.querySelector("#ctl-md_document_name");
const type_field = document.querySelector("#ctl-type_id");

ctl_attr_settings = {
    "6": { // Bbok
        "md_document_control_group.style.display":"none",
        "md_document_name_control.required":false,
        "md_file_control.required ":false,
        "page_uri_control_group.style.display":"block",
        "page_uri_control.required":false,
        "page_uri_control.disabled":false,
        "page_uri_control.placeholder":"Enter a link, starting http or https (optional)"
    },
    "7": { // Video
        "md_document_control_group.style.display":"none",
        "md_document_name_control.required":false,
        "md_file_control.required ":false,
        "page_uri_control_group.style.display":"block",
        "page_uri_control.required":true,
        "page_uri_control.disabled":false,
        "page_uri_control.placeholder":"Enter a link, starting http or https (required)"
    },
    "8": { // Website
        "md_document_control_group.style.display":"none",
        "md_document_name_control.required":false,
        "md_file_control.required ":false,
        "page_uri_control_group.style.display":"block",
        "page_uri_control.required":true,
        "page_uri_control.disabled":false,
        "page_uri_control.placeholder":"Enter a link, starting http or https (required)"
    },
    "10": { // Markdown
        "md_document_control_group.style.display":"block",
        "md_document_name_control.required":true,
        "md_file_control.required ":false,
        "page_uri_control_group.style.display":"block",
        "page_uri_control.required":false,
        "page_uri_control.disabled":true,
        "page_uri_control.placeholder":"Enter a link, starting http or https (use upload a markdown document)"
    },
}

function showHideMarkdownUpload(value) {
    // get comparison value from settings TODO: get value from settings
    if (value !== undefined) {
        settings = ctl_attr_settings[value]

        if (settings !== undefined) {
            md_document_control_group.style.display = settings["md_document_control_group.style.display"]
            md_document_name_control.required = settings["md_document_name_control.required"]
            md_file_control.required = settings["md_file_control.required"]
            page_uri_control_group.style.display = settings["page_uri_control_group.style.display"]
            page_uri_control.required = settings["page_uri_control.required"]
            page_uri_control.disabled = settings["page_uri_control.disabled"]
            page_uri_control.placeholder = settings["page_uri_control.placeholder"]
        }
    }
}

type_field.addEventListener('change', (e) => {
    showHideMarkdownUpload(e.target.value);
})

window.addEventListener('load', () => {
    showHideMarkdownUpload(type_field.value);
})