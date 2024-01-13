<script>
	import '../app.css';
	import Moon from '../components/Sun.svelte';
	import Sun from '../components/Moon.svelte';

	function theme() {
		const icon1 = document.getElementById('moon');
		const icon2 = document.getElementById('sun');
		const html = document.querySelector('html');

		html?.classList.toggle('dark');
		if (icon1 && icon2) {
			icon1.classList.toggle('hidden');
			icon2.classList.toggle('hidden');
		}
	}
</script>

<div class="app">
	<button
		id="toggleButton"
		on:click={theme}
		class="absolute end-0 m-4 rounded-full bg-blue fill-slate-800 dark:fill-yellow-400"
	>
		<Sun />
		<Moon />
	</button>
	<main>
		<slot />
	</main>
</div>
