<script>
  import {duckStore} from "../../../duck-store";

  export let data;

  let duck = $duckStore.find(duck => duck.id == data.id);
  console.log(duck);
</script>

<div>
  {#if duck}
    <p>{duck.name},{duck.age} años</p>
  {:else}
    <p>Not found Id:{data.id}</p>
  {/if}
</div>


