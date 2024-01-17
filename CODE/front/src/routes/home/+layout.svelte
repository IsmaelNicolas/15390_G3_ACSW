<script lang="ts">
	import Header  from '../../components/NavBar.svelte';
</script>

<div class="m-0 bg-white dark:bg-gray-800 h-auto">
	<Header/>
	<main class="m-0">
		<slot />
	</main>
</div>
