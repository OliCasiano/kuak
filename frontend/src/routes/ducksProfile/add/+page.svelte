<script>
  import { duckStore } from "../../../duck-store";
  import { goto } from "$app/navigation";

  let name = "";
  let age = "";
  let location = "";
  let files;
  let showInvalidMessage = false;

  let validFields = () => {
    return name.length > 4 && age.length > 4 && location.length > 10;
  };

  let handleSubmit = () => {
    if (!validFields()) {
      showInvalidMessage = true;
      return;
    }
    const endpoint = "http://localhost:8000/api/duckProfile/";
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
      <div class="mb-3">
        <input class="form-control" type="file" bind:files />
      </div>
      
      <button class="btn btn-primary" type="submit">Submit</button>
    </form>
  </div>
</div>
