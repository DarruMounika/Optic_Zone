document.addEventListener("DOMContentLoaded", function () {
    let addToCartBtn = document.getElementById("addToCartBtn");
    let quantityInput = document.getElementById("quantity");
    let incrementBtn = document.getElementById("increment");
    let decrementBtn = document.getElementById("decrement");
    let popupBox = document.getElementById("popupBox");
    let closePopupBtn = document.getElementById("closePopupBtn");

    // Increase quantity
    incrementBtn.onclick = function () {
        quantityInput.value = parseInt(quantityInput.value) + 1;
    };

    // Decrease quantity (minimum 1)
    decrementBtn.onclick = function () {
        if (parseInt(quantityInput.value) > 1) {
            quantityInput.value = parseInt(quantityInput.value) - 1;
        }
    };

    // Add to Cart
    addToCartBtn.onclick = function () {
        let product = {
            name: "{{ product.name }}",
            price: "{{ product.price }}",
            image: "{{ product.image.url }}",
            quantity: parseInt(quantityInput.value)
        };

        // Get cart from localStorage or create an empty array
        let cart = JSON.parse(localStorage.getItem("cart")) || [];

        // Add product to cart
        cart.push(product);

        // Save updated cart to localStorage
        localStorage.setItem("cart", JSON.stringify(cart));

        // Show popup
        popupBox.style.display = "block";
    };

    // Close popup
    closePopupBtn.onclick = function () {
        popupBox.style.display = "none";
    };
});
