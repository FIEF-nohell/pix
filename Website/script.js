window.addEventListener("DOMContentLoaded", (event) => {
    // Populate folderDropdown from 'palettes' folder
    populateFolderDropdown();

    // Add event listener for file input
    const imageInput = document.getElementById('imageInput');
    imageInput.addEventListener('change', function () {
        const file = this.files[0];
        if (file) {
            // Do something with the selected file
        }
    });
});

function populateFolderDropdown() {
    const folderDropdown = document.getElementById('folderDropdown');

    // Make an AJAX request to the specific URL
    fetch('http://127.0.0.1:5000/list_palettes')
        .then(response => response.json())
        .then(data => {
            // Assuming that data is an array of filenames
            data.forEach(item => {
                const option = document.createElement('option');
                option.value = item;
                option.text = item;
                folderDropdown.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching palette list:', error);
        });
}
