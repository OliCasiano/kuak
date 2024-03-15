<script>
  import { duckStore } from "../../../../duck-store";
  import { goto } from "$app/navigation";
  import { onMount } from "svelte";

  let name = "";
  let age = "";
  let location = "";
  let files;
  let showInvalidMessage = false;
  export let data;
  let id;

  let validFields = () => {
    return name.length > 4 && age.length < 3 && location.length > 2;
  };

  let handleSubmit = () => {
    if (!validFields()) {
      showInvalidMessage = true;
      return;
    }
    const endpoint = `http://localhost:8000/api/ducks/${id}/`;
    let data = new FormData();
    data.append("name", name);
    data.append("age", age);
    data.append("location", location);

    if (files) {
      data.append("image", files[0]);
    }

    fetch(endpoint, { method: "PUT", body: data })
      .then((response) => response.json())
      .then((data) => {
        duckStore.update((prev) => {
          let updateDucks = $duckStore.slice();
          let index = updateDucks.findIndex((duck) => duck.id == data.id);
          updateDucks[index] = data;
          return updateDucks;
        });
      });

    goto("/ducksProfile/");
  };

  onMount(async function () {
    id = data.id;
    let duck = {};
    if ($duckStore.length) {
      duck = $duckStore.find((duck) => duck.id == id);
    } else {
      const endpoint = `http://localhost:8000/api/ducks/${data.id}/`;
      let response = await fetch(endpoint);
      if (response.status == 200) {
        duck = await response.json();
      } else {
        duck = null;
      }
    }
    ({ name, age, location } = duck);
  });
</script>

<div>
  <h2 class="my-4">Añadir a Patos</h2>

  {#if showInvalidMessage}
    <h4 class="text-danger">Has metido la Pata!</h4>
  {/if}

  <div class="col-12 col-md-6">
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
          placeholder="age"
          bind:value={age}
        />
      </div>
      <div class="mb-3">
        <input
          class="form-control"
          type="text"
          placeholder="location"
          bind:value={location}
        />
      </div>
      <div class="mb-3">
        <input class="form-control" type="file" bind:files />
      </div>

      <button class="btn btn-primary" type="submit">Aceptar</button>
    </form>
  </div>
</div>
