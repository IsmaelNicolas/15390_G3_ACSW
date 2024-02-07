<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import TableHistory from '../../components/TableHistory.svelte';
	import UploadImage from '../../components/UploadImage.svelte';
	import Loader from '../../components/Loader.svelte';
	import { API, getCookie, setCookie } from '../../Utils/function';
	import DataInput from '../../components/DataInput.svelte';
	import type { HistoriaData } from '../../Models/HistoriaData';
	
	
	let confidence:number
	let historia: HistoriaData = { fecha: '', intensidad: '', blanco_biologico: '',id:'',imageURL:'' };

	function manejarMensajeDelHijo(event: CustomEvent<HistoriaData>) {
		historia = event.detail;
		// reloadHistories();
	}
	function viewConfidence(event:CustomEvent<number>){
		confidence = event.detail;

	}

	let reloadData = false;

	// Definir el tipo para un evento
	interface Event {
		fecha: string;
		intensidad: string;
		blanco_biologico: string;
	}

	let eventos: Event[] = [];

	async function load_histories() {
		const access_token = getCookie('access_token');
		const response = await fetch(API + '/historias', {
			headers: {
				Authorization: `Bearer ${access_token}`
			}
		});
		console.log(response);
		if (response.ok) {
			const data = await response.json();
			// console.log(data); // Verify that the data is logged correctly
			eventos = data; // Assign the data to the eventos variable
			return data;
		} else if (response.status === 401) {
			goto('/login');
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
		const response = await fetch(API + '/user/me', {
			headers: {
				Authorization: `Bearer ${access_token}`
			}
		});
		// console.log(response);
		if (!response.ok) {
			goto('/login');
		}
	});

	$: {
		// Esta expresión observa cambios en reloadData y ejecuta la función load_histories()
		if (reloadData) {
			load_histories();
			// reloadHistories(); // Restablece la variable después de cargar los datos
		}
	}
</script>

<svelte:head>
	<title>Sisamonitor Clasificador</title>
	<meta name="description" content="Clasificador de plagas" />
</svelte:head>

<div class="h-screen overflow-hidden">
	<section
		class="mx-auto w-11/12 md:h-1/2 flex justify-center items-center flex-col md:flex-row gap-2"
	>
		<UploadImage on:addHistory={manejarMensajeDelHijo} on:viewConfidence={viewConfidence} />
		<DataInput {historia} {confidence}/>
	</section>
	<section class="w-11/12 mx-auto">
		{#await load_histories()}
			<Loader />
		{:then events}
			{#if events.length > 0}
				<TableHistory {events} />
			{:else}
				<div class="flex justify-center items-center mt-10">
					<p>No hay exite historico...</p>
				</div>
			{/if}
		{/await}
	</section>
</div>
