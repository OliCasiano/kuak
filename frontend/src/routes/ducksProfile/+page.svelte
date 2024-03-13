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
