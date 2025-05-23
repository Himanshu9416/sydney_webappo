async function fetchEvents() {
    try {
        const res = await fetch("http://localhost:5000/events");
        const events = await res.json();
        const container = document.getElementById("events");

        events.forEach(event => {
            const div = document.createElement("div");
            div.className = "event-card";
            div.innerHTML = `
                <h3>${event.title}</h3>
                <p>${event.date}</p>
                <p>${event.location}</p>
                <form onsubmit="handleSubmit(event, '${event.link}')">
                    <input type="email" placeholder="Enter your email" required>
                    <button type="submit">GET TICKETS</button>
                </form>
            `;
            container.appendChild(div);
        });
    } catch (err) {
        console.error("Failed to fetch events", err);
    }
}

function handleSubmit(e, link) {
    e.preventDefault();
    const email = e.target.querySelector("input").value;
    console.log("Email submitted:", email);
    window.location.href = link;
}

fetchEvents();