function hospital_name() {
   var name = document.getElementById('pac-input').value;

   console.log("users value is: " + name);
   var js_data = JSON.stringify(name);
   console.log("test js data value: " + js_data);
   $.ajax({
       url: '/hospital-select',
       type : 'post',
       contentType: 'application/json',
       dataType : 'json',
       data : js_data
   }).done(function(result) {
       console.log(result);
       location.href="/hospital-create";
       $("#data").html(result);
   }).fail(function(jqXHR, textStatus, errorThrown) {
       console.log("fail: ",textStatus, errorThrown);
   });


}
