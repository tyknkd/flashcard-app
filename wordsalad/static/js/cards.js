/* JavaScript to control the display of cards' front and back */

// Display card edit button 
function addEditButton() {
    // Build card editing URL
    const cardID = cards[cardCount]['card_id'];
    const urlBase = cardID.toString();
    const editURL = urlBase.concat("/edit/"); 

    // Add edit button for editing card
    const editButton = document.createElement("button");
    editButton.id = "editButton";
    editButton.textContent = "Edit";
    document.getElementById("buttons").appendChild(editButton);

    // Add event listener to edit button
    editButton.addEventListener("click", function(){ window.location.replace(editURL )});

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
    
    // Remove edit button if owner
    if (owner) {
        document.getElementById("editButton").remove();
    }

    // Display front of next card
    document.getElementById("card").innerHTML = cards[cardCount]['front'];

    // Add flip button for flipping card
    const flipButton = document.createElement("button");
    flipButton.id = "flipButton";
    flipButton.textContent = "Flip Card";
    document.getElementById("buttons").appendChild(flipButton);

    // Add event listener to flip button
    flipButton.addEventListener("click", flipCard);

    // Display edit button if deck owner
    if (owner) {
        addEditButton();
    } 
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
        const buttonsNode = document.getElementById("buttons");
        if (owner) {
            editButton = document.getElementById("editButton");
            buttonsNode.insertBefore(nextButton, editButton);
        }
        else {
            buttonsNode.appendChild(nextButton);
        }

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

    // Add flip button for flipping card
    const flipButton = document.createElement("button");
    flipButton.id = "flipButton";
    flipButton.textContent = "Flip Card";
    document.getElementById("buttons").appendChild(flipButton);

    // Add event listener to flip button
    flipButton.addEventListener("click", flipCard);

    // Display edit button if deck owner
    if (owner) {
        addEditButton();
    } 
}
