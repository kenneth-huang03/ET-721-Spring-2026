document.querySelector("#upload-form").addEventListener("submit", event => {
    event.preventDefault();

    const fileInput = document.querySelector("#image-input");
    const message = document.querySelector("#message");

    if (fileInput.files.length === 0) {
        message.textContent = "Please select a file";
        message.style.color = "red";
        return;
    }

    const formData = new FormData();
    formData.append("image", fileInput.files[0]);

    fetch("upload", 
        {
            method: "POST",
            body: formData,
        }
    ).then(response => response.json())
    .then(data => {
        if (data.message) {
            message.textContent = data.message;
            message.style.color = "green";

            setTimeout(() => location.reload(), 1000);
        } else {
            message.textContent = data.error || "Upload Failed";
            message.color = "red";
        }
    });
});
    

function deleteImage(id) {
    if ( !confirm("Are you sure you want to delete this image?") ) return;

    fetch(`delete/${id}`, 
        {
            method: "DELETE",
        }
    ).then(response => response.json())
    .then(data => {
        if (data.message) {
            const element = document.getElementById(`image-${id}`);
            if (element) element.remove()
        } else {
            alert(data.error);
        }
    });
}
