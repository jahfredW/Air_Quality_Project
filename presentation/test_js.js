fetch("https://www.google.fr")
.then(function(res) {if (res.ok) {return res.json();}}).catch(function (err) {throw err}).then(function(value) {
    console.log(value);
})

document.getElementById("principal").
addEventListener('click', function(event) {
    event.defaultPrevented;

})