import { useState, useEffect } from 'react';

function App() {

  let [products, setProducts] = useState([])
  
  function handleClick(){

    console.log("clicked, fetching the data")

    fetch("http://localhost:8000/product/", {mode:"cors"}) //https://cors-anywhere.herokuapp.com/
    .then((response) => response.json())
    .then((data) => {
      setProducts(data)
      console.log(data)
    });
  }

  return (
    <div>
      <button onClick={handleClick}>
        Fetch The Products
      </button>
      {
        products && products.map((product) => {
            return(
            <em>
              <p>
                {JSON.stringify(product)}
              </p>
            </em>
            )
          }
        )
      }
      {/* <em>
        <p>
          {products}
        </p>
      </em> */}
    </div>
  );
}

export default App;
