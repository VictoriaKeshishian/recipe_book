
function isPageScrolledToBottom() {
    var scrollHeight = document.documentElement.scrollHeight;
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
    var clientHeight = window.innerHeight;

    return (scrollHeight - scrollTop === clientHeight);
}

function toggleFooterVisibility() {
    var footer = document.querySelector("footer");
    if (document.documentElement.scrollHeight - window.innerHeight <= window.scrollY) {
        footer.style.display = "block";
    } else {
        footer.style.display = "none";
    }
}

window.addEventListener("scroll", toggleFooterVisibility);

