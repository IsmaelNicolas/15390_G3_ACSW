<script lang="ts">
	import type { HistoriaData } from "../Models/HistoriaData";

	export let confidence = '';
	export let historia: HistoriaData = { fecha: '', intensidad: '', blanco_biologico: '',id:'',imageURL:'' };
	console.log(historia);
</script>

{#if historia.fecha}
	<section class="w-1/3">
		<!-- <div class="flex flex-col gap-2 md:flex-row">
		<InputForm id="bed" label="Cama" placeholder="Número de cama" type="number" />
		<InputForm id="block" label="Bloque" placeholder="Número de bloque" type="number" />
	</div> -->
		<div class="flex flex-col gap-4">
			<div>
				<strong class="font-semibold text-gray-900 dark:text-white">Fecha:</strong>
				<p>{historia.fecha}</p>
			</div>
			<div>
				<strong class="font-semibold text-gray-900 dark:text-white">Intensidad:</strong>
				{#if historia.intensidad === 'severe'}
					<span
						class="bg-red-100 text-red-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded dark:bg-red-900 dark:text-red-300"
						>Severo</span
					>
				{/if}
				{#if historia.intensidad === 'moderate'}
					<span
						class="bg-yellow-100 text-yellow-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded dark:bg-yellow-900 dark:text-yellow-300"
						>Moderado</span
					>
				{/if}
			</div>
			<div>
				<strong class="font-semibold text-gray-900 dark:text-white">Blanco biologico:</strong>
				<p>{historia.blanco_biologico}</p>
			</div>
			{#if confidence !=='' }

			<div>
				<strong class="font-semibold text-gray-900 dark:text-white">Fiabilidad:</strong>
				<p>confidence</p>
			</div>
				
			{/if}
		</div>
	</section>
{/if}
