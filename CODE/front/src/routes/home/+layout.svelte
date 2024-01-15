<script lang="ts">
	import '../../app.css';
	import Header  from '../../components/NavBar.svelte';

</script>

<div class="m-0 bg-white dark:bg-gray-800 h-dvh">
	<Header/>
	<main class="m-0">
		<slot />
	</main>
</div>
