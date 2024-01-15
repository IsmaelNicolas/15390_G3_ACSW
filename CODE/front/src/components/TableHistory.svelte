<script lang="ts">
	interface Event {
		fecha: string;
		intensidad: string;
		blanco_biologico: string;
	}
	export let events: Event[] = [];
</script>

<div class="relative overflow-x-auto">
	<table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
		<thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
			<tr>
				<th scope="col" class="px-6 py-3"> Fecha </th>
				<th scope="col" class="px-6 py-3"> Intensidad </th>
				<th scope="col" class="px-6 py-3"> Blanco biologico </th>
				<th scope="col" class="px-6 py-3"> Accion </th>
			</tr>
		</thead>
		<tbody>
			{#each events as { fecha, intensidad, blanco_biologico }, index}
				<tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
					<th
						scope="row"
						class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
					>
						{fecha}
					</th>
					<td class="px-6 py-4"> {intensidad} </td>
					<td class="px-6 py-4"> {blanco_biologico} </td>
					<td class="px-6 py-4"> Borrar </td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
