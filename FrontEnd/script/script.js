
function close_menu(){
    if (document.getElementById("navigation_container_open").id == "none"){
        document.getElementById("navigation_container_open").style.display = "none";
        document.getElementById("header_container_id").style.width = "100%";
        document.getElementById("body_container_id").style.width = "90%";
    }

    else {
        document.getElementById("navigation_container_open").style.display = "block";
        document.getElementById("header_container_id").style.width = "80%";
        document.getElementById("body_container_id").style.width = "78%";
    }
}

function close_table(data_id){
    console.log(data_id);
    if (document.getElementById(data_id).style.display == "none"){
        document.getElementById(data_id).style.display = "table-row";
    }

    else {
        document.getElementById(data_id).style.display = "none";
    }
}

