var registertab=document.getElementById("registertab");
var registerbutton=document.getElementById("register");
var loginbutton=document.getElementById("login");
var logintab=document.getElementById("logintab");
var confirm=document.getElementById("confirm");

registertab.addEventListener("click",(e) => {
    registertab.className="nav-link active";
    logintab.className="nav-link";
    loginbutton.setAttribute("hidden",true);
    registerbutton.removeAttribute("hidden");
    confirm.removeAttribute("hidden");
});
logintab.addEventListener("click",() => {
    logintab.className="nav-link active";
    registertab.className="nav-link";
    registerbutton.setAttribute("hidden",true);
    confirm.setAttribute("hidden",true);
    loginbutton.removeAttribute("hidden");
});