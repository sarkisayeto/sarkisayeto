document.addEventListener("DOMContentLoaded", function () {
  const brelEcoModal = document.getElementById("brelEcoModal");
  const brelGestModal = document.getElementById("brelGestModal");

  const brelEcoButton = document.getElementById("brelEcoButton");
  const brelGestButton = document.getElementById("brelGestButton");

  const closeBrelEco = document.getElementById("closeBrelEco");
  const closeBrelGest = document.getElementById("closeBrelGest");

  const brelEcoBody = document.getElementById("brelEcoBody");
  const brelGestBody = document.getElementById("brelGestBody");

  const historiqueBrelEco = [];
  const historiqueBrelGest = [];

  document
    .getElementById("updateForm")
    .addEventListener("submit", function (e) {
      e.preventDefault();

      const date = document.getElementById("date").value;
      const version = document.getElementById("version").value;
      const typeLogiciel = document.getElementById("typeLogiciel").value;
      const nomClient = document.getElementById("nomClient").value;
      const poste = document.getElementById("poste").value;
      const adresseMAC = document.getElementById("adresseMAC").value;
      const nomAgent = document.getElementById("nomAgent").value;

      const newEntry = `
            <tr>
                <td class="border text-center py-2">${date}</td>
                <td class="border text-center py-2">${version}</td>
                <td class="border text-center py-2">${nomClient}</td>
                <td class="border text-center py-2">${poste}</td>
                <td class="border text-center py-2">${adresseMAC}</td>
                <td class="border text-center py-2">${nomAgent}</td>
            </tr>`;

      if (typeLogiciel === "BrelEco") {
        historiqueBrelEco.push(newEntry);
        brelEcoBody.innerHTML = historiqueBrelEco.join("");
      } else if (typeLogiciel === "BrelGest") {
        historiqueBrelGest.push(newEntry);
        brelGestBody.innerHTML = historiqueBrelGest.join("");
      }

      document.getElementById("updateForm").reset();
    });

  brelEcoButton.addEventListener("click", function () {
    brelEcoModal.classList.remove("hidden");
  });

  brelGestButton.addEventListener("click", function () {
    brelGestModal.classList.remove("hidden");
  });

  closeBrelEco.addEventListener("click", function () {
    brelEcoModal.classList.add("hidden");
  });

  closeBrelGest.addEventListener("click", function () {
    brelGestModal.classList.add("hidden");
  });
});
