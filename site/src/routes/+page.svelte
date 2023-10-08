<script lang="ts">
    import { onMount } from "svelte";
    import doorCloseIcon from "$lib/icons/door_close.svg"
    import doorOpenIcon from "$lib/icons/door_open.svg"
    import loadingIcon from "$lib/icons/loading.svg"

    
    let door: null | string = null
    
    

    onMount(() => {
        const socket = new WebSocket("ws://88.122.234.97:50001");

        socket.addEventListener("message", function (event) {

            console.log("Door was ", event.data);
            door = String(event.data).replace("door_", "")
        });

        socket.addEventListener("close", (event) => {
            alert("La connexion a été interrompue.")
        })
    })

</script>

<main>
    <div>
    {#if door === "open"}
        <img src={doorOpenIcon} alt="Open Door" class="icon"/>
        <span class="open">La porte est ouverte</span>
    {:else if door === "close"}
        <img src={doorCloseIcon} alt="Close Door" class="icon"/>
        <span class="close" >La porte est fermée</span>
    {:else}
        <img src={loadingIcon} alt="Loading" class="icon loading"/>
        <span>Connexion au serveur ...</span>
    {/if}
</div>
</main>



<style lang="scss">
    main{
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }
    div{
        width: 400px;
        text-align: center;
        display: flex;
        flex-direction: column;
        padding: 20px;

        span{
            font-size: 40px;
            font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
            //font-weight: bold;

            &.open{
                color: red;
                
            }

            &.close{
                color: green;
            }
        }

        .icon{
            width: 50%;
            margin-left: auto;
            margin-right: auto;

            &.loading{
                animation: rotating forwards 2s ease;

                animation-iteration-count: infinite;
                -moz-animation-iteration-count: infinite;
                -webkit-animation-iteration-count: infinite;
                -o-animation-iteration-count: infinite;
            }
        }
    }

    @keyframes rotating{
        from{
            transform: rotate(0deg);
        }

        to{
            transform: rotate(360deg);
        }
    }
</style>