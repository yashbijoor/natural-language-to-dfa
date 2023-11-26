if (window.history.replaceState) {
  window.history.replaceState(null, null, window.location.href);
}

function clearInputs() {
  document.querySelector(".charset").value = "";
  document.querySelector(".query").value = "";
}
