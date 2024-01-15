<script>
	import Sun from './Sun.svelte';
	import Moon from './Moon.svelte';

	export let styles = '';

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

<button
	id="toggleButton"
	on:click={theme}
	class=" end-0 m-4 {styles} rounded-full bg-blue fill-slate-800 dark:fill-yellow-400"
>
	<Sun />
	<Moon />
</button>
