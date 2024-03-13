<script>
  import { duckStore } from "../../duck-store";

  let handleClick = () =>
    duckStore.update((prev) => {
      let newDuck = { id: 5, name: "Drive", age: "24", location: "Gijon" };
      return [...prev, newDuck];
    });
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
            src=""
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
              <a href="/ducksProfile/{duck.id}" class="btn btn-primary">Ver Perfil</a>
            </div>
          </div>
        </div>
      </div>
    {/each}
  </div>
</div>
