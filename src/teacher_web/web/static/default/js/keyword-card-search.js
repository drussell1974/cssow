function is_match(e) {
    // TODO: partial search
    var current_term = e.querySelector(".card-title").textContent;
    var search_term = input.value;
    return (current_term.toUpperCase().includes(search_term.toUpperCase()));
};  

function on_enter_search_term(e) {
    var elems = Array.from(document.querySelectorAll(".card-keyword"));
    // filter based on search
    elems.forEach(e => e.style.display = is_match(e) ? 'block' : 'none');
};

var input = document.querySelector("#ctl-keyword_search");

input.addEventListener('input', on_enter_search_term);