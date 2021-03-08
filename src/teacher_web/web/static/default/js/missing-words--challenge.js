let orig_notes = {};

var hide_hidden_words = (notes, phrase, id) => {
    var regPhrase = new RegExp(phrase.trim(), "ig");
    let placeholder = Array(phrase.trim().length).join('_');
    notes.textContent = notes.textContent.replace(regPhrase, placeholder);
}

var reveal_hidden_words = (notes, id) => {
    notes.textContent = orig_notes[id];
}

var previewMissingWordsChallengeToggleOnClick = (button_class) => {
  var els = document.getElementsByClassName(button_class);
  Array.prototype.forEach.call(els, function(el) {
  
      const id = el.getAttribute('data-target');
      const card_elem = document.querySelector('#' + id);
      const notes = card_elem.querySelector(".class-notes");
      orig_notes[id] = notes.textContent;
      const replace_words = card_elem.querySelector(".missing-words-challenge");
      const replace_words_list = replace_words.textContent.split(',');
      replace_words.hidden = true;
      let hidden = false;
      // store original text
      el.addEventListener('click', () => {
        // get current card
        if (hidden) {
            reveal_hidden_words(notes, id);
            hidden = false;
            el.innerHTML = "Challenge";
            replace_words.hidden = true;
        } else {
            replace_words_list.map(phrase => {
                hide_hidden_words(notes, phrase, id);
            });
            hidden = true;  
            el.innerHTML = "Reveal";
            replace_words.hidden = false;
        };
    });
  });
}
