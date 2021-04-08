const getParamOrDefault = (selector, dft) => {
    let elem = document.querySelector(selector);
    if (elem !== undefined && elem.value !== undefined && elem.value != "") {
        return elem.value;
    }
    return dft;
}

const getParams = (show_all) => {
    // set only institute_id if show all, otherwise inspect dom for input
    return {
        institute_id: getParamOrDefault("input#teacher_react_apps__institute_id", 0),
        department_id: show_all === true ? 0 : getParamOrDefault("input#teacher_react_apps__department_id", 0),
        schemeofwork_id: show_all === true ? 0 : getParamOrDefault("input#teacher_react_apps__scheme_of_work_id", 0),
        lesson_id: show_all === true ? 0 : getParamOrDefault("input#teacher_react_apps__lesson_id", 0)
    }
}

export default getParams;
