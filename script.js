function uploadFile() {
  const fileInput = document.getElementById('fileInput');
  const statusDiv = document.getElementById('status');

  const file = fileInput.files[0];
  if (file) {
    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      statusDiv.innerHTML = data.message;
    })
    .catch(error => {
      console.error('Error:', error);
      statusDiv.innerHTML = 'Error uploading file.';
    });
  } else {
    statusDiv.innerHTML = 'Please select a file.';
  }
}
