<script>
  import { duckStore } from "../../duck-store";
  import { onMount } from "svelte";

  onMount(async function () {
    if (!$duckStore.lenght) {
      const endpoint = "http://localhost:8000/api/ducks/";
      const response = await fetch(endpoint);
      const data = await response.json();
      duckStore.set(data);
    }
  });

  let handleDelete = (id) => {
    const endpoint = `http://localhost:8000/api/ducks/${id}`;
    fetch(endpoint, { method: "DELETE" }).then(response => {
      if (response.status == 204) {
        duckStore.update(prev => prev.filter(duck => duck.id != id));
      }
    });
  };
</script>

<div>
  <h2 class="my-4">Lista de Usupatos</h2>

  <div class="my-4 row">
    {#each $duckStore as duck}
      <div class="col-12 col-sm-6 col-md-4">
        <div class="card w-100 h-100">
          <img
            class="card-img-top"
            style="height: 300px; object-fit: cover"
            src={duck.image}
            alt="Duck"
          />
          <div
            class="card-body d-flex flex-column justify-content-between gap-4"
          >
            <div>
              <h5 class="card-title">{duck.name}</h5>
              <p class="card-text">Edad: {duck.age}</p>
            </div>
            <div>
              <a href="/ducksProfile/{duck.id}" class="btn btn-primary"
                >Ver Perfil</a
              >
              <button
                on:click={() => handleDelete(duck.id)}
                class="btn btn-danger m1-2"
              >
                Delete</button
              >
            </div>
          </div>
        </div>
      </div>
    {/each}
  </div>
</div>
