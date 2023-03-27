document.getElementById("submit-btn").onclick = function() {
    // Récupérer les valeurs des champs de formulaire
    var master = document.getElementById('master').value;
    var domain = document.getElementById('domain').value;
    // Afficher les valeurs dans la console
    console.log('Master : ' + master);
    console.log('Domain : ' + domain);

    fetch('C:/Users/basti/OneDrive/COURS/COURS CERI/M2/S4/APPLICATION SECURITE AVANCEE/TP/main.py', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          body: 'master=' + encodeURIComponent(master) + '&domain=' + encodeURIComponent(domain)
        })
        .then(response => response.json())
        .then(data => {
          // Handle the response from the server
          console.log(data.result);
        })
        .catch(error => {
          // Handle errors
          console.error(error);
    });
}