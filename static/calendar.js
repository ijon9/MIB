var month = document.getElementById('monthselect');

var year = document.getElementById("yearselect");

var selector = document.getElementById("selector");

month.addEventListener("change", (e) => {
  selector.submit();
});
year.addEventListener("change",(e)=>{
  selector.submit();
});