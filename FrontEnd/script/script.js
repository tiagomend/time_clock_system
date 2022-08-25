
function close_menu(){
    if (document.getElementById("navigation_container_open")){
        document.getElementById("navigation_container_open").style.display = "none";
        document.getElementById("header_container_id").style.width = "100%";
        document.getElementById("body_container_id").style.width = "90%";
        document.getElementById("navigation_container_open").id = "navigation_container_close";
    }

    else {
        document.getElementById("navigation_container_close").style.display = "block";
        document.getElementById("header_container_id").style.width = "80%";
        document.getElementById("body_container_id").style.width = "78%";
        document.getElementById("navigation_container_close").id = "navigation_container_open";
    }
}

function close_table(){
    if (document.getElementById("row_edit_1").style.display == "none"){
        document.getElementById("row_edit_1").style.display = "table-row";
    }

    else {
        document.getElementById("row_edit_1").style.display = "none";
    }
}

