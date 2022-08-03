/* JavaScript to control the display of cards' front and back */

// Determine if user is deck owner and display edit button if so
function editButton() {
    /* 
    Need to adapt Jinja template code below to JS (might need to use request to Flask to render url)
    {% if g.user['user_id'] == deck['owner_id'] %}
        <a class="action" href="{{ url_for('cards.edit', deck_id=deck['deck_id'], card_id=card['card_id']) }}">Edit</a>
    {% endif %}
    */
    // Add edit button for editing card
    const editButton = document.createElement("button");
    editButton.id = "editButton";
    editButton.textContent = "Edit";
    document.getElementById("buttons").appendChild(editButton);

    // Add event listener to flip button
    flipButton.addEventListener("click", flipCard);
}

// Display next card in deck
function nextCard(){
    // Increment click count
    clickCount += 1;
    
    // Increment card count
    cardCount += 1;
    
    // Remove card notes
    document.getElementById("notes").innerHTML = "";

    // Remove next button
    document.getElementById("nextButton").remove();
    
    // Display front of next card
    document.getElementById("card").innerHTML = cards[cardCount]['front'];

    // Display edit button if appropriate
    editButton();
 
    // Add flip button for flipping card
    const flipButton = document.createElement("button");
    flipButton.id = "flipButton";
    flipButton.textContent = "Flip Card";
    document.getElementById("buttons").appendChild(flipButton);

    // Add event listener to flip button
    flipButton.addEventListener("click", flipCard);
}

// Flip current card
function flipCard() {
    // Increment click count
    clickCount += 1;

    // Display back of current card
    document.getElementById("card").innerHTML = cards[cardCount]['back'];

    // Display card notes 
    document.getElementById("notes").innerHTML = cards[cardCount]['notes'];

    // Remove flip button
    document.getElementById("flipButton").remove();

    // If more cards in deck
    if (cardCount + 1 < numCards) {
        // Add next card button
        const nextButton = document.createElement("button");
        nextButton.id = "nextButton";
        nextButton.textContent = "Next Card";
        document.getElementById("buttons").appendChild(nextButton);

        // Add event listener to next button
        nextButton.addEventListener("click", nextCard);
    }
}

// Get cards JSON string from HTML (cards is list of card dicts) 
const cardsJSONstring = document.getElementById("cards").dataset.cards; 

// Parse string to JSON object
const cards = JSON.parse(cardsJSONstring);

// Get number of cards
const numCards = cards.length;

// Set card counter
let cardCount = 0;

// Click counter
let clickCount = 0;


// If deck not empty
if (numCards > 0) {
    // Display front of first card
    document.getElementById("card").innerHTML = cards[cardCount]['front'];

    // Determine if deck owner and display edit button if so
    editButton();
    
    // Add flip button for flipping card
    const flipButton = document.createElement("button");
    flipButton.id = "flipButton";
    flipButton.textContent = "Flip Card";
    document.getElementById("buttons").appendChild(flipButton);

    // Add event listener to flip button
    flipButton.addEventListener("click", flipCard);

}
