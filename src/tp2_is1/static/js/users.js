const editUserForm = document.getElementById('edit-user-form')

if (editUserForm){
    editUserForm.addEventListener("submit", async function (event) {
        event.preventDefault()
        const userId = editUserForm.dataset.userId

        const formData = new FormData(editUserForm)
        const userData = Object.fromEntries(formData.entries())

        try {
            const response = await fetch(`/users/${userId}/edit`, {
            method: 'PATCH',
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(userData)
            });
            const result = await response.json();
            if (!response.ok){
                alert(result.error || "No se puedo actualizar el usuario")
                return
            }
            alert(result.message)
            window.location.href = result.redirect_url
        } catch (error) {
            console.error("Error capturado:", error);

        }
    })
}

const deleteUserButton = document.getElementById('delete-user-btn');

if (deleteUserButton) {
    deleteUserButton.addEventListener('click', async function () {

        const userId = deleteUserButton.dataset.userId;

        const confirmation = confirm(
            "¿Estás seguro de que deseas eliminar este usuario?"
        );

        if (!confirmation) {
            return;
        }

        try {
            const response = await fetch(`/users/${userId}`, {
                method: 'DELETE'
            });

            const result = await response.json();

            if (!response.ok) {
                alert(result.error || "No se pudo eliminar el usuario");
                return;
            }

            alert(result.message);

            window.location.href = '/users/';

        } catch (error) {
            console.error("Error:", error);
            alert("Error al comunicarse con el servidor");
        }
    });
}