import {writable} from 'svelte/store' 

export const duckStore = writable([
    {id: 1, name: 'El Pato con botas', age: '21', location:"Mieres"},
    {id: 2, name: "Pato Donald", age: "20", location:"Mieres"},
    {id: 3, name: 'Daisy', age: '16', location:"Mieres"},
    {id: 4, name: "Calimero", age: "7", location:"Langreo"}
])