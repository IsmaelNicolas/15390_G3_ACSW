<script lang="ts">
	import { onMount } from 'svelte';
	import { API, getCookie } from '../Utils/function';
	import { goto } from '$app/navigation';

	// Definir el tipo para un evento
	interface Evento {
		fecha: string;
		intensidad: string;
		blanco_biologico: string;
	}

	let eventos: Evento[] = [];

	onMount(async () => {
		const access_token = getCookie('access_token');
		// console.log(access_token);
		const response = await fetch(API +'/user/me', {
			headers: {
				Authorization: `Bearer ${access_token}`
			}
		});
		// console.log(response);
		if (!response.ok) {
			goto('/login');
		}else{
			goto('/home')
		}
	});
</script>

<svelte:head>
	<title>Inicio</title>
	<meta name="description" content="Clasificador de plagas" />
</svelte:head>