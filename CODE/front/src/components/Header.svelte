<script lang="ts">
    import ButtonTheme from './ButtonTheme.svelte';
    import NavBar from './NavBar.svelte';

    import { page } from '$app/stores';
	import { onMount } from 'svelte';

	let currentPath: any;

	onMount(() => {
		// Obtén la ruta actual al cargar el componente
		currentPath = $page.route['id'];
		console.log(currentPath);
	});

</script>

{#if currentPath === '/login'}
	<ButtonTheme styles="absolute" />
{:else}
	<NavBar />
{/if}
