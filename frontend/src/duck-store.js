import {writable} from 'svelte/store' 

export const duckStore = writable([
    {id: 1, name: 'El Pato con botas', age: '21'},
    {id: 2, name: "Pato Donald", age: "20"},
    {id: 3, name: 'Daisy', age: '16'},
    {id: 4, name: "Calimero", age: "7"}
])