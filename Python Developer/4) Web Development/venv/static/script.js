document.addEventListener('DOMContentLoaded', function () {
    const uploadForm = document.getElementById('upload-form');
    const imageInput = document.getElementById('image-input');
    const resultsTable = document.getElementById('results-table').getElementsByTagName('tbody')[0];

    uploadForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const images = imageInput.files;

        for (let i = 0; i < images.length; i++) {
            const image = images[i];
            const newRow = resultsTable.insertRow();
            const imageCell = newRow.insertCell(0);
            const resultCell = newRow.insertCell(1);

            imageCell.innerHTML = `<img src="${URL.createObjectURL(image)}" alt="Uploaded Image" style="max-width: 100px; max-height: 100px;">`;
            resultCell.textContent = 'Model Result'; // Replace with your actual model result
        }

        uploadForm.reset();
    });
});
