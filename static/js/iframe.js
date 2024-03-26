// Function to set iframe dimensions based on browser dimensions
/**
 * Sets the size of the iframe based on the browser window dimensions.
 */
function setIframeSize() {
  var iframe = document.getElementById("iframe");
  var iframeContainer = document.getElementById("iframe-container");

  // Get browser window dimensions
  var windowWidth = window.innerWidth || document.documentElement.clientWidth;
  var windowHeight =
    window.innerHeight || document.documentElement.clientHeight;

  // Set iframe dimensions
  iframe.width = windowWidth * 0.8; // Adjust the factor (0.8) according to your preference
  iframe.height = windowHeight * 0.8; // Adjust the factor (0.8) according to your preference
}

// Call the function initially and on window resize
setIframeSize();
window.addEventListener("resize", setIframeSize);
