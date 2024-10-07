// // Event listener for sending messages
// document.getElementById('send-message').addEventListener('click', function() {
//     const ingredients = document.getElementById('ingredients').value.trim();
//     if (!ingredients) {
//         alert('Please enter some ingredients.');
//         return; // Prevent sending empty messages
//     }

//     addMessage(ingredients, 'right'); // Add user's message to chat
//     document.getElementById('ingredients').value = ''; // Clear input field
//     addMessage('Fetching recipes...', 'left'); // Inform user that recipes are being fetched

//     // Fetch recipes based on ingredients
//     fetch('/get_recipes', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
//         body: `ingredients=${encodeURIComponent(ingredients)}`
//     })
//     .then(response => response.json())
//     .then(data => {
//         const chatBox = document.getElementById('chat-box');
//         // Clear the fetching message
//         const fetchingMessage = chatBox.querySelector('.msg:contains("Fetching recipes...")');
//         if (fetchingMessage) {
//             fetchingMessage.remove();
//         }

//         if (data.error) {
//             addMessage(data.error, 'left'); // Show error message from chatbot
//         } else {
//             data.forEach(recipe => {
//                 addMessage(`${recipe.title} <img src="${recipe.image}" alt="${recipe.title}" style="width: 50px; height: auto;">`, 'left');
//             });
//         }
//     })
//     .catch(error => {
//         console.error('Error:', error);
//         addMessage('An error occurred while fetching recipes.', 'left'); // Show generic error message
//     });
// });


// // Function to add messages to the chat box
// function addMessage(message, side) {
//     const chatBox = document.getElementById('chat-box');
//     const messageDiv = document.createElement('div');
//     messageDiv.classList.add('item');
    
//     // Only show the chatbot icon for messages from the chatbot
//     if (side === 'left') {
//         messageDiv.innerHTML = `
//             <div class="icon">
//                 <img src="static/354bf71208671163b57dd7109211dec4.ico/favicon-32x32.png" alt="Chatbot Icon" style="width: 40px; height: 40px;">
//             </div>
//             <div class="msg">${message}</div>
//         `;
//     } else {
//         messageDiv.innerHTML = `
//             <div class="icon">
//                 <i class="fa fa-user"></i>
//             </div>
//             <div class="msg">${message}</div>
//         `;
//     }
    
//     messageDiv.classList.add(side === 'right' ? 'right' : '');
//     chatBox.appendChild(messageDiv);
//     chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
// }


// // Handle pressing Enter to send messages
// document.getElementById('ingredients').addEventListener('keypress', function(event) {
//     if (event.key === 'Enter') {
//         document.getElementById('send-message').click(); // Trigger button click
//     }
// });