/**
 * Created by Mrzipa on 19.01.2019.
 */
const renderProduct = ({name, cost, id}) => (
    `
    <li class="products-list__item">
        <h2 class="products-list__item-name">${name}</h2>
        <span class="product-list__item-cost">${cost}</span>
        <a class="product-list__item-link" href="/products/${id}/"></a>
    </li>
    `
)