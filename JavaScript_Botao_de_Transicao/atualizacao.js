var manipula = document.getElementById("manipula")
var class_name = document.getElementsByClassName.apply("manipula")


function novo_site() {

  //APAGANDO SITE ANTIGO
  document.getElementById("antigo").style.display = "none"



  // NOVO SITE
  document.getElementsByClassName("btn_upgrade")[0].style.display = "none"
  // adiciona a imagem ao fundo do body.
  document.getElementsByTagName("body")[0].style.backgroundImage = "url(img/FUNDO_30%.png)"
  manipula.style.backgroundRepeat = "no-repeat"
  manipula.style.backgroundSize = "cover"

  // Manipulando do header 
  topo = document.getElementById("topo")
  topo.style.backgroundColor = "#fff"
  topo.style.borderRadius = "10px"
  topo.style.boxShadow = "0px 1px 10px #00000015"
  // Alinhando os botões
  topo.style.display = "flex"
  topo.style.alignItems = "center"
  topo.style.justifyContent = "end"


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


  //Ajustando corpo do site
  document.getElementById("corpo_site").style.width = "600px" //Corpo do site
  document.getElementById("corpo_site").style.color = "#a23c1b" //Cor da fonte

  //Ajustando logo
  logo = document.getElementById("logo")
  logo.innerHTML = "<img src='img/Los_Pollos_Hermanos_logo.png' alt=''>"
  logo.style.display = "flex"
  logo.style.flexDirection = "row"
  logo.style.justifyContent = "center"

  //Alinhando div centralizar1
  centralizar1 = document.getElementById("centralizar1")
  centralizar1.style.display = "flex"
  centralizar1.style.flexDirection = "row"
  centralizar1.style.justifyContent = "center"
  centralizar1.style.alignItems = "center"


  //Ajustando texto Esquerda superior
  esquerda1 = document.getElementById("esquerda1")
  esquerda1.innerHTML = "Os melhores ingredientes são reunidos com amor e carinho e depois cozidos lentamente até a perfeição. Sim, os métodos antigos ainda são melhores em Los Pollos Hermanos. Mas não acredite apenas na minha palavra. Uma prova e você saberá."
  esquerda1.style.color = "#a23c1b" //Cor da fonte
  esquerda1.style.width = "600px"
  esquerda1.style.fontSize = "25px"
  esquerda1.style.textAlign = "justify"
  esquerda1.style.display = "flex"
  esquerda1.style.alignItems = "center"
  esquerda1.style.margin = "40px"
  esquerda1.style.width = "400px"


  //Inserindo direita superior
  direita1 = document.getElementById("direita1")
  direita1.innerHTML = "<img  src='img/direita01.webp'>"



  //Alinhando div centralizar2
  centralizar2 = document.getElementById("centralizar2")
  centralizar2.style.display = "flex"
  centralizar2.style.flexDirection = "row"
  centralizar2.style.justifyContent = "center"
  centralizar2.style.alignItems = "center"

  // Ajustando texto direita inferior
  direita2 = document.getElementById("direita2")
  direita2.innerHTML = " A necessidade de um hambúrguer fresco e batatas fritas é real. O mesmo vale para um trabalho que permite que você seja você. Aqui na Los Pollos Hermanos trabalharemos de acordo com a sua necessidade. E vamos celebrar quem você é. Traga seu verdadeiro eu e vamos fazer isso. E divirta-se também.NÓS TEMOS. NÓS PEGAMOS VOCÊ! "
  direita2.style.color = "#a23c1b" //Cor da fonte
  direita2.style.width = "600px"
  direita2.style.fontSize = "25px"
  direita2.style.textAlign = "justify"
  direita2.style.display = "flex"
  direita2.style.alignItems = "center"
  direita2.style.margin = "40px"
  direita2.style.width = "400px"

  //Inserindo o video
  video = document.getElementById("esquerda2")
  video.innerHTML = '<video controls width="450px"><source src="img/Video.mp4" type="video/mp4"> </video>'
  

}
