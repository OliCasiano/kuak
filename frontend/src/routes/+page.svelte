<script>
  import { duckStore } from "../duck-store";
  import { goto } from "$app/navigation";
  import logo from "../public/logo.jpg";

  let name = "";
  let age = "";
  let location = "";
  let files;
  let showInvalidMessage = false;

  let validFields = () => {
    return name.length > 4 && age.length < 3 && location.length > 2;
  };

  let handleSubmit = () => {
    if (!validFields()) {
      showInvalidMessage = true;
      return;
    }
    const endpoint = "http://localhost:8000/api/ducks/";
    let data = new FormData();
    data.append("name", name);
    data.append("age", age);
    data.append("location", location);
    data.append("image", files[0]);

    fetch(endpoint, { method: "POST", body: data })
      .then((response) => response.json())
      .then((data) => {
        duckStore.update((prev) => [...prev, data]);
      });

    goto("/ducksProfile/");
  };
</script>

<nav class="navbar navbar-expand-lg navbar-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="/ducksProfile/">Muac-Kuack</a>
    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarNav"
      aria-controls="navbarNav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
  </div>
</nav>

<div class="container">
  <slot />
</div>

<div class="container">
  <div class="row justify-content-center">
    <h2>¡Buena suerte en tu búsqueda de amor entre patos!🦆♥️</h2>
    <img src={logo} alt="Logo Foto" />
    <div class="col-md-6">
      <div class="card">
        <div class="card-header">
          <h2>Registro</h2>
        </div>

        <div class="card-body">
          <form on:submit|preventDefault={handleSubmit}>
            <div class="mb-3">
              <input
                class="form-control"
                type="text"
                placeholder="name"
                bind:value={name}
              />
            </div>
            <div class="mb-3">
              <input
                class="form-control"
                type="text"
                placeholder="Age"
                bind:value={age}
              />
            </div>
            <div class="mb-3">
              <input
                class="form-control"
                type="text"
                placeholder="Location"
                bind:value={location}
              />
            </div>
            <div class="mb-3">
              <input class="form-control" type="file" bind:files />
            </div>
            <div class="center-button">
              <button class="btn btn-primary" type="submit">Enviar</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
  .navbar {
    background-image: linear-gradient(to right, rgb(242, 237, 99), #ff9900) !important;
  }
  h2 {
    text-align: center;
  }
  img {
    height: 350px;
    width: 350px;
    border-radius: 5%;
  }
  .container {
    margin-top: 20px;
  }

  .card {
    border-radius: 10px;
  }

  .card-header {
    text-align: center;
  }

  .center-button {
    display: flex;
    justify-content: center;
  }

  .container-fluid {
    display: flex;
    justify-content: center;
  }
</style>
