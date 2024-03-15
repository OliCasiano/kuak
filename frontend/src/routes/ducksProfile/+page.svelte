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
    fetch(endpoint, { method: "DELETE" }).then((response) => {
      if (response.status == 204) {
        duckStore.update((prev) => prev.filter((duck) => duck.id != id));
      }
    });
  };
  let showSlide = false;

  function toggleSlide() {
    showSlide = !showSlide;
  }
</script>

<div>
  <h2 class="my-4">Lista de Usupatos</h2>
  <button class="btn btn-primary" on:click={toggleSlide}>Abrir Chat</button>

  <div class={`slide-container ${showSlide ? "slide-open" : ""}`}>
    <div class="slide-content">
      <h2>Panel de Chat</h2>
    </div>
    <div class="my-4"> <div class="duck-grid"> {#each $duckStore as duck}
      <div class="duck-card"> 
        <img
          class="card-img"
          style="width: 100%; height: 100px; object-fit: cover"
          src={duck.image}
          alt="Duck"
        />
        <div class="card-body"> 
          <h5 class="card-title">{duck.name}</h5>
          <div class="btn-row"> 
            <a href="/ducksProfile/{duck.id}" class="btn btn-primary">Ver Perfil</a>
            <button on:click={() => handleDelete(duck.id)} class="btn btn-danger m1-2">Eliminar</button>
            <a href="/ducksProfile/chat/{duck.id}" class="btn btn-success m1-2">Chat</a>
          </div>
        </div>
      </div>
    {/each}
  </div>
</div>
    <button class="btn btn-primary" on:click={toggleSlide}>Cerrar Chat</button>
  </div>

  <div class="main-content"></div>
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

<style>
  .slide-container {
    position: fixed;
    left: 0;
    top: 0;
    height: 100%;
    width: 400px; 
    background-color: #fff;
    transition: transform 0.3s ease-in-out;
    transform: translateX(-100%);
    z-index: 1000; 
  }

  .slide-open {
    transform: translateX(0);
  }


  .slide-content {
    padding: 20px;
  }

  .my-4 {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.duck-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.duck-card {
  width: 350px; 
  height: 100px;
  margin-bottom: 70px; 
  border: 1px solid #ddd; 
}

.card-body {
  display: flex;
  align-items: center; 
  justify-content: space-between; 
  margin-bottom: 5px;
}

.btn-row {
  display: flex;
  margin-top: 10px;
  margin-left: 5px;
  margin-right: 5px;
  gap: 5px;
}
</style>
