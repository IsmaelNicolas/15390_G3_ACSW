<script lang="ts">
	import { onMount } from 'svelte';
	import TableHistory from '../../components/TableHistory.svelte';
	import UploadImage from '../../components/UploadImage.svelte';
	// Definir el tipo para un evento
	interface Event {
		fecha: string;
		intensidad: string;
		blanco_biologico: string;
	}

	let eventos: Event[] = [];

	async function load_histories() {
		const response = await fetch('http://localhost:8000/historias');
		if (response.ok) {
			const data = await response.json();
			console.log(data); // Verify that the data is logged correctly
			eventos = data; // Assign the data to the eventos variable
			return data;
		} else {
			console.error('Error al obtener datos de la API');
			return [];
		}
	}
	
</script>

<svelte:head>
	<title>Inicio</title>
	<meta name="description" content="Clasificador de plagas" />
</svelte:head>

<div class="h-screen overflow-hidden">
	<section class="mx-auto w-3/4   md:h-1/2 flex justify-center items-center">
		<UploadImage />
	</section>
	<section class="w-11/12 mx-auto  ">
		{#await load_histories()}
			<p>Cargando eventos...</p>
		{:then events}
			{#if events.length > 0}
				<TableHistory {events} />
			{:else}
				<p>No hay eventos disponibles...</p>
			{/if}
		{/await}
	</section>
</div>
