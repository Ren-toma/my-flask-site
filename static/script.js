const API_URL = '/api';

// 1. Fetch data when the page loads
function loadProfile() {
    fetch(`${API_URL}/profile`)
        .then(res => res.json())
        .then(data => {
            document.getElementById('name').innerText = data.name;
            document.getElementById('role').innerText = data.role;
            document.getElementById('status').innerText = data.status;
            document.getElementById('quote').innerText = data.quote;
        });
}

// 2. Send new status to backend when button is clicked
document.getElementById('updateBtn').addEventListener('click', () => {
    const input = document.getElementById('statusInput');
    const newStatus = input.value;

    if (!newStatus) return;

    fetch(`${API_URL}/status`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ new_status: newStatus })
    })
        .then(res => res.json())
        .then(data => {
            document.getElementById('status').innerText = data.status;
            input.value = '';
        });
});

// Initialize
loadProfile();