fetch("/api/products")
  .then((r) => (r.ok ? r.json() : Promise.reject(new Error(`HTTP ${r.status}`))))
  .then((items) => {
    const list = document.getElementById("products");
    list.replaceChildren(...items.map((p) => {
      const li = document.createElement("li");
      li.textContent = `${p.name}: ?${p.price_inr}`;
      return li;
    }));
  })
  .catch((err) => {
    document.getElementById("products").textContent = `API unavailable (${err.message})`;
  });
