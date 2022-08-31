
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


function close_table(data_id){
    
    if (document.getElementById(data_id).style.display == "none"){
        document.getElementById(data_id).style.display = "table-row";
    }

    else {
        document.getElementById(data_id).style.display = "none";
    }
}

// Obtenha o elemento com id="defaultOpen" e clique nele
document.getElementById("defaultOpen").click();
 
function openCity(evt, cityName) {
    var i, tabcontent, tablinks;

    // Obtenha todos os elementos com class="tabcontent" e oculte-os
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Obtenha todos os elementos com class="tablinks" e remova a classe "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Mostre a guia atual e adicione uma classe "ativa" ao botão que abriu a guia
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}
