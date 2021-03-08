let orig_notes = {};

var hide_hidden_words = (notes, phrase, id) => {
    orig_notes[id] = notes.textContent;
    var regPhrase = new RegExp(phrase.trim(), "ig");
    let placeholder = Array(phrase.trim().length).join('_');
    notes.textContent = notes.textContent.replace(regPhrase, placeholder);
}

var reveal_hidden_words = (notes, id) => {
    notes.textContent = orig_notes[id];
}

var previewMissingWordsChallengeShowAllOnClick = (button_id, card_class_selector) => {
    const btn = document.getElementById(button_id);
    btn.addEventListener('click', () => {
        const els = document.querySelectorAll(card_class_selector);
        Array.prototype.forEach.call(els, function(card_elem) {
            const id = card_elem.getAttribute('data-target');
            const notes = card_elem.querySelector(".class-notes");
            const replace_words = card_elem.querySelector(".missing-words-challenge");
            const replace_words_list = replace_words.textContent.split(',');
            replace_words_list.map(phrase => {
                reveal_hidden_words(notes, phrase, id);
            });
        })
    });
};

var previewMissingWordsChallengeHideAllOnClick = (button_id, card_class_selector) => {
    const btn = document.getElementById(button_id);
    btn.addEventListener('click', () => {
        const els = document.querySelectorAll(card_class_selector);
        Array.prototype.forEach.call(els, function(card_elem) {
            const id = card_elem.getAttribute('data-target');
            console.log(id);
            const notes = card_elem.querySelector(".class-notes");
            orig_notes[id] = notes.textContent;
            const replace_words = card_elem.querySelector(".missing-words-challenge");
            const replace_words_list = replace_words.textContent.split(',');
            // get current card
            hide_hidden_words(notes, id);
        })
    });
};

var previewMissingWordsChallengeToggleOnClick = (button_class) => {
  var els = document.getElementsByClassName(button_class);
  
  Array.prototype.forEach.call(els, function(el) {
  
      const id = el.getAttribute('data-target');
      const card_elem = document.querySelector('#' + id);
      
      const notes = card_elem.querySelector(".class-notes");
      const replace_words = card_elem.querySelector(".missing-words-challenge");
      const replace_words_list = replace_words.textContent.split(',');
      let hidden = false;
      // store original text
      el.addEventListener('click', () => {
        // get current card
        if (hidden) {
            reveal_hidden_words(notes, id);
            hidden = false;
        } else {
            replace_words_list.map(phrase => {
                hide_hidden_words(notes, phrase, id);
            });
            hidden = true;  
        };
    });
  });
}
