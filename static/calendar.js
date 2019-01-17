var month = document.getElementById('monthselect');

var year = document.getElementById("yearselect");

var set = document.getElementById("set");

month.addEventListener("change", (e) => {
    set.innerHTML="{%set y = '"+year.options[year.selectedIndex].value+"'%} {%set m = '"+month.options[month.selectedIndex].value+"'%}";
    console.log(e);
  }
);

year.addEventListener("change", (e) => {
    set.innerHTML="{%set y = '"+year.options[year.selectedIndex].value+"'%} {%set m = '"+month.options[month.selectedIndex].value+"'%}";
    console.log(e);
  }
);
