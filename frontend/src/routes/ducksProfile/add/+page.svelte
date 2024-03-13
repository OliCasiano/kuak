<script>
  import { duckStore } from "../../../duck-store";
  import { goto } from "$app/navigation";

  let name = "";
  let age = "";
  let location = "";

  let handleSubmit = () => {
    duckStore.update((prev) => {
      let id = prev[prev.length - 1].id + 1;
      let newDuck = { id: id, name: name, age: age, location: location };
      return [...prev, newDuck];
    });

    goto("/duckProfile/");
  };
</script>

<div>
  <h2 class="my-4">Hazte Usupato</h2>

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

      <button class="btn btn-primary" type="submit">Submit</button>
    </form>
  </div>
</div>
