  // const a =  setTimeout( function fun(){
  //        alert("Welcome To Home :")
  //    }, 1000);


  

  // using for showing date

  var myji = setInterval(donji, 1000)

  function donji() {
      var d = new Date()
      document.getElementById("time").innerHTML = d.toLocaleTimeString();
      document.getElementById("time").style.fontSize='35px';
  }



  function changeBG(color) {
    document.body.style.backgroundColor = color;
    let txt = document.getElementsByClassName("txt");
    if (color == '#000000') {
        for(let elem of txt){
            elem.style.color = 'white';
        }
    }
    else{
        for(let elem of txt){
            elem.style.color = 'black';
        }
    }
  }