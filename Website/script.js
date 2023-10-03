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

window.addEventListener("DOMContentLoaded", (event) => {
    // Listen for file input changes
    const imageInput = document.getElementById('imageInput');
    imageInput.addEventListener('change', function () {
        const file = this.files[0];
        if (file) {
            displayImage(file);
        }
    });
});

function displayImage(file) {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onloadend = function () {
        const imageElement = document.getElementById('inputImage');
        imageElement.src = reader.result;
        imageElement.style.display = "block";  // Make the image visible
        imageElement.style.width = '40%';      // Set the width to 20% of the page
    };
}



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

function sendData() {
    const imageInput = document.getElementById('imageInput');
    const file = imageInput.files[0];

    if (!file) {
        console.error("No file selected");
        return;
    }

    // Get the resolution value from the slider
    const resolution = document.getElementById('resolutionSlider').value;

    // Get the selected item from the dropdown
    const dropdown = document.getElementById('folderDropdown');
    const selectedItem = dropdown.options[dropdown.selectedIndex].value;

    // Convert the image to a Base64 string
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onloadend = function () {
        const base64data = reader.result;

        // Create a JSON object to send
        const data = {
            image: base64data,
            resolution: resolution,
            selectedItem: selectedItem
        };

        fetch('http://127.0.0.1:5000/post_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data => {
                // Assuming 'image' is the key in the returned JSON object that contains the Base64 image
                const base64Image = data.image;
                const imageElement = document.getElementById('generatedImage'); // Get the image element by its id

                imageElement.src = base64Image; // Set the image src to display it
                imageElement.style.display = "block";  // Make the image visible
                imageElement.style.width = '40%';      // Set the width to 20% of the page
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    };
}
