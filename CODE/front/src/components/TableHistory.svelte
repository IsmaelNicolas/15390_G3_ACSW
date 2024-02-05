<script lang="ts">
	import { Button, Modal } from 'flowbite-svelte';
	import Eye from '../components/Eye.svelte';
	import type { HistoriaData } from '../Models/HistoriaData';
	import DataInput from './DataInput.svelte';
	let defaultModal = false;

	export let events: HistoriaData[] = [];
	let historia:HistoriaData = {fecha:'',blanco_biologico:'',id:'',intensidad:''}

	function setData(intensidad:string,blanco_biologico:string,id:string,fecha:string){
		historia = {intensidad,blanco_biologico,fecha,id}
		console.log(historia)
		defaultModal = true
	}

</script>

<div class="relative overflow-x-auto overflow-y-auto">
	<table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
		<thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
			<tr>
				<th scope="col" class="px-6 py-3"> Fecha </th>
				<th scope="col" class="px-6 py-3"> Intensidad </th>
				<th scope="col" class="px-6 py-3"> Blanco biologico </th>
				<th scope="col" class="px-6 py-3"> </th>
			</tr>
		</thead>
		<tbody>
			{#each events as {id, fecha, intensidad, blanco_biologico }, index}
				<tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
					<th
						scope="row"
						class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
					>
						{fecha}
					</th>
					{#if blanco_biologico === 'healthy'}
						<td colspan="2" class="px-6 py-4 text-center">
							<span
								class="bg-green-100 text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-green-400 border border-green-400"
								>Saludable</span
							>
						</td>
					{:else}
						<td class="px-6 py-4">
							{#if intensidad === 'severe'}
								<span
									class="bg-red-100 text-red-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded dark:bg-red-900 dark:text-red-300"
									>Severo</span
								>
							{/if}
							{#if intensidad === 'moderate'}
								<span
									class="bg-yellow-100 text-yellow-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded dark:bg-yellow-900 dark:text-yellow-300"
									>Moderado</span
								>
							{/if}
						</td>
						<td class="px-6 py-4">
							{#if blanco_biologico === 'botrytis'}
								Botritys
							{/if}
							{#if blanco_biologico === 'oidio'}
								Oidio
							{/if}
						</td>
					{/if}
					<td class="px-2 py-1">
						<button
							class="inline-flex items-center font-medium text-blue-600 dark:text-blue-500 hover:underline"
							on:click={() => setData(intensidad, blanco_biologico, id, fecha)}
						>
							<Eye clss="w-8 h-6" />
							Ver
						</button>
					</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
<Modal title="Evento {historia.fecha}" bind:open={defaultModal} autoclose>
	<DataInput {historia}/>
	<svelte:fragment slot="footer">
		<Button color="alternative">Cerrar</Button>
	</svelte:fragment>
</Modal>
