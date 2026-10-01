fetch("/api/products")
  .then((r) => (r.ok ? r.json() : Promise.reject(r.status)))
  .then((items) => {
    const list = document.getElementById("products");
    list.replaceChildren(...items.map((p) => {
      const li = document.createElement("li");
      li.textContent = `${p.name}: ?${p.price_inr}`;
      return li;
    }));
  })
  .catch((status) => {
    document.getElementById("products").textContent = `API unavailable (${status})`;
  });
