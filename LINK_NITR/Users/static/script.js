document.addEventListener('DOMContentLoaded', () => {
    const loginButton = document.getElementById('one');
    const signupButton = document.querySelector('.btn:last-child'); // Assuming it's the second button
    const loginPopup = document.getElementById('loginPopup');
    const signupPopup = document.getElementById('signupPopup');
    const popupOverlay = document.createElement('div');
    popupOverlay.classList.add('popup-overlay');
    document.body.appendChild(popupOverlay);

    // Show login pop-up
    loginButton.addEventListener('click', (event) => {
        event.preventDefault(); // Prevent default link behavior
        showPopup(loginPopup);
    });

    // Show signup pop-up
    signupButton.addEventListener('click', (event) => {
        event.preventDefault(); // Prevent default link behavior
        showPopup(signupPopup);
    });

    // Close pop-up when clicking outside of it
    popupOverlay.addEventListener('click', () => {
        closePopup();
    });

    function showPopup(popup) {
        popup.style.display = 'block';
        popupOverlay.style.display = 'block';
        document.body.classList.add('blur-background');
    }

    function closePopup() {
        loginPopup.style.display = 'none';
        signupPopup.style.display = 'none';
        popupOverlay.style.display = 'none';
        document.body.classList.remove('blur-background');
    }
});
