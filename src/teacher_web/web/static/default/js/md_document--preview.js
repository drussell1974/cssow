$('#collapseMarkdown').on('show.bs.collapse', function () {
    
    const resource_id = document.querySelector("input[name='id']").value
    if (resource_id > 0) {
        const MARKDOWN_SERVICE_URI = document.querySelector("#ctl-md_document_service_uri").value;
        const scheme_of_work_id = document.querySelector("input[name='scheme_of_work_id']").value;
        const lesson_id = document.querySelector("input[name='lesson_id']").value
        const md_document_name = document.querySelector("input[name='md_document_name']").value
        const preview_selector = document.querySelector(".markdown-body");
        const uri = `${MARKDOWN_SERVICE_URI}/${scheme_of_work_id}/${lesson_id}/${resource_id}/${md_document_name}?format=json`;
    
        preview_selector.innerHTML = "loading...";
        
        fetch(uri)
            .then(res => res.json())
            .then(
                (result) => {
                    
                    preview_selector.innerHTML = result;
                },
                (error) => {
                    preview_selector.innerHTML = `<p>unable to preview document at this time</p><p class="error">${error}</p>` ;
                }
            );
}
// do something…
})