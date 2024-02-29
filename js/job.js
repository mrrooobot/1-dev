    // Define o tempo inicial como 10 minutos a partir do momento em que a página é carregada
    var tempoInicial = new Date().getTime() + (10 * 60 * 1000);

    // Atualiza a contagem regressiva a cada segundo
    var x = setInterval(function() {
      // Obtém a data e hora atual
      var now = new Date().getTime();

      // Calcula o tempo restante
      var distance = tempoInicial - now;

      // Calcula dias, horas, minutos e segundos
      var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance % (1000 * 60)) / 1000);

      // Atualiza o elemento HTML com o tempo restante formatado
      document.getElementById("tempo").innerHTML = minutes + " : " + seconds;

      // Verifica se o tempo acabou
      if (distance < 0) {
          clearInterval(x);
          document.getElementById("tempo").innerHTML = "Terminou";
      }
    }, 1000);