function loadImage(event) {
    var originalImage = document.getElementById('originalImage');
    originalImage.src = URL.createObjectURL(event.target.files[0]);
}

function downloadBoundingBox() {
    // JSON data from the HTML content
    var jsonData = document.getElementById('json-content').textContent;

    // Create a Blob from the JSON data
    var blob = new Blob([jsonData], {type: "application/json"});

    // Create a download link
    var downloadLink = document.createElement("a");
    downloadLink.href = URL.createObjectURL(blob);
    downloadLink.download = "bounding_box_data.json";
    downloadLink.click();
    URL.revokeObjectURL(downloadLink.href);  // Clean up
}

function downloadImage() {
    var editedImageSrc = document.getElementById('editedImage').src;
    var link = document.createElement('a');
    link.href = editedImageSrc;
    link.download = 'edited_image.jpg';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

function downloadText() {
    var textContent = document.getElementById('ocrTextDisplay').textContent;
    var blob = new Blob([textContent], { type: 'text/plain' });

    var downloadLink = document.createElement('a');
    downloadLink.href = URL.createObjectURL(blob);
    downloadLink.download = 'extracted_text.txt';
    downloadLink.click();
    URL.revokeObjectURL(downloadLink.href);  // Clean up
}