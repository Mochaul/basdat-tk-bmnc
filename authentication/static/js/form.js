function checkRole(selected) {
    var val = document.selected.value;
    if (val === "mahasiswa") {
        document.getElementById("status-kemahasiswaan").style.display = 'inline';
        document.getElementById("id-universitas").style.display = 'none';
    } else{
        document.getElementById("status-kemahasiswaan").style.display = 'none';
        document.getElementById("id-universitas").style.display = 'inline';
    }
}