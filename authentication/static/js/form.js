$("#password").change(function(){
    var pass=$(this).val();
    if(^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$.test(pass)){
      alert("Your password must be at least 8 characters long and contain alphanumeric. Please try another.")
    }
  });

$("#nomor-id").change(function(){
    var no=$(this).val();
    if(no.length!=10){
      alert("NPM/NIK you entered must be 10 characters long.")
    }
  });