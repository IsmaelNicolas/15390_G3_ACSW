<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import TableHistory from '../../components/TableHistory.svelte';
	import UploadImage from '../../components/UploadImage.svelte';
	import Loader from '../../components/Loader.svelte';
	import {getCookie,setCookie} from '../../Utils/function'

	// Definir el tipo para un evento
	interface Event {
		fecha: string;
		intensidad: string;
		blanco_biologico: string;
	}

	let eventos: Event[] = [];

	async function load_histories() {
		const access_token = getCookie('access_token');
		const response = await fetch('http://localhost:8000/historias', {
			headers: {
				Authorization: `Bearer ${access_token}`
			}
		});
		if (response.ok) {
			const data = await response.json();
			// console.log(data); // Verify that the data is logged correctly
			eventos = data; // Assign the data to the eventos variable
			return data;
		} else if (response.status === 401) {
			goto('/login');
		} else {
			console.error('Error al obtener datos de la API');
			return [];
		}
	}

	onMount(async () => {
		const access_token = getCookie('access_token');
		// console.log(access_token);
		const response = await fetch('http://localhost:8000/api/user/me', {
			headers: {
				Authorization: `Bearer ${access_token}`
			}
		});
		// console.log(response);
		if (!response.ok) {
			goto('/login');
		}
	});
</script>

<svelte:head>
	<title>Sisamonitor Clasificador</title>
	<meta name="description" content="Clasificador de plagas" />
</svelte:head>

<div class="h-screen overflow-hidden">
	<section class="mx-auto w-3/4 md:h-1/2 flex justify-center items-center">
		<UploadImage />
	</section>
	<section class="w-11/12 mx-auto">
		{#await load_histories()}
			<Loader />
		{:then events}
			{#if events.length > 0}
				<TableHistory {events} />
			{:else}
				<p>No hay eventos disponibles...</p>
			{/if}
		{/await}
	</section>
</div>
