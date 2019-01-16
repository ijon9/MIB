// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var del = document.getElementById("delete");

var close=document.getElementById("close");
var cancel=document.getElementById("cancel");

// When the user clicks on the button, open the modal
del.addEventListener("click", (e) => {
    modal.style.display="block";
    console.log(e);
    }
);

close.addEventListener("click", (e) => {
        modal.style.display="none";
        console.log(e);
    }
);
cancel.addEventListener("click", (e) => {
    modal.style.display="none";
    console.log(e);
}
);



