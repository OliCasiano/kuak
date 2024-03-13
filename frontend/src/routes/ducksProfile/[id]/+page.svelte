<script>
  import { duckStore } from "../../../duck-store";

  export let data;

  let duck = $duckStore.find((duck) => duck.id == data.id);
  console.log(duck);
</script>

<div>
  {#if duck}
    <p>{duck.name}, Tiene {duck.age} años y es de {duck.location}</p>
  {:else}
    <p>Not found Id:{data.id}</p>
  {/if}
</div>
<button><a href="/ducksProfile">Volver a la Pagina Principal</a></button>

