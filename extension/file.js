document.getElementById("submit-btn").onclick = function() {
    // Récupérer les valeurs des champs de formulaire
    var master = document.getElementById('master').value;
    var domain = document.getElementById('domain').value;
    // Afficher les valeurs dans la console
    console.log('Master : ' + master);
    console.log('Domain : ' + domain);

    fetch('http://127.0.0.1:5000/password', {
    method: 'POST',
    body: JSON.stringify({ master: master, domain: domain })
    })
    .then(response => response.json())
    .then(data => {
      console.log(data.result);
      document.getElementById("output").innerHTML = data.result;    
  });
}