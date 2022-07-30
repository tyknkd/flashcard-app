/* JavaScript to control the display of cards' front/back */

function displayCards(cards) {
    
    // Get card element for displaying card contents
    const cardElement = document.getElementById("card");

    //Get next button to move to next card
    const nextButton = document.getElementById("nextButton");

    // Iterate through cards
    for (card in cards) {
        // Display front of card 
        cardElement.innerHTML = card['front']
    

        // Display edit link if owner  
            // Need to convert Jinja template code below to JS
            // Might need to use request to Flask to render url
            // {% if g.user['user_id'] == deck['owner_id'] %}
            // <a class="action" href="{{ url_for('cards.edit', deck_id=deck['deck_id'], card_id=card['card_id']) }}">Edit</a>

    }
}

// Get cards JSON from HTML (cards is list of card dicts) 
const cards = document.getElementById("cards").dataset.cards; 

// If cards not null
if (cards) {
    // Run displayCards with cards JSON object
    displayCards(cards);
}
