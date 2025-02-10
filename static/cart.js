document.addEventListener("DOMContentLoaded", function () {
    let cartBody = document.getElementById("cartBody");

    function loadCart() {
        let cart = JSON.parse(localStorage.getItem("cart")) || [];

        // Clear table first
        cartBody.innerHTML = "";

        cart.forEach(function (item, index) {
            let row = document.createElement("tr");

            row.innerHTML = `
                <td>${item.name}</td>
                <td><img src="${item.image}" alt="${item.name}" width="100"></td>
                <td>$${item.price}</td>
                <td>${item.quantity}</td>
                <td>$${(item.price * item.quantity).toFixed(2)}</td>
                <td><button onclick="removeItem(${index})">Remove</button></td>
            `;

            cartBody.appendChild(row);
        });
    }

    // Remove item from cart
    window.removeItem = function (index) {
        let cart = JSON.parse(localStorage.getItem("cart")) || [];
        cart.splice(index, 1);
        localStorage.setItem("cart", JSON.stringify(cart));
        loadCart();
    };

    // Clear entire cart
    window.clearCart = function () {
        localStorage.removeItem("cart");
        loadCart();
    };

    loadCart();
});
// function removeRow(button) {
//     var row = button.parentNode.parentNode;  // Get the row containing the button
//     row.parentNode.removeChild(row);  // Remove the row from the table
// }
