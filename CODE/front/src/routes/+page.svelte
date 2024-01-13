<script lang="ts">
	import { onMount } from 'svelte';

	// Definir el tipo para un evento
	interface Evento {
		fecha: string;
		intensidad: string;
		blanco_biologico: string;
	}

	let eventos: Evento[] = [];

	onMount(async () => {
		try {
			// Hacer la llamada a la API
			const response = await fetch('http://192.168.0.160:8000/historias');

			// Verificar si la respuesta es exitosa
			if (response.ok) {
				const data: Evento[] = await response.json();
				eventos = data;
				console.log(eventos);
			} else {
				console.error('Error al obtener datos de la API');
			}
		} catch (error) {
			console.error('Error en la llamada a la API', error);
		}
	});
</script>

<svelte:head>
	<title>Inicio</title>
	<meta name="description" content="Clasificador de plagas" />
</svelte:head>

{#if eventos.length > 0}
	<ul>
		{#each eventos as { fecha, intensidad, blanco_biologico }, index (fecha)}
			<li>
				<p>Fecha: {fecha}</p>
				<p>Intensidad: {intensidad}</p>
				<p>Blanco Biológico: {blanco_biologico}</p>
			</li>
		{/each}
	</ul>
{:else}
	<p>No hay eventos disponibles.</p>
{/if}
