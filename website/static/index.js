

function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId }), // Changed noteId to noteID
    }).then((_res) => { // Corrected the placement of closing parentheses
        window.location.href = "/";
    });
}


