<script lang="ts">
	import Moon from '../../components/Sun.svelte';
	import Sun from '../../components/Moon.svelte';
	import { page } from '$app/stores';
	import { onMount } from 'svelte';

	
	let currentPath:any;

	onMount(() => {
		// Obtén la ruta actual al cargar el componente
		currentPath = $page.route['id'];
		console.log(currentPath);
	});

	function theme() {
		const icon1 = document.getElementById('moon');
		const icon2 = document.getElementById('sun');
		const html = document.querySelector('html');

		html?.classList.toggle('dark');
		if (icon1 && icon2) {
			icon1.classList.toggle('hidden');
			icon2.classList.toggle('hidden');
		}
	}
</script>

<div class="m-0 bg-white dark:bg-gray-800 h-dvh">
	{#if currentPath == '/login'}
		<button
			id="toggleButton"
			on:click={theme}
			class="absolute end-0 m-4 rounded-full bg-blue fill-slate-800 dark:fill-yellow-400"
		>
			<Sun />
			<Moon />
		</button>
	{/if}
	<main class="m-0">
		<slot />
	</main>
</div>
