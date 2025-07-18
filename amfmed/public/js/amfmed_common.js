// Set navbar to an obvious colour if running on dev machine:
const r = document.querySelector(':root');
if (window.location.host.indexOf("localhost") >= 0) {
    r.style.setProperty('--navbar-color', '#e98332ff');
}

function wait_for_form(timeout=5000) {
    const start = Date.now();
    
    function check() {
        if ((cur_frm) && (cur_frm.doc) && (cur_frm.doc.company)) {
            // Set country flags based on company:
            const company = cur_frm.doc.company;
            if (company.indexOf(' SA') >= 0) {
                r.style.setProperty('--flag', 'url("/assets/amfmed/img/ch.png")');
            } else if (company.indexOf(' LTD') >= 0) {
                r.style.setProperty('--flag', 'url("/assets/amfmed/img/uk.png")');
            }
        } else if (Date.now() - start < timeout) {
            setTimeout(check, 100);
        } else {
            console.log("not a form with company");
        }
    }
    
    check();
}

wait_for_form(timeout=5000);
