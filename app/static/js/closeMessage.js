/**
 * Removes the flash message element from the DOM when the close button is clicked.
 *
 * @param {HTMLElement} button - The close button element.
 */
function closeFlashMessage(button) {
	var flashMessage = button.closest("div");
	flashMessage.remove();
}
