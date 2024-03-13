<script>
    import {duckStore} from '../../duck-store'
</script>

<ul>
    {#each $duckStore as duck}
        <li>
            <a href="ducksProfile/{duck.id}">{duck.name}</a>
        </li>
    {/each}
</ul>
<button><a href="/">HOME PAGE</a></button>


<style>
    ul {
        background-color: aqua;
        font-size: 40px;
    }
</style>
