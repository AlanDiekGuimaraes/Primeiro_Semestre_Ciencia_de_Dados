var manipula = document.getElementById("manipula")
var class_name = document.getElementsByClassName.apply("manipula")


function novo_site() {
  
  //APAGANDO SITE ANTIGO
  // Manipulando do header 
  document.getElementById("topo").style.backgroundColor = "#fff"
  document.getElementById("topo").style.borderRadius = "10px"
  document.getElementById("topo").style.boxShadow = "0px 1px 10px #00000015"
 
 // Tira o titulo h1 do site
  document.getElementsByClassName("titulo")[0].innerHTML = ""
  document.getElementById("manipula").style.display = "none"
  // Elimina os gifs do site
  document.getElementsByClassName("gif")[0].style.display = "none"
  document.getElementsByClassName("gif")[1].style.display = "none"
  document.getElementsByClassName("gif")[2].style.display = "none"
  

// NOVO SITE
// Adiciona uma logo ao site
  // NÃO DEFINIDO AINDA
// adiciona a imagem ao fundo do body.
document.getElementsByTagName("body")[0].style.backgroundImage = "url(img/FUNDO_30%.png)"
manipula.style.backgroundRepeat = "no-repeat"
manipula.style.backgroundSize = "cover"


  // Ajustando os botões
  var x = document.getElementById("botoes")
  var y = x.getElementsByTagName("input")
  var i
  for (i = 0; i < y.length; i++) {
    y[i].style.backgroundColor = "transparent" //"#faebcc"
    y[i].style.borderRadius = "10px"
    y[i].style.height = "40px"
    // y[i].style.width = "120px"
    y[i].style.fontSize = "16px"
    y[i].style.fontWeight = "bold"
    y[i].style.textAlign = "center"
    y[i].style.color = "#a23c1b"
    y[i].style.border = "none" //"2px solid #fc6a3a"
    y[i].style.margin = "0 auto"
    }
  // Alinhando os botões
  document.getElementById("topo").style.display = "flex"
  document.getElementById("topo").style.alignItems = "center"
  document.getElementById("topo").style.justifyContent = "end"

  //Ajustando corpo do site
  document.getElementById("corpo_site").style.width = "600px" //Corpo do site
  document.getElementById("corpo_site").style.color = "#a23c1b" //Cor da fonte


 //Ajustando texto 1
  document.getElementById("esquerda1").innerHTML = "Os melhores ingredientes são reunidos com amor e carinho e depois cozidos lentamente até a perfeição. Sim, os métodos antigos ainda são melhores em Los Pollos Hermanos. Mas não acredite apenas na minha palavra. Uma prova e você saberá."
  document.getElementById("esquerda1").style.color = "#a23c1b" //Cor da fonte
  document.getElementById("esquerda1").style.width = "600px"
  document.getElementById("esquerda1").style.fontSize = "20px"

  //Ajustando img 1
  document.getElementById("direita1").style.backgroundImage = "url(img/Los_Pollos_Hermanos_logo.png)"
  document.getElementById("topo1").style.display = "flex"
  document.getElementById("topo1").style.flexDirection = "row"
  document.getElementById("topo1").style.justifyContent = "center"

  //ajustando texto 2
  document.getElementsByClassName("direita2")[0].innerHTML = "A necessidade de um hambúrguer fresco e batatas fritas é real. O mesmo vale para um trabalho que permite que você seja você. Aqui na Los Pollos Hermanos trabalharemos de acordo com a sua necessidade. E vamos celebrar quem você é. Traga seu verdadeiro eu e vamos fazer isso. E divirta-se também. NÓS TEMOS. NÓS PEGAMOS VOCÊ! "
  document.getElementsByClassName("direita2")[0].style.color = "#a23c1b" 
  document.getElementsByClassName("direita2")[0].style.width = "600px"
  document.getElementsByClassName("direita2")[0].style.fontSize = "20px"




}
