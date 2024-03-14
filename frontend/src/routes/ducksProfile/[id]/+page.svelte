<script>
  import {duckStore} from "../../../duck-store";
  import { onMount } from "svelte";

  export let data;
  let duck

  onMount(async function() {
        if ($duckStore.length) {
            duck = $duckStore.find(duck => duck.id == data.id)
        } else {
            const endpoint = `http://localhost:8000/api/ducksProfile/${data.id}/`
            let response = await fetch(endpoint)
            if (response.status == 200) {
                duck = await response.json()
            } else {
                duck = null;
            }
        }
    })
</script>

<div class="row mt-4">
  {#if duck }
      <h2 class="mb-4">{ duck.name }</h2>
      <div class="col-12 col-md-4">
          <img src="{ duck.image }" alt="Film" class="w-100"/>
      </div>
      <div class="col-12 col-md-8">
          <p class="mb-2"><b>{ duck.name }</b>, Edad: <i>{ duck.age }</i></p>
          <p class="mb-2">{ duck.location }</p>
      </div>
  {:else }
      <p>Este pato no ta! {data.id}</p>
  {/if }
</div>


