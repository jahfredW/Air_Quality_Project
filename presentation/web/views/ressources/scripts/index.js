const axios = window.axios

getVersionEnvironment();

async function getVersionEnvironment() {
    try {
        console.log("Lecture des informations via l'API du couteau suisse");
        const response = await axios.get('http://127.0.0.1:8001/environnement');
        console.log(response.data.version);
        console.log(response.data.target);

    let versionDiv = document.getElementById("version");
    let environmentDiv = document.getElementById("environment");

    versionDiv.innerText = " version" + response.data.version;
    environmentDiv.innerText = "Environnement" + response.data.target;

    } catch (error){
        console.log(error)
    }
}


function disableSubmit(disabled) {
  if (disabled) {
    document
      .getElementById("button_primary")
      .setAttribute("disabled", true);
  } else {
    document
      .getElementById("button_primary")
      .removeAttribute("disabled");
  }
}

/*
document
  .getElementById("ville_input")
  .addEventListener("input", function(e) {
  if (/^CODE-/.test(e.target.value)) {
    getCodeValidation().innerText = "Code valide";
    disableSubmit(false);
  } else {
    getCodeValidation().innerText = "Code invalide";
    disableSubmit(true);
  }
});

 */